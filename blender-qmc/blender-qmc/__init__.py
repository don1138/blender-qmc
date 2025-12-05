# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name"       : "QMC (Quick Material Colors)",
    "description": "Sets the Base Color of a Material Shader",
    "author"     : "Don Schnitzius",
    "version"    : (1, 15, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > Quick Material Colors",
    "warning"    : "",
    "doc_url"    : "https://github.com/don1138/blender-qmc",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}


import os
import bpy
import bpy.utils.previews


# IMPORT GLOBALS
from .color_sets.globals import *


# BOOLEAN FOR PANEL
class QMC_SETTINGS(bpy.types.PropertyGroup):
    active_node_more:     bpy.props.BoolProperty(name='Selected Nodes Only', default=False)
    group_more:           bpy.props.BoolProperty(name='Skip Node Groups', default=False)
    rename_material_more: bpy.props.BoolProperty(name='Rename Material', default=False)
    diffuse_more:         bpy.props.BoolProperty(name='Set Viewport Color', default=False)
    world_color_more:     bpy.props.BoolProperty(name='Set World Background', default=False)


# PARENT PANEL
class QMCPanel(bpy.types.Panel):
    bl_idname = "QMC_PT_Panel"
    bl_label = "Quick Material Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        settings = context.scene.qmc_settings

        row2 = layout.row(align=True)
        check_col = row2.column(align=True)
        check_col.scale_y = 1.25
        check_col.prop(settings, "active_node_more", text="")
        check_col.prop(settings, "group_more", text="")
        check_col.prop(settings, "rename_material_more", text="")
        check_col.prop(settings, "diffuse_more", text="")
        check_col.prop(settings, "world_color_more", text="")

        label_col = row2.column(align=True)
        label_col.scale_y = 1.25
        label_col.scale_x = 3
        label_col.label(text="Selected Nodes Only")
        label_col.label(text="Skip Node Groups")
        label_col.label(text="Rename Material")
        label_col.label(text="Set Viewport Color")
        label_col.label(text="Set World Background")


# IMPORT PANELS
from .color_sets.ams_595a import *
from .color_sets.bclr import *
from .color_sets.bsc import *
from .color_sets.coco import *
from .color_sets.ecc import *
from .color_sets.f58 import *
from .color_sets.ge import *
from .color_sets.hg71 import *
from .color_sets.mcm import *
from .color_sets.moods import *
from .color_sets.pcoy import *
from .color_sets.ral import *
from .color_sets.sw_ext import *
from .color_sets.sw_int import *
from .color_sets.sw_ja import *
from .color_sets.wgsn import *


# INTERNAL CLASSES
array_int = [
    QMC_SETTINGS,
    QMCPanel,
]


# IMPORT & CONCATENATE CLASSES
classes = [
   *array_int,
   *array_ams,
   *array_bclr,
   *array_bsc,
   *array_coco,
   *array_ecc,
   *array_f58,
   *array_ge,
   *array_hg71,
   *array_mcm,
   *array_moods,
   *array_pcoy,
   *array_ral,
   *array_sw_ext,
   *array_sw_int,
   *array_sw_ja,
   *array_wgsn,
]


def register():
    # LOAD CUSTOM ICONS
    addon_path = os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")

    if not os.path.exists(icons_dir):
        print(f"Warning: Icons directory {icons_dir} not found.")
    else:
        for entry in os.listdir(icons_dir):
            icon_path = os.path.join(icons_dir, entry)
            if os.path.isfile(icon_path):
                try:
                    icon_name = os.path.splitext(entry)[0]
                    g.c_icons.load(icon_name, icon_path, "IMAGE")
                except Exception as e:
                    print(f"Error loading icon {entry}: {e}")
            else:
                print(f"Warning: {entry} is not a file and will be skipped.")

    # Register classes
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register the single PointerProperty ONCE outside the loop,
    # after the QMC_SETTINGS class has been registered.
    bpy.types.Scene.qmc_settings = bpy.props.PointerProperty(type=QMC_SETTINGS)


def unregister():
    bpy.utils.previews.remove(g.c_icons)

    # Remove the single PointerProperty (New structure cleanup)
    if hasattr(bpy.types.Scene, 'qmc_settings'):
        delattr(bpy.types.Scene, 'qmc_settings')

    # Safely remove the 5 old properties if they somehow persist
    old_props = ["active_bool", "more_bool", "diffuse_bool", "group_bool", "world_bool"]
    for prop in old_props:
        if hasattr(bpy.types.Scene, prop):
            delattr(bpy.types.Scene, prop)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
