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
    "name"       : "F58 (Ford Colors 1958)",
    "description": "Sets the Base Color of a Principled BSDF",
    "author"     : "Don Schnitzius",
    "version"    : (0, 6, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > Ford Colors 1958",
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
        mat_bool = bpy.context.scene.f_bool.rename_material_f
        plaster = bpy.data.materials.get('QMM Plaster')
        D_BSDF = material.node_tree.nodes.get('Diffuse BSDF')
        BSDF = material.node_tree.nodes.get('Principled BSDF')
        RGB = material.node_tree.nodes.get('RGB')
        ColorRamp = material.node_tree.nodes.get('ColorRamp')

        if material == plaster:
            ColorRamp.color_ramp.elements[0].color = hex_to_rgb(hex)
            BSDF.inputs[3].default_value = hex_to_rgb(hex)
            RGB.outputs[0].default_value = hex_to_rgb(hex)
            material.diffuse_color = hex_to_rgb(hex)
        elif D_BSDF:
            D_BSDF.inputs[0].default_value = hex_to_rgb(hex)
            material.diffuse_color = hex_to_rgb(hex)
            if mat_bool == True:
                material.name = mat_name
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

# Ford Colors 1958

class F58ARavenBlack(bpy.types.Operator):
    """Ford Colors 1958 - A Raven Black"""
    bl_label = "A Raven Black"
    bl_idname = 'color.f58a_raven_black'
    def execute(self, context):
        set_base_color(0x010303, self.bl_label)
        return {'FINISHED'}

class F58CDesertBeige(bpy.types.Operator):
    """Ford Colors 1958 - C Desert Beige"""
    bl_label = "C Desert Beige"
    bl_idname = 'color.f58c_desert_beige'
    def execute(self, context):
        set_base_color(0xc0ab83, self.bl_label)
        return {'FINISHED'}

class F58DPalaminoTan(bpy.types.Operator):
    """Ford Colors 1958 - D Palamino Tan"""
    bl_label = "D Palamino Tan"
    bl_idname = 'color.f58d_palamino_tan'
    def execute(self, context):
        set_base_color(0xab7832, self.bl_label)
        return {'FINISHED'}

class F58EColonialWhite(bpy.types.Operator):
    """Ford Colors 1958 - E Colonial White"""
    bl_label = "E Colonial White"
    bl_idname = 'color.f58e_colonial_white'
    def execute(self, context):
        set_base_color(0xe7e4c1, self.bl_label)
        return {'FINISHED'}

class F58FSilvertoneGreen(bpy.types.Operator):
    """Ford Colors 1958 - F Silvertone Green"""
    bl_label = "F Silvertone Green"
    bl_idname = 'color.f58f_silvertone_green'
    def execute(self, context):
        set_base_color(0x1e3226, self.bl_label)
        return {'FINISHED'}

class F58GSunGold(bpy.types.Operator):
    """Ford Colors 1958 - G Sun Gold"""
    bl_label = "G Sun Gold"
    bl_idname = 'color.f58g_sun_gold'
    def execute(self, context):
        set_base_color(0xe7d74a, self.bl_label)
        return {'FINISHED'}

class F58HGunmetalGray(bpy.types.Operator):
    """Ford Colors 1958 - H Gunmetal Gray"""
    bl_label = "H Gunmetal Gray"
    bl_idname = 'color.f58h_gunmetal_gray'
    def execute(self, context):
        set_base_color(0x4c4f50, self.bl_label)
        return {'FINISHED'}

class F58JBaliBronze(bpy.types.Operator):
    """Ford Colors 1958 - J Bali Bronze"""
    bl_label = "J Bali Bronze"
    bl_idname = 'color.f58j_bali_bronze'
    def execute(self, context):
        set_base_color(0x654935, self.bl_label)
        return {'FINISHED'}

class F58LAzureBlue(bpy.types.Operator):
    """Ford Colors 1958 - L Azure Blue"""
    bl_label = "L Azure Blue"
    bl_idname = 'color.f58l_azure_blue'
    def execute(self, context):
        set_base_color(0x7aafd5, self.bl_label)
        return {'FINISHED'}

class F58MGulfstreamBlue(bpy.types.Operator):
    """Ford Colors 1958 - M Gulfstream Blue"""
    bl_label = "M Gulfstream Blue"
    bl_idname = 'color.f58m_gulfstream_blue'
    def execute(self, context):
        set_base_color(0x2b758c, self.bl_label)
        return {'FINISHED'}

class F58NSeasprayGreen(bpy.types.Operator):
    """Ford Colors 1958 - N Seaspray Green"""
    bl_label = "N Seaspray Green"
    bl_idname = 'color.f58n_seaspray_green'
    def execute(self, context):
        set_base_color(0xa0c78e, self.bl_label)
        return {'FINISHED'}

class F58RTorchRed(bpy.types.Operator):
    """Ford Colors 1958 - R Torch Red"""
    bl_label = "R Torch Red"
    bl_idname = 'color.f58r_torch_red'
    def execute(self, context):
        set_base_color(0x620800, self.bl_label)
        return {'FINISHED'}

class F58TSilvetoneBlue(bpy.types.Operator):
    """Ford Colors 1958 - T Silvetone Blue"""
    bl_label = "T Silvetone Blue"
    bl_idname = 'color.f58t_silvetone_blue'
    def execute(self, context):
        set_base_color(0x243b59, self.bl_label)
        return {'FINISHED'}


# BOOLEAN FOR PANEL
class F58_SETTINGS(bpy.types.PropertyGroup):
    rename_material_f: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )



