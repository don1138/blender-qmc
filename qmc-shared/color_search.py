"""Pure-Python filtering and sorting for QMC Color Finder records."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence


ALL_HUES = "ALL"
NEUTRAL_SATURATION_MAX = 5.0
HUE_FILTERS = frozenset(
    {ALL_HUES, "RED", "YELLOW", "GREEN", "CYAN", "BLUE", "MAGENTA", "NEUTRAL"}
)
SORT_MODES = frozenset({"RELEVANCE", "ALPHABETICAL", "COLLECTION"})
_WORD_PATTERN = re.compile(r"\w+", flags=re.UNICODE)


@dataclass(frozen=True)
class SearchPage:
    """One visible page plus the size of the complete matching result set."""

    items: tuple[Mapping[str, object], ...]
    total: int


def normalize_text(value: object) -> str:
    text = unicodedata.normalize("NFKC", str(value)).casefold()
    return " ".join(text.split())


def text_terms(value: object) -> tuple[str, ...]:
    return tuple(_WORD_PATTERN.findall(normalize_text(value)))


def hue_category(hue: float, saturation: float) -> str:
    """Return the V1 hue bucket for numeric HSV hue and saturation values."""

    if not 0.0 <= saturation <= 100.0:
        raise ValueError(f"Saturation must be between 0 and 100, got {saturation!r}.")
    if saturation <= NEUTRAL_SATURATION_MAX:
        return "NEUTRAL"

    normalized_hue = hue % 360.0
    if normalized_hue >= 330.0 or normalized_hue < 30.0:
        return "RED"
    if normalized_hue < 90.0:
        return "YELLOW"
    if normalized_hue < 150.0:
        return "GREEN"
    if normalized_hue < 210.0:
        return "CYAN"
    if normalized_hue < 270.0:
        return "BLUE"
    return "MAGENTA"


def record_collection_key(record: Mapping[str, object]) -> str:
    key = record.get("collection_key")
    if key is not None:
        return str(key)
    return f'{record.get("source", "")}:{record.get("collection_id", "")}'


def record_search_text(record: Mapping[str, object]) -> str:
    value = record.get("search_text")
    if value is not None:
        return normalize_text(value)
    return normalize_text(
        f'{record.get("label", "")} {record.get("collection_name", "")}'
    )


def matches_text(record: Mapping[str, object], query_terms: Sequence[str]) -> bool:
    searchable = record_search_text(record)
    return all(term in searchable for term in query_terms)


def relevance_key(
    record: Mapping[str, object],
    normalized_query: str,
    query_terms: Sequence[str],
) -> tuple[object, ...]:
    label = normalize_text(record.get("label", ""))
    collection = normalize_text(record.get("collection_name", ""))
    label_words = set(text_terms(label))

    if label == normalized_query:
        rank = 0
    elif label.startswith(normalized_query):
        rank = 1
    elif query_terms and all(term in label_words for term in query_terms):
        rank = 2
    elif normalized_query and normalized_query in label:
        rank = 3
    elif query_terms and all(term in label for term in query_terms):
        rank = 4
    elif normalized_query and normalized_query in collection:
        rank = 5
    elif query_terms and all(term in collection for term in query_terms):
        rank = 6
    else:
        rank = 7

    return (rank, label, collection, str(record.get("id", "")))


def alphabetical_key(record: Mapping[str, object]) -> tuple[str, str, str]:
    return (
        normalize_text(record.get("label", "")),
        normalize_text(record.get("collection_name", "")),
        str(record.get("id", "")),
    )


def collection_key(record: Mapping[str, object]) -> tuple[str, str, str]:
    return (
        normalize_text(record.get("collection_name", "")),
        normalize_text(record.get("label", "")),
        str(record.get("id", "")),
    )


def find_colors(
    records: Iterable[Mapping[str, object]],
    *,
    query: str = "",
    hue: str = ALL_HUES,
    collections: Iterable[str] | None = None,
    sort: str = "RELEVANCE",
    descending: bool = False,
    limit: int = 50,
) -> SearchPage:
    """Filter and order all matching records before applying the visible limit."""

    hue_filter = hue.upper()
    if hue_filter not in HUE_FILTERS:
        raise ValueError(f"Unknown hue filter: {hue!r}")
    sort_mode = sort.upper()
    if sort_mode not in SORT_MODES:
        raise ValueError(f"Unknown sort mode: {sort!r}")
    if limit < 0:
        raise ValueError(f"Result limit cannot be negative: {limit!r}")

    normalized_query = normalize_text(query)
    query_words = text_terms(normalized_query)
    selected_collections = None if collections is None else frozenset(collections)

    # All collections, no query, and no hue selection is the intentionally idle state.
    if not normalized_query and hue_filter == ALL_HUES and selected_collections is None:
        return SearchPage(items=(), total=0)
    if selected_collections == frozenset():
        return SearchPage(items=(), total=0)

    matches = []
    for record in records:
        if (
            selected_collections is not None
            and record_collection_key(record) not in selected_collections
        ):
            continue
        if hue_filter != ALL_HUES:
            category = hue_category(
                float(record.get("hue", 0.0)),
                float(record.get("saturation", 0.0)),
            )
            if category != hue_filter:
                continue
        if query_words and not matches_text(record, query_words):
            continue
        matches.append(record)

    effective_sort = "ALPHABETICAL" if sort_mode == "RELEVANCE" and not normalized_query else sort_mode
    if effective_sort == "RELEVANCE":
        matches.sort(key=lambda item: relevance_key(item, normalized_query, query_words))
    elif effective_sort == "ALPHABETICAL":
        matches.sort(key=alphabetical_key, reverse=descending)
    else:
        matches.sort(key=collection_key, reverse=descending)

    return SearchPage(items=tuple(matches[:limit]), total=len(matches))
