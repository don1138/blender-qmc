# DON1138 SELECT COLORS SET

import bpy

from .globals import *
from .color_functions import *

# DON1138 SELECT OPERATORS

class DON_GREEN(bpy.types.Operator):
    """Don Green"""
    bl_label = "Don Green"
    bl_idname = 'color.don_green'
    def execute(self, context):
        set_base_color(0xa6ce39, self.bl_label)
        return {'FINISHED'}

class PMS_381U(bpy.types.Operator):
    """PMS 381 U"""
    bl_label = "PMS 381 U"
    bl_idname = 'color.pms_381_u'
    def execute(self, context):
        set_base_color(0xb6d741, self.bl_label)
        return {'FINISHED'}

class DON_RED(bpy.types.Operator):
    """Don Red"""
    bl_label = "Don Red"
    bl_idname = 'color.don_red'
    def execute(self, context):
        set_base_color(0xff3600, self.bl_label)
        return {'FINISHED'}

class PMS_172_C(bpy.types.Operator):
    """PMS 172 C"""
    bl_label = "PMS 172 C"
    bl_idname = 'color.pms_172_c'
    def execute(self, context):
        set_base_color(0xfe4819, self.bl_label)
        return {'FINISHED'}

class DON_BLUE(bpy.types.Operator):
    """Don Blue"""
    bl_label = "Don Blue"
    bl_idname = 'color.don_blue'
    def execute(self, context):
        set_base_color(0x62579d, self.bl_label)
        return {'FINISHED'}

class PMS_2685U(bpy.types.Operator):
    """PMS 2685 U"""
    bl_label = "PMS 2685 U"
    bl_idname = 'color.pms_2685_u'
    def execute(self, context):
        set_base_color(0x6a549b, self.bl_label)
        return {'FINISHED'}

class DON_YELLOW(bpy.types.Operator):
    """Don Yellow"""
    bl_label = "Don Yellow"
    bl_idname = 'color.don_yellow'
    def execute(self, context):
        set_base_color(0xe1ec12, self.bl_label)
        return {'FINISHED'}

class PMS_396U(bpy.types.Operator):
    """PMS 396 U"""
    bl_label = "PMS 396 U"
    bl_idname = 'color.pms_396_u'
    def execute(self, context):
        set_base_color(0xd7e200, self.bl_label)
        return {'FINISHED'}

class DON_BRONZE_PALE(bpy.types.Operator):
    """Don Bronze Pale"""
    bl_label = "Don Bronze Pale"
    bl_idname = 'color.don_bronze_pale'
    def execute(self, context):
        set_base_color(0xc1977e, self.bl_label)
        return {'FINISHED'}

class PMS_729U(bpy.types.Operator):
    """PMS 729 U"""
    bl_label = "PMS 729 U"
    bl_idname = 'color.pms_729_u'
    def execute(self, context):
        set_base_color(0xbf9376, self.bl_label)
        return {'FINISHED'}

class DON_BRONZE_RICH(bpy.types.Operator):
    """Don Bronze Rich"""
    bl_label = "Don Bronze Rich"
    bl_idname = 'color.don_bronze_rich'
    def execute(self, context):
        set_base_color(0x806969, self.bl_label)
        return {'FINISHED'}

class PMS_7518U(bpy.types.Operator):
    """PMS 7518 U"""
    bl_label = "PMS 7518 U"
    bl_idname = 'color.pms_7518_u'
    def execute(self, context):
        set_base_color(0x7d6d6a, self.bl_label)
        return {'FINISHED'}

class DON_WHITE(bpy.types.Operator):
    """Don White"""
    bl_label = "Don White"
    bl_idname = 'color.don_white'
    def execute(self, context):
        set_base_color(0xfffde4, self.bl_label)
        return {'FINISHED'}

class PMS_7499U(bpy.types.Operator):
    """PMS 7499 U"""
    bl_label = "PMS 7499 U"
    bl_idname = 'color.pms_7499_u'
    def execute(self, context):
        set_base_color(0xf6edca, self.bl_label)
        return {'FINISHED'}

class DEEPLY_UNCOMFORTABLE(bpy.types.Operator):
    """Deeply Uncomfortable"""
    bl_label = "Deeply Uncomfortable"
    bl_idname = 'color.deeply_uncomfotable'
    def execute(self, context):
        set_base_color(0x412a42, self.bl_label)
        return {'FINISHED'}

class BAKER_MILLER_PINK(bpy.types.Operator):
    """Baker-Miller Pink"""
    bl_label = "Baker-Miller Pink"
    bl_idname = 'color.baker_miller_pink'
    def execute(self, context):
        set_base_color(0xFF91AF, self.bl_label)
        return {'FINISHED'}

class FINALLY_HEALING(bpy.types.Operator):
    """Finally Healing"""
    bl_label = "Finally Healing"
    bl_idname = 'color.finally_healing'
    def execute(self, context):
        set_base_color(0xebe094, self.bl_label)
        return {'FINISHED'}

