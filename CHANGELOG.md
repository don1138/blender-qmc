# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.17.0] - 2026-09-04

### Added

- Added the 46-color **QMC Select** collection to the public QMC edition

### Changed

- Moved the former **Don1138 Select > Also** colors into **QMC Select**
- Kept **Don1138 Select > True** and **Don1138 Select > Safe** exclusive to QMC Plus

## [1.16.2] - 2026-08-14

### Changed

- Moved the version number into the main panel title.

## 1.16.1 - 2026-08-10

### Changed

- Changed panel category from **MAT** to **Quick Tools**

## 1.16.0 - 2026-08-09

### Added

- Added a persistent **Color Finder** for searching colors by name, catalog code, or collection
- Added filters for collection, six HSV hue families, and neutral colors
- Added relevance, alphabetical, and collection sorting with cumulative **Show More** results
- Added **Don1138 Select** results to Color Finder when using QMC Plus
- Added the installed QMC version to the main panel

### Changed

- Kept Color Finder controls and results open while trying different colors
- Grouped existing palette panels under a collapsible **Browse Collections** panel

### Fixed

- Fixed a duplicate **Radiant Earth** definition in **WGSN & Coloro Color Trends**

## 1.15.1 - 2026-08-09

### Fixed

- Fixed custom icon preview cleanup when disabling, reloading, or reinstalling the add-on

## [1.15.0] - 2026-07-14

### Added

- Added support for selected utility and texture nodes with writable color inputs
- Added support for setting the **B** color input on selected Mix nodes
- Added **9 WGSN & Coloro colors** for **2027** and **2028**
  - 4 colors for 2027
  - 5 colors for 2028

### Changed

- Updated minimum supported Blender version to **4.5.0**
- Improved color application across Blender 4.5+ and 5.2+
  - Find shader nodes by node type instead of editable node name
  - Add safer handling for missing objects, materials, worlds, and node trees
  - Preserve automatic material fallback order: Principled BSDF, Diffuse BSDF, then Emission
- Improved error messages

### Fixed

- Removed duplicate color helper code

## [1.14.0] - 2025-12-05

### Added

- Added **Cloud Dancer** to **Pantone Color of the Year**

## 1.13.0 - 2025-07-13

### Added

- Added **Cosmic Spectrum Green** to **Don1138 Select**

## [1.12.0] - 2025-07-08

### Added

- Added **WGSN & Coloro Color Trends** set of 64 colors

## [1.11.1] - 2025-03-29

### Changed

- Reordered **British Standard Colors** sets by year

### Fixed

- Fixed spelling of **9097 Dark Admiralty Grey**
- Fixed acronym capitalization for **633 RAF Blue Grey** and **636 PRU Blue**
  - **RAF**: Royal Air Force
  - **PRU**: Photographic Reconnaissance Unit (RAF)

## [1.11.0] - 2025-03-15

### Added

- Added **Best Colors for Living Rooms** set of 13 colors

## [1.10.0] - 2024-12-06

### Added

- Added **Mocha Mousse** to **Pantone Color of the Year**

## [1.9.0] - 2024-11-27

### Added

- Added Blender 4.3.0 compatibility
  - Added support for **Metallic BSDF**

### Changed

- Updated **Don1138 Select** in **QMC+**
  - Reorganized menus

### Fixed

- Fixed issues in **Don1138 Select**
- Renamed `deeply_uncomfotable` to `deeply_uncomfortable`

## [1.8.0] - 2024-08-11

### Changed

- Refactored code

## [1.7.0] - 2024-08-08

### Added

- Added **Set Viewport Color** checkbox
  - When selected, changes the **Viewport Color** of the material

### Changed

- Renamed **Selected Node** to **Selected Nodes Only**
- Renamed **World Background** to **Set World Background**

## [1.6.0] - 2024-07-05

### Added

- Added **COCO Segmentation** set of 183 colors
- Added **Emission Shader** to the chain of affected shader nodes
  - If a Principled BSDF node is found, change Base Color and exit
  - Otherwise, if a Diffuse node is found, change Base Color and exit
  - Otherwise, if an Emission node is found, change Base Color and exit

## [1.5.1] - 2024-03-18

### Fixed

- Fixed color chip names

## [1.5.0] - 2024-03-15

### Added

