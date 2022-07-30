<h1>Blender QMC (Quick Material Colors)</h1>

Blender Add-ons That Assign a Custom Color to a Principled BSDF's Base Color

<!-- ## F58 (Ford Colors 1958)

![Blender F58 Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-f58.jpg)
 -->
## HG71 (House & Garden Colors 1971)

![Blender HG71 Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-hg71.jpg)

## MCMC (Mid-Century Modern Colors)

![Blender MCMC Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-mcmc.jpg)

## MC (More Colors)

![Blender MCMC Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-mc.jpg)

## PCOY (Pantone Color of the Year)

![Blender PCOY Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-pcoy.jpg)

## Installation

Download the latest ZIPs from **Releases**.

Install them **individually** via ``Edit > Preferences > Add-ons > Install…``.

Once activated, a new tab named **MAT** will appear in the 3D viewport sidebar.
<!-- - **F58** creates a panel named **Ford Colors** -->
- **HG71** creates a panel named **House & Garden 1971**
- **MCMC** creates a panel named **Mid-Century Modern Colors**
- **MC** creates a panel named **More Colors** contianing these color sets:
  - **Ford 1958**
  - **General Electric**
  - **Moods**
  - **Suburban Modern**
  - **The Jazz Age**
- **PCOY** creates a panel named **Pantone Color of the Year**

## Usage

Select an object in your view, and click a button to assign that color to it.

Set the ``Rename Material`` checkbox to ``True`` to change the material name.

## Caveats & Warnings

**These add-ons do one very specific thing:**

They set the Base Color of the Principled BSDF Shader node specifically named "Principled BSDF" -- which is created by default with all new materials -- to a custom color. It will also change the Base Color of a Diffuse BSDF material as well as the **Plaster** material. It also sets the object's `Viewport Display > Color` to the same color.

**This add-on will only affect the Active Material of the Currently Selected Object.**

The operation will fail if:
- No object is selected
- The active object has no material
- The active material does not include a Principled BSDF Shader named "Principled BSDF" or a Diffuse BSDF Shader named "Diffuse BSDF"

## Usage Notes

### House & Garden 1971 & Mid-Century Modern Colors
These colors were calculated for best use on interior walls. The **MCMC** blues, greens, reds, and browns are also great starters for terrains.

### More Colors
**Ford 1958** colors were calculated for best use on automobiles

**General Electric** colors were calculated for best use on home appliances. **Avacado** greens and **Harvest** yellows are as close to 60s and 70s era-correct as I've yet found.

**Moods**, **Suburban Modern**, and **The Jazz Age** colors were calculated for best use on interior walls. IMO, the **Moods** colors also work well as `World` colors.

### Pantone Color of the Year
These colors are calculated for use in print and digital design. They might look over-saturated and garish on large objects, but can pop nicely on small objects and details.

I use **Sand Dollar**, **2020 Bleached Coral**, and **2043 Dead Coral** a lot. [**The Ugliest Color in the World**](https://www.huffpost.com/entry/ugliest-color-pantone_n_57570df6e4b0ca5c7b504538) is nice for for dirt, cracks, or crevices.

## Attributions

- **Pantone Color of the Year** is sourced from [the Pantone website](https://www.pantone.com/articles/past-colors-of-the-year).
- **Mid-Century Modern Colors** is sourced from [**7 Paint Colors That Nail the Midcentury Modern Look**](https://www.dwell.com/article/best-midcentury-modern-paint-colors-111e82a1) on **Dwell.com**.
- **House & Garden Colors 1971** is sourced from a scan of a vintage magazine cover found online.
- **Ford Colors 1958** is sourced from a scan of vintage promotional material found online.
- **More Colors** is sourced from [Sherwin Williams Historic Paint Colors](https://www.sherwin-williams.com/en-us/color/color-collections/historic-paint-colors), [Sherwin Williams Exterior Color Schemes](https://www.sherwin-williams.com/homeowners/color/find-and-explore-colors/paint-colors-by-collection/exterior-color-schemes/suburban-modern),  [Paintref.com General Electric Paint Cross-Reference](https://paintref.com/cgi-bin/colorcodedisplay.cgi?model=General%20Electric), and [Paint Colors For Every Mood](https://www.domino.com/content/paint-colors-for-every-mood).

<br><br>
<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-qmc">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-qmc">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-qmc/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/52e50c70eb6c2d9d025cc8b7bf8f3c40ddf5b214.svg" alt="Repobeats analytics image">
</p>
