"""Generate and validate the static QMC Color Finder indexes."""

from __future__ import annotations

import argparse
import ast
import colorsys
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class IndexSource:
    source_id: str
    color_sets: Path
    icons: Path
    output: Path


INDEX_SOURCES = (
    IndexSource(
        source_id="qmc",
        color_sets=PROJECT_ROOT / "qmc-shared" / "color_sets",
        icons=PROJECT_ROOT / "qmc-shared" / "icons",
        output=PROJECT_ROOT / "qmc-shared" / "color_index.py",
    ),
    IndexSource(
        source_id="qmc_plus",
        color_sets=PROJECT_ROOT / "qmc-plus" / "color_sets",
        icons=PROJECT_ROOT / "qmc-plus" / "icons",
        output=PROJECT_ROOT / "qmc-plus" / "color_index_plus.py",
    ),
)

EXPECTED_UNREGISTERED = {
    "qmc": {
        "color.moods_white_01",
        "color.moods_white_02",
        "color.moods_white_03",
        "color.moods_white_04",
    },
    "qmc_plus": set(),
}

EXPECTED_UNUSED_ICONS = {
    "qmc": {
        "_null",
        "ams_24172",
        "moods_white_01",
        "moods_white_02",
        "moods_white_03",
        "moods_white_04",
    },
    "qmc_plus": set(),
}


def assignment_value(node: ast.ClassDef, name: str) -> object | None:
    for statement in node.body:
        if (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
            and statement.targets[0].id == name
            and isinstance(statement.value, ast.Constant)
        ):
            return statement.value.value
    return None


def inherits_blender_type(node: ast.ClassDef, type_name: str) -> bool:
    return any(
        isinstance(base, ast.Attribute) and base.attr == type_name
        for base in node.bases
    )


def color_hex(node: ast.ClassDef) -> int | None:
    for statement in node.body:
        if not isinstance(statement, ast.FunctionDef) or statement.name != "execute":
            continue
        for child in ast.walk(statement):
            if (
                isinstance(child, ast.Call)
                and isinstance(child.func, ast.Name)
                and child.func.id == "set_base_color"
                and child.args
                and isinstance(child.args[0], ast.Constant)
                and isinstance(child.args[0].value, int)
            ):
                return child.args[0].value
    return None


def registered_class_names(tree: ast.Module) -> set[str]:
    names: set[str] = set()
    for statement in tree.body:
        if not (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
            and statement.targets[0].id.startswith("array_")
            and isinstance(statement.value, (ast.List, ast.Tuple))
        ):
            continue
        names.update(
            element.id
            for element in statement.value.elts
            if isinstance(element, ast.Name)
        )
    return names


def collection_name(tree: ast.Module, source_path: Path) -> str | None:
    labels = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef) or not inherits_blender_type(node, "Panel"):
            continue
        if assignment_value(node, "bl_parent_id") == "QMC_PT_Panel":
            label = assignment_value(node, "bl_label")
            if isinstance(label, str):
                labels.append(label.strip())
    if len(labels) > 1:
        raise ValueError(f"{source_path} defines multiple top-level collection panels.")
    return labels[0] if labels else None


