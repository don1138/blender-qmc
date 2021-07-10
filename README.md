# Blender PCOY (Pantone Color of the Year) and MCMC (Mid-Century Modern Colors)

### Blender Add-ons That Assign a Custom Color to a Principled BSDF's Base Color.

![Blender PCOY Screenshot](https://github.com/don1138/blender-pcoy/blob/main/blender-pcoy.jpg)

![Blender PCOY Screenshot](https://github.com/don1138/blender-pcoy/blob/main/blender-mcmc.jpg)

## Installation

Download the latest ZIPs from **Releases** or grab ``pcoy_panel.py`` and ``mcmc_panel.py`` from the repo.

Install via ``Edit > Preferences > Add-ons > Install…``.

## Usage

PCOY creates a Panel named **Pantone Color of the Year** under ``3D Viewport > Sidebar > PCOY``.

MCMC creates a Panel named **Mid-Century Modern Colors** under ``3D Viewport > Sidebar > MCMC``.

Select an Object in your view, and click a button to assign that color to it.

Set the ``Rename Material`` checkbox to ``True`` to update the material name.

## Caveats & Warnings

**This add-on does one very specific thing:**

It sets the Base Color of the Principled BSDF Shader node specifically named "Principled BSDF" -- which is created by default with all new materials -- to a custom color. It also sets the Object's Viewport Display Color to the same color.

**This add-on will only affect the Active Material of the Currently Selected Object.**

- If no Object is selected, the add-on may error out.
- If the Active Material does not include a Principled BSDF Shader named "Principled BSDF", the add-on will error out.
- If the Active Material does include a Principled BSDF Shader named "Principled BSDF", but it is not directly connected to the Material Output, the Object's color may or may not be affected.
- If the Active Material does include a Principled BSDF Shader named "Principled BSDF", and is directly connected to the Material Output node, but the Base Color Input is connected to the Output of another node, the Object's color will be unaffected.

## Notes

The PMOY colors can be too harsh and saturated for large objects, but some of them pop nicely when used for details. I use **Sand Dollar** a lot.

Or use them as a starting point, and tweak them into something better. Cut the saturation by 50-75% and see what you get.

[**The Ugliest Color in the World**](https://www.huffpost.com/entry/ugliest-color-pantone_n_57570df6e4b0ca5c7b504538) is nice for for dirt, cracks, or crevices, you're covered.

The MCMC colors are pretty good as-is.

## Attributions

**Pantone Color of the Year** is sourced from the Pantone website.

**Mid-Century Modern Colors** is sourced from [**7 Paint Colors That Nail the Midcentury Modern Look**](https://www.dwell.com/article/best-midcentury-modern-paint-colors-111e82a1) on Dwell.com.

<p align="center">
  <img align="center" src="https://badges.pufler.dev/created/don1138/blender-pcoy?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Created">
  <img align="center" src="https://badges.pufler.dev/updated/don1138/blender-pcoy?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Updated">
</p>

