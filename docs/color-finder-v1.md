# Color Finder V1 Specification

## Purpose

Color Finder shortens the path from having an idea of a color to applying it.
V1 supports three primary tasks:

1. Find a specific color quickly.
2. Reduce the number of choices.
3. Avoid opening and manually searching multiple collections.

It also provides the data foundation for later saturation, value, and
nearest-color filtering.

## Interface

Color Finder is a persistent sub-panel inside the Quick Material Colors panel
in the 3D Viewport sidebar. It is not a floating popup. The installed add-on
version appears directly below the Quick Material Colors title and is read from
`bl_info["version"]` rather than stored as a second version string.

The top-level panel hierarchy is:

```text
Quick Material Colors
├── Version
├── Selected Nodes Only
├── Rename Material
├── Set Viewport Color
├── Set World Background
├── Color Finder
└── Browse Collections
    └── Existing collection and sub-collection panels
```

Color Finder contains:

1. A text search field.
2. Compact sort and direction controls.
3. Single-choice hue filters.
4. A collapsible, multi-select Filter by Collection section.
5. A consolidated results list.

Browse Collections wraps the existing collection panels so the entire catalog
browser can be collapsed at once. Existing top-level collection panels are
reparented from Quick Material Colors to Browse Collections. Their internal
sub-collection panels and color buttons otherwise remain unchanged in V1.

### Text search

The search field matches color names and collection names. Existing color
labels already contain catalog codes where applicable, so V1 does not require
a separate searchable or displayed code field.

Text matching is case-insensitive. Multiple query terms use AND logic: every
term must match the record's normalized search text.

### Hue filters

V1 allows one hue filter at a time:

- All
- Red
- Yellow
- Green
- Cyan
- Blue
- Magenta
- Neutral

The controls use text-only buttons. Blender's depressed-button state identifies
the active filter; no color chips appear beside the labels. The preferred
layout is:

```text
[       All       ] [    Neutral    ]
[ Red   ] [ Yellow ] [ Green       ]
[ Cyan  ] [ Blue   ] [ Magenta     ]
```

The implementation may use Blender's adaptive grid layout to reduce the column
count when the sidebar is too narrow.

Chromatic colors use six 60-degree HSV hue ranges centered on the standard RGB
and CMY hue anchors:

| Filter | Hue range |
| --- | --- |
| Red | 330 degrees through 360 degrees, and 0 degrees through 30 degrees |
| Yellow | 30 degrees through 90 degrees |
| Green | 90 degrees through 150 degrees |
| Cyan | 150 degrees through 210 degrees |
| Blue | 210 degrees through 270 degrees |
| Magenta | 270 degrees through 330 degrees |

Boundary ownership must be consistent and covered by automated validation.

Neutral is provisional in V1. The initial candidate rule is HSV saturation at
or below 10 percent. The catalog audit found too few items to justify separate
Black, Grey, and White filters under the initial thresholds, so V1 uses one
Neutral filter. Thresholds remain subject to visual review before implementation.

### Collection filters

Collections appear as persistent checkboxes in a collapsible Filter by
Collection section inside Color Finder. This is distinct from the Browse
Collections sub-panel containing the existing palette browser. Users may
select any number of collections.

- Selected collections use OR logic with each other.
- Collection, hue, and text filters use AND logic with each other.
- All selects every available collection.
- Clear selects none.

QMC and QMC Plus supply separate master color-list files. When QMC Plus is
present, Color Finder combines both indexes in memory. The shared record format
must also allow a future user-saved collection index.

### Results

Results appear in one consolidated list rather than by hiding buttons in the
existing collection panels.

Each result is a full-width apply button containing:

1. The existing color label first.
2. The collection name second.
3. A swatch icon when one is available without excessive redraw cost.

Example:

```text
5002 Ultramarine Blue - RAL Classic
```

The full color label, collection, HEX value, and HSV values should be available
in the tooltip. Clicking the row applies the color immediately. The Color
Finder remains open and preserves its query, filters, sort, visible result
count, and panel state.

Color application should use one generic indexed-color operator. It receives
the record's label and HEX value and delegates to QMC's existing color-
application function. Search results must not require a dedicated Python
operator class, because future user-created colors will not have one.

### Initial and expanded result counts

Color Finder displays no results until the user enters text or selects a hue or
collection filter that narrows the default catalog state.

The initial result limit is 50. Show More increases the visible count
cumulatively:

- Initial display: 50
- First Show More: 100 total
- Second Show More: 150 total

Changing the query, filters, sort, or direction resets the visible count to 50.
The complete matching set remains in memory.

## Search and sort pipeline

Color Finder processes a request in this order:

```text
all indexed records
-> apply collection filter
-> apply hue filter
-> apply text filter
-> rank or sort the entire matching set
-> display the first N records
-> apply a clicked record
```

Sorting always operates on the complete matching set before the visible result
limit is applied.

### Relevance

