import bpy

from .globals import *
from .color_functions import *


# SHERWIN WILLIAMS - INTERIOR

class SMAppleBlossom(bpy.types.Operator):
    """Suburban Modern Apple Blossom"""
    bl_label = "Apple Blossom"
    bl_idname = 'color.sm_appleblossom'
    def execute(self, context):
        set_base_color(0xdab5b4, self.bl_label)
        return {'FINISHED'}

class SMAvocado(bpy.types.Operator):
    """Suburban Modern Avocado"""
    bl_label = "Avocado"
    bl_idname = 'color.sm_avocado'
    def execute(self, context):
        set_base_color(0x857c5d, self.bl_label)
        return {'FINISHED'}

class SMBeige(bpy.types.Operator):
    """Suburban Modern Beige"""
    bl_label = "Beige"
    bl_idname = 'color.sm_beige'
    def execute(self, context):
        set_base_color(0xdfc8b5, self.bl_label)
        return {'FINISHED'}

class SMCaribbeanCoral(bpy.types.Operator):
    """Suburban Modern Caribbean Coral"""
    bl_label = "Caribbean Coral"
    bl_idname = 'color.sm_caribbean_coral'
    def execute(self, context):
        set_base_color(0xbe795e, self.bl_label)
        return {'FINISHED'}

class SMChartreuse(bpy.types.Operator):
    """Suburban Modern Chartreuse"""
    bl_label = "Chartreuse"
    bl_idname = 'color.sm_chartreuse'
    def execute(self, context):
        set_base_color(0xe1d286, self.bl_label)
        return {'FINISHED'}

class SMChelseaGray(bpy.types.Operator):
    """Suburban Modern Chelsea Gray"""
    bl_label = "Chelsea Gray"
    bl_idname = 'color.sm_chelsea_gray'
    def execute(self, context):
        set_base_color(0xb6b7b0, self.bl_label)
        return {'FINISHED'}

class SMClassicFrenchGray(bpy.types.Operator):
    """Suburban Modern Classic French Gray"""
    bl_label = "Classic French Gray"
    bl_idname = 'color.sm_classic_french_gray'
    def execute(self, context):
        set_base_color(0x888782, self.bl_label)
        return {'FINISHED'}

class SMFairfaxBrown(bpy.types.Operator):
    """Suburban Modern Fairfax Brown"""
    bl_label = "Fairfax Brown"
    bl_idname = 'color.sm_fairfax_brown'
    def execute(self, context):
        set_base_color(0x61463a, self.bl_label)
        return {'FINISHED'}

class SMHarvestGold(bpy.types.Operator):
    """Suburban Modern Harvest Gold"""
    bl_label = "Harvest Gold"
    bl_idname = 'color.sm_harvest_gold'
    def execute(self, context):
        set_base_color(0xd9a06a, self.bl_label)
        return {'FINISHED'}

class SMHolidayTurquoise(bpy.types.Operator):
    """Suburban Modern Holiday Turquoise"""
    bl_label = "Holiday Turquoise"
    bl_idname = 'color.sm_holiday_turquoise'
    def execute(self, context):
        set_base_color(0x8ac6bd, self.bl_label)
        return {'FINISHED'}

class SMNewColonialYellow(bpy.types.Operator):
    """Suburban Modern New Colonial Yellow"""
    bl_label = "New Colonial Yellow"
    bl_idname = 'color.sm_new_colonial_yellow'
    def execute(self, context):
        set_base_color(0xe1bd99, self.bl_label)
        return {'FINISHED'}

class SMPeaceYellow(bpy.types.Operator):
    """Suburban Modern Peace Yellow"""
    bl_label = "Peace Yellow"
    bl_idname = 'color.sm_peace_yellow'
    def execute(self, context):
        set_base_color(0xeecf9e, self.bl_label)
        return {'FINISHED'}

class SMPinkFlamingo(bpy.types.Operator):
    """Suburban Modern Pink Flamingo"""
    bl_label = "Pink Flamingo"
    bl_idname = 'color.sm_pink_flamingo'
    def execute(self, context):
        set_base_color(0xcd717b, self.bl_label)
        return {'FINISHED'}

class SMPinkyBeige(bpy.types.Operator):
    """Suburban Modern Pinky Beige"""
    bl_label = "Pinky Beige"
    bl_idname = 'color.sm_pinky_beige'
    def execute(self, context):
        set_base_color(0xc9aa98, self.bl_label)
        return {'FINISHED'}

class SMPowderBlu(bpy.types.Operator):
    """Suburban Modern Powder Blu"""
    bl_label = "Powder Blu"
    bl_idname = 'color.sm_powder_blu'
    def execute(self, context):
        set_base_color(0x89a4ad, self.bl_label)
        return {'FINISHED'}

