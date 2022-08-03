import bpy

from .globals import *
from .color_functions import *


# SHERWIN WILLIAMS - THE JAZZ AGE

class JAChineseRed(bpy.types.Operator):
    """Jazz Age Chinese Red"""
    bl_label = "Chinese Red"
    bl_idname = 'color.ja_chinese_red'
    def execute(self, context):
        set_base_color(0x9e3e33, self.bl_label)
        return {'FINISHED'}

class JAJazzAgeCoral(bpy.types.Operator):
    """Jazz Age Jazz Age Coral"""
    bl_label = "Jazz Age Coral"
    bl_idname = 'color.ja_jazz_age_coral'
    def execute(self, context):
        set_base_color(0xf1bfb1, self.bl_label)
        return {'FINISHED'}

class JAFrostwork(bpy.types.Operator):
    """Jazz Age Frostwork"""
    bl_label = "Frostwork"
    bl_idname = 'color.ja_frostwork'
    def execute(self, context):
        set_base_color(0xcbd0c2, self.bl_label)
        return {'FINISHED'}

class JAAlexandrite(bpy.types.Operator):
    """Jazz Age Alexandrite"""
    bl_label = "Alexandrite"
    bl_idname = 'color.ja_alexandrite'
    def execute(self, context):
        set_base_color(0x598c74, self.bl_label)
        return {'FINISHED'}

class JASalonRose(bpy.types.Operator):
    """Jazz Age Salon Rose"""
    bl_label = "Salon Rose"
    bl_idname = 'color.ja_salon_rose'
    def execute(self, context):
        set_base_color(0xab7878, self.bl_label)
        return {'FINISHED'}

class JAStudioMauve(bpy.types.Operator):
    """Jazz Age Studio Mauve"""
    bl_label = "Studio Mauve"
    bl_idname = 'color.ja_studio_mauve'
    def execute(self, context):
        set_base_color(0xc6b9b8, self.bl_label)
        return {'FINISHED'}

class JABlueSky(bpy.types.Operator):
    """Jazz Age Blue Sky"""
    bl_label = "Blue Sky"
    bl_idname = 'color.ja_blue_sky'
    def execute(self, context):
        set_base_color(0xabd1c9, self.bl_label)
        return {'FINISHED'}

class JABluePeacock(bpy.types.Operator):
    """Jazz Age Blue Peacock"""
    bl_label = "Blue Peacock"
    bl_idname = 'color.ja_blue_peacock'
    def execute(self, context):
        set_base_color(0x014e4c, self.bl_label)
        return {'FINISHED'}


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


array_sw_ja = [
    JAPanel,
    JAChineseRed,
    JAJazzAgeCoral,
    JAFrostwork,
    JAAlexandrite,
    JASalonRose,
    JAStudioMauve,
    JABlueSky,
    JABluePeacock,
]