class COSMIC_LATTE(bpy.types.Operator):
    """Cosmic Latte"""
    bl_label = "Cosmic Latte"
    bl_idname = 'color.cosmic_latte'
    def execute(self, context):
        set_base_color(0xfff8e7, self.bl_label)
        return {'FINISHED'}

class REAL_BLACK(bpy.types.Operator):
    """Real Black (Eigengrau)"""
    bl_label = "Real Black"
    bl_idname = 'color.real_black'
    def execute(self, context):
        set_base_color(0x292724, self.bl_label)
        return {'FINISHED'}

class REAL_WHITE(bpy.types.Operator):
    """Real White"""
    bl_label = "Real White"
    bl_idname = 'color.real_white'
    def execute(self, context):
        set_base_color(0xD6D8DB, self.bl_label)
        return {'FINISHED'}

class SAFETY_BLACK(bpy.types.Operator):
    """Non-Zero Black (0.01, 0.01, 0.01) for use in CGI"""
    bl_label = "Safety Black"
    bl_idname = 'color.safety_black'
    def execute(self, context):
        set_base_color(0x191919, self.bl_label)
        return {'FINISHED'}

class TRUE_BLACK(bpy.types.Operator):
    """True Black (Eigengrau)"""
    bl_label = "True Black (Eigengrau)"
    bl_idname = 'color.true_black'
    def execute(self, context):
        set_base_color(0x16161d, self.bl_label)
        return {'FINISHED'}

class TRUE_WHITE(bpy.types.Operator):
    """True White"""
    bl_label = "True White"
    bl_idname = 'color.true_white'
    def execute(self, context):
        set_base_color(0xE9E9E2, self.bl_label)
        return {'FINISHED'}


# DON1138 SELECT PANEL

class Don1138Panel(bpy.types.Panel):
    bl_idname = "DON1138_PT_Panel"
    bl_label = "Don1138 Select"
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
        scol.label(text="", icon_value=g.c_icons["don_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_381_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_172_c"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_2685_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_396_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_bronze_pale"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_729_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_bronze_rich"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_7518_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["don_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_7499_u"].icon_id)
        scol.label(text="", icon_value=g.c_icons["deeply_uncomfotable"].icon_id)
        scol.label(text="", icon_value=g.c_icons["baker_miller_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["finally_healing"].icon_id)
        scol.label(text="", icon_value=g.c_icons["cosmic_latte"].icon_id)
        scol.label(text="", icon_value=g.c_icons["real_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["real_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["true_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["true_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["safety_black"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.don_green", text="Don Green")
        scol.operator("color.pms_381_u", text="PMS 381 U")
        scol.operator("color.don_red", text="Don Red")
        scol.operator("color.pms_172_c", text="PMS 172 C")
        scol.operator("color.don_blue", text="Don Blue")
        scol.operator("color.pms_2685_u", text="PMS 2685 U")
        scol.operator("color.don_yellow", text="Don Yellow")
        scol.operator("color.pms_396_u", text="PMS 396 U")
        scol.operator("color.don_bronze_pale", text="Don Bronze Pale")
        scol.operator("color.pms_729_u", text="PMS 729 U")
        scol.operator("color.don_bronze_rich", text="Don Bronze Rich")
        scol.operator("color.pms_7518_u", text="PMS 7518 U")
        scol.operator("color.don_white", text="Don White")
        scol.operator("color.pms_7499_u", text="PMS 7499 U")
        scol.operator("color.deeply_uncomfotable", text="Deeply Uncomfortable")
        scol.operator("color.baker_miller_pink", text="Baker-Miller Pink")
        scol.operator("color.finally_healing", text="Finally Healing")
        scol.operator("color.cosmic_latte", text="Cosmic Latte")
        scol.operator("color.real_black", text="Real Black")
        scol.operator("color.real_white", text="Real White")
        scol.operator("color.true_black", text="True Black (Eigengrau)")
        scol.operator("color.true_white", text="True White")
        scol.operator("color.safety_black", text="Safety Black")


# DON1138 SELECT CLASSES
array_ds = [
    Don1138Panel,
    DON_GREEN,
    PMS_381U,
    DON_RED,
    PMS_172_C,
    DON_BLUE,
    PMS_2685U,
    DON_YELLOW,
    PMS_396U,
    DON_BRONZE_PALE,
    PMS_729U,
    DON_BRONZE_RICH,
    PMS_7518U,
    DON_WHITE,
    PMS_7499U,
    DEEPLY_UNCOMFORTABLE,
    BAKER_MILLER_PINK,
    FINALLY_HEALING,
    COSMIC_LATTE,
    REAL_BLACK,
    REAL_WHITE,
    SAFETY_BLACK,
    TRUE_BLACK,
    TRUE_WHITE,
]
