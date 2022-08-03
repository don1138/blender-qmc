import bpy

from .globals import *
from .color_functions import *


# SCHNITZIUS SELECTS

class SCHNITZIUS_GREEN(bpy.types.Operator):
    """Schnitzius Green"""
    bl_label = "Schnitzius Green"
    bl_idname = 'color.schnitzius_green'
    def execute(self, context):
        set_base_color(0xa6ce39, self.bl_label)
        return {'FINISHED'}

class PMS_381U(bpy.types.Operator):
    """PMS 381 U"""
    bl_label = "PMS 381 U"
    bl_idname = 'color.pms_381_u'
    def execute(self, context):
        set_base_color(0xb6d741, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_RED(bpy.types.Operator):
    """Schnitzius Red"""
    bl_label = "Schnitzius Red"
    bl_idname = 'color.schnitzius_red'
    def execute(self, context):
        set_base_color(0xff3600, self.bl_label)
        return {'FINISHED'}

class PMS_172_C(bpy.types.Operator):
    """PMS 172 C"""
    bl_label = "PMS 172 C"
    bl_idname = 'color.pms_172_c'
    def execute(self, context):
        set_base_color(0xfe4819, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_BLUE(bpy.types.Operator):
    """Schnitzius Blue"""
    bl_label = "Schnitzius Blue"
    bl_idname = 'color.schnitzius_blue'
    def execute(self, context):
        set_base_color(0x62579d, self.bl_label)
        return {'FINISHED'}

class PMS_2685U(bpy.types.Operator):
    """PMS 2685 U"""
    bl_label = "PMS 2685 U"
    bl_idname = 'color.pms_2685_u'
    def execute(self, context):
        set_base_color(0x6a549b, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_YELLOW(bpy.types.Operator):
    """Schnitzius Yellow"""
    bl_label = "Schnitzius Yellow"
    bl_idname = 'color.schnitzius_yellow'
    def execute(self, context):
        set_base_color(0xe1ec12, self.bl_label)
        return {'FINISHED'}

class PMS_396U(bpy.types.Operator):
    """PMS 396 U"""
    bl_label = "PMS 396 U"
    bl_idname = 'color.pms_396_u'
    def execute(self, context):
        set_base_color(0xd7e200, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_BRONZE_PALE(bpy.types.Operator):
    """Schnitzius Bronze Pale"""
    bl_label = "Schnitzius Bronze Pale"
    bl_idname = 'color.schnitzius_bronze_pale'
    def execute(self, context):
        set_base_color(0xc1977e, self.bl_label)
        return {'FINISHED'}

class PMS_729U(bpy.types.Operator):
    """PMS 729 U"""
    bl_label = "PMS 729 U"
    bl_idname = 'color.pms_729_u'
    def execute(self, context):
        set_base_color(0xbf9376, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_BRONZE_RICH(bpy.types.Operator):
    """Schnitzius Bronze Rich"""
    bl_label = "Schnitzius Bronze Rich"
    bl_idname = 'color.schnitzius_bronze_rich'
    def execute(self, context):
        set_base_color(0x806969, self.bl_label)
        return {'FINISHED'}

class PMS_7518U(bpy.types.Operator):
    """PMS 7518 U"""
    bl_label = "PMS 7518 U"
    bl_idname = 'color.pms_7518_u'
    def execute(self, context):
        set_base_color(0x7d6d6a, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_WHITE(bpy.types.Operator):
    """Schnitzius White"""
    bl_label = "Schnitzius White"
    bl_idname = 'color.schnitzius_white'
    def execute(self, context):
        set_base_color(0xfffde4, self.bl_label)
        return {'FINISHED'}

class PMS_7499U(bpy.types.Operator):
    """PMS 7499 U"""
    bl_label = "PMS 7499 U"
    bl_idname = 'color.pms_7499_u'
    def execute(self, context):
        set_base_color(0xf6edca, self.bl_label)
        return {'FINISHED'}


# Schnitzius Selects PANEL
class SSPanel(bpy.types.Panel):
    bl_idname = "SS_PT_Panel"
    bl_label = "Schnitzius Select"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.grid_flow(row_major=True,even_columns=True,columns=2,align=True)
        col.scale_y = 1.25
        col.label(text="My Color")
        col.label(text="PMS Match")
        col.operator("color.schnitzius_green", text="Green")
        col.operator("color.pms_381_u", text="381 U")
        col.operator("color.schnitzius_red", text="Red")
        col.operator("color.pms_172_c", text="172 C")
        col.operator("color.schnitzius_blue", text="Blue")
        col.operator("color.pms_2685_u", text="2685 U")
        col.operator("color.schnitzius_yellow", text="Yellow")
        col.operator("color.pms_396_u", text="396 U")
        col.operator("color.schnitzius_bronze_pale", text="Bronze Pale")
        col.operator("color.pms_729_u", text="729 U")
        col.operator("color.schnitzius_bronze_rich", text="Bronze Rich")
        col.operator("color.pms_7518_u", text="7518 U")
        col.operator("color.schnitzius_white", text="White")
        col.operator("color.pms_7499_u", text="7499 U")


array_ss = [
    SSPanel,
    SCHNITZIUS_GREEN,
    PMS_381U,
    SCHNITZIUS_RED,
    PMS_172_C,
    SCHNITZIUS_BLUE,
    PMS_2685U,
    SCHNITZIUS_YELLOW,
    PMS_396U,
    SCHNITZIUS_BRONZE_PALE,
    PMS_729U,
    SCHNITZIUS_BRONZE_RICH,
    PMS_7518U,
    SCHNITZIUS_WHITE,
    PMS_7499U,
]
