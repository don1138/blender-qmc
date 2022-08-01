import bpy
from .colors_functions import *

# Ford Colors 1958

class F58ARavenBlack(bpy.types.Operator):
    """Ford Colors 1958 - A Raven Black"""
    bl_label = "A Raven Black"
    bl_idname = 'color.f58a_raven_black'
    def execute(self, context):
        set_base_color(0x010303, self.bl_label)
        return {'FINISHED'}

class F58CDesertBeige(bpy.types.Operator):
    """Ford Colors 1958 - C Desert Beige"""
    bl_label = "C Desert Beige"
    bl_idname = 'color.f58c_desert_beige'
    def execute(self, context):
        set_base_color(0xc0ab83, self.bl_label)
        return {'FINISHED'}

class F58DPalaminoTan(bpy.types.Operator):
    """Ford Colors 1958 - D Palamino Tan"""
    bl_label = "D Palamino Tan"
    bl_idname = 'color.f58d_palamino_tan'
    def execute(self, context):
        set_base_color(0xab7832, self.bl_label)
        return {'FINISHED'}

class F58EColonialWhite(bpy.types.Operator):
    """Ford Colors 1958 - E Colonial White"""
    bl_label = "E Colonial White"
    bl_idname = 'color.f58e_colonial_white'
    def execute(self, context):
        set_base_color(0xe7e4c1, self.bl_label)
        return {'FINISHED'}

class F58FSilvertoneGreen(bpy.types.Operator):
    """Ford Colors 1958 - F Silvertone Green"""
    bl_label = "F Silvertone Green"
    bl_idname = 'color.f58f_silvertone_green'
    def execute(self, context):
        set_base_color(0x1e3226, self.bl_label)
        return {'FINISHED'}

class F58GSunGold(bpy.types.Operator):
    """Ford Colors 1958 - G Sun Gold"""
    bl_label = "G Sun Gold"
    bl_idname = 'color.f58g_sun_gold'
    def execute(self, context):
        set_base_color(0xe7d74a, self.bl_label)
        return {'FINISHED'}

class F58HGunmetalGray(bpy.types.Operator):
    """Ford Colors 1958 - H Gunmetal Gray"""
    bl_label = "H Gunmetal Gray"
    bl_idname = 'color.f58h_gunmetal_gray'
    def execute(self, context):
        set_base_color(0x4c4f50, self.bl_label)
        return {'FINISHED'}

class F58JBaliBronze(bpy.types.Operator):
    """Ford Colors 1958 - J Bali Bronze"""
    bl_label = "J Bali Bronze"
    bl_idname = 'color.f58j_bali_bronze'
    def execute(self, context):
        set_base_color(0x654935, self.bl_label)
        return {'FINISHED'}

class F58LAzureBlue(bpy.types.Operator):
    """Ford Colors 1958 - L Azure Blue"""
    bl_label = "L Azure Blue"
    bl_idname = 'color.f58l_azure_blue'
    def execute(self, context):
        set_base_color(0x7aafd5, self.bl_label)
        return {'FINISHED'}

class F58MGulfstreamBlue(bpy.types.Operator):
    """Ford Colors 1958 - M Gulfstream Blue"""
    bl_label = "M Gulfstream Blue"
    bl_idname = 'color.f58m_gulfstream_blue'
    def execute(self, context):
        set_base_color(0x2b758c, self.bl_label)
        return {'FINISHED'}

class F58NSeasprayGreen(bpy.types.Operator):
    """Ford Colors 1958 - N Seaspray Green"""
    bl_label = "N Seaspray Green"
    bl_idname = 'color.f58n_seaspray_green'
    def execute(self, context):
        set_base_color(0xa0c78e, self.bl_label)
        return {'FINISHED'}

class F58RTorchRed(bpy.types.Operator):
    """Ford Colors 1958 - R Torch Red"""
    bl_label = "R Torch Red"
    bl_idname = 'color.f58r_torch_red'
    def execute(self, context):
        set_base_color(0x620800, self.bl_label)
        return {'FINISHED'}

class F58TSilvetoneBlue(bpy.types.Operator):
    """Ford Colors 1958 - T Silvetone Blue"""
    bl_label = "T Silvetone Blue"
    bl_idname = 'color.f58t_silvetone_blue'
    def execute(self, context):
        set_base_color(0x243b59, self.bl_label)
        return {'FINISHED'}
