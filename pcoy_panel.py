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
    "version"    : (0, 2, 2),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > PCOY",
    "warning"    : "WIP",
    "wiki_url"   : "https://github.com/don1138/blender-pcoy",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}



import bpy



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
    bl_label = "2000 Cerulean Blue"
    bl_idname = 'color.pms_2000'
    def execute(self, context):
        set_base_color(0x9BB7D4, self.bl_label)
        return {'FINISHED'}

class PMS2001(bpy.types.Operator):
    """Pantone 17-2031"""
    bl_label = "2001 Fuschia Rose"
    bl_idname = 'color.pms_2001'
    def execute(self, context):
        set_base_color(0xC74375, self.bl_label)
        return {'FINISHED'}

class PMS2002(bpy.types.Operator):
    """Pantone 19-1664"""
    bl_label = "2002 True Red"
    bl_idname = 'color.pms_2002'
    def execute(self, context):
        set_base_color(0xBF1932, self.bl_label)
        return {'FINISHED'}

class PMS2003(bpy.types.Operator):
    """Pantone 14-4811"""
    bl_label = "2003 Aqua Sky"
    bl_idname = 'color.pms_2003'
    def execute(self, context):
        set_base_color(0x7BC4C4, self.bl_label)
        return {'FINISHED'}

class PMS2004(bpy.types.Operator):
    """Pantone 17-1456"""
    bl_label = "2004 Tigerlily"
    bl_idname = 'color.pms_2004'
    def execute(self, context):
        set_base_color(0xE2583E, self.bl_label)
        return {'FINISHED'}

class PMS2005(bpy.types.Operator):
    """Pantone 15-5217"""
    bl_label = "2005 Blue Turquoise"
    bl_idname = 'color.pms_2005'
    def execute(self, context):
        set_base_color(0x53B0AE, self.bl_label)
        return {'FINISHED'}

class PMS2006(bpy.types.Operator):
    """Pantone 13-1106"""
    bl_label = "2006 Sand Dollar"
    bl_idname = 'color.pms_2006'
    def execute(self, context):
        set_base_color(0xDECDBE, self.bl_label)
        return {'FINISHED'}

class PMS2007(bpy.types.Operator):
    """Pantone 19-1557"""
    bl_label = "2007 Chili Pepper"
    bl_idname = 'color.pms_2007'
    def execute(self, context):
        set_base_color(0x9B1B30, self.bl_label)
        return {'FINISHED'}

class PMS2008(bpy.types.Operator):
    """Pantone 18-3943"""
    bl_label = "2008 Blue Iris"
    bl_idname = 'color.pms_2008'
    def execute(self, context):
        set_base_color(0x5A5B9F, self.bl_label)
        return {'FINISHED'}

class PMS2009(bpy.types.Operator):
    """Pantone 14-0848"""
    bl_label = "2009 Mimosa"
    bl_idname = 'color.pms_2009'
    def execute(self, context):
        set_base_color(0xF0C05A, self.bl_label)
        return {'FINISHED'}

class PMS2010(bpy.types.Operator):
    """Pantone 15-5519"""
    bl_label = "2010 Turquoise"
    bl_idname = 'color.pms_2010'
    def execute(self, context):
        set_base_color(0x45B5AA, self.bl_label)
        return {'FINISHED'}

class PMS2011(bpy.types.Operator):
    """Pantone 18-2120"""
    bl_label = "2011 Honeysuckle"
    bl_idname = 'color.pms_2011'
    def execute(self, context):
        set_base_color(0xD94F70, self.bl_label)
        return {'FINISHED'}

class PMS2012(bpy.types.Operator):
    """Pantone 17-1463"""
    bl_label = "2012 Tangerine"
    bl_idname = 'color.pms_2012'
    def execute(self, context):
        set_base_color(0xDD4124, self.bl_label)
        return {'FINISHED'}

class PMS2013(bpy.types.Operator):
    """Pantone 17-5641"""
    bl_label = "2013 Emerald"
    bl_idname = 'color.pms_2013'
    def execute(self, context):
        set_base_color(0x009473, self.bl_label)
        return {'FINISHED'}