- Added **British Standard Colors** set of 453 colors
  - **BS 2660 (1964)** - 96 colors
  - **BS 381C (1930)** - 119 colors
  - **BS 5252 (1976)** - 238 colors

## [1.4.0] - 2024-03-14

### Added

- Added **Exotic Car Colors** set of 142 colors
  - **Audi** - 1 color
  - **Ferrari** - 25 colors
  - **Lamborghini** - 63 colors
  - **McLaren** - 19 colors
  - **Porsche** - 34 colors
- Added **Cosmic Latte** to **Don1138 Select**

## [1.3.0] - 2023-12-07

### Added

- Added **Peach Fuzz** to **Pantone Color of the Year**

## [1.2.6] - 2023-09-28

### Added

- Added **AMS (Aerospace Material Specification) Standard 595A** set of 692 colors

## [1.2.5] - 2022-12-18

### Changed

- Refactored code

## [1.2.4] - 2022-12-02

### Added

- Added **Viva Magenta** to **Pantone Color of the Year**

### Changed

- Indented names of subcategories to improve legibility:
  - **House & Garden 1971**
  - **Mid-Century Modern**
  - **Moods**
  - **Pantone Color of the Year**
  - **RAL Classic**
  - **Suburban Modern Exterior**

## 1.2.3 - 2022-11-15

### Added

- Added **Baker-Miller Pink** to **QMC Plus** > **Don1138 Select**
- Added **Energy Conservation** node group to the list of affected nodes

### Changed

- Refactored code

## [1.2.2] - 2022-10-17

### Added

- Added `ShaderNodeRGB` to nodes affected by the **All Selected Materials** checkbox

## [1.2.1] - 2022-08-19

### Changed

