### 1.8.0 <!-- 08/11/24 -->

- Refactor code

### 1.7.0 <!-- 08/08/24 -->

- Add **Set Viewport Color** checkbox
  - When selected, this changes the **Viewport Color** of the material.
- Rename **Selected Node** > **Selected Nodes Only**
- Rename **World Background** > **Set World Background**

### 1.6.0 <!-- 07/05/24 -->

- Add **COCO Segmentation** set of 183 colors
- Add **Emission Shader** to chain of shader nodes affected.
  - If Principled BSDF node found, change Base Color and exit. If not, go to next.
  - If Diffuse node found, change Base Color and exit. If not, go to next.
  - If Emission node found, change Base Color and exit. If not, exit.

### 1.5.1 <!-- 03/18/24 -->

- Bugfix: Color chip names

### 1.5.0 <!-- 03/15/24 -->

- Add **British Standard Colors** set of 453 colors
  - **BS 2660 (1964)** - 96 color
  - **BS 381C (1930)** - 119 colors
  - **BS 5252 (1976)** - 238 colors

### 1.4.0 <!-- 03/14/24 -->

- Add **Exotic Car Colors** set of 142 colors
  - **Audi** - 1 color
  - **Ferrari** - 25 colors
  - **Lamborghini** - 63 colors
  - **McLaren** - 19 colors
  - **Porsche** - 34 colors
- Add **Cosmic Latte** to **Don1138 Select**

### 1.3.0 <!-- 12/07/23 -->

- Add **Peach Fuzz** to **Pantone Color of the Year**

### 1.2.6 <!-- 09/28/23 -->

- Add **AMS (Aerospace Material Specification) Standard 595A** set of 692 colors

### 1.2.5 <!-- 12/18/22 -->

- Code refactoring

### 1.2.4 <!-- 12/02/22 -->

- Add **Viva Magenta** to **Pantone Color of the Year**
- Indent names of sub-categories to improve legibility. This affects:
  - **House & Garden 1971**
  - **Mid-Century Modern**
  - **Moods**
  - **Pantone Color of the Year**
  - **RAL Classic**
  - **Suburban Modern Exterior**

### 1.2.3 <!-- 11/15/22 -->

- Add **Baker-Miller Pink** to **QMC Plus** > **Don1138 Select**
- Add **Energy Conservation** node group to list of affected nodes
- Code refactoring

### 1.2.2 <!-- 10/17/22 -->

- Add `ShaderNodeRGB` to nodes affected by **All Selected Materials** checkbox

### 1.2.1 <!-- 8/19/22 -->

- Optimize `color_functions.py`
  - Thank you to **iceythe** on [**Blender Artists**](https://blenderartists.org/t/roast-my-code-color-switcher/1397799/3) for code review

### 1.2.0 <!-- 8/18/22 -->

- Add **All Selected Materials** checkbox
  - When selected, this changes the **Base Color** of all selected shader nodes. This ignores nodes that do not have a **Base Color** attribute.

### 1.1.0 <!-- 8/12/22 -->

- Add **RAL Classic** set of 218 colors
- Set Parent Panel default to open

### 1.0.3 <!-- 8/09/22 -->

- Rename all instances of `QMC_MCMC` to `QMC_MCM`
- Rename panel label `Mid-Century Modern Colors` to `Mid-Century Modern`

### 1.0.2 <!-- 8/03/22 -->

- Add errror detection for missing `World`

### 1.0.1 <!-- 8/02/22 -->

- Merge **colors** and **panels** files into unified **color_sets** files

### 1.0.0 <!-- 8/01/22 -->

- Migrate all color sets into one add-on
  - **Ford 1958**
  - **House & Garden 1971**
  - **General Electric**
  - **Mid-Century Modern**
  - **Moods**
  - **Pantone Color of the Year**
  - **Suburban Modern Exterior**
  - **Suburban Modern Interior**
  - **The Jazz Age**
- Move color sets into separate files
  - Each color set gets a **colors** file and a **panels** file
