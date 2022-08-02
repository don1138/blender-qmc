import bpy

from .panel_classes import *

# FORD COLORS 1958 PANEL
class F1958Panel(bpy.types.Panel):
    bl_idname = "F1958_PT_Panel"
    bl_label = "Ford 1958"
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
        scol.label(text="", icon_value=g.c_icons["f58a_raven_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58c_desert_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58d_palamino_tan"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58e_colonial_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58f_silvertone_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58g_sun_gold"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58h_gunmetal_gray"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58j_bali_bronze"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58l_azure_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58m_gulfstream_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58n_seaspray_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58r_torch_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["f58t_silvetone_blue"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.f58a_raven_black", text="A Raven Black")
        scol.operator("color.f58c_desert_beige", text="C Desert Beige")
        scol.operator("color.f58d_palamino_tan", text="D Palamino Tan")
        scol.operator("color.f58e_colonial_white", text="E Colonial White")
        scol.operator("color.f58f_silvertone_green", text="F Silvertone Green")
        scol.operator("color.f58g_sun_gold", text="G Sun Gold")
        scol.operator("color.f58h_gunmetal_gray", text="H Gunmetal Gray")
        scol.operator("color.f58j_bali_bronze", text="J Bali Bronze")
        scol.operator("color.f58l_azure_blue", text="L Azure Blue")
        scol.operator("color.f58m_gulfstream_blue", text="M Gulfstream Blue")
        scol.operator("color.f58n_seaspray_green", text="N Seaspray Green")
        scol.operator("color.f58r_torch_red", text="R Torch Red")
        scol.operator("color.f58t_silvetone_blue", text="T Silvetone Blue")


