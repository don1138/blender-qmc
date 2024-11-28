# Color Functions v.2
# Revised: 24-08-11

import bpy

# Constants
NO_ACTIVE = "No Compatible Node Found"
NO_BSDF = "No Principled BSDF Shader Found"
NO_MATERIAL = "No Compatible Material Found"
NO_WORLD = "No World Found"
NO_WORLD_BG = 'World Background Shader Named "Background" Required'

PRINCIPLED_BSDF = 'Principled BSDF'
COLOR_RAMP = 'Color Ramp' if bpy.app.version >= (4, 0, 0) else 'ColorRamp'
BACKGROUND = 'Background'
ENERGY_CONSERVATION = 'Energy Conservation'
RGB = 'RGB'

# MESSAGE BOX


def show_message_box(message="", title="", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


# HEX TO RGB CALCS

def srgb_to_linearrgb(c):
    if c <= 0:
        return 0
    return c / 12.92 if c < 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def hex_to_rgb(h, alpha=1.0):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    rgb = tuple(srgb_to_linearrgb(c / 0xff) for c in (r, g, b))
    return rgb + (alpha,)


def set_input_color(node, num, hex):
    color = hex_to_rgb(hex)
    node.inputs[num].default_value = color


# SHADERS WITH BASE COLOR INPUTS

NODE_BL_IDNAMES = {
    "ShaderNodeAmbientOcclusion",
    "ShaderNodeBackground",
    "ShaderNodeBsdfAnisotropic",
    "ShaderNodeBsdfDiffuse",
    "ShaderNodeBsdfGlass",
    "ShaderNodeBsdfGlossy",
    "ShaderNodeBsdfHair",
    "ShaderNodeBsdfHairPrincipled",
    "ShaderNodeBsdfMetallic",
    "ShaderNodeBsdfPrincipled",
    "ShaderNodeBsdfRayPortal",
    "ShaderNodeBsdfRefraction",
    "ShaderNodeBsdfSheen",
    "ShaderNodeBsdfToon",
    "ShaderNodeBsdfTranslucent",
    "ShaderNodeBsdfTransparent",
    "ShaderNodeBsdfVelvet",
    "ShaderNodeEmission",
    "ShaderNodeRGB",
    "ShaderNodeSubsurfaceScattering",
    "ShaderNodeVolumeAbsorption",
    "ShaderNodeVolumePrincipled",
    "ShaderNodeVolumeScatter",
}


# COLOR SWITCHER

def set_base_color(hex, mat_name):
    wor_bool = bpy.context.scene.world_bool.world_color_more

    if wor_bool:
        world = bpy.context.scene.world
        if world:
            world_name = world.name
            curr_world = bpy.data.worlds.get(world_name)
            world_bg = curr_world.node_tree.nodes.get(BACKGROUND)
            if world_bg:
                set_input_color(world_bg, 0, hex)
                bpy.context.scene.world.color = hex_to_rgb(hex)
                set_mat_name(world, mat_name)
            else:
                show_message_box(NO_WORLD_BG, "Unable To Comply")
        else:
            show_message_box(NO_WORLD, "Unable To Comply")
    else:
        material = bpy.context.object.active_material
        if material:
            set_material(material, hex, mat_name)
        else:
            show_message_box(NO_MATERIAL, "Unable To Comply")

    return {'FINISHED'}


def set_material(material, hex, mat_name):
    nodes = material.node_tree.nodes
    bsdf_node = nodes.get(PRINCIPLED_BSDF)
    color_ramp_node = nodes.get(COLOR_RAMP)
    d_bsdf_node = nodes.get('Diffuse BSDF')
    ec_node = nodes.get(ENERGY_CONSERVATION)
    em_node = nodes.get('Emission')
    plaster = bpy.data.materials.get('QMM Plaster')

    an_bool = bpy.context.scene.active_bool.active_node_more
    if an_bool:
        changed = False
        for n in nodes:
            if n.select and n.bl_idname in NODE_BL_IDNAMES:
                if n.bl_idname == 'ShaderNodeRGB':
                    n.outputs[0].default_value = hex_to_rgb(hex)
                else:
                    set_input_color(n, 0, hex)
                set_dif_color(material, hex)
                set_mat_name(material, mat_name)
                changed = True
                if n.name == ENERGY_CONSERVATION:
                    set_input_color(n, 0, hex)
        if not changed:
            show_message_box(NO_ACTIVE, "Unable To Comply")
    elif material == plaster:
        color_ramp_node.color_ramp.elements[0].color = hex_to_rgb(hex)
        set_input_color(bsdf_node, 3 if bpy.app.version <
                        (4, 0, 0) else 0, hex)
        set_dif_color(material, hex)
    elif bsdf_node:
        set_bsdf(bsdf_node, hex, material, mat_name)
        if ec_node:
            set_input_color(ec_node, 0, hex)
    elif d_bsdf_node:
        set_bsdf(d_bsdf_node, hex, material, mat_name)
    elif em_node:
        set_bsdf(em_node, hex, material, mat_name)
    else:
        show_message_box(NO_BSDF, "Unable To Comply")


def set_bsdf(node, hex, material, mat_name):
    set_dif_color(material, hex)
    set_input_color(node, 0, hex)
    set_mat_name(material, mat_name)


def set_dif_color(thing, hex):
    if bpy.context.scene.diffuse_bool.diffuse_more:
        thing.diffuse_color = hex_to_rgb(hex)


def set_input_color(node, num, hex):
    node.inputs[num].default_value = hex_to_rgb(hex)


def set_mat_name(thing, mat_name):
    if bpy.context.scene.more_bool.rename_material_more:
        thing.name = mat_name
