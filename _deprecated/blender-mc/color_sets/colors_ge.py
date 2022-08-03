import bpy
from .colors_functions import *

# GENERAL ELECTRIC 1960S APPLIANCES

class GECoppertoneA(bpy.types.Operator):
    """General Electric Coppertone A"""
    bl_label = "Coppertone A"
    bl_idname = 'color.ge_coppertone_a'
    def execute(self, context):
        set_base_color(0x995b51, self.bl_label)
        return {'FINISHED'}

class GEDarkCoppertoneA(bpy.types.Operator):
    """General Electric Dark Coppertone A"""
    bl_label = "Dark Coppertone A"
    bl_idname = 'color.ge_dark_coppertone_a'
    def execute(self, context):
        set_base_color(0x683f36, self.bl_label)
        return {'FINISHED'}

class GECoppertoneB(bpy.types.Operator):
    """General Electric Coppertone B"""
    bl_label = "Coppertone B"
    bl_idname = 'color.ge_coppertone_b'
    def execute(self, context):
        set_base_color(0x6f4f4c, self.bl_label)
        return {'FINISHED'}

class GEDarkCoppertoneB(bpy.types.Operator):
    """General Electric Dark Coppertone B"""
    bl_label = "Dark Coppertone B"
    bl_idname = 'color.ge_dark_coppertone_b'
    def execute(self, context):
        set_base_color(0x462b29, self.bl_label)
        return {'FINISHED'}

class GEAvacado(bpy.types.Operator):
    """General Electric Avacado"""
    bl_label = "Avacado"
    bl_idname = 'color.ge_avacado'
    def execute(self, context):
        set_base_color(0xb3b280, self.bl_label)
        return {'FINISHED'}

class GEAvacadoLight(bpy.types.Operator):
    """General Electric Avacado Light"""
    bl_label = "Avacado Light"
    bl_idname = 'color.ge_avacado_light'
    def execute(self, context):
        set_base_color(0x99915d, self.bl_label)
        return {'FINISHED'}

class GEAvacadoDark(bpy.types.Operator):
    """General Electric Avacado Dark"""
    bl_label = "Avacado Dark"
    bl_idname = 'color.ge_avacado_dark'
    def execute(self, context):
        set_base_color(0x615b37, self.bl_label)
        return {'FINISHED'}

class GEHarvestGold(bpy.types.Operator):
    """General Electric Harvest Gold"""
    bl_label = "Harvest Gold"
    bl_idname = 'color.ge_harvest_gold'
    def execute(self, context):
        set_base_color(0xdcbc80, self.bl_label)
        return {'FINISHED'}

class GEHarvestDark(bpy.types.Operator):
    """General Electric Harvest Dark"""
    bl_label = "Harvest Dark"
    bl_idname = 'color.ge_harvest_dark'
    def execute(self, context):
        set_base_color(0xa68d56, self.bl_label)
        return {'FINISHED'}

class GEHarvestLight(bpy.types.Operator):
    """General Electric Harvest Light"""
    bl_label = "Harvest Light"
    bl_idname = 'color.ge_harvest_light'
    def execute(self, context):
        set_base_color(0xdebd80, self.bl_label)
        return {'FINISHED'}