- Optimized `color_functions.py`
  - Thanks to **iceythe** on [**Blender Artists**](https://blenderartists.org/t/roast-my-code-color-switcher/1397799/3) for code review

## [1.2.0] - 2022-08-18

### Added

- Added **All Selected Materials** checkbox
  - When selected, changes the **Base Color** of all selected shader nodes
  - Ignores nodes that do not have a **Base Color** attribute

## [1.1.0] - 2022-08-12

### Added

- Added **RAL Classic** set of 218 colors

### Changed

- Set Parent Panel default to open

## [1.0.3] - 2022-08-09

### Changed

- Renamed all instances of `QMC_MCMC` to `QMC_MCM`
- Renamed panel label **Mid-Century Modern Colors** to **Mid-Century Modern**

## [1.0.2] - 2022-08-03

### Added

- Added error detection for missing `World`

## [1.0.1] - 2022-08-02

### Changed

- Merged **colors** and **panels** files into unified **color_sets** files

## [1.0.0] - 2022-08-01

### Added

- Migrated all color sets into one add-on:
  - **Ford 1958**
  - **House & Garden 1971**
  - **General Electric**
  - **Mid-Century Modern**
  - **Moods**
  - **Pantone Color of the Year**
  - **Suburban Modern Exterior**
  - **Suburban Modern Interior**
  - **The Jazz Age**

### Changed

- Moved color sets into separate files
  - Each color set gets a **colors** file and a **panels** file

## [0.10.0] - 2022-08-01

### Added

- Added **World Background** option to change the World Background shader color

### Changed

- Moved color set classes and color functions to separate files

## [0.9.0] - 2022-07-30

### Changed

- Moved the **FC** color set into **MC**

### Removed

- Deprecated the standalone **F58 (Ford Colors 1958)** add-on after moving its color set to **MC**

## [0.8.0] - 2022-07-27

### Added

- Added **Moods** color set:
  - **Relaxed**
    - Blue 02
    - Blue 08
    - Green 02
    - Pink 04
  - **Energy**
    - Green 07
    - Green 08
    - Green 13
    - Yellow 06
  - **Cozy**
    - Beige 02
    - Beige 03
    - Pink 07
    - Pink 08
  - **Focus**
    - Blue 06
    - Blue 07
    - Blue 17
    - Blue 111
  - **Moody**
    - Black 01
    - Purple 03
    - Red 03
    - Teal 03
  - **Whites**
    - White 01
    - White 02
    - White 03
    - White 04

## [0.7.0] - 2022-05-27

### Changed

- Reorganized colors by hue
- Renamed **Suburban Modern Interior** to **Suburban Modern**

### Removed

- Removed **Suburban Modern Exterior**

## [0.6.0] - 2022-05-27

### Added

- Added support for changing Diffuse BSDF materials
- Added **More Colors** add-on with 86 colors in four categories:
  - Suburban Modern Interior
  - Suburban Modern Exterior
  - The Jazz Age
  - General Electric

## [0.5.1] - 2022-04-28

### Changed

- Renamed repository to **Blender QMC (Quick Material Colors)**

### Fixed

- Fixed conflicting property names when renaming materials in **MCMC**, **HG71**, and **F58**

### Added

- Version 0.5.0 added support for changing **QMM Plaster** material colors

## [0.4.2] - 2022-03-15

### Added

- Added **Pantone Freedom Blue** for Ukraine
- Added **Pantone Energizing Yellow** for Ukraine

## [0.4.0] - 2021-12-14

### Added

- Added **2022 Very Peri** to **Pantone Color of the Year**
- Created **HG71**
- Created **F58**

### Changed

- Changed `bl_category` to **MAT**

## [0.3.0] - 2021-08-09

### Added

- Added custom color chip icons

### Changed

- Updated `UILayout`
- Updated PCOY material renaming so the year is no longer added to the material name

## [0.2.2] - 2021-07-15

### Changed

- Added unique class names for checkbox booleans

> GitHub release: **Blender PCOY 0.2.2 & MCMC 0.1.2**

## [0.2.1] - 2021-07-11

### Added

- Added error detection

> GitHub release: **Blender PCOY 0.2.1 & MCMC 0.1.1**

## [0.2.0] - 2021-07-10

### Added

- Added **Rename Material** option

> GitHub tag: `v0.2.0-pcoy`

## [0.1.0-pcoy] - 2021-06-22

### Added

- Initial release of **Blender PCOY**

## [0.1.0-mcmc] - 2021-07-10

### Added

- Initial release of **Blender MCMC**

[1.16.2]: https://github.com/don1138/blender-qmc/releases/tag/v1.16.2
[1.15.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.15.0
[1.14.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.14.0
[1.12.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.12.0
[1.11.1]: https://github.com/don1138/blender-qmc/releases/tag/v1.11.1
[1.11.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.11.0
[1.10.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.10.0
[1.9.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.9.0
[1.8.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.8.0
[1.7.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.7.0
[1.6.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.6.0
[1.5.1]: https://github.com/don1138/blender-qmc/releases/tag/v1.5.1
[1.5.0]: https://github.com/don1138/blender-qmc/releases/tag/V1.5.0
[1.4.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.4.0
[1.3.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.3.0
[1.2.6]: https://github.com/don1138/blender-qmc/releases/tag/v1.2.6
[1.2.5]: https://github.com/don1138/blender-qmc/releases/tag/v1.2.5
[1.2.4]: https://github.com/don1138/blender-qmc/releases/tag/v1.2.4
[1.2.2]: https://github.com/don1138/blender-qmc/releases/tag/v1.2.2
[1.2.1]: https://github.com/don1138/blender-qmc/releases/tag/v1.2.1
[1.2.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.2.0
[1.1.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.1.0
[1.0.3]: https://github.com/don1138/blender-qmc/releases/tag/v1.0.3
[1.0.2]: https://github.com/don1138/blender-qmc/releases/tag/v1.0.2
[1.0.1]: https://github.com/don1138/blender-qmc/releases/tag/v1.0.1
[1.0.0]: https://github.com/don1138/blender-qmc/releases/tag/v1.0.0
[0.10.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.10.0
[0.9.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.9.0
[0.8.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.8.0
[0.7.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.7.0
[0.6.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.6.0
[0.5.1]: https://github.com/don1138/blender-qmc/releases/tag/v0.5.1
[0.4.2]: https://github.com/don1138/blender-qmc/releases/tag/v0.4.2
[0.4.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.4.0
[0.3.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.3.0
[0.2.2]: https://github.com/don1138/blender-qmc/releases/tag/v0.2.2
[0.2.1]: https://github.com/don1138/blender-qmc/releases/tag/v0.2.1
[0.2.0]: https://github.com/don1138/blender-qmc/releases/tag/v0.2.0-pcoy
[0.1.0-pcoy]: https://github.com/don1138/blender-qmc/releases/tag/v0.1.0-pcoy
[0.1.0-mcmc]: https://github.com/don1138/blender-qmc/releases/tag/v0.1.0-mcmc
