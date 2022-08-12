<h1>Blender QMC (Quick Material Colors)</h1>

Blender Add-on That Assign a Custom Color to a Material

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc.png)

## Installation

- Download the latest ZIP from **Releases**.
- Install  via ``Edit > Preferences > Add-ons > Install…``.

Once activated, a panel named **Quick Material Colors** will appear in the **MAT** tab in the 3D viewport sidebar.

## Usage

- Select an object in your view, and click one of the buttons to assign that color to it.
- Set the **World Background** checkbox to `True` and the button will assign that color to the `World > Background Shader > Color`.
- Set the **Rename Material** checkbox to `True` to change the material or world name.

## Caveats & Warnings

**This add-on does one very specific thing:**

It sets the **Base Color** of the following Nodes to a custom color.

- A **Principled BSDF Shader** node specifically named `Principled BSDF` -- which is created by default with all new materials
- A **Diffuse BSDF Shader** named `Diffuse BSDF`
- The [**Blender QMM**](https://github.com/don1138/blender-qmm) **Plaster** material
- The current `World's` **Background Shader** named `Background`

It also sets the material or the world's `Viewport Display > Color` to the same color.

**This add-on will only affect the Active Material of the Currently Selected Object.**

The operation will fail if:
- No object is selected
- The active object has no material
- The active material does not include a **Principled BSDF Shader** named `Principled BSDF` or a **Diffuse BSDF Shader** named `Diffuse BSDF`

And if no `World` is set, changing the **World Background** will cause an error.

## Swatches (437 Colors)

### Ford 1958 (13 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-f58.jpg)
```
- A Raven Black
- B Desert Beige
- D Palamino Tan
- E Colonial White
- F Silvertone Green
- G Sun Gold
- H Gunmetal Gray
- J Bali Bronze
- L Azure Blue
- M Gulfstream Blue
- N Seaspray Green
- R Torch Red
- T Silvetone Blue
```
### General Electric (11 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-ge.jpg)
```
- Avacado
- Awacado Light
- Avacado Dark
- Coppertone A
- Dark Coppertone A
- Coppertone B
- Dark Coppertone B
- Harvest Gold
- Harvest Light
- Harvest Dark
```
### House & Garden 1971 (36 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-hg71.jpg)
```
- Yellows
  - Pineapple
  - Sun Yellow
  - Kumquat
  - Goldenrod
  - Antique Gold
  - Maple Sugar
  - Pongee
- Greens
  - Moss Green
  - Lacquer Green
  - Green Mint
  - Parrot Green
  - Lettuce
  - Celery
- Blues
  - Midnight Blue
  - Ultramarine Blue
  - Space Blue
  - Blue Opaline
  - Blue Sky
  - Aquamarine Blue
- Oranges
  - Bittersweet
  - Tangerine
  - Pompeiian Red
  - Zinnia
  - Creamy Apricot
  - Velvet Brown
- Reds
  - Flag Red
  - Pink Coral
  - Pink Pink
  - Azalea
- Purples
  - Beach Plum
  - African Violet
  - Lavender
- Grays
  - Oyster White
  - Mercury
  - Mushroom
  - Black Pearl
```
### Mid-Century Modern (29 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-mcm.jpg)
```
- Golden Yellow
  - Miami Parasol
  - Ginger Ale
  - Pablo Honey
  - Tanlines
- Serena Aqua
  - Blue Seafoam
  - Novelty Wave
  - Saturday On Sunday
  - Sicily Or Cyprus
- Olive Green & Wasabi
  - Natural Habitat
  - Saged
  - Drive-Thru Safari
  - Green Root
  - Relentless Olive
- Pops of Red
  - Cherokee Red
  - Self-Portrait
  - Negroni
  - Lipstick on the Mirror
- Tangerine and Ochre
  - Aperitivo Hour
  - Bright Marigold
  - Autumn Glimmer
  - Orange Fruit
- Pewter Gray
  - Wright Soft Gray
  - No Curfew
  - Motor Gray
  - After Hours
- Soft and Earthy Brown
  - Fawn Doe
  - Sentimental Reasons
  - Cobblestone Streets
  - Cocoa Shell
```
### Moods (20 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-moods.jpg)
```
- Relaxed
  - Blue 02
  - Blue 08
  - Green 02
  - Pink 1014
- Energy
  - Green 07
  - Green 08
  - Green 13
  - Yellow 06
- Cozy
  - Beige 02
  - Beige 03
  - Pink 07
  - Pink 08
- Focus
  - Blue 06
  - Blue 07
  - Blue 17
  - Blue 111
- Moody
  - Black 01
  - Purple 03
  - Red 03
  - Tea 03
```
### Pantone Color of the Year (54 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-pcoy.jpg)
```
- 2000-09
  - Cerulean Blue
  - Fuschia Rose
  - True Red
  - Aqua Sky
  - Tigerlily
  - Blue Turquoise
  - Sand Dollar
  - Chili Pepper
  - Blue Iris
  - Mimosa
- 2010-19
  - Turquoise
  - Honeysuckle
  - Tangerine
  - Emerald
  - Radiant Orchio
  - Marsala
  - Rose Quartz
  - Serenity
  - Greenery
  - Ultra Violet
  - Living Coral
- 2020-29
  - Classic Blue
  - Ultimate Gray
  - Illuminating
  - Very Peri
- SS2022 London
  - Cascade
  - Coral Rose
  - Super Sonic
  - Popcorn
  - Potpourri
  - Bubblegum
  - Sudan Brown
  - Fragile Sprou
  - Orchid Bloom
  - Coffee Quartz
- SS2022 New York
  - Spun Sugar
  - Gossamer Pink
  - Innuendo
  - Skydiver
  - Daffodil
  - Glacier Lake
  - Harbor Blue
  - Coca Mocha
  - Dahlia
  - Poinciana
```
### RAL Classic (218 Colors)
[**View swatches on Wikipedia**](https://en.wikipedia.org/wiki/List_of_RAL_colors#RAL_Classic)

```
- RAL Classic Yellow
  - 1000 Green Beige
  - 1001 Beige
  - 1002 Sand Yellow
  - 1003 Signal Yellow
  - 1004 Golden Yellow
  - 1005 Honey Yellow
  - 1006 Green Beige
  - 1007 Beige
  - 1008 Sand Yellow
  - 1009 Green Beige
  - 1010 Beige
  - 1011 Brown Beige
  - 1012 Lemon Yellow
  - 1013 Oyster White
  - 1014 Ivory
  - 1015 Light Ivory
  - 1016 Sulfur Yellow
  - 1017 Saffron Yellow
  - 1018 Zinc Yellow
  - 1019 Grey Beige
  - 1020 Olive Yellow
  - 1021 Rope Yellow
  - 1023 Traffic Yellow
  - 1024 Ochre Yellow
  - 1026 Luminous Yellow
  - 1027 Curry
  - 1028 Melon Yellow
  - 1032 Broom Yellow
  - 1033 Dahlia Yellow
  - 1034 Pastel Yellow
  - 1035 Pearl Beige
  - 1036 Pearl Gold
  - 1037 Sun Yellow

- RAL Classic Orange
  - 2000 Yellow Orange
  - 2001 Red Orange
  - 2002 Vermilion
  - 2003 Pastel Orange
  - 2004 Pure Orange
  - 2005 Luminous Orange
  - 2007 Luminous Bright Orange
  - 2008 Bright Red Orange
  - 2009 Traffic Orange
  - 2010 Signal Orange
  - 2011 Deep Orange
  - 2012 Salmon Orange
  - 2013 Pearl Orange
  - 2017 RAL Orange

- RAL Classic Red
  - 3000 Flame Red
  - 3001 Signal Red
  - 3002 Carmine Red
  - 3003 Ruby Red
  - 3004 Purple Red
  - 3005 Wine Red
  - 3007 Black Red
  - 3008 Oxide Red
  - 3009 Oxide Red
  - 3011 Brown Red
  - 3012 Beige Red
  - 3013 Tomato Red
  - 3014 Antique Pink
  - 3015 Light Pink
  - 3016 Coral Red
  - 3017 Rose
  - 3018 Strawberry Red
  - 3020 Traffic Red
  - 3022 Salmon Pink
  - 3024 Luminous Red
  - 3026 Luminous Bright Red
  - 3027 Raspberry Red
  - 3028 Pure Red
  - 3031 Orient Red
  - 3032 Pearl Ruby Red
  - 3033 Pearl Pink

- RAL Classic Violet
  - 4001 Red Lilac
  - 4002 Red Violet
  - 4003 Heather Violet
  - 4004 Claret Violet
  - 4005 Blue Lilac
  - 4006 Traffic Purple
  - 4007 Purple Violet
  - 4008 Signal Violet
  - 4009 Pastel Violet
  - 4010 Telemagenta
  - 4011 Pearl Violet
  - 4012 Pearl Blackberry

- RAL Classic Blue
  - 5000 Violet Blue
  - 5001 Green Blue
  - 5002 Ultramarine Blue
  - 5003 Sapphire Blue
  - 5004 Black Blue
  - 5005 Signal Blue
  - 5007 Brilliant Blue
  - 5008 Grey Blue
  - 5009 Azure Blue
  - 5010 Gentian Blue
  - 5011 Steel Blue
  - 5012 Light Blue
  - 5013 Cobalt Blue
  - 5014 Pigeon Blue
  - 5015 Sky Blue
  - 5017 Traffic Blue
  - 5018 Turquoise Blue
  - 5019 Capri Blue
  - 5020 Ocean Blue
  - 5021 Water Blue
  - 5022 Night Blue
  - 5023 Distant Blue
  - 5024 Pastel Blue
  - 5025 Pearl Gentian Blue
  - 5026 Pearl Night Blue

- RAL Classic Green
  - 6000 Patina Green
  - 6001 Emerald Green
  - 6003 Olive Green
  - 6004 Blue Green
  - 6005 Moss Green
  - 6006 Grey Olive
  - 6007 Bottle Green
  - 6008 Brown Green
  - 6009 Fir Green
  - 6010 Grass Green
  - 6011 Reseda Green
  - 6012 Black Green
  - 6013 Reed Green
  - 6014 Yellow Olive
  - 6015 Black Olive
  - 6016 Turquoise Green
  - 6017 May Green
  - 6018 Yellow Green
  - 6019 Pastel Green
  - 6020 Chrome Green
  - 6021 Pale Green
  - 6022 Olive-Drab/Brown Olive
  - 6024 Traffic Green
  - 6025 Fern Green
  - 6026 Opal Green
  - 6027 Light Green
  - 6028 Pine Green
  - 6029 Mint Green
  - 6032 Signal Green
  - 6033 Mint Turquoise
  - 6034 Pastel Turquoise
  - 6035 Pearl Green
  - 6036 Pearl Opal Green
  - 6037 Pure Green
  - 6038 Luminous Green

- RAL Classic Grey
  - 7000 Squirrel Grey
  - 7001 Silver Grey
  - 7002 Olive Grey
  - 7003 Moss Grey
  - 7004 Signal Grey
  - 7005 Mouse Grey
  - 7006 Beige Grey
  - 7008 Khaki Grey
  - 7009 Green Grey
  - 7010 Tarpaulin Grey
  - 7011 Iron Grey
  - 7012 Basalt Grey
  - 7013 Brown Grey
  - 7015 Slate Grey
  - 7016 Anthracite Grey
  - 7021 Black Grey
  - 7022 Umbra Grey
  - 7023 Concrete Grey
  - 7024 Graphite Grey
  - 7026 Granite Grey
  - 7030 Stone Grey
  - 7031 Blue Grey
  - 7032 Pebble Grey
  - 7033 Cement Grey
  - 7034 Yellow Grey
  - 7035 Light Grey
  - 7036 Platinum Grey
  - 7037 Dusty Grey
  - 7038 Agate Grey
  - 7039 Quartz Grey
  - 7040 Window Grey
  - 7042 Traffic Grey
  - 7043 Traffic Grey
  - 7044 Silk Grey
  - 7045 Telegrey 1
  - 7046 Telegrey 2
  - 7047 Telegrey 4
  - 7048 Pearl Mouse Grey

- RAL Classic Brown
  - 8000 Green Brown
  - 8001 Ochre Brown
  - 8002 Signal Brown
  - 8003 Clay Brown
  - 8004 Copper Brown
  - 8007 Fawn Brown
  - 8008 Olive Brown
  - 8011 Nut Brown
  - 8012 Red Brown
  - 8014 Sepia Brown
  - 8015 Chestnut Brown
  - 8016 Mahogany Brown
  - 8017 Chocolate Brown
  - 8019 Grey Brown
  - 8022 Black Brown
  - 8023 Orange Brown
  - 8024 Beige Brown
  - 8025 Pale Brown
  - 8028 Terra Brown
  - 8029 Pearl Copper

- RAL Classic White/Black
  - 9001 Cream
  - 9002 Grey White
  - 9003 Signal White
  - 9004 Signal Black
  - 9005 Jet Black
  - 9006 White Aluminium
  - 9007 Grey Aluminium
  - 9010 Pure White
  - 9011 Graphite Black
  - 9012 Clean Room White
  - 9016 Traffic White
  - 9017 Traffic Black
  - 9018 Papyrus White
  - 9022 Pearl Light Grey
  - 9023 Pearl Dark Grey
```

### Suburban Modern Exterior (27 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-sme.jpg)
```
- Set A
  - Birdseye Maple
  - Cocoon
  - Olde World Gold
- Set B
  - Wool Skein
  - Artisan Tan
  - Status Bronze
- Set C
  - Tatami Tan
  - Colony Buff
  - Homburg Gray
- Set D
  - Muslin
  - Straw Harvest
  - Rural Green
- Set E
  - Extra White
  - Rushing River
  - Spiced Cider
- Set F
  - Retreat
  - Netsuke
  - Edgy Gold
- Set G
  - Jogging Path
  - Intellectual Gray
  - Thunder Gray
- Set H
  - Anjou Pear
  - Jersey Cream
  - warm Stone
- Set J
  - Cork Wedge
  - Smokehouse
  - Rustic Red
```
N.B. These sets are designed to be used as follows:
```
- Set
  - Body / Wall
  - Trim
  - Accent
```
### Suburban Modern Interior (21 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-smi.jpg)
```
- Pink Flamingo
- Apple Blossom
- Caribbean Coral
- Fairtax Brown
- Pinky Beige
- Beige
- Harvest Gold
- New Colonial Yellow
- Sycamore Tan
- Peace Yellow
- Sunbeam Yellow
- Chartreuse
- Avocado
- Sage
- Sage Green Light
- Holiday Turquoise
- Powder Blu
- Radiant Lilac
- Chelsea Gray
- Westchester Gray
- Classic French Gray
```
### The Jazz Age (8 Colors)

![Blender QMC](https://github.com/don1138/blender-qmc/blob/main/imx/blender-qmc-ja.jpg)
```
- Salon Rose
- Chinese Red
- Studio Mauve
- Jazz Age Coral
- Frostwork
- Alexandrite
- Blue Peacock
- Blue Sky
```

## Usage Notes

### Ford 1958
- These colors are calculated for best use on automobiles.

### General Electric
- These colors are calculated for best use on home appliances.
- **Avacado** greens and **Harvest** yellows are as close to 60s and 70s era-correct as I've yet found.

### House & Garden 1971, Mid-Century Modern
- These colors are calculated for best use on interior walls.
- The **MCM** blues, greens, reds, and browns are also great starters for terrains.

### Moods, Suburban Modern Interior, The Jazz Age
- These colors are calculated for best use on interior walls.
- IMO, the **Moods** colors also work well as `World` colors.

### RAL Classic
- These colors are calculated for use as varnish, powder coating, and plastics.
- They look, like, *really* good in high-contrast Filmic renders.

### Pantone Color of the Year
- These colors are calculated for use in print and digital design.
- They might look over-saturated and garish on large objects, but can pop nicely on small objects and details.
- I use **Sand Dollar**, **2020 Bleached Coral**, and **2043 Dead Coral** a lot.
- [**The Ugliest Color in the World**](https://www.huffpost.com/entry/ugliest-color-pantone_n_57570df6e4b0ca5c7b504538) is nice for for dirt, cracks, or crevices.

### Suburban Modern Exterior
- These colors are calculated for best use on building exteriors.
- Each of the nine sets provides a **Body**, **Trim**, and **Accent** color.

## Attributions

- **Ford Colors 1958** is sourced from a scan of vintage promotional material found online.
- **General Electric** is sourced from [**General Electric Paint Cross-Reference** (paintref.com)](https://paintref.com/cgi-bin/colorcodedisplay.cgi?model=General%20Electric).
- **Mid-Century Modern** is sourced from [**7 Paint Colors That Nail the Midcentury Modern Look** (dwell.com)](https://www.dwell.com/article/best-midcentury-modern-paint-colors-111e82a1).
- **House & Garden Colors 1971** is sourced from a scan of a vintage magazine cover found online.
- **Moods** is sourced from [**Paint Colors For Every Mood** (domino.com)](https://www.domino.com/content/paint-colors-for-every-mood).
- **Pantone Color of the Year** is sourced from the [**Pantone**](https://www.pantone.com/articles/past-colors-of-the-year) website.
- **RAL Classic** is sourced from the [**List of RAL colors**](https://en.wikipedia.org/wiki/List_of_RAL_colors#RAL_Classic) page on Wikipedia.
- **Suburban Modern Exterior** is sourced from [**Exterior Color Schemes** (sherwin-williams.com)](https://www.sherwin-williams.com/homeowners/color/find-and-explore-colors/paint-colors-by-collection/exterior-color-schemes/suburban-modern).
- **Suburban Modern Interior** is sourced from [**Historic Paint Colors** (sherwin-williams.com)](https://www.sherwin-williams.com/en-us/color/color-collections/historic-paint-colors).

<br><br>
<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-qmc">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-qmc">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-qmc/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/52e50c70eb6c2d9d025cc8b7bf8f3c40ddf5b214.svg" alt="Repobeats analytics image">
</p>
