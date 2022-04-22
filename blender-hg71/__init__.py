# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name"       : "HG71 (House & Garden 1971)",
    "description": "Sets the Base Color of a Principled BSDF",
    "author"     : "Don Schnitzius",
    "version"    : (0, 5, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > House & Garden 1971",
    # "warning"    : "WIP",
    "wiki_url"   : "https://github.com/don1138/blender-pcoy",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}



import os
import bpy
import bpy.utils.previews



# MESSAGE BOX

no_material = "No Compatable Material Found"
no_bsdf = "No Principled BSDF Shader Found"
def ShowMessageBox(message = "", title = "", icon = 'INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)



# HEX TO RGB CALCS

def srgb_to_linearrgb(c):
    if   c < 0:       return 0
    elif c < 0.04045: return c/12.92
    else:             return ((c+0.055)/1.055)**2.4

def hex_to_rgb(h,alpha=1):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)] + [alpha])



# COLOR SWITCHER

def set_base_color(hex, mat_name):
    material = bpy.context.object.active_material
    if material:
        mat_bool = bpy.context.scene.pms_bool.rename_material_pcoy
        plaster = bpy.data.materials.get('QMM Plaster')
        BSDF = material.node_tree.nodes.get('Principled BSDF')
        RGB = material.node_tree.nodes.get('RGB')
        ColorRamp = material.node_tree.nodes.get('ColorRamp')

        if material == plaster:
            ColorRamp.color_ramp.elements[0].color = hex_to_rgb(hex)
            BSDF.inputs[3].default_value = hex_to_rgb(hex)
            RGB.outputs[0].default_value = hex_to_rgb(hex)
            material.diffuse_color = hex_to_rgb(hex)
        elif BSDF:
            BSDF.inputs[0].default_value = hex_to_rgb(hex)
            material.diffuse_color = hex_to_rgb(hex)
            if mat_bool == True:
                material.name = mat_name
        else:
            ShowMessageBox(no_bsdf, "Unable To Comply")
            return {'FINISHED'}
    else:
        ShowMessageBox(no_material, "Unable To Comply")
        return {'FINISHED'}



# COLOR CLASSES

# House & Garden 1971

class HG71Pineapple(bpy.types.Operator):
    """House & Garden 1971 Pineapple"""
    bl_label = "Pineapple"
    bl_idname = 'color.hg71_pineapple'
    def execute(self, context):
        set_base_color(0xfaf076, self.bl_label)
        return {'FINISHED'}

class HG71SunYellow(bpy.types.Operator):
    """House & Garden 1971 Sun Yellow"""
    bl_label = "Sun Yellow"
    bl_idname = 'color.hg71_sun_yellow'
    def execute(self, context):
        set_base_color(0xfce612, self.bl_label)
        return {'FINISHED'}

class HG71Kumquat(bpy.types.Operator):
    """House & Garden 1971 Kumquat"""
    bl_label = "Kumquat"
    bl_idname = 'color.hg71_kumquat'
    def execute(self, context):
        set_base_color(0xf2ac18, self.bl_label)
        return {'FINISHED'}

class HG71Bittersweet(bpy.types.Operator):
    """House & Garden 1971 Bittersweet"""
    bl_label = "Bittersweet"
    bl_idname = 'color.hg71_bittersweet'
    def execute(self, context):
        set_base_color(0xfd4f1c, self.bl_label)
        return {'FINISHED'}

class HG71Tangerine(bpy.types.Operator):
    """House & Garden 1971 Tangerine"""
    bl_label = "Tangerine"
    bl_idname = 'color.hg71_tangerine'
    def execute(self, context):
        set_base_color(0xec4c53, self.bl_label)
        return {'FINISHED'}

class HG71PompeiianRed(bpy.types.Operator):
    """House & Garden 1971 Pompeiian Red"""
    bl_label = "Pompeiian Red"
    bl_idname = 'color.hg71_pompeiian_red'
    def execute(self, context):
        set_base_color(0xb34848, self.bl_label)
        return {'FINISHED'}

