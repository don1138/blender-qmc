from __future__ import annotations

import ast
import importlib.util
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = PROJECT_ROOT / "qmc-shared" / "color_search.py"
SPEC = importlib.util.spec_from_file_location("qmc_color_search", MODULE_PATH)
color_search = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = color_search
SPEC.loader.exec_module(color_search)


def record(
    identifier: str,
    label: str,
    *,
    collection: str = "Collection A",
    collection_key: str = "qmc:a",
    hue: float = 0.0,
    saturation: float = 100.0,
):
    return {
        "id": identifier,
        "source": "qmc",
        "collection_id": collection_key.split(":", 1)[-1],
        "collection_key": collection_key,
        "collection_name": collection,
        "label": label,
        "hue": hue,
        "saturation": saturation,
        "search_text": color_search.normalize_text(f"{label} {collection}"),
    }


def load_index(path: Path):
    tree = ast.parse(path.read_text(), filename=str(path))
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "COLOR_INDEX" for target in node.targets)
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"COLOR_INDEX not found in {path}")


class HueCategoryTests(unittest.TestCase):
    def test_six_hue_boundaries(self):
        cases = (
            (0.0, "RED"),
            (29.999, "RED"),
            (30.0, "YELLOW"),
            (89.999, "YELLOW"),
            (90.0, "GREEN"),
            (149.999, "GREEN"),
            (150.0, "CYAN"),
            (209.999, "CYAN"),
            (210.0, "BLUE"),
            (269.999, "BLUE"),
            (270.0, "MAGENTA"),
            (329.999, "MAGENTA"),
            (330.0, "RED"),
            (360.0, "RED"),
        )
        for hue, expected in cases:
            with self.subTest(hue=hue):
                self.assertEqual(color_search.hue_category(hue, 100.0), expected)

    def test_neutral_overrides_hue_at_five_percent(self):
        self.assertEqual(color_search.hue_category(240.0, 5.0), "NEUTRAL")
        self.assertEqual(color_search.hue_category(240.0, 5.001), "BLUE")


class SearchTests(unittest.TestCase):
    def setUp(self):
        self.records = (
            record("exact", "Blue", hue=240.0),
            record("prefix", "Blue Sky", hue=200.0),
            record("words", "Deep Blue Sea", hue=220.0),
            record("partial", "Ultramarine", hue=245.0),
            record(
                "collection",
                "Naval",
                collection="Blue Collection",
                collection_key="qmc:blue_collection",
                hue=230.0,
            ),
            record(
                "other",
                "Signal Red",
                collection="Collection B",
                collection_key="qmc:b",
                hue=0.0,
            ),
        )

    def test_idle_state_returns_no_results(self):
        page = color_search.find_colors(self.records)
        self.assertEqual(page.total, 0)
        self.assertEqual(page.items, ())

    def test_relevance_order(self):
        page = color_search.find_colors(self.records, query="blue", limit=50)
        self.assertEqual(
            [item["id"] for item in page.items],
            ["exact", "prefix", "words", "collection"],
        )

    def test_partial_name_match(self):
        page = color_search.find_colors(self.records, query="marine")
        self.assertEqual([item["id"] for item in page.items], ["partial"])

    def test_multiple_query_terms_use_and_logic(self):
        page = color_search.find_colors(self.records, query="deep sea")
        self.assertEqual([item["id"] for item in page.items], ["words"])

    def test_hue_and_collection_filters_combine(self):
        page = color_search.find_colors(
            self.records,
            hue="BLUE",
            collections={"qmc:a", "qmc:b"},
            sort="ALPHABETICAL",
        )
        self.assertEqual([item["id"] for item in page.items], ["exact", "words", "partial"])

    def test_empty_collection_selection_returns_no_results(self):
        page = color_search.find_colors(self.records, hue="BLUE", collections=set())
        self.assertEqual(page.total, 0)

    def test_alphabetical_directions(self):
        ascending = color_search.find_colors(
            self.records, hue="ALL", collections={"qmc:a", "qmc:b"}, sort="ALPHABETICAL"
        )
        descending = color_search.find_colors(
            self.records,
            hue="ALL",
            collections={"qmc:a", "qmc:b"},
            sort="ALPHABETICAL",
            descending=True,
        )
        self.assertEqual(
            [item["id"] for item in descending.items],
            list(reversed([item["id"] for item in ascending.items])),
        )

    def test_collection_sort(self):
        page = color_search.find_colors(
            self.records,
            hue="ALL",
            collections={"qmc:a", "qmc:b", "qmc:blue_collection"},
            sort="COLLECTION",
        )
        self.assertEqual(page.items[0]["collection_name"], "Blue Collection")
        self.assertEqual(page.items[-1]["collection_name"], "Collection B")

    def test_limit_is_applied_after_sorting(self):
        records = tuple(record(str(number), f"Color {number:03d}") for number in range(120, 0, -1))
        first = color_search.find_colors(records, hue="RED", sort="ALPHABETICAL", limit=50)
        more = color_search.find_colors(records, hue="RED", sort="ALPHABETICAL", limit=100)
        self.assertEqual(first.total, 120)
        self.assertEqual(len(first.items), 50)
        self.assertEqual(len(more.items), 100)
        self.assertEqual(more.items[:50], first.items)
        self.assertEqual(first.items[0]["label"], "Color 001")


class GeneratedIndexTests(unittest.TestCase):
    def test_generated_indexes_have_expected_active_counts(self):
        public = load_index(PROJECT_ROOT / "qmc-shared" / "color_index.py")
        plus = load_index(PROJECT_ROOT / "qmc-plus" / "color_index_plus.py")
        self.assertEqual(len(public), 2041)
        self.assertEqual(len(plus), 14)
        self.assertEqual(
            sum(item["collection_key"] == "qmc:qmc_select" for item in public),
            46,
        )
        self.assertTrue(
            all(item["collection_key"] == "qmc_plus:ds" for item in plus)
        )
        combined = public + plus
        self.assertEqual(len({item["id"] for item in combined}), 2055)
        self.assertTrue(all(item["collection_key"].startswith(f'{item["source"]}:') for item in combined))


if __name__ == "__main__":
    unittest.main()