class SMRadiantLilac(bpy.types.Operator):
    """Suburban Modern Radiant Lilac"""
    bl_label = "Radiant Lilac"
    bl_idname = 'color.sm_radiant_lilac'
    def execute(self, context):
        set_base_color(0xa489a0, self.bl_label)
        return {'FINISHED'}

class SMSage(bpy.types.Operator):
    """Suburban Modern Sage"""
    bl_label = "Sage"
    bl_idname = 'color.sm_sage'
    def execute(self, context):
        set_base_color(0xb3ae95, self.bl_label)
        return {'FINISHED'}

class SMSageGreenLight(bpy.types.Operator):
    """Suburban Modern Sage Green Light"""
    bl_label = "Sage Green Light"
    bl_idname = 'color.sm_sage_green_light'
    def execute(self, context):
        set_base_color(0x73705e, self.bl_label)
        return {'FINISHED'}

class SMSunbeamYellow(bpy.types.Operator):
    """Suburban Modern Sunbeam Yellow"""
    bl_label = "Sunbeam Yellow"
    bl_idname = 'color.sm_sunbeam_yellow'
    def execute(self, context):
        set_base_color(0xf0d39d, self.bl_label)
        return {'FINISHED'}

class SMSycamoreTan(bpy.types.Operator):
    """Suburban Modern Sycamore Tan"""
    bl_label = "Sycamore Tan"
    bl_idname = 'color.sm_sycamore_tan'
    def execute(self, context):
        set_base_color(0x9c8a79, self.bl_label)
        return {'FINISHED'}

class SMWestchesterGray(bpy.types.Operator):
    """Suburban Modern Westchester Gray"""
    bl_label = "Westchester Gray"
    bl_idname = 'color.sm_westchester_gray'
    def execute(self, context):
        set_base_color(0x797978, self.bl_label)
        return {'FINISHED'}


# SHERWIN WILLIAMS - INTERIOR PANEL
class SMIPanel(bpy.types.Panel):
    bl_idname = "SMI_PT_Panel"
    bl_label = "Suburban Modern Interior"
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
        scol.label(text="", icon_value=g.c_icons["sm_pink_flamingo"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_appleblossom"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_caribbean_coral"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_fairfax_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_pinky_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_harvest_gold"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_new_colonial_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_sycamore_tan"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_peace_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_sunbeam_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_chartreuse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_avocado"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_sage"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_sage_green_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_holiday_turquoise"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_powder_blu"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_radiant_lilac"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_chelsea_gray"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_westchester_gray"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_classic_french_gray"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.sm_pink_flamingo", text="Pink Flamingo")
        scol.operator("color.sm_appleblossom", text="Apple Blossom")
        scol.operator("color.sm_caribbean_coral", text="Caribbean Coral")
        scol.operator("color.sm_fairfax_brown", text="Fairfax Brown")
        scol.operator("color.sm_pinky_beige", text="Pinky Beige")
        scol.operator("color.sm_beige", text="Beige")
        scol.operator("color.sm_harvest_gold", text="Harvest Gold")
        scol.operator("color.sm_new_colonial_yellow", text="New Colonial Yellow")
        scol.operator("color.sm_sycamore_tan", text="Sycamore Tan")
        scol.operator("color.sm_peace_yellow", text="Peace Yellow")
        scol.operator("color.sm_sunbeam_yellow", text="Sunbeam Yellow")
        scol.operator("color.sm_chartreuse", text="Chartreuse")
        scol.operator("color.sm_avocado", text="Avocado")
        scol.operator("color.sm_sage", text="Sage")
        scol.operator("color.sm_sage_green_light", text="Sage Green Light")
        scol.operator("color.sm_holiday_turquoise", text="Holiday Turquoise")
        scol.operator("color.sm_powder_blu", text="Powder Blu")
        scol.operator("color.sm_radiant_lilac", text="Radiant Lilac")
        scol.operator("color.sm_chelsea_gray", text="Chelsea Gray")
        scol.operator("color.sm_westchester_gray", text="Westchester Gray")
        scol.operator("color.sm_classic_french_gray", text="Classic French Gray")


array_sw_int = [
    SMIPanel,
    SMChartreuse,
    SMRadiantLilac,
    SMHolidayTurquoise,
    SMAppleBlossom,
    SMClassicFrenchGray,
    SMSunbeamYellow,
    SMPinkyBeige,
    SMPinkFlamingo,
    SMWestchesterGray,
    SMChelseaGray,
    SMSageGreenLight,
    SMNewColonialYellow,
    SMCaribbeanCoral,
    SMSycamoreTan,
    SMFairfaxBrown,
    SMPeaceYellow,
    SMHarvestGold,
    SMBeige,
    SMSage,
    SMAvocado,
    SMPowderBlu,
]