class HG71Zinnia(bpy.types.Operator):
    """House & Garden 1971 Zinnia"""
    bl_label = "Zinnia"
    bl_idname = 'color.hg71_zinnia'
    def execute(self, context):
        set_base_color(0xdb7543, self.bl_label)
        return {'FINISHED'}

class HG71Mushroom(bpy.types.Operator):
    """House & Garden 1971 Mushroom"""
    bl_label = "Mushroom"
    bl_idname = 'color.hg71_mushroom'
    def execute(self, context):
        set_base_color(0x8b8484, self.bl_label)
        return {'FINISHED'}

class HG71VelvetBrown(bpy.types.Operator):
    """House & Garden 1971 Velvet Brown"""
    bl_label = "Velvet Brown"
    bl_idname = 'color.hg71_velvet_brown'
    def execute(self, context):
        set_base_color(0x4a3439, self.bl_label)
        return {'FINISHED'}

class HG71LacquerGreen(bpy.types.Operator):
    """House & Garden 1971 Lacquer Green"""
    bl_label = "Lacquer Green"
    bl_idname = 'color.hg71_lacquer_green'
    def execute(self, context):
        set_base_color(0x26572e, self.bl_label)
        return {'FINISHED'}

class HG71MossGreen(bpy.types.Operator):
    """House & Garden 1971 Moss Green"""
    bl_label = "Moss Green"
    bl_idname = 'color.hg71_moss_green'
    def execute(self, context):
        set_base_color(0x687d37, self.bl_label)
        return {'FINISHED'}

class HG71GreenMint(bpy.types.Operator):
    """House & Garden 1971 Green Mint"""
    bl_label = "Green Mint"
    bl_idname = 'color.hg71_green_mint'
    def execute(self, context):
        set_base_color(0x42ab52, self.bl_label)
        return {'FINISHED'}

class HG71ParrotGreen(bpy.types.Operator):
    """House & Garden 1971 Parrot Green"""
    bl_label = "Parrot Green"
    bl_idname = 'color.hg71_parrot_green'
    def execute(self, context):
        set_base_color(0xa9ca5a, self.bl_label)
        return {'FINISHED'}

class HG71Lettuce(bpy.types.Operator):
    """House & Garden 1971 Lettuce"""
    bl_label = "Lettuce"
    bl_idname = 'color.hg71_lettuce'
    def execute(self, context):
        set_base_color(0xdceb71, self.bl_label)
        return {'FINISHED'}

class HG71Celery(bpy.types.Operator):
    """House & Garden 1971 Celery"""
    bl_label = "Celery"
    bl_idname = 'color.hg71_celery'
    def execute(self, context):
        set_base_color(0xe8e9ce, self.bl_label)
        return {'FINISHED'}

class HG71MapleSugar(bpy.types.Operator):
    """House & Garden 1971 Maple Sugar"""
    bl_label = "Maple Sugar"
    bl_idname = 'color.hg71_maple_sugar'
    def execute(self, context):
        set_base_color(0xb3a67f, self.bl_label)
        return {'FINISHED'}

class HG71Goldenrod(bpy.types.Operator):
    """House & Garden 1971 Goldenrod"""
    bl_label = "Goldenrod"
    bl_idname = 'color.hg71_goldenrod'
    def execute(self, context):
        set_base_color(0xd1ab4e, self.bl_label)
        return {'FINISHED'}

class HG71AntiqueGold(bpy.types.Operator):
    """House & Garden 1971 Antique Gold"""
    bl_label = "Antique Gold"
    bl_idname = 'color.hg71_antique_gold'
    def execute(self, context):
        set_base_color(0xb39859, self.bl_label)
        return {'FINISHED'}

class HG71Pongee(bpy.types.Operator):
    """House & Garden 1971 Pongee"""
    bl_label = "Pongee"
    bl_idname = 'color.hg71_pongee'
    def execute(self, context):
        set_base_color(0xd3c995, self.bl_label)
        return {'FINISHED'}

class HG71CreamyApricot(bpy.types.Operator):
    """House & Garden 1971 Creamy Apricot"""
    bl_label = "Creamy Apricot"
    bl_idname = 'color.hg71_creamy_apricot'
    def execute(self, context):
        set_base_color(0xf5caab, self.bl_label)
        return {'FINISHED'}

