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
    "version"    : (1, 11, 0),
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
    active_node_more:     bpy.props.BoolProperty(name='',default=False)
    rename_material_more: bpy.props.BoolProperty(name='',default=False)
    diffuse_more:         bpy.props.BoolProperty(name='',default=False)
    world_color_more:     bpy.props.BoolProperty(name='',default=False)


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
        active_bool = context.scene.active_bool
        more_bool = context.scene.more_bool
        diffuse_bool = context.scene.diffuse_bool
        world_bool = context.scene.world_bool

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.prop(active_bool, "active_node_more")
        scol.prop(more_bool, "rename_material_more")
        scol.prop(diffuse_bool, "diffuse_more")
        scol.prop(world_bool, "world_color_more")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Selected Nodes Only")
        scol.label(text="Rename Material")
        scol.label(text="Set Viewport Color")
        scol.label(text="Set World Background")


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
    bpy_types_scene_properties = ["active_bool", "more_bool", "diffuse_bool", "world_bool"]

    for cls in classes:
        bpy.utils.register_class(cls)
    
    for prop in bpy_types_scene_properties:
        setattr(bpy.types.Scene, prop, bpy.props.PointerProperty(type=QMC_SETTINGS))


def unregister():
    bpy.utils.previews.remove(g.c_icons)
    bpy_types_scene_properties = ["active_bool", "more_bool", "diffuse_bool", "world_bool"]
    
    for prop in bpy_types_scene_properties:
        delattr(bpy.types.Scene, prop)
        
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
