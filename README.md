<h1>Blender QMC (Quick Material Colors)</h1>

Blender Add-ons That Assign a Custom Color to a Principled BSDF's Base Color

## PCOY (Pantone Color of the Year)

![Blender PCOY Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-pcoy.jpg)

## MCMC (Mid-Century Modern Colors)
 
![Blender MCMC Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-mcmc.jpg)

## HG71 (House & Garden Colors 1971)
 
![Blender HG71 Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-hg71.jpg)

## F58 (Ford Colors 1958)
 
![Blender F58 Screenshot](https://github.com/don1138/blender-pcoy/blob/main/imx/blender-f58.jpg)

## Installation

Download the latest ZIPs from **Releases**.

Install them **individually** via ``Edit > Preferences > Add-ons > Install…``.

Once activated, a new tab named **MAT** will appear in the 3D viewport sidebar.
- **PCOY** creates a panel named **Pantone Color of the Year**
- **MCMC** creates a panel named **Mid-Century Modern Colors**
- **HG71** creates a panel named **House & Garden 1971**
- **F58** creates a panel named **Ford Colors**

## Usage


Select an object in your view, and click a button to assign that color to it.

Set the ``Rename Material`` checkbox to ``True`` to change the material name.

## Caveats & Warnings

**This add-on does one very specific thing:**

It sets the Base Color of the Principled BSDF Shader node specifically named "Principled BSDF" -- which is created by default with all new materials -- to a custom color. It also sets the object's `Viewport Display > Color` to the same color.

**This add-on will only affect the Active Material of the Currently Selected Object.**

The operation will fail if:
- No object is selected
- The active object has no material
- The active material does not include a Principled BSDF Shader named "Principled BSDF"

## Notes

The **PCOY** colors can be too harsh and saturated for large objects, but some of them pop nicely when used for details. Or use them as a starting point, and tweak them into something better. Cut the saturation by 50-75% and see what you get.

I use **Sand Dollar**, **2020 Bleached Coral**, and **2043 Dead Coral** a lot. [**The Ugliest Color in the World**](https://www.huffpost.com/entry/ugliest-color-pantone_n_57570df6e4b0ca5c7b504538) is nice for for dirt, cracks, or crevices.

The **MCMC** and **HG71** colors are rather nice just as they are. **MCMC's** blues, greens, reds, and browns are great starters for terrains.

**F58** is good for vintage cars and machinery.

## Attributions

- **Pantone Color of the Year** is sourced from the Pantone website.
- **Mid-Century Modern Colors** is sourced from [**7 Paint Colors That Nail the Midcentury Modern Look**](https://www.dwell.com/article/best-midcentury-modern-paint-colors-111e82a1) on **Dwell.com**.
- **House & Garden Colors 1971** is sourced from a scan of a vintage magazine cover found online.
- **Ford Colors 1958** is sourced from a scan of vintage promotional material found online.

<br><br>

<p align="center">
  <img align="center" src="https://badges.pufler.dev/created/don1138/blender-pcoy?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Created">
  <img align="center" src="https://badges.pufler.dev/updated/don1138/blender-pcoy?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Updated">
</p>

![Alt](https://repobeats.axiom.co/api/embed/8994807a0f77b114d51c66e558162c3b2295afeb.svg "Repobeats analytics image")