class HG71PinkCoral(bpy.types.Operator):
    """House & Garden 1971 Pink Coral"""
    bl_label = "Pink Coral"
    bl_idname = 'color.hg71_pink_coral'
    def execute(self, context):
        set_base_color(0xec939f, self.bl_label)
        return {'FINISHED'}

class HG71FlagRed(bpy.types.Operator):
    """House & Garden 1971 Flag Red"""
    bl_label = "Flag Red"
    bl_idname = 'color.hg71_flag_red'
    def execute(self, context):
        set_base_color(0xd21b5c, self.bl_label)
        return {'FINISHED'}

class HG71BeachPlum(bpy.types.Operator):
    """House & Garden 1971 Beach Plum"""
    bl_label = "Beach Plum"
    bl_idname = 'color.hg71_beach_plum'
    def execute(self, context):
        set_base_color(0x49134c, self.bl_label)
        return {'FINISHED'}

class HG71PinkPink(bpy.types.Operator):
    """House & Garden 1971 Pink Pink"""
    bl_label = "Pink Pink"
    bl_idname = 'color.hg71_pink_pink'
    def execute(self, context):
        set_base_color(0xe9c7e9, self.bl_label)
        return {'FINISHED'}

class HG71Azalea(bpy.types.Operator):
    """House & Garden 1971 Azalea"""
    bl_label = "Azalea"
    bl_idname = 'color.hg71_azalea'
    def execute(self, context):
        set_base_color(0xe586b9, self.bl_label)
        return {'FINISHED'}

class HG71AfricanViolet(bpy.types.Operator):
    """House & Garden 1971 African Violet"""
    bl_label = "African Violet"
    bl_idname = 'color.hg71_african_violet'
    def execute(self, context):
        set_base_color(0xce90cf, self.bl_label)
        return {'FINISHED'}

class HG71Lavender(bpy.types.Operator):
    """House & Garden 1971 Lavender"""
    bl_label = "Lavender"
    bl_idname = 'color.hg71_lavender'
    def execute(self, context):
        set_base_color(0xd1bce0, self.bl_label)
        return {'FINISHED'}

class HG71OysterWhite(bpy.types.Operator):
    """House & Garden 1971 Oyster White"""
    bl_label = "Oyster White"
    bl_idname = 'color.hg71_oyster_white'
    def execute(self, context):
        set_base_color(0xe2dddb, self.bl_label)
        return {'FINISHED'}

class HG71Mercury(bpy.types.Operator):
    """House & Garden 1971 Mercury"""
    bl_label = "Mercury"
    bl_idname = 'color.hg71_mercury'
    def execute(self, context):
        set_base_color(0xb2b0b5, self.bl_label)
        return {'FINISHED'}

class HG71BlackPearl(bpy.types.Operator):
    """House & Garden 1971 Black Pearl"""
    bl_label = "Black Pearl"
    bl_idname = 'color.hg71_black_pearl'
    def execute(self, context):
        set_base_color(0x0a0a13, self.bl_label)
        return {'FINISHED'}

class HG71MidnightBlue(bpy.types.Operator):
    """House & Garden 1971 Midnight Blue"""
    bl_label = "Midnight Blue"
    bl_idname = 'color.hg71_midnight_blue'
    def execute(self, context):
        set_base_color(0x17195c, self.bl_label)
        return {'FINISHED'}

class HG71UltramarineBlue(bpy.types.Operator):
    """House & Garden 1971 Ultramarine Blue"""
    bl_label = "Ultramarine Blue"
    bl_idname = 'color.hg71_ultramarine_blue'
    def execute(self, context):
        set_base_color(0x1648a6, self.bl_label)
        return {'FINISHED'}

class HG71SpaceBlue(bpy.types.Operator):
    """House & Garden 1971 Space Blue"""
    bl_label = "Space Blue"
    bl_idname = 'color.hg71_space_blue'
    def execute(self, context):
        set_base_color(0x1973cf, self.bl_label)
        return {'FINISHED'}

