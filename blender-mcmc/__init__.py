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
    "name"       : "MCMC (Mid-Century Modern Colors)",
    "description": "Sets the Base Color of a Principled BSDF",
    "author"     : "Don Schnitzius",
    "version"    : (0, 5, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > Mid-Century Modern Colors",
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

class GINGER_ALE(bpy.types.Operator):
    """Apply Color Ginger Ale"""
    bl_label = "Ginger Ale"
    bl_idname = 'color.ginger_ale'
    def execute(self, context):
        set_base_color(0xefd079, self.bl_label)
        return {'FINISHED'}

class PABLO_HONEY(bpy.types.Operator):
    """Apply Color Pablo Honey"""
    bl_label = "Pablo Honey"
    bl_idname = 'color.pablo_honey'
    def execute(self, context):
        set_base_color(0xeac164, self.bl_label)
        return {'FINISHED'}

class MIAMI_PARASOL(bpy.types.Operator):
    """Apply Color Miami Parasol"""
    bl_label = "Miami Parasol"
    bl_idname = 'color.miami_parasol'
    def execute(self, context):
        set_base_color(0xf0d3a4, self.bl_label)
        return {'FINISHED'}

class TANLINES(bpy.types.Operator):
    """Apply Color Tanlines"""
    bl_label = "Tanlines"
    bl_idname = 'color.tanlines'
    def execute(self, context):
        set_base_color(0xc48c3f, self.bl_label)
        return {'FINISHED'}

class BLUE_SEAFOAM(bpy.types.Operator):
    """Apply Color Blue Seafoam"""
    bl_label = "Blue Seafoam"
    bl_idname = 'color.blue_seafoam'
    def execute(self, context):
        set_base_color(0xafe3e9, self.bl_label)
        return {'FINISHED'}

class SATURDAY_ON_SUNDAY(bpy.types.Operator):
    """Apply Color Saturday On Sunday"""
    bl_label = "Saturday On Sunday"
    bl_idname = 'color.saturday_on_sunday'
    def execute(self, context):
        set_base_color(0x567475, self.bl_label)
        return {'FINISHED'}

class SICILY_OR_CYPRUS(bpy.types.Operator):
    """Apply Color Sicily Or Cyprus"""
    bl_label = "Sicily Or Cyprus"
    bl_idname = 'color.sicily_or_cyprus'
    def execute(self, context):
        set_base_color(0x488182, self.bl_label)
        return {'FINISHED'}

class NOVELTY_WAVE(bpy.types.Operator):
    """Apply Color Novelty Wave"""
    bl_label = "Novelty Wave"
    bl_idname = 'color.novelty_wave'
    def execute(self, context):
        set_base_color(0x73969f, self.bl_label)
        return {'FINISHED'}

class RELENTLESS_OLIVE(bpy.types.Operator):
    """Apply Color Relentless Olive"""
    bl_label = "Relentless Olive"
    bl_idname = 'color.relentless_olive'
    def execute(self, context):
        set_base_color(0x71713e, self.bl_label)
        return {'FINISHED'}

class GREEN_ROOT(bpy.types.Operator):
    """Apply Color Green Root"""
    bl_label = "Green Root"
    bl_idname = 'color.green_root'
    def execute(self, context):
        set_base_color(0x848551, self.bl_label)
        return {'FINISHED'}

class SAGED(bpy.types.Operator):
    """Apply Color Saged"""
    bl_label = "Saged"
    bl_idname = 'color.saged'
    def execute(self, context):
        set_base_color(0x969684, self.bl_label)
        return {'FINISHED'}

class DRIVE_THRU_SAFARI(bpy.types.Operator):
    """Apply Color Drive-Thru Safari"""
    bl_label = "Drive-Thru Safari"
    bl_idname = 'color.drive_thru_safari'
    def execute(self, context):
        set_base_color(0x8b9d82, self.bl_label)
        return {'FINISHED'}

class NATURAL_HABITAT(bpy.types.Operator):
    """Apply Color Natural Habitat"""
    bl_label = "Natural Habitat"
    bl_idname = 'color.natural_habitat'
    def execute(self, context):
        set_base_color(0xc4c2a3, self.bl_label)
        return {'FINISHED'}

class CHEROKEE_RED(bpy.types.Operator):
    """Apply Color Cherokee Red"""
    bl_label = "Cherokee Red"
    bl_idname = 'color.cherokee_red'
    def execute(self, context):
        set_base_color(0x764139, self.bl_label)
        return {'FINISHED'}

class LIPSTICK_ON_THE_MIRROR(bpy.types.Operator):
    """Apply Color Lipstick on the Mirror"""
    bl_label = "Lipstick on the Mirror"
    bl_idname = 'color.lipstick_on_the_mirror'
    def execute(self, context):
        set_base_color(0xac2c3e, self.bl_label)
        return {'FINISHED'}

class SELF_PORTRAIT(bpy.types.Operator):
    """Apply Color Self-Portrait"""
    bl_label = "Self-Portrait"
    bl_idname = 'color.self_portrait'
    def execute(self, context):
        set_base_color(0x642c2f, self.bl_label)
        return {'FINISHED'}

class NEGRONI(bpy.types.Operator):
    """Apply Color Negroni"""
    bl_label = "Negroni"
    bl_idname = 'color.negroni'
    def execute(self, context):
        set_base_color(0xa53b33, self.bl_label)
        return {'FINISHED'}

class AUTUMN_GLIMMER(bpy.types.Operator):
    """Apply Color Autumn Glimmer"""
    bl_label = "Autumn Glimmer"
    bl_idname = 'color.autumn_glimmer'
    def execute(self, context):
        set_base_color(0xE97F4E, self.bl_label)
        return {'FINISHED'}

class ORANGE_FRUIT(bpy.types.Operator):
    """Apply Color Orange Fruit"""
    bl_label = "Orange Fruit"
    bl_idname = 'color.orange_fruit'
    def execute(self, context):
        set_base_color(0xf88f21, self.bl_label)
        return {'FINISHED'}

class APERITIVO_HOUR(bpy.types.Operator):
    """Apply Color Aperitivo Hour"""
    bl_label = "Aperitivo Hour"
    bl_idname = 'color.aperitivo_hour'
    def execute(self, context):
        set_base_color(0xe7a885, self.bl_label)
        return {'FINISHED'}

class BRIGHT_MARIGOLD(bpy.types.Operator):
    """Apply Color Bright Marigold"""
    bl_label = "Bright Marigold"
    bl_idname = 'color.bright_marigold'
    def execute(self, context):
        set_base_color(0xd78754, self.bl_label)
        return {'FINISHED'}

class WRIGHT_SOFT_GRAY(bpy.types.Operator):
    """Apply Color Wright Soft Gray"""
    bl_label = "Wright Soft Gray"
    bl_idname = 'color.wright_soft_gray'
    def execute(self, context):
        set_base_color(0x8e8fbf, self.bl_label)
        return {'FINISHED'}

class AFTER_HOURS(bpy.types.Operator):
    """Apply Color After Hours"""
    bl_label = "After Hours"
    bl_idname = 'color.after_hours'
    def execute(self, context):
        set_base_color(0x3c3b3e, self.bl_label)
        return {'FINISHED'}

class MOTOR_GRAY(bpy.types.Operator):
    """Apply Color Motor Gray"""
    bl_label = "Motor Gray"
    bl_idname = 'color.motor_gray'
    def execute(self, context):
        set_base_color(0x5c5d5f, self.bl_label)
        return {'FINISHED'}

class NO_CURFEW(bpy.types.Operator):
    """Apply Color No Curfew"""
    bl_label = "No Curfew"
    bl_idname = 'color.no_curfew'
    def execute(self, context):
        set_base_color(0x626669, self.bl_label)
        return {'FINISHED'}

class COCOA_SHELL(bpy.types.Operator):
    """Apply Color Cocoa Shell"""
    bl_label = "Cocoa Shell"
    bl_idname = 'color.cocoa_shell'
    def execute(self, context):
        set_base_color(0x7e6657, self.bl_label)
        return {'FINISHED'}

class FAWN_DOE(bpy.types.Operator):
    """Apply Color Fawn Doe"""
    bl_label = "Fawn Doe"
    bl_idname = 'color.fawn_doe'
    def execute(self, context):
        set_base_color(0xb5a99d, self.bl_label)
        return {'FINISHED'}

class SENTIMENTAL_REASONS(bpy.types.Operator):
    """Apply Color Sentimental Reasons"""
    bl_label = "Sentimental Reasons"
    bl_idname = 'color.sentimental_reasons'
    def execute(self, context):
        set_base_color(0xa29790, self.bl_label)
        return {'FINISHED'}

class COBBLESTONE_STREETS(bpy.types.Operator):
    """Apply Color Cobblestone Streets"""
    bl_label = "Cobblestone Streets"
    bl_idname = 'color.cobblestone_streets'
    def execute(self, context):
        set_base_color(0x918475, self.bl_label)
        return {'FINISHED'}



# BOOLEAN FOR PANEL
class MCMC_SETTINGS(bpy.types.PropertyGroup):
    rename_material_mcmc: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )



