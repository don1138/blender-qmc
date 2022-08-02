import bpy

from .panel_classes import *

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
