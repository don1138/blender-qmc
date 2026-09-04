# DON1138 SELECT COLORS SET

import bpy

from .globals import *
from .color_functions import *

# DON1138 SELECT OPERATORS

class DON_GREEN(bpy.types.Operator):
    """Don Green"""
    bl_label = "Don Green"
    bl_idname = 'color.don_green'
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

class DON_RED(bpy.types.Operator):
    """Don Red"""
    bl_label = "Don Red"
    bl_idname = 'color.don_red'
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

class DON_BLUE(bpy.types.Operator):
    """Don Blue"""
    bl_label = "Don Blue"
    bl_idname = 'color.don_blue'
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

class DON_YELLOW(bpy.types.Operator):
    """Don Yellow"""
    bl_label = "Don Yellow"
    bl_idname = 'color.don_yellow'
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

class DON_BRONZE_PALE(bpy.types.Operator):
    """Don Bronze Pale"""
    bl_label = "Don Bronze Pale"
    bl_idname = 'color.don_bronze_pale'
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

class DON_BRONZE_RICH(bpy.types.Operator):
    """Don Bronze Rich"""
    bl_label = "Don Bronze Rich"
    bl_idname = 'color.don_bronze_rich'
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

class DON_WHITE(bpy.types.Operator):
    """Don White"""
    bl_label = "Don White"
    bl_idname = 'color.don_white'
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

# DON1138 SELECT PANEL
class DON1138Panel(bpy.types.Panel):
    bl_idname = "DON1138_PT_Panel"
    bl_label = "Don1138 Select"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Quick Tools"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# DON1138 TRUE
class DON1138TruePanel(bpy.types.Panel):
    bl_idname = "DON1138_TRUE_PT_Panel"
    bl_label = "    True"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Quick Tools"
    bl_parent_id = 'DON1138_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["don_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_bronze_pale"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_bronze_rich"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_white"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.don_green", text="Don Green")
        scol.operator("color.don_red", text="Don Red")
        scol.operator("color.don_blue", text="Don Blue")
        scol.operator("color.don_yellow", text="Don Yellow")
        scol.operator("color.don_bronze_pale", text="Don Bronze Pale")
        scol.operator("color.don_bronze_rich", text="Don Bronze Rich")
        scol.operator("color.don_white", text="Don White")


# DON1138 SAFE
class DON1138SafePanel(bpy.types.Panel):
    bl_idname = "DON1138_SAFE_PT_Panel"
    bl_label = "    Safe"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Quick Tools"
    bl_parent_id = 'DON1138_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pms_381_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_172_c"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_2685_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_396_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_729_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_7518_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_7499_u"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_381_u", text="PMS 381 U")
        scol.operator("color.pms_172_c", text="PMS 172 C")
        scol.operator("color.pms_2685_u", text="PMS 2685 U")
        scol.operator("color.pms_396_u", text="PMS 396 U")
        scol.operator("color.pms_729_u", text="PMS 729 U")
        scol.operator("color.pms_7518_u", text="PMS 7518 U")
        scol.operator("color.pms_7499_u", text="PMS 7499 U")


# DON1138 SELECT CLASSES
array_ds = [
    DON1138Panel,
    DON1138TruePanel,
    DON1138SafePanel,
    DON_GREEN,
    PMS_381U,
    DON_RED,
    PMS_172_C,
    DON_BLUE,
    PMS_2685U,
    DON_YELLOW,
    PMS_396U,
    DON_BRONZE_PALE,
    PMS_729U,
    DON_BRONZE_RICH,
    PMS_7518U,
    DON_WHITE,
    PMS_7499U,
]
