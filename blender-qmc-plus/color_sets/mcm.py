import bpy

from .globals import *
from .color_functions import *


# MID-CENTURY MODERN COLORS

class MCMGINGER_ALE(bpy.types.Operator):
    """Apply Color Ginger Ale"""
    bl_label = "Ginger Ale"
    bl_idname = 'color.ginger_ale'
    def execute(self, context):
        set_base_color(0xefd079, self.bl_label)
        return {'FINISHED'}

class MCMPABLO_HONEY(bpy.types.Operator):
    """Apply Color Pablo Honey"""
    bl_label = "Pablo Honey"
    bl_idname = 'color.pablo_honey'
    def execute(self, context):
        set_base_color(0xeac164, self.bl_label)
        return {'FINISHED'}

class MCMMIAMI_PARASOL(bpy.types.Operator):
    """Apply Color Miami Parasol"""
    bl_label = "Miami Parasol"
    bl_idname = 'color.miami_parasol'
    def execute(self, context):
        set_base_color(0xf0d3a4, self.bl_label)
        return {'FINISHED'}

class MCMTANLINES(bpy.types.Operator):
    """Apply Color Tanlines"""
    bl_label = "Tanlines"
    bl_idname = 'color.tanlines'
    def execute(self, context):
        set_base_color(0xc48c3f, self.bl_label)
        return {'FINISHED'}

class MCMBLUE_SEAFOAM(bpy.types.Operator):
    """Apply Color Blue Seafoam"""
    bl_label = "Blue Seafoam"
    bl_idname = 'color.blue_seafoam'
    def execute(self, context):
        set_base_color(0xafe3e9, self.bl_label)
        return {'FINISHED'}

class MCMSATURDAY_ON_SUNDAY(bpy.types.Operator):
    """Apply Color Saturday On Sunday"""
    bl_label = "Saturday On Sunday"
    bl_idname = 'color.saturday_on_sunday'
    def execute(self, context):
        set_base_color(0x567475, self.bl_label)
        return {'FINISHED'}

class MCMSICILY_OR_CYPRUS(bpy.types.Operator):
    """Apply Color Sicily Or Cyprus"""
    bl_label = "Sicily Or Cyprus"
    bl_idname = 'color.sicily_or_cyprus'
    def execute(self, context):
        set_base_color(0x488182, self.bl_label)
        return {'FINISHED'}

class MCMNOVELTY_WAVE(bpy.types.Operator):
    """Apply Color Novelty Wave"""
    bl_label = "Novelty Wave"
    bl_idname = 'color.novelty_wave'
    def execute(self, context):
        set_base_color(0x73969f, self.bl_label)
        return {'FINISHED'}

class MCMRELENTLESS_OLIVE(bpy.types.Operator):
    """Apply Color Relentless Olive"""
    bl_label = "Relentless Olive"
    bl_idname = 'color.relentless_olive'
    def execute(self, context):
        set_base_color(0x71713e, self.bl_label)
        return {'FINISHED'}

class MCMGREEN_ROOT(bpy.types.Operator):
    """Apply Color Green Root"""
    bl_label = "Green Root"
    bl_idname = 'color.green_root'
    def execute(self, context):
        set_base_color(0x848551, self.bl_label)
        return {'FINISHED'}

class MCMSAGED(bpy.types.Operator):
    """Apply Color Saged"""
    bl_label = "Saged"
    bl_idname = 'color.saged'
    def execute(self, context):
        set_base_color(0x969684, self.bl_label)
        return {'FINISHED'}

class MCMDRIVE_THRU_SAFARI(bpy.types.Operator):
    """Apply Color Drive-Thru Safari"""
    bl_label = "Drive-Thru Safari"
    bl_idname = 'color.drive_thru_safari'
    def execute(self, context):
        set_base_color(0x8b9d82, self.bl_label)
        return {'FINISHED'}

class MCMNATURAL_HABITAT(bpy.types.Operator):
    """Apply Color Natural Habitat"""
    bl_label = "Natural Habitat"
    bl_idname = 'color.natural_habitat'
    def execute(self, context):
        set_base_color(0xc4c2a3, self.bl_label)
        return {'FINISHED'}

class MCMCHEROKEE_RED(bpy.types.Operator):
    """Apply Color Cherokee Red"""
    bl_label = "Cherokee Red"
    bl_idname = 'color.cherokee_red'
    def execute(self, context):
        set_base_color(0x764139, self.bl_label)
        return {'FINISHED'}

class MCMLIPSTICK_ON_THE_MIRROR(bpy.types.Operator):
    """Apply Color Lipstick on the Mirror"""
    bl_label = "Lipstick on the Mirror"
    bl_idname = 'color.lipstick_on_the_mirror'
    def execute(self, context):
        set_base_color(0xac2c3e, self.bl_label)
        return {'FINISHED'}

