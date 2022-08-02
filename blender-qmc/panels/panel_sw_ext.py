import bpy

from .panel_classes import *

# SHERWIN WILLIAMS - EXTERIOR PANEL
class SMEPanel(bpy.types.Panel):
    bl_idname = "SME_PT_Panel"
    bl_label = "Suburban Modern Exterior"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


class SME_APanel(bpy.types.Panel):
    bl_idname = "SME_A_PT_Panel"
    bl_label = "Set A"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_birdseye_maple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_cocoon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_olde_world_gold"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_birdseye_maple", text="Birdseye Maple")
        scol.operator("color.sm_cocoon", text="Cocoon")
        scol.operator("color.sm_olde_world_gold", text="Olde World Gold")

class SME_BPanel(bpy.types.Panel):
    bl_idname = "SME_B_PT_Panel"
    bl_label = "Set B"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_wool_skein"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_artisan_tan"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_status_bronze"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_wool_skein", text="Wool Skein")
        scol.operator("color.sm_artisan_tan", text="Artisan Tan")
        scol.operator("color.sm_status_bronze", text="Status Bronze")

class SME_CPanel(bpy.types.Panel):
    bl_idname = "SME_C_PT_Panel"
    bl_label = "Set C"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_tatami_tan"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_colony_buff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_homburg_gray"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_tatami_tan", text="Tatami Tan")
        scol.operator("color.sm_colony_buff", text="Colony Buff")
        scol.operator("color.sm_homburg_gray", text="Homburg Gray")

class SME_DPanel(bpy.types.Panel):
    bl_idname = "SME_D_PT_Panel"
    bl_label = "Set D"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_muslin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_straw_harvest"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_rural_green"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_muslin", text="Muslin")
        scol.operator("color.sm_straw_harvest", text="Straw Harvest")
        scol.operator("color.sm_rural_green", text="Rural Green")

class SME_EPanel(bpy.types.Panel):
    bl_idname = "SME_E_PT_Panel"
    bl_label = "Set E"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_extra_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_rushing_river"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_spiced_cider"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_extra_white", text="Extra White")
        scol.operator("color.sm_rushing_river", text="Rushing River")
        scol.operator("color.sm_spiced_cider", text="Spiced Cider")

class SME_FPanel(bpy.types.Panel):
    bl_idname = "SME_F_PT_Panel"
    bl_label = "Set F"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_retreat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_netsuke"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_edgy_gold"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_retreat", text="Retreat")
        scol.operator("color.sm_netsuke", text="Netsuke")
        scol.operator("color.sm_edgy_gold", text="Edgy Gold")

class SME_GPanel(bpy.types.Panel):
    bl_idname = "SME_G_PT_Panel"
    bl_label = "Set G"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_jogging_path"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_intellectual_gray"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_thunder_gray"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_jogging_path", text="Jogging Path")
        scol.operator("color.sm_intellectual_gray", text="Intellectual Gray")
        scol.operator("color.sm_thunder_gray", text="Thunder Gray")

class SME_HPanel(bpy.types.Panel):
    bl_idname = "SME_H_PT_Panel"
    bl_label = "Set H"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_anjou_pear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_jersey_cream"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_warm_stone"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_anjou_pear", text="Anjou Pear")
        scol.operator("color.sm_jersey_cream", text="Jersey Cream")
        scol.operator("color.sm_warm_stone", text="Warm Stone")

class SME_JPanel(bpy.types.Panel):
    bl_idname = "SME_J_PT_Panel"
    bl_label = "Set J"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'SME_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["_null"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_cork_wedge"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_smokehouse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["sm_rustic_red"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Body / Trim / Accent")
        scol.operator("color.sm_cork_wedge", text="Cork Wedge")
        scol.operator("color.sm_smokehouse", text="Smokehouse")
        scol.operator("color.sm_rustic_red", text="Rustic Red")
