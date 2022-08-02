import bpy
from .colors_functions import *

# MID-CENTURY MODERN COLORS

class MCMCGINGER_ALE(bpy.types.Operator):
    """Apply Color Ginger Ale"""
    bl_label = "Ginger Ale"
    bl_idname = 'color.ginger_ale'
    def execute(self, context):
        set_base_color(0xefd079, self.bl_label)
        return {'FINISHED'}

class MCMCPABLO_HONEY(bpy.types.Operator):
    """Apply Color Pablo Honey"""
    bl_label = "Pablo Honey"
    bl_idname = 'color.pablo_honey'
    def execute(self, context):
        set_base_color(0xeac164, self.bl_label)
        return {'FINISHED'}

class MCMCMIAMI_PARASOL(bpy.types.Operator):
    """Apply Color Miami Parasol"""
    bl_label = "Miami Parasol"
    bl_idname = 'color.miami_parasol'
    def execute(self, context):
        set_base_color(0xf0d3a4, self.bl_label)
        return {'FINISHED'}

class MCMCTANLINES(bpy.types.Operator):
    """Apply Color Tanlines"""
    bl_label = "Tanlines"
    bl_idname = 'color.tanlines'
    def execute(self, context):
        set_base_color(0xc48c3f, self.bl_label)
        return {'FINISHED'}

class MCMCBLUE_SEAFOAM(bpy.types.Operator):
    """Apply Color Blue Seafoam"""
    bl_label = "Blue Seafoam"
    bl_idname = 'color.blue_seafoam'
    def execute(self, context):
        set_base_color(0xafe3e9, self.bl_label)
        return {'FINISHED'}

class MCMCSATURDAY_ON_SUNDAY(bpy.types.Operator):
    """Apply Color Saturday On Sunday"""
    bl_label = "Saturday On Sunday"
    bl_idname = 'color.saturday_on_sunday'
    def execute(self, context):
        set_base_color(0x567475, self.bl_label)
        return {'FINISHED'}

class MCMCSICILY_OR_CYPRUS(bpy.types.Operator):
    """Apply Color Sicily Or Cyprus"""
    bl_label = "Sicily Or Cyprus"
    bl_idname = 'color.sicily_or_cyprus'
    def execute(self, context):
        set_base_color(0x488182, self.bl_label)
        return {'FINISHED'}

class MCMCNOVELTY_WAVE(bpy.types.Operator):
    """Apply Color Novelty Wave"""
    bl_label = "Novelty Wave"
    bl_idname = 'color.novelty_wave'
    def execute(self, context):
        set_base_color(0x73969f, self.bl_label)
        return {'FINISHED'}

class MCMCRELENTLESS_OLIVE(bpy.types.Operator):
    """Apply Color Relentless Olive"""
    bl_label = "Relentless Olive"
    bl_idname = 'color.relentless_olive'
    def execute(self, context):
        set_base_color(0x71713e, self.bl_label)
        return {'FINISHED'}

class MCMCGREEN_ROOT(bpy.types.Operator):
    """Apply Color Green Root"""
    bl_label = "Green Root"
    bl_idname = 'color.green_root'
    def execute(self, context):
        set_base_color(0x848551, self.bl_label)
        return {'FINISHED'}

class MCMCSAGED(bpy.types.Operator):
    """Apply Color Saged"""
    bl_label = "Saged"
    bl_idname = 'color.saged'
    def execute(self, context):
        set_base_color(0x969684, self.bl_label)
        return {'FINISHED'}

class MCMCDRIVE_THRU_SAFARI(bpy.types.Operator):
    """Apply Color Drive-Thru Safari"""
    bl_label = "Drive-Thru Safari"
    bl_idname = 'color.drive_thru_safari'
    def execute(self, context):
        set_base_color(0x8b9d82, self.bl_label)
        return {'FINISHED'}

class MCMCNATURAL_HABITAT(bpy.types.Operator):
    """Apply Color Natural Habitat"""
    bl_label = "Natural Habitat"
    bl_idname = 'color.natural_habitat'
    def execute(self, context):
        set_base_color(0xc4c2a3, self.bl_label)
        return {'FINISHED'}

class MCMCCHEROKEE_RED(bpy.types.Operator):
    """Apply Color Cherokee Red"""
    bl_label = "Cherokee Red"
    bl_idname = 'color.cherokee_red'
    def execute(self, context):
        set_base_color(0x764139, self.bl_label)
        return {'FINISHED'}