class MCMSELF_PORTRAIT(bpy.types.Operator):
    """Apply Color Self-Portrait"""
    bl_label = "Self-Portrait"
    bl_idname = 'color.self_portrait'
    def execute(self, context):
        set_base_color(0x642c2f, self.bl_label)
        return {'FINISHED'}

class MCMNEGRONI(bpy.types.Operator):
    """Apply Color Negroni"""
    bl_label = "Negroni"
    bl_idname = 'color.negroni'
    def execute(self, context):
        set_base_color(0xa53b33, self.bl_label)
        return {'FINISHED'}

class MCMAUTUMN_GLIMMER(bpy.types.Operator):
    """Apply Color Autumn Glimmer"""
    bl_label = "Autumn Glimmer"
    bl_idname = 'color.autumn_glimmer'
    def execute(self, context):
        set_base_color(0xE97F4E, self.bl_label)
        return {'FINISHED'}

class MCMORANGE_FRUIT(bpy.types.Operator):
    """Apply Color Orange Fruit"""
    bl_label = "Orange Fruit"
    bl_idname = 'color.orange_fruit'
    def execute(self, context):
        set_base_color(0xf88f21, self.bl_label)
        return {'FINISHED'}

class MCMAPERITIVO_HOUR(bpy.types.Operator):
    """Apply Color Aperitivo Hour"""
    bl_label = "Aperitivo Hour"
    bl_idname = 'color.aperitivo_hour'
    def execute(self, context):
        set_base_color(0xe7a885, self.bl_label)
        return {'FINISHED'}

class MCMBRIGHT_MARIGOLD(bpy.types.Operator):
    """Apply Color Bright Marigold"""
    bl_label = "Bright Marigold"
    bl_idname = 'color.bright_marigold'
    def execute(self, context):
        set_base_color(0xd78754, self.bl_label)
        return {'FINISHED'}

class MCMWRIGHT_SOFT_GRAY(bpy.types.Operator):
    """Apply Color Wright Soft Gray"""
    bl_label = "Wright Soft Gray"
    bl_idname = 'color.wright_soft_gray'
    def execute(self, context):
        set_base_color(0x8e8fbf, self.bl_label)
        return {'FINISHED'}

class MCMAFTER_HOURS(bpy.types.Operator):
    """Apply Color After Hours"""
    bl_label = "After Hours"
    bl_idname = 'color.after_hours'
    def execute(self, context):
        set_base_color(0x3c3b3e, self.bl_label)
        return {'FINISHED'}

class MCMMOTOR_GRAY(bpy.types.Operator):
    """Apply Color Motor Gray"""
    bl_label = "Motor Gray"
    bl_idname = 'color.motor_gray'
    def execute(self, context):
        set_base_color(0x5c5d5f, self.bl_label)
        return {'FINISHED'}

class MCMNO_CURFEW(bpy.types.Operator):
    """Apply Color No Curfew"""
    bl_label = "No Curfew"
    bl_idname = 'color.no_curfew'
    def execute(self, context):
        set_base_color(0x626669, self.bl_label)
        return {'FINISHED'}

class MCMCOCOA_SHELL(bpy.types.Operator):
    """Apply Color Cocoa Shell"""
    bl_label = "Cocoa Shell"
    bl_idname = 'color.cocoa_shell'
    def execute(self, context):
        set_base_color(0x7e6657, self.bl_label)
        return {'FINISHED'}

class MCMFAWN_DOE(bpy.types.Operator):
    """Apply Color Fawn Doe"""
    bl_label = "Fawn Doe"
    bl_idname = 'color.fawn_doe'
    def execute(self, context):
        set_base_color(0xb5a99d, self.bl_label)
        return {'FINISHED'}

class MCMSENTIMENTAL_REASONS(bpy.types.Operator):
    """Apply Color Sentimental Reasons"""
    bl_label = "Sentimental Reasons"
    bl_idname = 'color.sentimental_reasons'
    def execute(self, context):
        set_base_color(0xa29790, self.bl_label)
        return {'FINISHED'}

class MCMCOBBLESTONE_STREETS(bpy.types.Operator):
    """Apply Color Cobblestone Streets"""
    bl_label = "Cobblestone Streets"
    bl_idname = 'color.cobblestone_streets'
    def execute(self, context):
        set_base_color(0x918475, self.bl_label)
        return {'FINISHED'}


# MID-CENTURY MODERN COLORS PANEL

class MCMPanel(bpy.types.Panel):
    bl_idname = "MCM_PT_Panel"
    bl_label = "Mid-Century Modern Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout


