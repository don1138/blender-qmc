import bpy

from .panel_classes import *

# MID-CENTURY MODERN COLORS PANEL

class MCMCPanel(bpy.types.Panel):
    bl_idname = "MCMC_PT_Panel"
    bl_label = "Mid-Century Modern Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout


# Golden Yellow
class MCMCYELLOWS(bpy.types.Panel):
    bl_idname = "YELLOWS_PT_Panel"
    bl_label = "Golden Yellow"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_yellow_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_yellow_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_yellow_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_yellow_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.miami_parasol", text="Miami Parasol")
        scol.operator("color.ginger_ale", text="Ginger Ale")
        scol.operator("color.pablo_honey", text="Pablo Honey")
        scol.operator("color.tanlines", text="Tanlines")

# Serena Aqua
class MCMCBLUES(bpy.types.Panel):
    bl_idname = "BLUES_PT_Panel"
    bl_label = "Serena Aqua"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_blue_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_blue_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_blue_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_blue_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.blue_seafoam", text="Blue Seafoam")
        scol.operator("color.novelty_wave", text="Novelty Wave")
        scol.operator("color.saturday_on_sunday", text="Saturday On Sunday")
        scol.operator("color.sicily_or_cyprus", text="Sicily Or Cyprus")

# Olive Green and Wasabi
class MCMCGREENS(bpy.types.Panel):
    bl_idname = "GREENS_PT_Panel"
    bl_label = "Olive Green & Wasabi"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_green_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_green_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_green_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_green_04"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_green_05"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.natural_habitat", text="Natural Habitat")
        scol.operator("color.saged", text="Saged")
        scol.operator("color.drive_thru_safari", text="Drive-Thru Safari")
        scol.operator("color.green_root", text="Green Root")
        scol.operator("color.relentless_olive", text="Relentless Olive")

# Pops of Red
class MCMCREDS(bpy.types.Panel):
    bl_idname = "REDS_PT_Panel"
    bl_label = "Pops of Red"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_red_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_red_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_red_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_red_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.cherokee_red", text="Cherokee Red")
        scol.operator("color.self_portrait", text="Self-Portrait")
        scol.operator("color.negroni", text="Negroni")
        scol.operator("color.lipstick_on_the_mirror", text="Lipstick on the Mirror")

# Tangerine and Ochre
class MCMCORANGES(bpy.types.Panel):
    bl_idname = "ORANGES_PT_Panel"
    bl_label = "Tangerine and Ochre"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_orange_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_orange_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_orange_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_orange_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.aperitivo_hour", text="Aperitivo Hour")
        scol.operator("color.bright_marigold", text="Bright Marigold")
        scol.operator("color.autumn_glimmer", text="Autumn Glimmer")
        scol.operator("color.orange_fruit", text="Orange Fruit")

# Pewter Gray
class MCMCGRAYS(bpy.types.Panel):
    bl_idname = "GRAYS_PT_Panel"
    bl_label = "Pewter Gray"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_gray_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_gray_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_gray_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_gray_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.wright_soft_gray", text="Wright Soft Gray")
        scol.operator("color.no_curfew", text="No Curfew")
        scol.operator("color.motor_gray", text="Motor Gray")
        scol.operator("color.after_hours", text="After Hours")

# Soft and Earthy Brown
class MCMCBROWNS(bpy.types.Panel):
    bl_idname = "BROWNS_PT_Panel"
    bl_label = "Soft and Earthy Brown"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mcmc_brown_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_brown_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_brown_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mcmc_brown_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.fawn_doe", text="Fawn Doe")
        scol.operator("color.sentimental_reasons", text="Sentimental Reasons")
        scol.operator("color.cobblestone_streets", text="Cobblestone Streets")
        scol.operator("color.cocoa_shell", text="Cocoa Shell")
