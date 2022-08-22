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
- Set the **All Selected Materials** checkbox to `True` to change the **Base Color** of all selected shader nodes in a material. (This ignores nodes that do not have a **Base Color** attribute.)
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

If the operation fails, set the **All Selected Nodes** checkbox to `True`, and manually select the shader nodes you want to change.

And if no `World` is set, changing the **World Background** will cause an error.

## Swatches

For swatches and notes, [refer to the Wiki](https://github.com/don1138/blender-qmc/wiki).

<br><br>
<p align="center">
  <img alt="GitHub latest commit" src="https://img.shields.io/github/last-commit/don1138/blender-qmc">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/don1138/blender-qmc">
  <img alt="Github all releases" src="https://img.shields.io/github/downloads/don1138/blender-qmc/total.svg"><br>
  <img src="https://repobeats.axiom.co/api/embed/52e50c70eb6c2d9d025cc8b7bf8f3c40ddf5b214.svg" alt="Repobeats analytics image">
</p>
