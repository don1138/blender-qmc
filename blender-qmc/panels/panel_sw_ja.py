import bpy

from .panel_classes import *

# SHERWIN WILLIAMS - THE JAZZ AGE PANEL
class JAPanel(bpy.types.Panel):
    bl_idname = "JA_PT_Panel"
    bl_label = "The Jazz Age"
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
        scol.label(text="", icon_value=g.c_icons["ja_salon_rose"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_chinese_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_studio_mauve"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_jazz_age_coral"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_frostwork"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_alexandrite"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_blue_peacock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ja_blue_sky"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.ja_salon_rose", text="Salon Rose")
        scol.operator("color.ja_chinese_red", text="Chinese Red")
        scol.operator("color.ja_studio_mauve", text="Studio Mauve")
        scol.operator("color.ja_jazz_age_coral", text="Jazz Age Coral")
        scol.operator("color.ja_frostwork", text="Frostwork")
        scol.operator("color.ja_alexandrite", text="Alexandrite")
        scol.operator("color.ja_blue_peacock", text="Blue Peacock")
        scol.operator("color.ja_blue_sky", text="Blue Sky")