class PMS2014(bpy.types.Operator):
    """Pantone 18-3224"""
    bl_label = "2014 Radiant Orchid"
    bl_idname = 'color.pms_2014'
    def execute(self, context):
        set_base_color(0xB163A3, self.bl_label)
        return {'FINISHED'}

class PMS2015(bpy.types.Operator):
    """Pantone 18-1438"""
    bl_label = "2015 Marsala"
    bl_idname = 'color.pms_2015'
    def execute(self, context):
        set_base_color(0x955251, self.bl_label)
        return {'FINISHED'}

class PMS2016A(bpy.types.Operator):
    """Pantone 13-1520"""
    bl_label = "2016 Rose Quartz"
    bl_idname = 'color.pms_2016_a'
    def execute(self, context):
        set_base_color(0xF7CAC9, self.bl_label)
        return {'FINISHED'}

class PMS2016B(bpy.types.Operator):
    """Pantone 15-3919"""
    bl_label = "2016 Serenity"
    bl_idname = 'color.pms_2016_b'
    def execute(self, context):
        set_base_color(0x92A8D1, self.bl_label)
        return {'FINISHED'}

class PMS2017(bpy.types.Operator):
    """Pantone 15-0343"""
    bl_label = "2017 Greenery"
    bl_idname = 'color.pms_2017'
    def execute(self, context):
        set_base_color(0x88B04B, self.bl_label)
        return {'FINISHED'}

class PMS2018(bpy.types.Operator):
    """Pantone 18-3838"""
    bl_label = "2018 Ultra Violet"
    bl_idname = 'color.pms_2018'
    def execute(self, context):
        set_base_color(0x5F4B8B, self.bl_label)
        return {'FINISHED'}

class PMS2019(bpy.types.Operator):
    """Pantone 16-1546 TCX"""
    bl_label = "2019 Living Coral"
    bl_idname = 'color.pms_2019'
    def execute(self, context):
        set_base_color(0xFF6F61, self.bl_label)
        return {'FINISHED'}

class PMS2020(bpy.types.Operator):
    """Pantone 19-4052"""
    bl_label = "2020 Classic Blue"
    bl_idname = 'color.pms_2020'
    def execute(self, context):
        set_base_color(0x0F4C81, self.bl_label)
        return {'FINISHED'}

class PMS2021A(bpy.types.Operator):
    """Pantone 17-5104"""
    bl_label = "2021 Ultimate Gray"
    bl_idname = 'color.pms_2021_a'
    def execute(self, context):
        set_base_color(0x949597, self.bl_label)
        return {'FINISHED'}

class PMS2021B(bpy.types.Operator):
    """Pantone 13-0647"""
    bl_label = "2021 Illuminating"
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
    bl_label = "Team Coco Orange"
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
    bl_label = "2043 Dead Coral"
    bl_idname = 'color.pms_dcoral'
    def execute(self, context):
        set_base_color(0xA7997E, self.bl_label)
        return {'FINISHED'}

class PMSUnignorable(bpy.types.Operator):
    """Custom Color selected by Pantone"""
    bl_label = "United Way Unignorable"
    bl_idname = 'color.pms_uwign'
    def execute(self, context):
        set_base_color(0xFC502E, self.bl_label)
        return {'FINISHED'}

