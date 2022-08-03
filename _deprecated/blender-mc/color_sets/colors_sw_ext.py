import bpy
from .colors_functions import *

# SHERWIN WILLIAMS - EXTERIOR

class SMBirdseyeMaple(bpy.types.Operator):
    """Suburban Modern Birdseye Maple"""
    bl_label = "Birdseye Maple"
    bl_idname = 'color.sm_birdseye_maple'
    def execute(self, context):
        set_base_color(0xe4c495, self.bl_label)
        return {'FINISHED'}

class SMCocoon(bpy.types.Operator):
    """Suburban Modern Cocoon"""
    bl_label = "Cocoon"
    bl_idname = 'color.sm_cocoon'
    def execute(self, context):
        set_base_color(0x726b5b, self.bl_label)
        return {'FINISHED'}

class SMOldeWorldGold(bpy.types.Operator):
    """Suburban Modern Olde World Gold"""
    bl_label = "Olde World Gold"
    bl_idname = 'color.sm_olde_world_gold'
    def execute(self, context):
        set_base_color(0x8f6c3e, self.bl_label)
        return {'FINISHED'}

class SMWoolSkein(bpy.types.Operator):
    """Suburban Modern Wool Skein"""
    bl_label = "Wool Skein"
    bl_idname = 'color.sm_wool_skein'
    def execute(self, context):
        set_base_color(0xd9cfba, self.bl_label)
        return {'FINISHED'}

class SMArtisanTan(bpy.types.Operator):
    """Suburban Modern Artisan Tan"""
    bl_label = "Artisan Tan"
    bl_idname = 'color.sm_artisan_tan'
    def execute(self, context):
        set_base_color(0xb09879, self.bl_label)
        return {'FINISHED'}

class SMStatusBronze(bpy.types.Operator):
    """Suburban Modern Status Bronze"""
    bl_label = "Status Bronze"
    bl_idname = 'color.sm_status_bronze'
    def execute(self, context):
        set_base_color(0x5c4d3c, self.bl_label)
        return {'FINISHED'}

class SMTatamiTan(bpy.types.Operator):
    """Suburban Modern Tatami Tan"""
    bl_label = "Tatami Tan"
    bl_idname = 'color.sm_tatami_tan'
    def execute(self, context):
        set_base_color(0xba8c64, self.bl_label)
        return {'FINISHED'}

class SMColonyBuff(bpy.types.Operator):
    """Suburban Modern Colony Buff"""
    bl_label = "Colony Buff"
    bl_idname = 'color.sm_colony_buff'
    def execute(self, context):
        set_base_color(0xddc6ab, self.bl_label)
        return {'FINISHED'}

class SMHomburgGray(bpy.types.Operator):
    """Suburban Modern Homburg Gray"""
    bl_label = "Homburg Gray"
    bl_idname = 'color.sm_homburg_gray'
    def execute(self, context):
        set_base_color(0x666d69, self.bl_label)
        return {'FINISHED'}

class SMMuslin(bpy.types.Operator):
    """Suburban Modern Muslin"""
    bl_label = "Muslin"
    bl_idname = 'color.sm_muslin'
    def execute(self, context):
        set_base_color(0xeadfc9, self.bl_label)
        return {'FINISHED'}

class SMStrawHarvest(bpy.types.Operator):
    """Suburban Modern Straw Harvest"""
    bl_label = "Straw Harvest"
    bl_idname = 'color.sm_straw_harvest'
    def execute(self, context):
        set_base_color(0xdbc8a2, self.bl_label)
        return {'FINISHED'}

class SMRuralGreen(bpy.types.Operator):
    """Suburban Modern Rural Green"""
    bl_label = "Rural Green"
    bl_idname = 'color.sm_rural_green'
    def execute(self, context):
        set_base_color(0x8d844d, self.bl_label)
        return {'FINISHED'}

class SMExtraWhite(bpy.types.Operator):
    """Suburban Modern Extra White"""
    bl_label = "Extra White"
    bl_idname = 'color.sm_extra_white'
    def execute(self, context):
        set_base_color(0xeeefea, self.bl_label)
        return {'FINISHED'}

