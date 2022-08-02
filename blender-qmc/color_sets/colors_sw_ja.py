import bpy
from .colors_functions import *

# SHERWIN WILLIAMS - THE JAZZ AGE

class JAChineseRed(bpy.types.Operator):
    """Jazz Age Chinese Red"""
    bl_label = "Chinese Red"
    bl_idname = 'color.ja_chinese_red'
    def execute(self, context):
        set_base_color(0x9e3e33, self.bl_label)
        return {'FINISHED'}

class JAJazzAgeCoral(bpy.types.Operator):
    """Jazz Age Jazz Age Coral"""
    bl_label = "Jazz Age Coral"
    bl_idname = 'color.ja_jazz_age_coral'
    def execute(self, context):
        set_base_color(0xf1bfb1, self.bl_label)
        return {'FINISHED'}

class JAFrostwork(bpy.types.Operator):
    """Jazz Age Frostwork"""
    bl_label = "Frostwork"
    bl_idname = 'color.ja_frostwork'
    def execute(self, context):
        set_base_color(0xcbd0c2, self.bl_label)
        return {'FINISHED'}

class JAAlexandrite(bpy.types.Operator):
    """Jazz Age Alexandrite"""
    bl_label = "Alexandrite"
    bl_idname = 'color.ja_alexandrite'
    def execute(self, context):
        set_base_color(0x598c74, self.bl_label)
        return {'FINISHED'}

class JASalonRose(bpy.types.Operator):
    """Jazz Age Salon Rose"""
    bl_label = "Salon Rose"
    bl_idname = 'color.ja_salon_rose'
    def execute(self, context):
        set_base_color(0xab7878, self.bl_label)
        return {'FINISHED'}

class JAStudioMauve(bpy.types.Operator):
    """Jazz Age Studio Mauve"""
    bl_label = "Studio Mauve"
    bl_idname = 'color.ja_studio_mauve'
    def execute(self, context):
        set_base_color(0xc6b9b8, self.bl_label)
        return {'FINISHED'}

class JABlueSky(bpy.types.Operator):
    """Jazz Age Blue Sky"""
    bl_label = "Blue Sky"
    bl_idname = 'color.ja_blue_sky'
    def execute(self, context):
        set_base_color(0xabd1c9, self.bl_label)
        return {'FINISHED'}

class JABluePeacock(bpy.types.Operator):
    """Jazz Age Blue Peacock"""
    bl_label = "Blue Peacock"
    bl_idname = 'color.ja_blue_peacock'
    def execute(self, context):
        set_base_color(0x014e4c, self.bl_label)
        return {'FINISHED'}
