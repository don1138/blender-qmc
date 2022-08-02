import bpy

from .panel_classes import *

# GENERAL ELECTRIC 1960S APPLIANCES PANEL
class GEPanel(bpy.types.Panel):
    bl_idname = "GE_PT_Panel"
    bl_label = "General Electric"
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
        scol.label(text="", icon_value=g.c_icons["ge_avacado"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_avacado_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_avacado_dark"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_coppertone_a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_dark_coppertone_a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_coppertone_b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_dark_coppertone_b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_harvest_gold"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_harvest_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ge_harvest_dark"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.ge_avacado", text="Avacado")
        scol.operator("color.ge_avacado_light", text="Avacado Light")
        scol.operator("color.ge_avacado_dark", text="Avacado Dark")
        scol.operator("color.ge_coppertone_a", text="Coppertone A")
        scol.operator("color.ge_dark_coppertone_a", text="Dark Coppertone A")
        scol.operator("color.ge_coppertone_b", text="Coppertone B")
        scol.operator("color.ge_dark_coppertone_b", text="Dark Coppertone B")
        scol.operator("color.ge_harvest_gold", text="Harvest Gold")
        scol.operator("color.ge_harvest_light", text="Harvest Light")
        scol.operator("color.ge_harvest_dark", text="Harvest Dark")