class SMRushingRiver(bpy.types.Operator):
    """Suburban Modern Rushing River"""
    bl_label = "Rushing River"
    bl_idname = 'color.sm_rushing_river'
    def execute(self, context):
        set_base_color(0xa19c8f, self.bl_label)
        return {'FINISHED'}

class SMSpicedCider(bpy.types.Operator):
    """Suburban Modern Spiced Cider"""
    bl_label = "Spiced Cider"
    bl_idname = 'color.sm_spiced_cider'
    def execute(self, context):
        set_base_color(0xb0785c, self.bl_label)
        return {'FINISHED'}

class SMRetreat(bpy.types.Operator):
    """Suburban Modern Retreat"""
    bl_label = "Retreat"
    bl_idname = 'color.sm_retreat'
    def execute(self, context):
        set_base_color(0x7a8076, self.bl_label)
        return {'FINISHED'}

class SMNetsuke(bpy.types.Operator):
    """Suburban Modern Netsuke"""
    bl_label = "Netsuke"
    bl_idname = 'color.sm_netsuke'
    def execute(self, context):
        set_base_color(0xe0cfb0, self.bl_label)
        return {'FINISHED'}

class SMEdgyGold(bpy.types.Operator):
    """Suburban Modern Edgy Gold"""
    bl_label = "Edgy Gold"
    bl_idname = 'color.sm_edgy_gold'
    def execute(self, context):
        set_base_color(0xb1975f, self.bl_label)
        return {'FINISHED'}

class SMJoggingPath(bpy.types.Operator):
    """Suburban Modern Jogging Path"""
    bl_label = "Jogging Path"
    bl_idname = 'color.sm_jogging_path'
    def execute(self, context):
        set_base_color(0xc0b9a9, self.bl_label)
        return {'FINISHED'}

class SMIntellectualGray(bpy.types.Operator):
    """Suburban Modern Intellectual Gray"""
    bl_label = "Intellectual Gray"
    bl_idname = 'color.sm_intellectual_gray'
    def execute(self, context):
        set_base_color(0xa8a093, self.bl_label)
        return {'FINISHED'}

class SMThunderGray(bpy.types.Operator):
    """Suburban Modern Thunder Gray"""
    bl_label = "Thunder Gray"
    bl_idname = 'color.sm_thunder_gray'
    def execute(self, context):
        set_base_color(0x57534c, self.bl_label)
        return {'FINISHED'}

class SMAnjouPear(bpy.types.Operator):
    """Suburban Modern Anjou Pear"""
    bl_label = "Anjou Pear"
    bl_idname = 'color.sm_anjou_pear'
    def execute(self, context):
        set_base_color(0xddac6d, self.bl_label)
        return {'FINISHED'}

class SMJerseyCream(bpy.types.Operator):
    """Suburban Modern Jersey Cream"""
    bl_label = "Jersey Cream"
    bl_idname = 'color.sm_jersey_cream'
    def execute(self, context):
        set_base_color(0xf5debb, self.bl_label)
        return {'FINISHED'}

class SMWarmStone(bpy.types.Operator):
    """Suburban Modern Warm Stone"""
    bl_label = "Warm Stone"
    bl_idname = 'color.sm_warm_stone'
    def execute(self, context):
        set_base_color(0x887b6c, self.bl_label)
        return {'FINISHED'}

class SMCorkWedge(bpy.types.Operator):
    """Suburban Modern Cork Wedge"""
    bl_label = "Cork Wedge"
    bl_idname = 'color.sm_cork_wedge'
    def execute(self, context):
        set_base_color(0xc1a98a, self.bl_label)
        return {'FINISHED'}

class SMSmokehouse(bpy.types.Operator):
    """Suburban Modern Smokehouse"""
    bl_label = "Smokehouse"
    bl_idname = 'color.sm_smokehouse'
    def execute(self, context):
        set_base_color(0x716354, self.bl_label)
        return {'FINISHED'}

class SMRusticRed(bpy.types.Operator):
    """Suburban Modern Rustic Red"""
    bl_label = "Rustic Red"
    bl_idname = 'color.sm_rustic_red'
    def execute(self, context):
        set_base_color(0x703229, self.bl_label)
        return {'FINISHED'}