class HG71BlueSky(bpy.types.Operator):
    """House & Garden 1971 Blue Sky"""
    bl_label = "Blue Sky"
    bl_idname = 'color.hg71_blue_sky'
    def execute(self, context):
        set_base_color(0x9ec4ef, self.bl_label)
        return {'FINISHED'}

class HG71BlueOpaline(bpy.types.Operator):
    """House & Garden 1971 Blue Opaline"""
    bl_label = "Blue Opaline"
    bl_idname = 'color.hg71_blue_opaline'
    def execute(self, context):
        set_base_color(0x3a66a2, self.bl_label)
        return {'FINISHED'}

class HG71AquamarineBlue(bpy.types.Operator):
    """House & Garden 1971 Aquamarine Blue"""
    bl_label = "Aquamarine Blue"
    bl_idname = 'color.hg71_aquamarine_blue'
    def execute(self, context):
        set_base_color(0xcad1d3, self.bl_label)
        return {'FINISHED'}


# BOOLEAN FOR PANEL
class HG71_SETTINGS(bpy.types.PropertyGroup):
    rename_material_pcoy: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )



# PARENT PANEL
class HG71Panel(bpy.types.Panel):
    bl_idname = "HG71_PT_Panel"
    bl_label = "House & Garden 1971"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"

    def draw(self, context):
        layout = self.layout
        pms_bool = context.scene.pms_bool

        col = layout.column(align=True)
        col.prop(pms_bool, "rename_material_pcoy")


# YELLOWS
class HG71_YELLOW_Panel(bpy.types.Panel):
    bl_idname = "HG71_YELLOW_PT_Panel"
    bl_label = "Yellows"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_pineapple"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_sun_yellow"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_kumquat"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_goldenrod"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_antique_gold"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_maple_sugar"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_pongee"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_pineapple", text="Pineapple")
        scol.operator("color.hg71_sun_yellow", text="Sun Yellow")
        scol.operator("color.hg71_kumquat", text="Kumquat")
        scol.operator("color.hg71_goldenrod", text="Goldenrod")
        scol.operator("color.hg71_antique_gold", text="Antique Gold")
        scol.operator("color.hg71_maple_sugar", text="Maple Sugar")
        scol.operator("color.hg71_pongee", text="Pongee")


# GREEN
class HG71_GREEN_Panel(bpy.types.Panel):
    bl_idname = "HG71_GREEN_PT_Panel"
    bl_label = "Greens"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_moss_green"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_lacquer_green"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_green_mint"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_parrot_green"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_lettuce"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_celery"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_moss_green", text="Moss Green")
        scol.operator("color.hg71_lacquer_green", text="Lacquer Green")
        scol.operator("color.hg71_green_mint", text="Green Mint")
        scol.operator("color.hg71_parrot_green", text="Parrot Green")
        scol.operator("color.hg71_lettuce", text="Lettuce")
        scol.operator("color.hg71_celery", text="Celery")


# BLUES
class HG71_BLUE_Panel(bpy.types.Panel):
    bl_idname = "HG71_BLUE_PT_Panel"
    bl_label = "Blues"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_midnight_blue"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_ultramarine_blue"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_space_blue"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_blue_opaline"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_blue_sky"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_aquamarine_blue"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_midnight_blue", text="Midnight Blue")
        scol.operator("color.hg71_ultramarine_blue", text="Ultramarine Blue")
        scol.operator("color.hg71_space_blue", text="Space Blue")
        scol.operator("color.hg71_blue_opaline", text="Blue Opaline")
        scol.operator("color.hg71_blue_sky", text="Blue Sky")
        scol.operator("color.hg71_aquamarine_blue", text="Aquamarine Blue")


# ORANGES
class HG71_ORANGE_Panel(bpy.types.Panel):
    bl_idname = "HG71_ORANGE_PT_Panel"
    bl_label = "Oranges"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_bittersweet"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_tangerine"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_pompeiian_red"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_zinnia"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_creamy_apricot"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_velvet_brown"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_bittersweet", text="Bittersweet")
        scol.operator("color.hg71_tangerine", text="Tangerine")
        scol.operator("color.hg71_pompeiian_red", text="Pompeiian Red")
        scol.operator("color.hg71_zinnia", text="Zinnia")
        scol.operator("color.hg71_creamy_apricot", text="Creamy Apricot")
        scol.operator("color.hg71_velvet_brown", text="Velvet Brown")