Relevance is available when the query contains text. Matches rank in this
order:

1. Exact full color-label match.
2. Color label starts with the complete query.
3. Every query term matches the color label.
4. Partial substring match in the color label.
5. Collection-name match.

Alphabetical color-label order resolves ties. Implementation may use numeric
scores, but it must preserve these observable ordering rules.

### Sort options

V1 provides:

- Relevance
- Alphabetical
- Collection

The three options appear in one dropdown, which shows only the active sort
label. A compact adjacent arrow icon toggles ascending and descending order.
The icon has an Ascending or Descending tooltip and is disabled for Relevance.

Alphabetical and Collection support ascending and descending directions.
Collection sort groups by collection name, then sorts by color label within
each collection. Relevance is disabled or unavailable when there is no text
query and always uses its defined ranking direction.

## Master color-list records

QMC and QMC Plus generate and ship separate static indexes using the same
record schema. Runtime UI code reads and combines the indexes; it does not
inspect source classes or calculate HSV values during search or panel redraw.

Each record requires:

| Key | Purpose |
| --- | --- |
| `id` | Stable record identifier unique within its source |
| `source` | Index source, such as `qmc`, `qmc_plus`, or a future user source |
| `collection_id` | Stable collection identifier used for filtering |
| `collection_name` | User-facing collection name |
| `label` | Existing user-facing color label, including code when present |
| `hex` | Original 24-bit sRGB color value |
| `hue` | Precomputed HSV hue in degrees |
| `saturation` | Precomputed HSV saturation from 0 through 100 |
| `value` | Precomputed HSV value from 0 through 100 |
| `search_text` | Pre-normalized color label and collection name |
| `operator_id` | Optional existing operator ID for validation and traceability |

The runtime apply operation uses `hex` and `label`; `operator_id` is not
required for applying a search result.

## Generation and validation

A build-time generator reads existing color operator definitions, extracts
their metadata, converts HEX to HSV once, and writes the static master lists.
The existing color files remain the source of truth and are not rewritten for
V1.

Generation must fail on:

- Missing color label.
- Missing or invalid HEX value.
- Missing collection mapping.
- Duplicate record ID within one source.
- Duplicate operator ID with conflicting values.
- HSV values outside their defined ranges.
- Hue-range gaps or overlaps caused by boundary handling.

Duplicate color labels are allowed because different collections can contain
colors with the same name.

## Catalog audit: 2026-08-09

The read-only audit parsed every `bpy.types.Operator` color definition that
calls `set_base_color()` with a literal HEX value.

### Counts

| Source | Collection file | Colors |
| --- | --- | ---: |
| QMC | `ams_595a.py` | 691 |
| QMC | `bclr.py` | 13 |
| QMC | `bsc.py` | 453 |
| QMC | `coco.py` | 183 |
| QMC | `ecc.py` | 142 |
| QMC | `f58.py` | 13 |
| QMC | `ge.py` | 10 |
| QMC | `hg71.py` | 36 |
| QMC | `mcm.py` | 29 |
| QMC | `moods.py` | 24 |
| QMC | `pcoy.py` | 58 |
| QMC | `ral.py` | 218 |
| QMC | `sw_ext.py` | 27 |
| QMC | `sw_int.py` | 21 |
| QMC | `sw_ja.py` | 8 |
| QMC | `wgsn.py` | 74 |
| QMC Plus | `ds.py` | 24 |
| **Total** | | **2,024** |

All 2,024 audited operators exposed an extractable label, operator ID, and HEX
value. There were no extraction failures.

### Duplicate findings

Five labels appear more than once with different HEX values:

- Blue Sky
- Harvest Gold
- Radiant Earth
- Saged
- Tangerine

Four are valid cross-collection name collisions. Collection identity
disambiguates them.

`Radiant Earth` is an invalid source collision in `wgsn.py`: the file defines
`WGSN_RadiantEarth` and `color.wgsn_radiant_earth` twice with different HEX
values, `#EAA6C5` and `#BA4433`. This must be resolved before generating a valid
QMC master list.

### Provisional hue distribution

Using six 60-degree hue buckets and treating saturation at or below 10 percent
as Neutral produced:

| Category | Colors |
| --- | ---: |
| Red | 464 |
| Yellow | 562 |
| Green | 166 |
| Cyan | 288 |
| Blue | 156 |
| Magenta | 73 |
| Neutral | 315 |

Within the 315 provisional Neutral records:

- 4 have value at or below 10 percent.
- 260 have value between 10 and 90 percent.
- 51 have value at or above 90 percent.

This distribution supports one Neutral filter for V1. The saturation threshold
and representative boundary colors still require visual review.

## Deferred work

Phase 2 may add numeric saturation and value filters and richer perceptual
categories such as brown. Phase 3 may add nearest-color lookup, related colors,
cross-collection alternatives, and user-saved collections.

The V1 index stores numeric HSV values so these features do not require a new
catalog format.
