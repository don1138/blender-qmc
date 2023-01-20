# PCOY COLORS SET

import bpy

from .globals import *
from .color_functions import *

# PCOY OPERATORS

class Viva Magenta(bpy.types.Operator):
    """Viva Magenta"""
    bl_label = "Viva Magenta"
    bl_idname = 'color.pms_2023'
    def execute(self, context):
        set_base_color(0xBB2649, self.bl_label)
        return {'FINISHED'}


# PCOY PANEL

class PCOYPanel(bpy.types.Panel):
    bl_idname = "PCOY_PT_Panel"
    bl_label = "PCOY"
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
        scol.label(text="", icon_value=g.c_icons["pms_2023"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_2023", text="Viva Magenta")


# PCOY CLASSES
array_pcoy = [
    PCOYPanel,
    Viva Magenta,
]