class MCMCLIPSTICK_ON_THE_MIRROR(bpy.types.Operator):
    """Apply Color Lipstick on the Mirror"""
    bl_label = "Lipstick on the Mirror"
    bl_idname = 'color.lipstick_on_the_mirror'
    def execute(self, context):
        set_base_color(0xac2c3e, self.bl_label)
        return {'FINISHED'}

class MCMCSELF_PORTRAIT(bpy.types.Operator):
    """Apply Color Self-Portrait"""
    bl_label = "Self-Portrait"
    bl_idname = 'color.self_portrait'
    def execute(self, context):
        set_base_color(0x642c2f, self.bl_label)
        return {'FINISHED'}

class MCMCNEGRONI(bpy.types.Operator):
    """Apply Color Negroni"""
    bl_label = "Negroni"
    bl_idname = 'color.negroni'
    def execute(self, context):
        set_base_color(0xa53b33, self.bl_label)
        return {'FINISHED'}

class MCMCAUTUMN_GLIMMER(bpy.types.Operator):
    """Apply Color Autumn Glimmer"""
    bl_label = "Autumn Glimmer"
    bl_idname = 'color.autumn_glimmer'
    def execute(self, context):
        set_base_color(0xE97F4E, self.bl_label)
        return {'FINISHED'}

class MCMCORANGE_FRUIT(bpy.types.Operator):
    """Apply Color Orange Fruit"""
    bl_label = "Orange Fruit"
    bl_idname = 'color.orange_fruit'
    def execute(self, context):
        set_base_color(0xf88f21, self.bl_label)
        return {'FINISHED'}

class MCMCAPERITIVO_HOUR(bpy.types.Operator):
    """Apply Color Aperitivo Hour"""
    bl_label = "Aperitivo Hour"
    bl_idname = 'color.aperitivo_hour'
    def execute(self, context):
        set_base_color(0xe7a885, self.bl_label)
        return {'FINISHED'}

class MCMCBRIGHT_MARIGOLD(bpy.types.Operator):
    """Apply Color Bright Marigold"""
    bl_label = "Bright Marigold"
    bl_idname = 'color.bright_marigold'
    def execute(self, context):
        set_base_color(0xd78754, self.bl_label)
        return {'FINISHED'}

class MCMCWRIGHT_SOFT_GRAY(bpy.types.Operator):
    """Apply Color Wright Soft Gray"""
    bl_label = "Wright Soft Gray"
    bl_idname = 'color.wright_soft_gray'
    def execute(self, context):
        set_base_color(0x8e8fbf, self.bl_label)
        return {'FINISHED'}

class MCMCAFTER_HOURS(bpy.types.Operator):
    """Apply Color After Hours"""
    bl_label = "After Hours"
    bl_idname = 'color.after_hours'
    def execute(self, context):
        set_base_color(0x3c3b3e, self.bl_label)
        return {'FINISHED'}

class MCMCMOTOR_GRAY(bpy.types.Operator):
    """Apply Color Motor Gray"""
    bl_label = "Motor Gray"
    bl_idname = 'color.motor_gray'
    def execute(self, context):
        set_base_color(0x5c5d5f, self.bl_label)
        return {'FINISHED'}

class MCMCNO_CURFEW(bpy.types.Operator):
    """Apply Color No Curfew"""
    bl_label = "No Curfew"
    bl_idname = 'color.no_curfew'
    def execute(self, context):
        set_base_color(0x626669, self.bl_label)
        return {'FINISHED'}

class MCMCCOCOA_SHELL(bpy.types.Operator):
    """Apply Color Cocoa Shell"""
    bl_label = "Cocoa Shell"
    bl_idname = 'color.cocoa_shell'
    def execute(self, context):
        set_base_color(0x7e6657, self.bl_label)
        return {'FINISHED'}

class MCMCFAWN_DOE(bpy.types.Operator):
    """Apply Color Fawn Doe"""
    bl_label = "Fawn Doe"
    bl_idname = 'color.fawn_doe'
    def execute(self, context):
        set_base_color(0xb5a99d, self.bl_label)
        return {'FINISHED'}

class MCMCSENTIMENTAL_REASONS(bpy.types.Operator):
    """Apply Color Sentimental Reasons"""
    bl_label = "Sentimental Reasons"
    bl_idname = 'color.sentimental_reasons'
    def execute(self, context):
        set_base_color(0xa29790, self.bl_label)
        return {'FINISHED'}

class MCMCCOBBLESTONE_STREETS(bpy.types.Operator):
    """Apply Color Cobblestone Streets"""
    bl_label = "Cobblestone Streets"
    bl_idname = 'color.cobblestone_streets'
    def execute(self, context):
        set_base_color(0x918475, self.bl_label)
        return {'FINISHED'}
