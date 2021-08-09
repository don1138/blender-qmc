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
    "name"       : "PCOY (Pantone Color of the Year)",
    "description": "Sets the Base Color of a Principled BSDF",
    "author"     : "Don Schnitzius",
    "version"    : (0, 3, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > PCOY",
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
        BSDF = material.node_tree.nodes.get('Principled BSDF')
        if BSDF:
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

class PMS2000(bpy.types.Operator):
    """Pantone 15-4020"""
    bl_label = "Cerulean Blue"
    bl_idname = 'color.pms_2000'
    def execute(self, context):
        set_base_color(0x9BB7D4, self.bl_label)
        return {'FINISHED'}

class PMS2001(bpy.types.Operator):
    """Pantone 17-2031"""
    bl_label = "Fuschia Rose"
    bl_idname = 'color.pms_2001'
    def execute(self, context):
        set_base_color(0xC74375, self.bl_label)
        return {'FINISHED'}

class PMS2002(bpy.types.Operator):
    """Pantone 19-1664"""
    bl_label = "True Red"
    bl_idname = 'color.pms_2002'
    def execute(self, context):
        set_base_color(0xBF1932, self.bl_label)
        return {'FINISHED'}

class PMS2003(bpy.types.Operator):
    """Pantone 14-4811"""
    bl_label = "Aqua Sky"
    bl_idname = 'color.pms_2003'
    def execute(self, context):
        set_base_color(0x7BC4C4, self.bl_label)
        return {'FINISHED'}

class PMS2004(bpy.types.Operator):
    """Pantone 17-1456"""
    bl_label = "Tigerlily"
    bl_idname = 'color.pms_2004'
    def execute(self, context):
        set_base_color(0xE2583E, self.bl_label)
        return {'FINISHED'}

class PMS2005(bpy.types.Operator):
    """Pantone 15-5217"""
    bl_label = "Blue Turquoise"
    bl_idname = 'color.pms_2005'
    def execute(self, context):
        set_base_color(0x53B0AE, self.bl_label)
        return {'FINISHED'}

class PMS2006(bpy.types.Operator):
    """Pantone 13-1106"""
    bl_label = "Sand Dollar"
    bl_idname = 'color.pms_2006'
    def execute(self, context):
        set_base_color(0xDECDBE, self.bl_label)
        return {'FINISHED'}

class PMS2007(bpy.types.Operator):
    """Pantone 19-1557"""
    bl_label = "Chili Pepper"
    bl_idname = 'color.pms_2007'
    def execute(self, context):
        set_base_color(0x9B1B30, self.bl_label)
        return {'FINISHED'}

class PMS2008(bpy.types.Operator):
    """Pantone 18-3943"""
    bl_label = "Blue Iris"
    bl_idname = 'color.pms_2008'
    def execute(self, context):
        set_base_color(0x5A5B9F, self.bl_label)
        return {'FINISHED'}

class PMS2009(bpy.types.Operator):
    """Pantone 14-0848"""
    bl_label = "Mimosa"
    bl_idname = 'color.pms_2009'
    def execute(self, context):
        set_base_color(0xF0C05A, self.bl_label)
        return {'FINISHED'}

class PMS2010(bpy.types.Operator):
    """Pantone 15-5519"""
    bl_label = "Turquoise"
    bl_idname = 'color.pms_2010'
    def execute(self, context):
        set_base_color(0x45B5AA, self.bl_label)
        return {'FINISHED'}

class PMS2011(bpy.types.Operator):
    """Pantone 18-2120"""
    bl_label = "Honeysuckle"
    bl_idname = 'color.pms_2011'
    def execute(self, context):
        set_base_color(0xD94F70, self.bl_label)
        return {'FINISHED'}

class PMS2012(bpy.types.Operator):
    """Pantone 17-1463"""
    bl_label = "Tangerine"
    bl_idname = 'color.pms_2012'
    def execute(self, context):
        set_base_color(0xDD4124, self.bl_label)
        return {'FINISHED'}

class PMS2013(bpy.types.Operator):
    """Pantone 17-5641"""
    bl_label = "Emerald"
    bl_idname = 'color.pms_2013'
    def execute(self, context):
        set_base_color(0x009473, self.bl_label)
        return {'FINISHED'}

class PMS2014(bpy.types.Operator):
    """Pantone 18-3224"""
    bl_label = "Radiant Orchid"
    bl_idname = 'color.pms_2014'
    def execute(self, context):
        set_base_color(0xB163A3, self.bl_label)
        return {'FINISHED'}

class PMS2015(bpy.types.Operator):
    """Pantone 18-1438"""
    bl_label = "Marsala"
    bl_idname = 'color.pms_2015'
    def execute(self, context):
        set_base_color(0x955251, self.bl_label)
        return {'FINISHED'}

class PMS2016A(bpy.types.Operator):
    """Pantone 13-1520"""
    bl_label = "Rose Quartz"
    bl_idname = 'color.pms_2016_a'
    def execute(self, context):
        set_base_color(0xF7CAC9, self.bl_label)
        return {'FINISHED'}

class PMS2016B(bpy.types.Operator):
    """Pantone 15-3919"""
    bl_label = "Serenity"
    bl_idname = 'color.pms_2016_b'
    def execute(self, context):
        set_base_color(0x92A8D1, self.bl_label)
        return {'FINISHED'}

class PMS2017(bpy.types.Operator):
    """Pantone 15-0343"""
    bl_label = "Greenery"
    bl_idname = 'color.pms_2017'
    def execute(self, context):
        set_base_color(0x88B04B, self.bl_label)
        return {'FINISHED'}

class PMS2018(bpy.types.Operator):
    """Pantone 18-3838"""
    bl_label = "Ultra Violet"
    bl_idname = 'color.pms_2018'
    def execute(self, context):
        set_base_color(0x5F4B8B, self.bl_label)
        return {'FINISHED'}

class PMS2019(bpy.types.Operator):
    """Pantone 16-1546 TCX"""
    bl_label = "Living Coral"
    bl_idname = 'color.pms_2019'
    def execute(self, context):
        set_base_color(0xFF6F61, self.bl_label)
        return {'FINISHED'}

class PMS2020(bpy.types.Operator):
    """Pantone 19-4052"""
    bl_label = "Classic Blue"
    bl_idname = 'color.pms_2020'
    def execute(self, context):
        set_base_color(0x0F4C81, self.bl_label)
        return {'FINISHED'}

class PMS2021A(bpy.types.Operator):
    """Pantone 17-5104"""
    bl_label = "Ultimate Gray"
    bl_idname = 'color.pms_2021_a'
    def execute(self, context):
        set_base_color(0x949597, self.bl_label)
        return {'FINISHED'}

class PMS2021B(bpy.types.Operator):
    """Pantone 13-0647"""
    bl_label = "Illuminating"
    bl_idname = 'color.pms_2021_b'
    def execute(self, context):
        set_base_color(0xF5DF4D, self.bl_label)
        return {'FINISHED'}

class PMSPrince(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "Prince"
    bl_idname = 'color.pms_prince'
    def execute(self, context):
        set_base_color(0x493452, self.bl_label)
        return {'FINISHED'}

class PMSConan(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "Team Coco"
    bl_idname = 'color.pms_conan'
    def execute(self, context):
        set_base_color(0xFE7A0B, self.bl_label)
        return {'FINISHED'}

class PMSBCoral(bpy.types.Operator):
    """Pantone P-115-1-U (Community reaction to 2019 Living Coral)"""
    bl_label = "Bleached Coral"
    bl_idname = 'color.pms_bcoral'
    def execute(self, context):
        set_base_color(0xF4F7FC, self.bl_label)
        return {'FINISHED'}

class PMSSDCoral(bpy.types.Operator):
    """(Community reaction to 2019 Living Coral)"""
    bl_label = "Dead Coral"
    bl_idname = 'color.pms_dcoral'
    def execute(self, context):
        set_base_color(0xA7997E, self.bl_label)
        return {'FINISHED'}

class PMSUnignorable(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "UW Unignorable"
    bl_idname = 'color.pms_uwign'
    def execute(self, context):
        set_base_color(0xFC502E, self.bl_label)
        return {'FINISHED'}

class PMS383(bpy.types.Operator):
    """Pantone 383"""
    bl_label = "Nice Green"
    bl_idname = 'color.pms_383'
    def execute(self, context):
        set_base_color(0xD0DF68, self.bl_label)
        return {'FINISHED'}

class PMS448C(bpy.types.Operator):
    """Pantone 448 C"""
    bl_label = "Ugliest Color in the World"
    bl_idname = 'color.pms_448c'
    def execute(self, context):
        set_base_color(0x4A412A, self.bl_label)
        return {'FINISHED'}

class SCHNITZIUS_GREEN(bpy.types.Operator):
    """Schnitzius Green"""
    bl_label = "Schnitzius Green"
    bl_idname = 'color.schnitzius_green'
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

class SCHNITZIUS_RED(bpy.types.Operator):
    """Schnitzius Red"""
    bl_label = "Schnitzius Red"
    bl_idname = 'color.schnitzius_red'
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

class SCHNITZIUS_BLUE(bpy.types.Operator):
    """Schnitzius Blue"""
    bl_label = "Schnitzius Blue"
    bl_idname = 'color.schnitzius_blue'
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

class SCHNITZIUS_YELLOW(bpy.types.Operator):
    """Schnitzius Yellow"""
    bl_label = "Schnitzius Yellow"
    bl_idname = 'color.schnitzius_yellow'
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

class SCHNITZIUS_BRONZE_PALE(bpy.types.Operator):
    """Schnitzius Bronze Pale"""
    bl_label = "Schnitzius Bronze Pale"
    bl_idname = 'color.schnitzius_bronze_pale'
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

class SCHNITZIUS_BRONZE_RICH(bpy.types.Operator):
    """Schnitzius Bronze Rich"""
    bl_label = "Schnitzius Bronze Rich"
    bl_idname = 'color.schnitzius_bronze_rich'
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

class SCHNITZIUS_WHITE(bpy.types.Operator):
    """Schnitzius White"""
    bl_label = "Schnitzius White"
    bl_idname = 'color.schnitzius_white'
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



# BOOLEAN FOR PANEL
class PMS_SETTINGS(bpy.types.PropertyGroup):
    rename_material_pcoy: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )



# PARENT PANEL
class PMSPanel(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel"
    bl_label = "Pantone Color of the Year"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PCOY"

    def draw(self, context):
        layout = self.layout
        pms_bool = context.scene.pms_bool

        col = layout.column(align=True)
        col.prop(pms_bool, "rename_material_pcoy")

# 2000-09 PANEL
class PMSPanel2000(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2000"
    bl_label = "2000-09"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PMS"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2000")
        scol.label(text="2001")
        scol.label(text="2002")
        scol.label(text="2003")
        scol.label(text="2004")
        scol.label(text="2005")
        scol.label(text="2006")
        scol.label(text="2007")
        scol.label(text="2008")
        scol.label(text="2009")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["pcoy_2000"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2001"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2002"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2003"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2004"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2005"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2006"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2007"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2008"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2009"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2000", text="Cerulean Blue")
        scol.operator("color.pms_2001", text="Fuschia Rose")
        scol.operator("color.pms_2002", text="True Red")
        scol.operator("color.pms_2003", text="Aqua Sky")
        scol.operator("color.pms_2004", text="Tigerlily")
        scol.operator("color.pms_2005", text="Blue Turquoise")
        scol.operator("color.pms_2006", text="Sand Dollar")
        scol.operator("color.pms_2007", text="Chili Pepper")
        scol.operator("color.pms_2008", text="Blue Iris")
        scol.operator("color.pms_2009", text="Mimosa")


# 2010-19 PANEL
class PMSPanel2010(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2010"
    bl_label = "2010-19"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PMS"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2010")
        scol.label(text="2011")
        scol.label(text="2012")
        scol.label(text="2013")
        scol.label(text="2014")
        scol.label(text="2015")
        scol.label(text="2016")
        scol.label(text="2016")
        scol.label(text="2017")
        scol.label(text="2018")
        scol.label(text="2019")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["pcoy_2010"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2011"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2012"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2013"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2014"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2015"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2016a"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2016b"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2017"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2018"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2019"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2010", text="Turquoise")
        scol.operator("color.pms_2011", text="Honeysuckle")
        scol.operator("color.pms_2012", text="Tangerine")
        scol.operator("color.pms_2013", text="Emerald")
        scol.operator("color.pms_2014", text="Radiant Orchid")
        scol.operator("color.pms_2015", text="Marsala")
        scol.operator("color.pms_2016_a", text="Rose Quartz")
        scol.operator("color.pms_2016_b", text="Serenity")
        scol.operator("color.pms_2017", text="Greenery")
        scol.operator("color.pms_2018", text="Ultra Violet")
        scol.operator("color.pms_2019", text="Living Coral")


# 2020+ PANEL
class PMSPanel2020(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2020"
    bl_label = "2020-29"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PMS"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2020")
        scol.label(text="2021")
        scol.label(text="2021")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["pcoy_2020"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2021a"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2021b"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2020", text="Classic Blue")
        scol.operator("color.pms_2021_a", text="Ultimate Gray")
        scol.operator("color.pms_2021_b", text="Illuminating")


# Extras & Apocrypha PANEL
class PMSPanelExtras(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_Extras"
    bl_label = "Extras & Apocrypha"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PMS"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["pcoy_2020b"].icon_id)
        scol.label(text="", icon_value=c_icons["pcoy_2043"].icon_id)
        scol.label(text="", icon_value=c_icons["prince"].icon_id)
        scol.label(text="", icon_value=c_icons["conan"].icon_id)
        scol.label(text="", icon_value=c_icons["uw"].icon_id)
        scol.label(text="", icon_value=c_icons["pms_383"].icon_id)
        scol.label(text="", icon_value=c_icons["pms_448"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_bcoral", text="2020 Bleached Coral")
        scol.operator("color.pms_dcoral", text="2043 Dead Coral")
        scol.operator("color.pms_prince", text="Prince")
        scol.operator("color.pms_conan", text="Team Coco Orange")
        scol.operator("color.pms_uwign", text="United Way Unignorable")
        scol.operator("color.pms_383", text="A Nice Green")
        scol.operator("color.pms_448c", text="Ugliest Color in the World (Official)")


# Schnitzius Selects PANEL
class PMSPanelSchnitzius(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_Schitzius"
    bl_label = "Schnitzius Select"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PMS"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.grid_flow(row_major=True,even_columns=True,columns=2,align=True)
        col.scale_y = 1.25
        col.label(text="My Color")
        col.label(text="PMS Match")
        col.operator("color.schnitzius_green", text="Green")
        col.operator("color.pms_381_u", text="PMS 381 U")
        col.operator("color.schnitzius_red", text="Red")
        col.operator("color.pms_172_c", text="PMS 172 C")
        col.operator("color.schnitzius_blue", text="Blue")
        col.operator("color.pms_2685_u", text="PMS 2685 U")
        col.operator("color.schnitzius_yellow", text="Yellow")
        col.operator("color.pms_396_u", text="PMS 396 U")
        col.operator("color.schnitzius_bronze_pale", text="Bronze Pale")
        col.operator("color.pms_729_u", text="PMS 729 U")
        col.operator("color.schnitzius_bronze_rich", text="Bronze Rich")
        col.operator("color.pms_7518_u", text="PMS 7518 U")
        col.operator("color.schnitzius_white", text="White")
        col.operator("color.pms_7499_u", text="PMS 7499 U")



classes = [
    PMS_SETTINGS,
    PMSPanel,
    PMSPanel2000,
    PMSPanel2010,
    PMSPanel2020,
    PMSPanelExtras,
    PMSPanelSchnitzius,
    PMS2000,
    PMS2001,
    PMS2002,
    PMS2003,
    PMS2004,
    PMS2005,
    PMS2006,
    PMS2007,
    PMS2008,
    PMS2009,
    PMS2010,
    PMS2011,
    PMS2012,
    PMS2013,
    PMS2014,
    PMS2015,
    PMS2016A,
    PMS2016B,
    PMS2017,
    PMS2018,
    PMS2019,
    PMS2020,
    PMS2021A,
    PMS2021B,
    PMSPrince,
    PMSConan,
    PMSBCoral,
    PMSSDCoral,
    PMSUnignorable,
    PMS383,
    PMS448C,
    SCHNITZIUS_GREEN,
    PMS_381U,
    SCHNITZIUS_RED,
    PMS_172_C,
    SCHNITZIUS_BLUE,
    PMS_2685U,
    SCHNITZIUS_YELLOW,
    PMS_396U,
    SCHNITZIUS_BRONZE_PALE,
    PMS_729U,
    SCHNITZIUS_BRONZE_RICH,
    PMS_7518U,
    SCHNITZIUS_WHITE,
    PMS_7499U,
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
        bpy.types.Scene.pms_bool = bpy.props.PointerProperty(type=PMS_SETTINGS)


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