import bpy

from .globals import *
from .color_functions import *


# MOOD COLORS

class MoodsGreen02(bpy.types.Operator):
    """Soft sage green with a hint of blue"""
    bl_label = "Green 02"
    bl_idname = 'color.moods_green_02'
    def execute(self, context):
        set_base_color(0x8A9082, self.bl_label)
        return {'FINISHED'}

class MoodsBlue02(bpy.types.Operator):
    """Fresh clean minty blue"""
    bl_label = "Blue 02"
    bl_idname = 'color.moods_blue_02'
    def execute(self, context):
        set_base_color(0xd3dbd9, self.bl_label)
        return {'FINISHED'}

class MoodsBlue08(bpy.types.Operator):
    """Vibrant mid-tone sky blue"""
    bl_label = "Blue 08"
    bl_idname = 'color.moods_blue_08'
    def execute(self, context):
        set_base_color(0xabccd3, self.bl_label)
        return {'FINISHED'}

class MoodsPink04(bpy.types.Operator):
    """Muted pink with a touch of grey"""
    bl_label = "Pink 04"
    bl_idname = 'color.moods_pink_04'
    def execute(self, context):
        set_base_color(0xF3E0E4, self.bl_label)
        return {'FINISHED'}

class MoodsGreen07(bpy.types.Operator):
    """Foliage green with hint of blue & yellow"""
    bl_label = "Green 07"
    bl_idname = 'color.moods_green_07'
    def execute(self, context):
        set_base_color(0x698a66, self.bl_label)
        return {'FINISHED'}

class MoodsGreen08(bpy.types.Operator):
    """Fresh neo green"""
    bl_label = "Green 08"
    bl_idname = 'color.moods_green_08'
    def execute(self, context):
        set_base_color(0xa2c3af, self.bl_label)
        return {'FINISHED'}

class MoodsGreen13(bpy.types.Operator):
    """Sage green with added optimism"""
    bl_label = "Green 13"
    bl_idname = 'color.moods_green_13'
    def execute(self, context):
        set_base_color(0xb9ccae, self.bl_label)
        return {'FINISHED'}

class MoodsYellow06(bpy.types.Operator):
    """Daffodil yellow with a lemon tang"""
    bl_label = "Yellow 06"
    bl_idname = 'color.moods_yellow_06'
    def execute(self, context):
        set_base_color(0xffe887, self.bl_label)
        return {'FINISHED'}

class MoodsPink07(bpy.types.Operator):
    """A romantic, muted pink"""
    bl_label = "Pink 07"
    bl_idname = 'color.moods_pink_07'
    def execute(self, context):
        set_base_color(0xd2c5bc, self.bl_label)
        return {'FINISHED'}

class MoodsPink08(bpy.types.Operator):
    """Dusty pink on a distinctly earthy base"""
    bl_label = "Pink 08"
    bl_idname = 'color.moods_pink_08'
    def execute(self, context):
        set_base_color(0xc2a79c, self.bl_label)
        return {'FINISHED'}

class MoodsBeige02(bpy.types.Operator):
    """Light buff brown with touch of grey"""
    bl_label = "Beige 02"
    bl_idname = 'color.moods_beige_02'
    def execute(self, context):
        set_base_color(0xb6a18b, self.bl_label)
        return {'FINISHED'}

class MoodsBeige03(bpy.types.Operator):
    """Soft, earthy beige with notes of grey and yellow"""
    bl_label = "Beige 03"
    bl_idname = 'color.moods_beige_03'
    def execute(self, context):
        set_base_color(0xdfdbcf, self.bl_label)
        return {'FINISHED'}

class MoodsBlue06(bpy.types.Operator):
    """Deep slate blue"""
    bl_label = "Blue 06"
    bl_idname = 'color.moods_blue_06'
    def execute(self, context):
        set_base_color(0x4c5f6b, self.bl_label)
        return {'FINISHED'}

class MoodsBlue07(bpy.types.Operator):
    """Dark inky blue with touch of green"""
    bl_label = "Blue 07"
    bl_idname = 'color.moods_blue_07'
    def execute(self, context):
        set_base_color(0x3d4f56, self.bl_label)
        return {'FINISHED'}

