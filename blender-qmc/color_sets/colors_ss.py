import bpy
from .colors_functions import *

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