def panel_icon_map(tree: ast.Module, source_path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, ast.ClassDef) or not inherits_blender_type(node, "Panel"):
            continue
        for statement in node.body:
            if not isinstance(statement, ast.FunctionDef) or statement.name != "draw":
                continue
            icons: list[tuple[int, str]] = []
            operators: list[tuple[int, str]] = []
            for child in ast.walk(statement):
                if (
                    isinstance(child, ast.Subscript)
                    and isinstance(child.value, ast.Attribute)
                    and child.value.attr == "c_icons"
                    and isinstance(child.slice, ast.Constant)
                    and isinstance(child.slice.value, str)
                    and child.slice.value != "_null"
                ):
                    icons.append((child.lineno, child.slice.value))
                if (
                    isinstance(child, ast.Call)
                    and isinstance(child.func, ast.Attribute)
                    and child.func.attr == "operator"
                    and child.args
                    and isinstance(child.args[0], ast.Constant)
                    and isinstance(child.args[0].value, str)
                    and child.args[0].value.startswith("color.")
                ):
                    operators.append((child.lineno, child.args[0].value))
            icon_names = [value for _, value in sorted(icons)]
            operator_ids = [value for _, value in sorted(operators)]
            if len(icon_names) != len(operator_ids):
                raise ValueError(
                    f"{source_path}:{node.name} has {len(icon_names)} color icons "
                    f"but {len(operator_ids)} color buttons."
                )
            for operator_id, icon_name in zip(operator_ids, icon_names):
                existing = mapping.get(operator_id)
                if existing is not None and existing != icon_name:
                    raise ValueError(
                        f"{source_path} maps {operator_id} to both {existing} and {icon_name}."
                    )
                mapping[operator_id] = icon_name
    return mapping


def normalized_search_text(label: str, collection: str) -> str:
    text = unicodedata.normalize("NFKC", f"{label} {collection}").casefold()
    return " ".join(text.split())


def hsv_from_hex(hex_value: int) -> tuple[float, float, float]:
    if not 0 <= hex_value <= 0xFFFFFF:
        raise ValueError(f"HEX value is outside 24-bit sRGB: {hex_value!r}")
    rgb = tuple(((hex_value >> shift) & 0xFF) / 255 for shift in (16, 8, 0))
    hue, saturation, value = colorsys.rgb_to_hsv(*rgb)
    return round(hue * 360, 6), round(saturation * 100, 6), round(value * 100, 6)


def records_for(source: IndexSource) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    defined_operator_ids: set[str] = set()
    indexed_operator_ids: set[str] = set()
    used_icons: set[str] = set()

    for source_path in sorted(source.color_sets.glob("*.py")):
        tree = ast.parse(source_path.read_text(), filename=str(source_path))
        registered = registered_class_names(tree)
        collection = collection_name(tree, source_path)
        icon_map = panel_icon_map(tree, source_path)

        color_classes: dict[str, tuple[str, str, int]] = {}
        for node in tree.body:
            if not isinstance(node, ast.ClassDef) or not inherits_blender_type(node, "Operator"):
                continue
            label = assignment_value(node, "bl_label")
            operator_id = assignment_value(node, "bl_idname")
            hex_value = color_hex(node)
            if not (
                isinstance(label, str)
                and isinstance(operator_id, str)
                and operator_id.startswith("color.")
                and isinstance(hex_value, int)
            ):
                continue
            if operator_id in defined_operator_ids:
                raise ValueError(f"Duplicate operator ID: {operator_id}")
            defined_operator_ids.add(operator_id)
            color_classes[node.name] = (label.strip(), operator_id, hex_value)

        registered_colors = sorted(set(color_classes) & registered)
        if registered_colors and collection is None:
            raise ValueError(f"{source_path} has registered colors but no collection panel.")

        for class_name in registered_colors:
            label, operator_id, hex_value = color_classes[class_name]
            icon = icon_map.get(operator_id)
            if icon is None:
                raise ValueError(f"{source_path} has no panel icon mapping for {operator_id}.")
            if not (source.icons / f"{icon}.png").is_file():
                raise ValueError(f"Missing icon for {operator_id}: {icon}.png")
            hue, saturation, value = hsv_from_hex(hex_value)
            record = {
                "id": operator_id,
                "source": source.source_id,
                "collection_id": source_path.stem,
                "collection_key": f"{source.source_id}:{source_path.stem}",
                "collection_name": collection,
                "label": label,
                "hex": hex_value,
                "hue": hue,
                "saturation": saturation,
                "value": value,
                "search_text": normalized_search_text(label, collection),
                "icon": icon,
                "operator_id": operator_id,
            }
            records.append(record)
            indexed_operator_ids.add(operator_id)
            used_icons.add(icon)

    unregistered = defined_operator_ids - indexed_operator_ids
    expected_unregistered = EXPECTED_UNREGISTERED[source.source_id]
    if unregistered != expected_unregistered:
        raise ValueError(
            f"Unexpected unregistered colors for {source.source_id}: "
            f"found {sorted(unregistered)}, expected {sorted(expected_unregistered)}"
        )

    available_icons = {path.stem for path in source.icons.glob("*.png")}
    unused_icons = available_icons - used_icons
    expected_unused = EXPECTED_UNUSED_ICONS[source.source_id]
    if unused_icons != expected_unused:
        raise ValueError(
            f"Unexpected unused icons for {source.source_id}: "
            f"found {sorted(unused_icons)}, expected {sorted(expected_unused)}"
        )

    records.sort(key=lambda item: (str(item["collection_name"]).casefold(), str(item["label"]).casefold(), str(item["id"])))
    if len({record["id"] for record in records}) != len(records):
        raise ValueError(f"Generated duplicate record IDs for {source.source_id}.")
    return records


