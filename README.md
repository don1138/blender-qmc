# Blender PCOY (Pantone Color of the Year)

**Blender Add-on which sets a Material's Base Color to one of Pantone's Colors of the Year.

<!-- ![Blender QLE Screenshot](https://github.com/don1138/blender-qmm/blob/main/blender-qmm.jpg) -->

## Installation

Download ``pcoy_panel.py`` and install it via ``Edit > Preferences > Add-ons > Install…``.

## Usage

This addon creates a panel named **Pantone Color of the Year** under ``3D Viewport > Sidebar > PCOY``.

Select an object in your view, and click a button to assign that color to it.

## Caveats & Warnings

**This add-on does one very specific thing:**

It sets the Base Color of the Principled BSDF Shader node specifically named "Principled BSDF" -- which is created by default with all new materials -- and also the Object's Viewport Display Color to one of the colors that Pantone has named Color of the Year.

This add-on will only affect the Active Material of the Currently Sleected Object.

- If no Object is seleceted, the add-on may error out.
- If the Active Material does not include a Principled BSDF Shader named "Principled BSDF", the add-on will error out.
- If the Active Material does include a Principled BSDF Shader named "Principled BSDF", but it is not directly connected to the Material Output, the Object's color may or may not be affected.
- If the Active Material does include a Principled BSDF Shader named "Principled BSDF", and is directly connected to the Material Output node, but the Base Color Input is connected to the Output of another node, the Object's color will be unaffected.

## Why Did I Make This Add-on?

**Because I wanted to.** 🎤💥🤯

And because I wanted to figure out how to do this in Python.

And because my swipe file has a bunch of Pantone swatches gathering dust, so I thought that maybe this might help me put them to practical use.

## Okay, Yeah, But Are These Colors Actually of Any Practical Use?

**Jeez, mate -- IDK. You're riding me pretty hard here over an open-source freebie.

Look, they're too harsh and saturated for large objects, but some of them pop nicely when used for details.

Or use them as a starting point, and tweak them into something better. I like them better when I cut the saturation by 50-75%.

And if you have need of [The Ugliest Color in the World](https://www.huffpost.com/entry/ugliest-color-pantone_n_57570df6e4b0ca5c7b504538) for dirt, cracks, or crevices, you're covered.

<!-- ## Online Presence

- [Artstation](https://www.artstation.com/marketplace/p/p88LG/blender-qmm-quick-metal-materials)
- [Blender Addons](https://blender-addons.org/quick-metal-materials/)
- [Blender Artists Thread](https://blenderartists.org/t/blender-qmm-quick-metal-materials-free-addon/1290433)
- [Gumroad](https://gumroad.com/l/blender-qmm) -->

<p align="center">
  <img align="center" src="https://badges.pufler.dev/created/don1138/blender-pcoy?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Created">
  <img align="center" src="https://badges.pufler.dev/updated/don1138/blender-pcoy?style=for-the-badge&colorA=222&colorB=48684b" alt="Repo Updated">
</p>

