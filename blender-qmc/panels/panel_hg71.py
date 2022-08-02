import bpy

from .panel_classes import *

# House & Garden 1971 PANEL
class HG71Panel(bpy.types.Panel):
    bl_idname = "HG71_PT_Panel"
    bl_label = "House & Garden 1971"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout


# YELLOWS
class HG71_YELLOW_Panel(bpy.types.Panel):
    bl_idname = "HG71_YELLOW_PT_Panel"
    bl_label = "Yellows"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_pineapple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_sun_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_kumquat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_goldenrod"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_antique_gold"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_maple_sugar"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_pongee"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_pineapple", text="Pineapple")
        scol.operator("color.hg71_sun_yellow", text="Sun Yellow")
        scol.operator("color.hg71_kumquat", text="Kumquat")
        scol.operator("color.hg71_goldenrod", text="Goldenrod")
        scol.operator("color.hg71_antique_gold", text="Antique Gold")
        scol.operator("color.hg71_maple_sugar", text="Maple Sugar")
        scol.operator("color.hg71_pongee", text="Pongee")


# GREEN
class HG71_GREEN_Panel(bpy.types.Panel):
    bl_idname = "HG71_GREEN_PT_Panel"
    bl_label = "Greens"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_moss_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_lacquer_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_green_mint"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_parrot_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_lettuce"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_celery"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_moss_green", text="Moss Green")
        scol.operator("color.hg71_lacquer_green", text="Lacquer Green")
        scol.operator("color.hg71_green_mint", text="Green Mint")
        scol.operator("color.hg71_parrot_green", text="Parrot Green")
        scol.operator("color.hg71_lettuce", text="Lettuce")
        scol.operator("color.hg71_celery", text="Celery")


# BLUES
class HG71_BLUE_Panel(bpy.types.Panel):
    bl_idname = "HG71_BLUE_PT_Panel"
    bl_label = "Blues"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_midnight_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_ultramarine_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_space_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_blue_opaline"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_blue_sky"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_aquamarine_blue"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_midnight_blue", text="Midnight Blue")
        scol.operator("color.hg71_ultramarine_blue", text="Ultramarine Blue")
        scol.operator("color.hg71_space_blue", text="Space Blue")
        scol.operator("color.hg71_blue_opaline", text="Blue Opaline")
        scol.operator("color.hg71_blue_sky", text="Blue Sky")
        scol.operator("color.hg71_aquamarine_blue", text="Aquamarine Blue")


# ORANGES
class HG71_ORANGE_Panel(bpy.types.Panel):
    bl_idname = "HG71_ORANGE_PT_Panel"
    bl_label = "Oranges"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_bittersweet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_tangerine"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_pompeiian_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_zinnia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_creamy_apricot"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_velvet_brown"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_bittersweet", text="Bittersweet")
        scol.operator("color.hg71_tangerine", text="Tangerine")
        scol.operator("color.hg71_pompeiian_red", text="Pompeiian Red")
        scol.operator("color.hg71_zinnia", text="Zinnia")
        scol.operator("color.hg71_creamy_apricot", text="Creamy Apricot")
        scol.operator("color.hg71_velvet_brown", text="Velvet Brown")


# REDS
class HG71_RED_Panel(bpy.types.Panel):
    bl_idname = "HG71_RED_PT_Panel"
    bl_label = "Reds"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_flag_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_pink_coral"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_pink_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_azalea"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_flag_red", text="Flag Red")
        scol.operator("color.hg71_pink_coral", text="Pink Coral")
        scol.operator("color.hg71_pink_pink", text="Pink Pink")
        scol.operator("color.hg71_azalea", text="Azalea")


# PURPLES
class HG71_PURPLE_Panel(bpy.types.Panel):
    bl_idname = "HG71_PURPLE_PT_Panel"
    bl_label = "Purples"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_beach_plum"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_african_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_lavender"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_beach_plum", text="Beach Plum")
        scol.operator("color.hg71_african_violet", text="African Violet")
        scol.operator("color.hg71_lavender", text="Lavender")


# GRAYS
class HG71_GRAY_Panel(bpy.types.Panel):
    bl_idname = "HG71_GRAY_PT_Panel"
    bl_label = "Grays"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["hg71_oyster_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_mercury"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_mushroom"].icon_id)
        scol.label(text="", icon_value=g.c_icons["hg71_black_pearl"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_oyster_white", text="Oyster White")
        scol.operator("color.hg71_mercury", text="Mercury")
        scol.operator("color.hg71_mushroom", text="Mushroom")
        scol.operator("color.hg71_black_pearl", text="Black Pearl")
