import bpy
from .colors_functions import *

# MOOD COLORS

class MoodsGreen02(bpy.types.Operator):
    """Soft sage green with a hint of blue"""
    bl_label = "Green 02"
    bl_idname = 'color.moods_green_02'
    def execute(self, context):
        set_base_color(0x8A9082, self.bl_label)
        return {'FINISHED'}

class MoodsBlue02(bpy.types.Operator):
    """Fresh clean minty blue"""
    bl_label = "Blue 02"
    bl_idname = 'color.moods_blue_02'
    def execute(self, context):
        set_base_color(0xd3dbd9, self.bl_label)
        return {'FINISHED'}

class MoodsBlue08(bpy.types.Operator):
    """Vibrant mid-tone sky blue"""
    bl_label = "Blue 08"
    bl_idname = 'color.moods_blue_08'
    def execute(self, context):
        set_base_color(0xabccd3, self.bl_label)
        return {'FINISHED'}

class MoodsPink04(bpy.types.Operator):
    """Muted pink with a touch of grey"""
    bl_label = "Pink 04"
    bl_idname = 'color.moods_pink_04'
    def execute(self, context):
        set_base_color(0xF3E0E4, self.bl_label)
        return {'FINISHED'}

class MoodsGreen07(bpy.types.Operator):
    """Foliage green with hint of blue & yellow"""
    bl_label = "Green 07"
    bl_idname = 'color.moods_green_07'
    def execute(self, context):
        set_base_color(0x698a66, self.bl_label)
        return {'FINISHED'}

class MoodsGreen08(bpy.types.Operator):
    """Fresh neo green"""
    bl_label = "Green 08"
    bl_idname = 'color.moods_green_08'
    def execute(self, context):
        set_base_color(0xa2c3af, self.bl_label)
        return {'FINISHED'}

class MoodsGreen13(bpy.types.Operator):
    """Sage green with added optimism"""
    bl_label = "Green 13"
    bl_idname = 'color.moods_green_13'
    def execute(self, context):
        set_base_color(0xb9ccae, self.bl_label)
        return {'FINISHED'}

class MoodsYellow06(bpy.types.Operator):
    """Daffodil yellow with a lemon tang"""
    bl_label = "Yellow 06"
    bl_idname = 'color.moods_yellow_06'
    def execute(self, context):
        set_base_color(0xffe887, self.bl_label)
        return {'FINISHED'}

class MoodsPink07(bpy.types.Operator):
    """A romantic, muted pink"""
    bl_label = "Pink 07"
    bl_idname = 'color.moods_pink_07'
    def execute(self, context):
        set_base_color(0xd2c5bc, self.bl_label)
        return {'FINISHED'}

class MoodsPink08(bpy.types.Operator):
    """Dusty pink on a distinctly earthy base"""
    bl_label = "Pink 08"
    bl_idname = 'color.moods_pink_08'
    def execute(self, context):
        set_base_color(0xc2a79c, self.bl_label)
        return {'FINISHED'}

class MoodsBeige02(bpy.types.Operator):
    """Light buff brown with touch of grey"""
    bl_label = "Beige 02"
    bl_idname = 'color.moods_beige_02'
    def execute(self, context):
        set_base_color(0xb6a18b, self.bl_label)
        return {'FINISHED'}

class MoodsBeige03(bpy.types.Operator):
    """Soft, earthy beige with notes of grey and yellow"""
    bl_label = "Beige 03"
    bl_idname = 'color.moods_beige_03'
    def execute(self, context):
        set_base_color(0xdfdbcf, self.bl_label)
        return {'FINISHED'}

class MoodsBlue06(bpy.types.Operator):
    """Deep slate blue"""
    bl_label = "Blue 06"
    bl_idname = 'color.moods_blue_06'
    def execute(self, context):
        set_base_color(0x4c5f6b, self.bl_label)
        return {'FINISHED'}

class MoodsBlue07(bpy.types.Operator):
    """Dark inky blue with touch of green"""
    bl_label = "Blue 07"
    bl_idname = 'color.moods_blue_07'
    def execute(self, context):
        set_base_color(0x3d4f56, self.bl_label)
        return {'FINISHED'}

class MoodsBlue17(bpy.types.Operator):
    """A grounded, muted blue"""
    bl_label = "Blue 17"
    bl_idname = 'color.moods_blue_17'
    def execute(self, context):
        set_base_color(0x8398a5, self.bl_label)
        return {'FINISHED'}

class MoodsBlue111(bpy.types.Operator):
    """Cobalt keyworker blue"""
    bl_label = "Blue1 11"
    bl_idname = 'color.moods_blue1_11'
    def execute(self, context):
        set_base_color(0x1a4677, self.bl_label)
        return {'FINISHED'}

class MoodsPurple03(bpy.types.Operator):
    """Deep, velvety purple with blue undertones"""
    bl_label = "Purple 03"
    bl_idname = 'color.moods_purple_03'
    def execute(self, context):
        set_base_color(0x432d2e, self.bl_label)
        return {'FINISHED'}

class MoodsTeal03(bpy.types.Operator):
    """Charcoal blue with grey undertones"""
    bl_label = "Teal 03"
    bl_idname = 'color.moods_teal_03'
    def execute(self, context):
        set_base_color(0x596869, self.bl_label)
        return {'FINISHED'}

class MoodsRed03(bpy.types.Operator):
    """Deep terracotta"""
    bl_label = "Red 03"
    bl_idname = 'color.moods_red_03'
    def execute(self, context):
        set_base_color(0xc3867b, self.bl_label)
        return {'FINISHED'}

class MoodsBlack01(bpy.types.Operator):
    """Graphite black with blue undertones"""
    bl_label = "Black 01"
    bl_idname = 'color.moods_black_01'
    def execute(self, context):
        set_base_color(0x444A4C, self.bl_label)
        return {'FINISHED'}

class MoodsWhite04(bpy.types.Operator):
    """Soft linen white with grey undertones"""
    bl_label = "White 04"
    bl_idname = 'color.moods_white_04'
    def execute(self, context):
        set_base_color(0xe4e2d7, self.bl_label)
        return {'FINISHED'}

class MoodsWhite03(bpy.types.Operator):
    """Soft creamy white with touch of yellow"""
    bl_label = "White 03"
    bl_idname = 'color.moods_white_03'
    def execute(self, context):
        set_base_color(0xf3f1e5, self.bl_label)
        return {'FINISHED'}

class MoodsWhite02(bpy.types.Operator):
    """Off-white with a touch of grey"""
    bl_label = "White 02"
    bl_idname = 'color.moods_white_02'
    def execute(self, context):
        set_base_color(0xeceae2, self.bl_label)
        return {'FINISHED'}

class MoodsWhite01(bpy.types.Operator):
    """Pure white with the lightest touch of grey"""
    bl_label = "White 01"
    bl_idname = 'color.moods_white_01'
    def execute(self, context):
        set_base_color(0xf2f2eb, self.bl_label)
        return {'FINISHED'}
