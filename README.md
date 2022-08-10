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

## Swatches (219 Colors)

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
- These colors were calculated for best use on automobiles.

### General Electric
- These colors were calculated for best use on home appliances.
- **Avacado** greens and **Harvest** yellows are as close to 60s and 70s era-correct as I've yet found.

### House & Garden 1971, Mid-Century Modern
- These colors were calculated for best use on interior walls.
- The **MCM** blues, greens, reds, and browns are also great starters for terrains.

### Moods, Suburban Modern Interior, The Jazz Age
- These colors were calculated for best use on interior walls.
- IMO, the **Moods** colors also work well as `World` colors.

### Pantone Color of the Year
- These colors are calculated for use in print and digital design.
- They might look over-saturated and garish on large objects, but can pop nicely on small objects and details.
- I use **Sand Dollar**, **2020 Bleached Coral**, and **2043 Dead Coral** a lot.
- [**The Ugliest Color in the World**](https://www.huffpost.com/entry/ugliest-color-pantone_n_57570df6e4b0ca5c7b504538) is nice for for dirt, cracks, or crevices.

### Suburban Modern Exterior
- These colors were calculated for best use on building exteriors.
- Each of the nine sets provides a **Body**, **Trim**, and **Accent** color.

## Attributions

- **Ford Colors 1958** is sourced from a scan of vintage promotional material found online.
- **General Electric** is sourced from [**General Electric Paint Cross-Reference** (paintref.com)](https://paintref.com/cgi-bin/colorcodedisplay.cgi?model=General%20Electric).
- **Mid-Century Modern** is sourced from [**7 Paint Colors That Nail the Midcentury Modern Look** (dwell.com)](https://www.dwell.com/article/best-midcentury-modern-paint-colors-111e82a1).
- **House & Garden Colors 1971** is sourced from a scan of a vintage magazine cover found online.
- **Moods** is sourced from [**Paint Colors For Every Mood** (domino.com)](https://www.domino.com/content/paint-colors-for-every-mood).
- **Pantone Color of the Year** is sourced from the [**Pantone**](https://www.pantone.com/articles/past-colors-of-the-year) website.
- **Suburban Modern Exterior** is sourced from [**Exterior Color Schemes** (sherwin-williams.com)](https://www.sherwin-williams.com/homeowners/color/find-and-explore-colors/paint-colors-by-collection/exterior-color-schemes/suburban-modern).
- **Suburban Modern Interior** is sourced from [**Historic Paint Colors** (sherwin-williams.com)](https://www.sherwin-williams.com/en-us/color/color-collections/historic-paint-colors).

<br><br>
<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-qmc">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-qmc">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-qmc/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/52e50c70eb6c2d9d025cc8b7bf8f3c40ddf5b214.svg" alt="Repobeats analytics image">
</p>
