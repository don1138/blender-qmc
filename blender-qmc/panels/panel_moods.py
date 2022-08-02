import bpy

from .panel_classes import *

# MOODS PANEL
class MOODSPanel(bpy.types.Panel):
    bl_idname = "MOODS_PT_Panel"
    bl_label = "Moods"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

class MOODRELAXPanel(bpy.types.Panel):
    bl_idname = "MOODSRELAX_PT_Panel"
    bl_label = "Relaxed"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["moods_blue_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_blue_08"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_green_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_pink_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_blue_02", text="Blue 02")
        scol.operator("color.moods_blue_08", text="Blue 08")
        scol.operator("color.moods_green_02", text="Green 02")
        scol.operator("color.moods_pink_04", text="Pink 04")

class MOODENERGYPanel(bpy.types.Panel):
    bl_idname = "MOODENERGY_PT_Panel"
    bl_label = "Energy"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["moods_green_07"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_green_08"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_green_13"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_yellow_06"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_green_07", text="Green 07")
        scol.operator("color.moods_green_08", text="Green 08")
        scol.operator("color.moods_green_13", text="Green 13")
        scol.operator("color.moods_yellow_06", text="Yellow 06")

class MOODCOZYPanel(bpy.types.Panel):
    bl_idname = "MOODCOZY_PT_Panel"
    bl_label = "Cozy"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["moods_beige_02"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_beige_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_pink_07"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_pink_08"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_beige_02", text="Beige 02")
        scol.operator("color.moods_beige_03", text="Beige 03")
        scol.operator("color.moods_pink_07", text="Pink 07")
        scol.operator("color.moods_pink_08", text="Pink 08")

class MOODFOCUSPanel(bpy.types.Panel):
    bl_idname = "MOODFOCUS_PT_Panel"
    bl_label = "Focus"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["moods_blue_06"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_blue_07"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_blue_17"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_blue1_11"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_blue_06", text="Blue 06")
        scol.operator("color.moods_blue_07", text="Blue 07")
        scol.operator("color.moods_blue_17", text="Blue 17")
        scol.operator("color.moods_blue1_11", text="Blue 111")

class MOODMOODYPanel(bpy.types.Panel):
    bl_idname = "MOODMOODY_PT_Panel"
    bl_label = "Moody"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["moods_black_01"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_purple_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_red_03"].icon_id)
        scol.label(text="", icon_value=g.c_icons["moods_teal_03"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_black_01", text="Black 01")
        scol.operator("color.moods_purple_03", text="Purple 03")
        scol.operator("color.moods_red_03", text="Red 03")
        scol.operator("color.moods_teal_03", text="Teal 03")

# class MOODWHITESPanel(bpy.types.Panel):
#     bl_idname = "MOODWHITES_PT_Panel"
#     bl_label = "Whites"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "MAT"
#     bl_parent_id = 'MOODS_PT_Panel'
#     bl_options = {'DEFAULT_CLOSED'}

#     def draw(self, context):
#         g.c_icons
#         layout = self.layout

#         srow = layout.row()
#         scol = srow.column(align=True)
#         scol.scale_y = 1.25
#         scol.label(text="", icon_value=g.c_icons["moods_white_01"].icon_id)
#         scol.label(text="", icon_value=g.c_icons["moods_white_02"].icon_id)
#         scol.label(text="", icon_value=g.c_icons["moods_white_03"].icon_id)
#         scol.label(text="", icon_value=g.c_icons["moods_white_04"].icon_id)

#         scol = srow.column(align=True)
#         scol.scale_y = 1.25
#         scol.scale_x = 3.0
#         scol.operator("color.moods_white_01", text="White 01")
#         scol.operator("color.moods_white_02", text="White 02")
#         scol.operator("color.moods_white_03", text="White 03")
#         scol.operator("color.moods_white_04", text="White 04")