class PMS383(bpy.types.Operator):
    """Pantone 383"""
    bl_label = "A Nice Green"
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

        row = layout.row()
        row.prop(pms_bool, "rename_material_pcoy")

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
        layout = self.layout
        row = layout.row()
        row.operator("color.pms_2000", text="2000  ·  Cerulean Blue")
        row = layout.row()
        row.operator("color.pms_2001", text="2001  ·  Fuschia Rose")
        row = layout.row()
        row.operator("color.pms_2002", text="2002  ·  True Red")
        row = layout.row()
        row.operator("color.pms_2003", text="2003  ·  Aqua Sky")
        row = layout.row()
        row.operator("color.pms_2004", text="2004  ·  Tigerlily")
        row = layout.row()
        row.operator("color.pms_2005", text="2005  ·  Blue Turquoise")
        row = layout.row()
        row.operator("color.pms_2006", text="2006  ·  Sand Dollar")
        row = layout.row()
        row.operator("color.pms_2007", text="2007  ·  Chili Pepper")
        row = layout.row()
        row.operator("color.pms_2008", text="2008  ·  Blue Iris")
        row = layout.row()
        row.operator("color.pms_2009", text="2009  ·  Mimosa")

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
        layout = self.layout
        row = layout.row()
        row.operator("color.pms_2010", text="2010  ·  Turquoise")
        row = layout.row()
        row.operator("color.pms_2011", text="2011  ·  Honeysuckle")
        row = layout.row()
        row.operator("color.pms_2012", text="2012  ·  Tangerine")
        row = layout.row()
        row.operator("color.pms_2013", text="2013  ·  Emerald")
        row = layout.row()
        row.operator("color.pms_2014", text="2014  ·  Radiant Orchid")
        row = layout.row()
        row.operator("color.pms_2015", text="2015  ·  Marsala")
        row = layout.row()
        row.operator("color.pms_2016_a", text="2016  ·  Rose Quartz")
        row = layout.row()
        row.operator("color.pms_2016_b", text="2016  ·  Serenity")
        row = layout.row()
        row.operator("color.pms_2017", text="2017  ·  Greenery")
        row = layout.row()
        row.operator("color.pms_2018", text="2018  ·  Ultra Violet")
        row = layout.row()
        row.operator("color.pms_2019", text="2019  ·  Living Coral")

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
        layout = self.layout
        row = layout.row()
        row.operator("color.pms_2020", text="2020  ·  Classic Blue")
        row = layout.row()
        row.operator("color.pms_2021_a", text="2021  ·  Ultimate Gray")
        row = layout.row()
        row.operator("color.pms_2021_b", text="2021  ·  Illuminating")

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
        layout = self.layout
        row = layout.row()
        row.operator("color.pms_bcoral", text="2020  ·  Bleached Coral")
        row = layout.row()
        row.operator("color.pms_dcoral", text="2043  ·  Dead Coral")
        row = layout.row()
        row.operator("color.pms_prince", text="Prince")
        row = layout.row()
        row.operator("color.pms_conan", text="Team Coco Orange")
        row = layout.row()
        row.operator("color.pms_uwign", text="United Way Unignorable")
        row = layout.row()
        row.operator("color.pms_383", text="A Nice Green")
        row = layout.row()
        row.operator("color.pms_448c", text="Ugliest Color in the World (Official)")



classes = [
    PMS_SETTINGS,
    PMSPanel,
    PMSPanel2000,
    PMSPanel2010,
    PMSPanel2020,
    PMSPanelExtras,
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
]


def register():
    # Addon updater code and configurations.
    # In case of a broken version, try to register the updater first so that
    # users can revert back to a working version.
#    addon_updater_ops.register(bl_info)

    # Register the example panel, to show updater buttons.
    for cls in classes:
#        addon_updater_ops.make_annotations(cls)  # Avoid blender 2.8 warnings.
        bpy.utils.register_class(cls)
        bpy.types.Scene.pms_bool = bpy.props.PointerProperty(type=PMS_SETTINGS)


def unregister():
    # Addon updater unregister.
#    addon_updater_ops.unregister()
    del bpy.types.Scene.pms_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()




#LIST NODE OUTPUTS
#for i, o in enumerate(BSDF.inputs):
#    print(i, o.name)
# 0 Base Color
# 1 Subsurface
# 2 Subsurface Radius
# 3 Subsurface Color
# 4 Metallic
# 5 Specular
# 6 Specular Tint
# 7 Roughness
# 8 Anisotropic
# 9 Anisotropic Rotation
# 10 Sheen
# 11 Sheen Tint
# 12 Clearcoat
# 13 Clearcoat Roughness
# 14 IOR
# 15 Transmission
# 16 Transmission Roughness
# 17 Emission
# 18 Emission Strength
# 19 Alpha
# 20 Normal
# 21 Clearcoat Normal
# 22 Tangent

