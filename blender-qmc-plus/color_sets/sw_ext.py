import bpy

from .globals import *
from .color_functions import *


# SHERWIN WILLIAMS - EXTERIOR

class SMBirdseyeMaple(bpy.types.Operator):
    """Suburban Modern Birdseye Maple"""
    bl_label = "Birdseye Maple"
    bl_idname = 'color.sm_birdseye_maple'
    def execute(self, context):
        set_base_color(0xe4c495, self.bl_label)
        return {'FINISHED'}

class SMCocoon(bpy.types.Operator):
    """Suburban Modern Cocoon"""
    bl_label = "Cocoon"
    bl_idname = 'color.sm_cocoon'
    def execute(self, context):
        set_base_color(0x726b5b, self.bl_label)
        return {'FINISHED'}

class SMOldeWorldGold(bpy.types.Operator):
    """Suburban Modern Olde World Gold"""
    bl_label = "Olde World Gold"
    bl_idname = 'color.sm_olde_world_gold'
    def execute(self, context):
        set_base_color(0x8f6c3e, self.bl_label)
        return {'FINISHED'}

class SMWoolSkein(bpy.types.Operator):
    """Suburban Modern Wool Skein"""
    bl_label = "Wool Skein"
    bl_idname = 'color.sm_wool_skein'
    def execute(self, context):
        set_base_color(0xd9cfba, self.bl_label)
        return {'FINISHED'}

class SMArtisanTan(bpy.types.Operator):
    """Suburban Modern Artisan Tan"""
    bl_label = "Artisan Tan"
    bl_idname = 'color.sm_artisan_tan'
    def execute(self, context):
        set_base_color(0xb09879, self.bl_label)
        return {'FINISHED'}

class SMStatusBronze(bpy.types.Operator):
    """Suburban Modern Status Bronze"""
    bl_label = "Status Bronze"
    bl_idname = 'color.sm_status_bronze'
    def execute(self, context):
        set_base_color(0x5c4d3c, self.bl_label)
        return {'FINISHED'}

class SMTatamiTan(bpy.types.Operator):
    """Suburban Modern Tatami Tan"""
    bl_label = "Tatami Tan"
    bl_idname = 'color.sm_tatami_tan'
    def execute(self, context):
        set_base_color(0xba8c64, self.bl_label)
        return {'FINISHED'}

class SMColonyBuff(bpy.types.Operator):
    """Suburban Modern Colony Buff"""
    bl_label = "Colony Buff"
    bl_idname = 'color.sm_colony_buff'
    def execute(self, context):
        set_base_color(0xddc6ab, self.bl_label)
        return {'FINISHED'}

class SMHomburgGray(bpy.types.Operator):
    """Suburban Modern Homburg Gray"""
    bl_label = "Homburg Gray"
    bl_idname = 'color.sm_homburg_gray'
    def execute(self, context):
        set_base_color(0x666d69, self.bl_label)
        return {'FINISHED'}

class SMMuslin(bpy.types.Operator):
    """Suburban Modern Muslin"""
    bl_label = "Muslin"
    bl_idname = 'color.sm_muslin'
    def execute(self, context):
        set_base_color(0xeadfc9, self.bl_label)
        return {'FINISHED'}

class SMStrawHarvest(bpy.types.Operator):
    """Suburban Modern Straw Harvest"""
    bl_label = "Straw Harvest"
    bl_idname = 'color.sm_straw_harvest'
    def execute(self, context):
        set_base_color(0xdbc8a2, self.bl_label)
        return {'FINISHED'}

class SMRuralGreen(bpy.types.Operator):
    """Suburban Modern Rural Green"""
    bl_label = "Rural Green"
    bl_idname = 'color.sm_rural_green'
    def execute(self, context):
        set_base_color(0x8d844d, self.bl_label)
        return {'FINISHED'}

class SMExtraWhite(bpy.types.Operator):
    """Suburban Modern Extra White"""
    bl_label = "Extra White"
    bl_idname = 'color.sm_extra_white'
    def execute(self, context):
        set_base_color(0xeeefea, self.bl_label)
        return {'FINISHED'}

class SMRushingRiver(bpy.types.Operator):
    """Suburban Modern Rushing River"""
    bl_label = "Rushing River"
    bl_idname = 'color.sm_rushing_river'
    def execute(self, context):
        set_base_color(0xa19c8f, self.bl_label)
        return {'FINISHED'}

class SMSpicedCider(bpy.types.Operator):
    """Suburban Modern Spiced Cider"""
    bl_label = "Spiced Cider"
    bl_idname = 'color.sm_spiced_cider'
    def execute(self, context):
        set_base_color(0xb0785c, self.bl_label)
        return {'FINISHED'}