def render_index(source: IndexSource, records: list[dict[str, object]]) -> str:
    lines = [
        '"""Generated Color Finder index. Do not edit by hand."""',
        "",
        "# Generated by generate_color_indexes.py.",
        f'SOURCE_ID = "{source.source_id}"',
        "COLOR_INDEX = (",
    ]
    for record in records:
        fields = [
            f'"id": {record["id"]!r}',
            f'"source": {record["source"]!r}',
            f'"collection_id": {record["collection_id"]!r}',
            f'"collection_key": {record["collection_key"]!r}',
            f'"collection_name": {record["collection_name"]!r}',
            f'"label": {record["label"]!r}',
            f'"hex": 0x{int(record["hex"]):06X}',
            f'"hue": {record["hue"]!r}',
            f'"saturation": {record["saturation"]!r}',
            f'"value": {record["value"]!r}',
            f'"search_text": {record["search_text"]!r}',
            f'"icon": {record["icon"]!r}',
            f'"operator_id": {record["operator_id"]!r}',
        ]
        lines.append("    {" + ", ".join(fields) + "},")
    lines.extend((")", ""))
    return "\n".join(lines)


def expected_indexes() -> dict[Path, str]:
    source_records = {source: records_for(source) for source in INDEX_SOURCES}
    operator_sources: dict[str, str] = {}
    for source, records in source_records.items():
        for record in records:
            operator_id = str(record["operator_id"])
            existing = operator_sources.get(operator_id)
            if existing is not None:
                raise ValueError(
                    f"Operator ID {operator_id} exists in both {existing} and "
                    f"{source.source_id}."
                )
            operator_sources[operator_id] = source.source_id
    return {
        source.output: render_index(source, records)
        for source, records in source_records.items()
    }


def generate_indexes() -> dict[Path, str]:
    indexes = expected_indexes()
    for output, content in indexes.items():
        output.write_text(content)
    return indexes


def check_indexes() -> dict[Path, str]:
    indexes = expected_indexes()
    stale = [
        output
        for output, expected in indexes.items()
        if not output.is_file() or output.read_text() != expected
    ]
    if stale:
        relative = ", ".join(str(path.relative_to(PROJECT_ROOT)) for path in stale)
        raise ValueError(
            f"Generated color indexes are missing or stale: {relative}. "
            "Run python3 generate_color_indexes.py."
        )
    return indexes


def record_count(index_text: str) -> int:
    return len(re.findall(r'^    \{"id":', index_text, flags=re.MULTILINE))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that checked-in indexes match the color source files.",
    )
    arguments = parser.parse_args()
    indexes = check_indexes() if arguments.check else generate_indexes()
    action = "Validated" if arguments.check else "Generated"
    for output, content in indexes.items():
        print(f"{action} {output.relative_to(PROJECT_ROOT)}: {record_count(content)} colors")


if __name__ == "__main__":
    main()