# PARENT PANEL
class MCMCPanel(bpy.types.Panel):
    bl_idname = "MCMC_PT_Panel"
    bl_label = "Mid-Century Modern Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"

    def draw(self, context):
        layout = self.layout
        mcmc_bool = context.scene.mcmc_bool

        row = layout.row()
        row.prop(mcmc_bool, "rename_material_mcmc")

# Golden Yellow
class YELLOWS(bpy.types.Panel):
    bl_idname = "YELLOWS_PT_Panel"
    bl_label = "Golden Yellow"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["yellow_01"].icon_id)
        scol.label(text="", icon_value=c_icons["yellow_02"].icon_id)
        scol.label(text="", icon_value=c_icons["yellow_03"].icon_id)
        scol.label(text="", icon_value=c_icons["yellow_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.miami_parasol", text="Miami Parasol")
        scol.operator("color.ginger_ale", text="Ginger Ale")
        scol.operator("color.pablo_honey", text="Pablo Honey")
        scol.operator("color.tanlines", text="Tanlines")

# Serena Aqua
class BLUES(bpy.types.Panel):
    bl_idname = "BLUES_PT_Panel"
    bl_label = "Serena Aqua"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["blue_01"].icon_id)
        scol.label(text="", icon_value=c_icons["blue_02"].icon_id)
        scol.label(text="", icon_value=c_icons["blue_03"].icon_id)
        scol.label(text="", icon_value=c_icons["blue_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.blue_seafoam", text="Blue Seafoam")
        scol.operator("color.novelty_wave", text="Novelty Wave")
        scol.operator("color.saturday_on_sunday", text="Saturday On Sunday")
        scol.operator("color.sicily_or_cyprus", text="Sicily Or Cyprus")

# Olive Green and Wasabi
class GREENS(bpy.types.Panel):
    bl_idname = "GREENS_PT_Panel"
    bl_label = "Olive Green & Wasabi"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["green_01"].icon_id)
        scol.label(text="", icon_value=c_icons["green_02"].icon_id)
        scol.label(text="", icon_value=c_icons["green_03"].icon_id)
        scol.label(text="", icon_value=c_icons["green_04"].icon_id)
        scol.label(text="", icon_value=c_icons["green_05"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.natural_habitat", text="Natural Habitat")
        scol.operator("color.saged", text="Saged")
        scol.operator("color.drive_thru_safari", text="Drive-Thru Safari")
        scol.operator("color.green_root", text="Green Root")
        scol.operator("color.relentless_olive", text="Relentless Olive")

# Pops of Red
class REDS(bpy.types.Panel):
    bl_idname = "REDS_PT_Panel"
    bl_label = "Pops of Red"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["red_01"].icon_id)
        scol.label(text="", icon_value=c_icons["red_02"].icon_id)
        scol.label(text="", icon_value=c_icons["red_03"].icon_id)
        scol.label(text="", icon_value=c_icons["red_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.cherokee_red", text="Cherokee Red")
        scol.operator("color.self_portrait", text="Self-Portrait")
        scol.operator("color.negroni", text="Negroni")
        scol.operator("color.lipstick_on_the_mirror", text="Lipstick on the Mirror")

# Tangerine and Ochre
class ORANGES(bpy.types.Panel):
    bl_idname = "ORANGES_PT_Panel"
    bl_label = "Tangerine and Ochre"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["orange_01"].icon_id)
        scol.label(text="", icon_value=c_icons["orange_02"].icon_id)
        scol.label(text="", icon_value=c_icons["orange_03"].icon_id)
        scol.label(text="", icon_value=c_icons["orange_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.aperitivo_hour", text="Aperitivo Hour")
        scol.operator("color.bright_marigold", text="Bright Marigold")
        scol.operator("color.autumn_glimmer", text="Autumn Glimmer")
        scol.operator("color.orange_fruit", text="Orange Fruit")

# Pewter Gray
class GRAYS(bpy.types.Panel):
    bl_idname = "GRAYS_PT_Panel"
    bl_label = "Pewter Gray"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["gray_01"].icon_id)
        scol.label(text="", icon_value=c_icons["gray_02"].icon_id)
        scol.label(text="", icon_value=c_icons["gray_03"].icon_id)
        scol.label(text="", icon_value=c_icons["gray_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.wright_soft_gray", text="Wright Soft Gray")
        scol.operator("color.no_curfew", text="No Curfew")
        scol.operator("color.motor_gray", text="Motor Gray")
        scol.operator("color.after_hours", text="After Hours")

# Soft and Earthy Brown
class BROWNS(bpy.types.Panel):
    bl_idname = "BROWNS_PT_Panel"
    bl_label = "Soft and Earthy Brown"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MCMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["brown_01"].icon_id)
        scol.label(text="", icon_value=c_icons["brown_02"].icon_id)
        scol.label(text="", icon_value=c_icons["brown_03"].icon_id)
        scol.label(text="", icon_value=c_icons["brown_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.fawn_doe", text="Fawn Doe")
        scol.operator("color.sentimental_reasons", text="Sentimental Reasons")
        scol.operator("color.cobblestone_streets", text="Cobblestone Streets")
        scol.operator("color.cocoa_shell", text="Cocoa Shell")


classes = [
    MCMC_SETTINGS,
    MCMCPanel,
    GINGER_ALE,
    PABLO_HONEY,
    MIAMI_PARASOL,
    TANLINES,
    BLUE_SEAFOAM,
    SATURDAY_ON_SUNDAY,
    SICILY_OR_CYPRUS,
    NOVELTY_WAVE,
    RELENTLESS_OLIVE,
    GREEN_ROOT,
    SAGED,
    DRIVE_THRU_SAFARI,
    NATURAL_HABITAT,
    CHEROKEE_RED,
    LIPSTICK_ON_THE_MIRROR,
    SELF_PORTRAIT,
    NEGRONI,
    AUTUMN_GLIMMER,
    ORANGE_FRUIT,
    APERITIVO_HOUR,
    BRIGHT_MARIGOLD,
    WRIGHT_SOFT_GRAY,
    AFTER_HOURS,
    MOTOR_GRAY,
    NO_CURFEW,
    COCOA_SHELL,
    FAWN_DOE,
    SENTIMENTAL_REASONS,
    COBBLESTONE_STREETS,
    YELLOWS,
    BLUES,
    GREENS,
    REDS,
    ORANGES,
    GRAYS,
    BROWNS
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
        bpy.types.Scene.mcmc_bool = bpy.props.PointerProperty(type=MCMC_SETTINGS)


def unregister():
    # Addon updater unregister.
#    addon_updater_ops.unregister()
#   UNREGISTER ICONS
    global c_icons
    bpy.utils.previews.remove(c_icons)

    del bpy.types.Scene.mcmc_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