class MoodsBlue17(bpy.types.Operator):
    """A grounded, muted blue"""
    bl_label = "Blue 17"
    bl_idname = 'color.moods_blue_17'
    def execute(self, context):
        set_base_color(0x8398a5, self.bl_label)
        return {'FINISHED'}

class MoodsBlue111(bpy.types.Operator):
    """Cobalt keyworker blue"""
    bl_label = "Blue1 11"
    bl_idname = 'color.moods_blue1_11'
    def execute(self, context):
        set_base_color(0x1a4677, self.bl_label)
        return {'FINISHED'}

class MoodsPurple03(bpy.types.Operator):
    """Deep, velvety purple with blue undertones"""
    bl_label = "Purple 03"
    bl_idname = 'color.moods_purple_03'
    def execute(self, context):
        set_base_color(0x432d2e, self.bl_label)
        return {'FINISHED'}

class MoodsTeal03(bpy.types.Operator):
    """Charcoal blue with grey undertones"""
    bl_label = "Teal 03"
    bl_idname = 'color.moods_teal_03'
    def execute(self, context):
        set_base_color(0x596869, self.bl_label)
        return {'FINISHED'}

class MoodsRed03(bpy.types.Operator):
    """Deep terracotta"""
    bl_label = "Red 03"
    bl_idname = 'color.moods_red_03'
    def execute(self, context):
        set_base_color(0xc3867b, self.bl_label)
        return {'FINISHED'}

class MoodsBlack01(bpy.types.Operator):
    """Graphite black with blue undertones"""
    bl_label = "Black 01"
    bl_idname = 'color.moods_black_01'
    def execute(self, context):
        set_base_color(0x444A4C, self.bl_label)
        return {'FINISHED'}

class MoodsWhite04(bpy.types.Operator):
    """Soft linen white with grey undertones"""
    bl_label = "White 04"
    bl_idname = 'color.moods_white_04'
    def execute(self, context):
        set_base_color(0xe4e2d7, self.bl_label)
        return {'FINISHED'}

class MoodsWhite03(bpy.types.Operator):
    """Soft creamy white with touch of yellow"""
    bl_label = "White 03"
    bl_idname = 'color.moods_white_03'
    def execute(self, context):
        set_base_color(0xf3f1e5, self.bl_label)
        return {'FINISHED'}

class MoodsWhite02(bpy.types.Operator):
    """Off-white with a touch of grey"""
    bl_label = "White 02"
    bl_idname = 'color.moods_white_02'
    def execute(self, context):
        set_base_color(0xeceae2, self.bl_label)
        return {'FINISHED'}

class MoodsWhite01(bpy.types.Operator):
    """Pure white with the lightest touch of grey"""
    bl_label = "White 01"
    bl_idname = 'color.moods_white_01'
    def execute(self, context):
        set_base_color(0xf2f2eb, self.bl_label)
        return {'FINISHED'}


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
    bl_label = "    Relaxed"
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
    bl_label = "    Energy"
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
    bl_label = "    Cozy"
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
    bl_label = "    Focus"
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
    bl_label = "    Moody"
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


array_moods = [
    MOODSPanel,
    MOODRELAXPanel,
    MOODENERGYPanel,
    MOODCOZYPanel,
    MOODFOCUSPanel,
    MOODMOODYPanel,
    MoodsGreen02,
    MoodsBlue02,
    MoodsBlue08,
    MoodsPink04,
    MoodsGreen07,
    MoodsGreen08,
    MoodsGreen13,
    MoodsYellow06,
    MoodsPink07,
    MoodsPink08,
    MoodsBeige02,
    MoodsBeige03,
    MoodsBlue06,
    MoodsBlue07,
    MoodsBlue17,
    MoodsBlue111,
    MoodsPurple03,
    MoodsTeal03,
    MoodsRed03,
    MoodsBlack01,
    # MoodsWhite04,
    # MoodsWhite03,
    # MoodsWhite02,
    # MoodsWhite01,
]