# REDS
class HG71_RED_Panel(bpy.types.Panel):
    bl_idname = "HG71_RED_PT_Panel"
    bl_label = "Reds"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_flag_red"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_pink_coral"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_pink_pink"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_azalea"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_flag_red", text="Flag Red")
        scol.operator("color.hg71_pink_coral", text="Pink Coral")
        scol.operator("color.hg71_pink_pink", text="Pink Pink")
        scol.operator("color.hg71_azalea", text="Azalea")


# PURPLES
class HG71_PURPLE_Panel(bpy.types.Panel):
    bl_idname = "HG71_PURPLE_PT_Panel"
    bl_label = "Purples"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_beach_plum"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_african_violet"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_lavender"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_beach_plum", text="Beach Plum")
        scol.operator("color.hg71_african_violet", text="African Violet")
        scol.operator("color.hg71_lavender", text="Lavender")


# GRAYS
class HG71_GRAY_Panel(bpy.types.Panel):
    bl_idname = "HG71_GRAY_PT_Panel"
    bl_label = "Grays"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'HG71_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["hg71_oyster_white"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_mercury"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_mushroom"].icon_id)
        scol.label(text="", icon_value=c_icons["hg71_black_pearl"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.hg71_oyster_white", text="Oyster White")
        scol.operator("color.hg71_mercury", text="Mercury")
        scol.operator("color.hg71_mushroom", text="Mushroom")
        scol.operator("color.hg71_black_pearl", text="Black Pearl")


classes = [
    HG71_SETTINGS,
    HG71Panel,
    HG71_YELLOW_Panel,
    HG71_GREEN_Panel,
    HG71_BLUE_Panel,
    HG71_ORANGE_Panel,
    HG71_RED_Panel,
    HG71_PURPLE_Panel,
    HG71_GRAY_Panel,
    HG71Pineapple,
    HG71SunYellow,
    HG71Kumquat,
    HG71Goldenrod,
    HG71AntiqueGold,
    HG71MapleSugar,
    HG71Pongee,
    HG71MossGreen,
    HG71LacquerGreen,
    HG71GreenMint,
    HG71ParrotGreen,
    HG71Lettuce,
    HG71Celery,
    HG71MidnightBlue,
    HG71UltramarineBlue,
    HG71SpaceBlue,
    HG71BlueOpaline,
    HG71BlueSky,
    HG71AquamarineBlue,
    HG71Bittersweet,
    HG71Tangerine,
    HG71PompeiianRed,
    HG71Zinnia,
    HG71CreamyApricot,
    HG71VelvetBrown,
    HG71FlagRed,
    HG71PinkCoral,
    HG71PinkPink,
    HG71Azalea,
    HG71BeachPlum,
    HG71AfricanViolet,
    HG71Lavender,
    HG71OysterWhite,
    HG71Mercury,
    HG71Mushroom,
    HG71BlackPearl,
]


def register():
    # Addon updater code and configurations.
    # In case of a broken version, try to register the updater first so that
    # users can revert back to a working version.
#    addon_updater_ops.register(bl_info)

#   LOAD CUSTOM ICONS
    global c_icons
    c_icons = bpy.utils.previews.new()
    addon_path =  os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")
    for entry in os.listdir(icons_dir):
        c_icons.load(os.path.splitext(entry)[0], os.path.join(icons_dir, entry), "IMAGE")

    # Register the example panel, to show updater buttons.
    for cls in classes:
#        addon_updater_ops.make_annotations(cls)  # Avoid blender 2.8 warnings.
        bpy.utils.register_class(cls)
        bpy.types.Scene.pms_bool = bpy.props.PointerProperty(type=HG71_SETTINGS)


def unregister():
    # Addon updater unregister.
#    addon_updater_ops.unregister()
#   UNREGISTER ICONS
    global c_icons
    bpy.utils.previews.remove(c_icons)

    del bpy.types.Scene.pms_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