class SMRetreat(bpy.types.Operator):
    """Suburban Modern Retreat"""
    bl_label = "Retreat"
    bl_idname = 'color.sm_retreat'
    def execute(self, context):
        set_base_color(0x7a8076, self.bl_label)
        return {'FINISHED'}

class SMNetsuke(bpy.types.Operator):
    """Suburban Modern Netsuke"""
    bl_label = "Netsuke"
    bl_idname = 'color.sm_netsuke'
    def execute(self, context):
        set_base_color(0xe0cfb0, self.bl_label)
        return {'FINISHED'}

class SMEdgyGold(bpy.types.Operator):
    """Suburban Modern Edgy Gold"""
    bl_label = "Edgy Gold"
    bl_idname = 'color.sm_edgy_gold'
    def execute(self, context):
        set_base_color(0xb1975f, self.bl_label)
        return {'FINISHED'}

class SMJoggingPath(bpy.types.Operator):
    """Suburban Modern Jogging Path"""
    bl_label = "Jogging Path"
    bl_idname = 'color.sm_jogging_path'
    def execute(self, context):
        set_base_color(0xc0b9a9, self.bl_label)
        return {'FINISHED'}

class SMIntellectualGray(bpy.types.Operator):
    """Suburban Modern Intellectual Gray"""
    bl_label = "Intellectual Gray"
    bl_idname = 'color.sm_intellectual_gray'
    def execute(self, context):
        set_base_color(0xa8a093, self.bl_label)
        return {'FINISHED'}

class SMThunderGray(bpy.types.Operator):
    """Suburban Modern Thunder Gray"""
    bl_label = "Thunder Gray"
    bl_idname = 'color.sm_thunder_gray'
    def execute(self, context):
        set_base_color(0x57534c, self.bl_label)
        return {'FINISHED'}

class SMAnjouPear(bpy.types.Operator):
    """Suburban Modern Anjou Pear"""
    bl_label = "Anjou Pear"
    bl_idname = 'color.sm_anjou_pear'
    def execute(self, context):
        set_base_color(0xddac6d, self.bl_label)
        return {'FINISHED'}

class SMJerseyCream(bpy.types.Operator):
    """Suburban Modern Jersey Cream"""
    bl_label = "Jersey Cream"
    bl_idname = 'color.sm_jersey_cream'
    def execute(self, context):
        set_base_color(0xf5debb, self.bl_label)
        return {'FINISHED'}

class SMWarmStone(bpy.types.Operator):
    """Suburban Modern Warm Stone"""
    bl_label = "Warm Stone"
    bl_idname = 'color.sm_warm_stone'
    def execute(self, context):
        set_base_color(0x887b6c, self.bl_label)
        return {'FINISHED'}

class SMCorkWedge(bpy.types.Operator):
    """Suburban Modern Cork Wedge"""
    bl_label = "Cork Wedge"
    bl_idname = 'color.sm_cork_wedge'
    def execute(self, context):
        set_base_color(0xc1a98a, self.bl_label)
        return {'FINISHED'}

class SMSmokehouse(bpy.types.Operator):
    """Suburban Modern Smokehouse"""
    bl_label = "Smokehouse"
    bl_idname = 'color.sm_smokehouse'
    def execute(self, context):
        set_base_color(0x716354, self.bl_label)
        return {'FINISHED'}

class SMRusticRed(bpy.types.Operator):
    """Suburban Modern Rustic Red"""
    bl_label = "Rustic Red"
    bl_idname = 'color.sm_rustic_red'
    def execute(self, context):
        set_base_color(0x703229, self.bl_label)
        return {'FINISHED'}


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


array_sw_ext = [
    SMEPanel,
    SME_APanel,
    SME_BPanel,
    SME_CPanel,
    SME_DPanel,
    SME_EPanel,
    SME_FPanel,
    SME_GPanel,
    SME_HPanel,
    SME_JPanel,
    SMBirdseyeMaple,
    SMCocoon,
    SMOldeWorldGold,
    SMWoolSkein,
    SMArtisanTan,
    SMStatusBronze,
    SMTatamiTan,
    SMColonyBuff,
    SMHomburgGray,
    SMMuslin,
    SMStrawHarvest,
    SMRuralGreen,
    SMExtraWhite,
    SMRushingRiver,
    SMSpicedCider,
    SMRetreat,
    SMNetsuke,
    SMEdgyGold,
    SMJoggingPath,
    SMIntellectualGray,
    SMThunderGray,
    SMAnjouPear,
    SMJerseyCream,
    SMWarmStone,
    SMCorkWedge,
    SMSmokehouse,
    SMRusticRed,
]
