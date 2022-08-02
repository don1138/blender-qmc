import bpy

from .panel_classes import *

# Schnitzius Selects PANEL
class PMSPanelSchnitzius(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_Schitzius"
    bl_label = "Schnitzius Select"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.grid_flow(row_major=True,even_columns=True,columns=2,align=True)
        col.scale_y = 1.25
        col.label(text="My Color")
        col.label(text="PMS Match")
        col.operator("color.schnitzius_green", text="Green")
        col.operator("color.pms_381_u", text="381 U")
        col.operator("color.schnitzius_red", text="Red")
        col.operator("color.pms_172_c", text="172 C")
        col.operator("color.schnitzius_blue", text="Blue")
        col.operator("color.pms_2685_u", text="2685 U")
        col.operator("color.schnitzius_yellow", text="Yellow")
        col.operator("color.pms_396_u", text="396 U")
        col.operator("color.schnitzius_bronze_pale", text="Bronze Pale")
        col.operator("color.pms_729_u", text="729 U")
        col.operator("color.schnitzius_bronze_rich", text="Bronze Rich")
        col.operator("color.pms_7518_u", text="7518 U")
        col.operator("color.schnitzius_white", text="White")
        col.operator("color.pms_7499_u", text="7499 U")
