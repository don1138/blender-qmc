# BCLR COLORS SET

import bpy

from .globals import *
from .color_functions import *

# BCLR OPERATORS

class BCLR_ChantillyLace(bpy.types.Operator):
    """Chantilly Lace"""
    bl_label = "Chantilly Lace"
    bl_idname = 'color.bclr_chantilly_lace'
    def execute(self, context):
        set_base_color(0xf4f6f1, self.bl_label)
        return {'FINISHED'}

class BCLR_GreekVilla(bpy.types.Operator):
    """Greek Villa"""
    bl_label = "Greek Villa"
    bl_idname = 'color.bclr_greek_villa'
    def execute(self, context):
        set_base_color(0xf0ece2, self.bl_label)
        return {'FINISHED'}

class BCLR_WhiteDove(bpy.types.Operator):
    """White Dove"""
    bl_label = "White Dove"
    bl_idname = 'color.bclr_white_dove'
    def execute(self, context):
        set_base_color(0xefeee5, self.bl_label)
        return {'FINISHED'}

class BCLR_DecoratorsWhite(bpy.types.Operator):
    """Decorator's White"""
    bl_label = "Decorator's White"
    bl_idname = 'color.bclr_decorators_white'
    def execute(self, context):
        set_base_color(0xebedea, self.bl_label)
        return {'FINISHED'}

class BCLR_SuperWhite(bpy.types.Operator):
    """Super White"""
    bl_label = "Super White"
    bl_idname = 'color.bclr_super_white'
    def execute(self, context):
        set_base_color(0xf1f2ee, self.bl_label)
        return {'FINISHED'}

class BCLR_SimplyWhite(bpy.types.Operator):
    """Simply White"""
    bl_label = "Simply White"
    bl_idname = 'color.bclr_simply_white'
    def execute(self, context):
        set_base_color(0xf6f6ed, self.bl_label)
        return {'FINISHED'}

class BCLR_Pointing(bpy.types.Operator):
    """Pointing"""
    bl_label = "Pointing"
    bl_idname = 'color.bclr_pointing'
    def execute(self, context):
        set_base_color(0xf3efe3, self.bl_label)
        return {'FINISHED'}

class BCLR_LightPewter(bpy.types.Operator):
    """Light Pewter"""
    bl_label = "Light Pewter"
    bl_idname = 'color.bclr_light_pewter'
    def execute(self, context):
        set_base_color(0xdbd8ce, self.bl_label)
        return {'FINISHED'}

class BCLR_CloudCover(bpy.types.Operator):
    """Cloud Cover"""
    bl_label = "Cloud Cover"
    bl_idname = 'color.bclr_cloud_cover'
    def execute(self, context):
        set_base_color(0xe9e8e0, self.bl_label)
        return {'FINISHED'}

class BCLR_Saged(bpy.types.Operator):
    """Saged"""
    bl_label = "Saged"
    bl_idname = 'color.bclr_saged'
    def execute(self, context):
        set_base_color(0x949583, self.bl_label)
        return {'FINISHED'}

class BCLR_TempletonGrey(bpy.types.Operator):
    """Templeton Grey"""
    bl_label = "Templeton Grey"
    bl_idname = 'color.bclr_templeton_grey'
    def execute(self, context):
        set_base_color(0x778686, self.bl_label)
        return {'FINISHED'}

class BCLR_DeNimes(bpy.types.Operator):
    """De Nimes"""
    bl_label = "De Nimes"
    bl_idname = 'color.bclr_denimes'
    def execute(self, context):
        set_base_color(0x748284, self.bl_label)
        return {'FINISHED'}

class BCLR_GreenSmoke(bpy.types.Operator):
    """Green Smoke"""
    bl_label = "Green Smoke"
    bl_idname = 'color.bclr_green_smoke'
    def execute(self, context):
        set_base_color(0x6f7b71, self.bl_label)
        return {'FINISHED'}


# BCLR PANEL

class BCLRPanel(bpy.types.Panel):
    bl_idname = "BCLR_PT_Panel"
    bl_label = "Best Colors for Living Rooms"
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
        scol.label(text="", icon_value=g.c_icons["bclr_chantilly_lace"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_greek_villa"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_white_dove"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_decorators_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_super_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_simply_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_pointing"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_light_pewter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_cloud_cover"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_saged"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_templeton_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_denimes"].icon_id)
        scol.label(text="", icon_value=g.c_icons["bclr_green_smoke"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.bclr_chantilly_lace", text="Chantilly Lace")
        scol.operator("color.bclr_greek_villa", text="Greek Villa")
        scol.operator("color.bclr_white_dove", text="White Dove")
        scol.operator("color.bclr_decorators_white", text="Decorator's White")
        scol.operator("color.bclr_super_white", text="Super White")
        scol.operator("color.bclr_simply_white", text="Simply White")
        scol.operator("color.bclr_pointing", text="Pointing")
        scol.operator("color.bclr_light_pewter", text="Light Pewter")
        scol.operator("color.bclr_cloud_cover", text="Cloud Cover")
        scol.operator("color.bclr_saged", text="Saged")
        scol.operator("color.bclr_templeton_grey", text="Templeton Grey")
        scol.operator("color.bclr_denimes", text="De Nimes")
        scol.operator("color.bclr_green_smoke", text="Green Smoke")


# BCLR CLASSES
array_bclr = [
    BCLRPanel,
    BCLR_ChantillyLace,
    BCLR_GreekVilla,
    BCLR_WhiteDove,
    BCLR_DecoratorsWhite,
    BCLR_SuperWhite,
    BCLR_SimplyWhite,
    BCLR_Pointing,
    BCLR_LightPewter,
    BCLR_CloudCover,
    BCLR_Saged,
    BCLR_TempletonGrey,
    BCLR_DeNimes,
    BCLR_GreenSmoke,
]