# Golden Yellow
class MCMYELLOWS(bpy.types.Panel):
    bl_idname = "YELLOWS_PT_Panel"
    bl_label = "Golden Yellow"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_yellow_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_yellow_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_yellow_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_yellow_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.miami_parasol", text="Miami Parasol")
        scol.operator("color.ginger_ale", text="Ginger Ale")
        scol.operator("color.pablo_honey", text="Pablo Honey")
        scol.operator("color.tanlines", text="Tanlines")

# Serena Aqua
class MCMBLUES(bpy.types.Panel):
    bl_idname = "BLUES_PT_Panel"
    bl_label = "Serena Aqua"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_blue_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_blue_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_blue_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_blue_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.blue_seafoam", text="Blue Seafoam")
        scol.operator("color.novelty_wave", text="Novelty Wave")
        scol.operator("color.saturday_on_sunday", text="Saturday On Sunday")
        scol.operator("color.sicily_or_cyprus", text="Sicily Or Cyprus")

# Olive Green and Wasabi
class MCMGREENS(bpy.types.Panel):
    bl_idname = "GREENS_PT_Panel"
    bl_label = "Olive Green & Wasabi"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_green_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_green_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_green_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_green_04"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_green_05"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.natural_habitat", text="Natural Habitat")
        scol.operator("color.saged", text="Saged")
        scol.operator("color.drive_thru_safari", text="Drive-Thru Safari")
        scol.operator("color.green_root", text="Green Root")
        scol.operator("color.relentless_olive", text="Relentless Olive")

# Pops of Red
class MCMREDS(bpy.types.Panel):
    bl_idname = "REDS_PT_Panel"
    bl_label = "Pops of Red"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_red_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_red_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_red_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_red_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.cherokee_red", text="Cherokee Red")
        scol.operator("color.self_portrait", text="Self-Portrait")
        scol.operator("color.negroni", text="Negroni")
        scol.operator("color.lipstick_on_the_mirror", text="Lipstick on the Mirror")

# Tangerine and Ochre
class MCMORANGES(bpy.types.Panel):
    bl_idname = "ORANGES_PT_Panel"
    bl_label = "Tangerine and Ochre"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_orange_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_orange_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_orange_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_orange_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.aperitivo_hour", text="Aperitivo Hour")
        scol.operator("color.bright_marigold", text="Bright Marigold")
        scol.operator("color.autumn_glimmer", text="Autumn Glimmer")
        scol.operator("color.orange_fruit", text="Orange Fruit")

# Pewter Gray
class MCMGRAYS(bpy.types.Panel):
    bl_idname = "GRAYS_PT_Panel"
    bl_label = "Pewter Gray"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_gray_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_gray_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_gray_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_gray_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.wright_soft_gray", text="Wright Soft Gray")
        scol.operator("color.no_curfew", text="No Curfew")
        scol.operator("color.motor_gray", text="Motor Gray")
        scol.operator("color.after_hours", text="After Hours")

# Soft and Earthy Brown
class MCMBROWNS(bpy.types.Panel):
    bl_idname = "BROWNS_PT_Panel"
    bl_label = "Soft and Earthy Brown"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCM_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcm_brown_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_brown_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_brown_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcm_brown_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.fawn_doe", text="Fawn Doe")
        scol.operator("color.sentimental_reasons", text="Sentimental Reasons")
        scol.operator("color.cobblestone_streets", text="Cobblestone Streets")
        scol.operator("color.cocoa_shell", text="Cocoa Shell")


array_mcm = [
    MCMPanel,
    MCMYELLOWS,
    MCMBLUES,
    MCMGREENS,
    MCMREDS,
    MCMORANGES,
    MCMGRAYS,
    MCMBROWNS,
    MCMGINGER_ALE,
    MCMPABLO_HONEY,
    MCMMIAMI_PARASOL,
    MCMTANLINES,
    MCMBLUE_SEAFOAM,
    MCMSATURDAY_ON_SUNDAY,
    MCMSICILY_OR_CYPRUS,
    MCMNOVELTY_WAVE,
    MCMRELENTLESS_OLIVE,
    MCMGREEN_ROOT,
    MCMSAGED,
    MCMDRIVE_THRU_SAFARI,
    MCMNATURAL_HABITAT,
    MCMCHEROKEE_RED,
    MCMLIPSTICK_ON_THE_MIRROR,
    MCMSELF_PORTRAIT,
    MCMNEGRONI,
    MCMAUTUMN_GLIMMER,
    MCMORANGE_FRUIT,
    MCMAPERITIVO_HOUR,
    MCMBRIGHT_MARIGOLD,
    MCMWRIGHT_SOFT_GRAY,
    MCMAFTER_HOURS,
    MCMMOTOR_GRAY,
    MCMNO_CURFEW,
    MCMCOCOA_SHELL,
    MCMFAWN_DOE,
    MCMSENTIMENTAL_REASONS,
    MCMCOBBLESTONE_STREETS,
]