# PARENT PANEL
class F58Panel(bpy.types.Panel):
    bl_idname = "F58_PT_Panel"
    bl_label = "Ford Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"

    def draw(self, context):
        layout = self.layout
        f_bool = context.scene.f_bool

        col = layout.column(align=True)
        col.prop(f_bool, "rename_material_f")



# FORD COLORS 1958 PANEL
class F58SubPanel(bpy.types.Panel):
    bl_idname = "F58_PT_Sub_Panel"
    bl_label = "1958"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'F58_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["f58a_raven_black"].icon_id)
        scol.label(text="", icon_value=c_icons["f58c_desert_beige"].icon_id)
        scol.label(text="", icon_value=c_icons["f58d_palamino_tan"].icon_id)
        scol.label(text="", icon_value=c_icons["f58e_colonial_white"].icon_id)
        scol.label(text="", icon_value=c_icons["f58f_silvertone_green"].icon_id)
        scol.label(text="", icon_value=c_icons["f58g_sun_gold"].icon_id)
        scol.label(text="", icon_value=c_icons["f58h_gunmetal_gray"].icon_id)
        scol.label(text="", icon_value=c_icons["f58j_bali_bronze"].icon_id)
        scol.label(text="", icon_value=c_icons["f58l_azure_blue"].icon_id)
        scol.label(text="", icon_value=c_icons["f58m_gulfstream_blue"].icon_id)
        scol.label(text="", icon_value=c_icons["f58n_seaspray_green"].icon_id)
        scol.label(text="", icon_value=c_icons["f58r_torch_red"].icon_id)
        scol.label(text="", icon_value=c_icons["f58t_silvetone_blue"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.f58a_raven_black", text="A Raven Black")
        scol.operator("color.f58c_desert_beige", text="C Desert Beige")
        scol.operator("color.f58d_palamino_tan", text="D Palamino Tan")
        scol.operator("color.f58e_colonial_white", text="E Colonial White")
        scol.operator("color.f58f_silvertone_green", text="F Silvertone Green")
        scol.operator("color.f58g_sun_gold", text="G Sun Gold")
        scol.operator("color.f58h_gunmetal_gray", text="H Gunmetal Gray")
        scol.operator("color.f58j_bali_bronze", text="J Bali Bronze")
        scol.operator("color.f58l_azure_blue", text="L Azure Blue")
        scol.operator("color.f58m_gulfstream_blue", text="M Gulfstream Blue")
        scol.operator("color.f58n_seaspray_green", text="N Seaspray Green")
        scol.operator("color.f58r_torch_red", text="R Torch Red")
        scol.operator("color.f58t_silvetone_blue", text="T Silvetone Blue")


classes = [
    F58_SETTINGS,
    F58Panel,
    F58SubPanel,
    F58ARavenBlack,
    F58CDesertBeige,
    F58DPalaminoTan,
    F58EColonialWhite,
    F58FSilvertoneGreen,
    F58GSunGold,
    F58HGunmetalGray,
    F58JBaliBronze,
    F58LAzureBlue,
    F58MGulfstreamBlue,
    F58NSeasprayGreen,
    F58RTorchRed,
    F58TSilvetoneBlue,
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
        bpy.types.Scene.f_bool = bpy.props.PointerProperty(type=F58_SETTINGS)


def unregister():
    # Addon updater unregister.
#    addon_updater_ops.unregister()
#   UNREGISTER ICONS
    global c_icons
    bpy.utils.previews.remove(c_icons)

    del bpy.types.Scene.f_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
