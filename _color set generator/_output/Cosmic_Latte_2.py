# AMS COLORS SET

import bpy

from .globals import *
from .color_functions import *

# AMS OPERATORS

class COSMIC_LATTE(bpy.types.Operator):
    """Cosmic Latte"""
    bl_label = "Cosmic Latte"
    bl_idname = 'color.cosmic_latte'
    def execute(self, context):
        set_base_color(0xfff8e7, self.bl_label)
        return {'FINISHED'}


# AMS PANEL

class AMSPanel(bpy.types.Panel):
    bl_idname = "AMS_PT_Panel"
    bl_label = "AMS"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["cosmic_latte"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.cosmic_latte", text="Cosmic Latte")


# AMS CLASSES
array_ams = [
    AMSPanel,
    Cosmic Latte,
]
