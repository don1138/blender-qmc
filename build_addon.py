# Build both Blender QMC editions with: python3 build_addon.py
# Run this command from the project root. It writes QMC_<version>.zip and
# QMC_PLUS_<version>.zip beside this script, without changing the source folders.

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SHARED_SOURCE = PROJECT_ROOT / "qmc-shared"
PERSONAL_OVERLAY = PROJECT_ROOT / "qmc-personal-overlay"
SKIP_NAMES = {".DS_Store", "__pycache__"}


def version_from(source_init: Path) -> str:
    match = re.search(r'"version"\s*:\s*\(([^)]+)\)', source_init.read_text())
    if match is None:
        raise ValueError(f"Could not find a version in {source_init}.")
    return ".".join(part.strip() for part in match.group(1).split(","))


def copy_directory(source: Path, destination: Path) -> None:
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns(*SKIP_NAMES, "*.pyc", "*.pyo"),
    )


def required_personal_icons(ds_source: Path) -> set[str]:
    pattern = r'g\.c_icons\["([^"]+)"\]'
    return set(re.findall(pattern, ds_source.read_text()))


def apply_qmc_plus_overlay(addon: Path) -> None:
    ds_source = PERSONAL_OVERLAY / "color_sets" / "ds.py"
    overlay_icons = PERSONAL_OVERLAY / "icons"
    if not ds_source.is_file() or not overlay_icons.is_dir():
        raise FileNotFoundError("QMC+ needs qmc-personal-overlay/color_sets/ds.py and icons/.")

    missing_icons = [
        icon for icon in sorted(required_personal_icons(ds_source))
        if not (overlay_icons / f"{icon}.png").is_file()
    ]
    if missing_icons:
        raise FileNotFoundError(f"QMC+ is missing icon files: {', '.join(missing_icons)}")

    shutil.copy2(ds_source, addon / "color_sets" / "ds.py")
    for icon in overlay_icons.iterdir():
        if icon.is_file() and icon.name not in SKIP_NAMES:
            shutil.copy2(icon, addon / "icons" / icon.name)

    init_path = addon / "__init__.py"
    init = init_path.read_text()
    replacements = (
        (
            '"name"       : "QMC (Quick Material Colors)",',
            '"name"       : "QMC+ (Quick Material Colors Plus)",',
        ),
        (
            "# IMPORT PANELS\nfrom .color_sets.ams_595a import *",
            "# IMPORT PANELS\nfrom .color_sets.ds import *\nfrom .color_sets.ams_595a import *",
        ),
        (
            "classes = [\n   *array_int,",
            "classes = [\n   *array_int,\n   *array_ds,",
        ),
    )
    for old, new in replacements:
        if old not in init:
            raise ValueError(f"Could not prepare QMC+; expected text is missing: {old!r}")
        init = init.replace(old, new, 1)
    init_path.write_text(init)


def archive(addon: Path, archive_path: Path) -> None:
    temporary_archive = archive_path.with_suffix(".zip.tmp")
    with zipfile.ZipFile(temporary_archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zip_file:
        for path in sorted(addon.rglob("*")):
            if path.is_file() and not any(part in SKIP_NAMES for part in path.parts):
                zip_file.write(path, Path(addon.name, path.relative_to(addon)).as_posix())
    temporary_archive.replace(archive_path)


def validate_archive(archive_path: Path, addon_name: str) -> None:
    with zipfile.ZipFile(archive_path) as zip_file:
        names = set(zip_file.namelist())
    expected_init = f"{addon_name}/__init__.py"
    if expected_init not in names:
        raise ValueError(f"{archive_path.name} is not a Blender-ready add-on ZIP.")
    roots = {name.split("/", 1)[0] for name in names}
    if roots != {addon_name}:
        raise ValueError(f"{archive_path.name} has unexpected top-level files: {sorted(roots)}")


def build(addon_name: str, archive_name: str, include_personal: bool) -> Path:
    with tempfile.TemporaryDirectory(prefix="qmc-build-") as temporary_directory:
        addon = Path(temporary_directory) / addon_name
        copy_directory(SHARED_SOURCE, addon)
        if include_personal:
            apply_qmc_plus_overlay(addon)
        archive_path = PROJECT_ROOT / archive_name
        archive(addon, archive_path)
        validate_archive(archive_path, addon_name)
    return archive_path


def main() -> None:
    source_init = SHARED_SOURCE / "__init__.py"
    if not source_init.is_file():
        raise FileNotFoundError("Missing qmc-shared/__init__.py.")
    version = version_from(source_init)
    public = build("blender-qmc", f"QMC_{version}.zip", include_personal=False)
    personal = build("blender-qmc-plus", f"QMC_PLUS_{version}.zip", include_personal=True)
    print(f"Built public QMC: {public.name}")
    print(f"Built personal QMC+: {personal.name}")


if __name__ == "__main__":
    main()
