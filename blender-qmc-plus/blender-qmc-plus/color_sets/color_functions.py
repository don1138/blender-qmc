import bpy


# MESSAGE BOX

no_active = "No Compatable Node Found"
no_bsdf = "No Principled BSDF Shader Found"
no_material = "No Compatable Material Found"
no_world = "No World Found"
no_world_bg = "World Background Shader Named \"Background\" Required"


def ShowMessageBox(message="", title="", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


# HEX TO RGB CALCS

def srgb_to_linearrgb(c):
    if c < 0:
        return 0
    elif c < 0.04045:
        return c/12.92
    else:
        return ((c+0.055)/1.055)**2.4


def hex_to_rgb(h, alpha=1):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r, g, b)] + [alpha])


def hex_to_rgb_sm(h):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple(srgb_to_linearrgb(c/0xff) for c in (r, g, b))


# SHADERS WITH BASE COLOR INPUTS

node_bl_idnames = {
    "ShaderNodeBackground",
    "ShaderNodeBsdfAnisotropic",
    "ShaderNodeBsdfDiffuse",
    "ShaderNodeBsdfGlass",
    "ShaderNodeBsdfGlossy",
    "ShaderNodeBsdfHair",
    "ShaderNodeBsdfHairPrincipled",
    "ShaderNodeBsdfPrincipled",
    "ShaderNodeBsdfRefraction",
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

    if wor_bool == True:
        if world := bpy.context.scene.world:
            world_name = world.name
            curr_world = bpy.data.worlds.get(world_name)
            if world_bg := curr_world.node_tree.nodes.get("Background"):
                set_input_color(world_bg, 0, hex)
                bpy.context.scene.world.color = hex_to_rgb_sm(hex)
                set_mat_name(world, mat_name)
            else:
                ShowMessageBox(no_world_bg, "Unable To Comply")
        else:
            ShowMessageBox(no_world, "Unable To Comply")
    elif material := bpy.context.object.active_material:
        set_material(material, hex, mat_name)
    else:
        ShowMessageBox(no_material, "Unable To Comply")
    return {'FINISHED'}


def set_material(material, hex, mat_name):
    AN = material.node_tree.nodes
    BSDF = material.node_tree.nodes.get('Principled BSDF')
    if bpy.app.version < (4, 0, 0):
        ColorRamp = material.node_tree.nodes.get('ColorRamp')
    else:
        ColorRamp = material.node_tree.nodes.get('Color Ramp')
    D_BSDF = material.node_tree.nodes.get('Diffuse BSDF')
    EC = material.node_tree.nodes.get('Energy Conservation')
    EM = material.node_tree.nodes.get('Emission')
    Plaster = bpy.data.materials.get('QMM Plaster')
    RGB = material.node_tree.nodes.get('RGB')

    an_bool = bpy.context.scene.active_bool.active_node_more
    if an_bool == True:
        changed = False
        for n in AN:
            if n.select:
                if n.bl_idname in node_bl_idnames:
                    if n.bl_idname == 'ShaderNodeRGB':
                        n.outputs[0].default_value = hex_to_rgb(hex)
                    else:
                        set_input_color(n, 0, hex)
                    set_dif_color(material, hex)
                    set_mat_name(material, mat_name)
                    changed = True
                if n.name == 'Energy Conservation':
                    set_input_color(n, 0, hex)
                    changed = True
        if changed == False:
            ShowMessageBox(no_active, "Unable To Comply")
    elif material == Plaster:
        ColorRamp.color_ramp.elements[0].color = hex_to_rgb(hex)
        if bpy.app.version < (4, 0, 0):
            set_input_color(BSDF, 3, hex)
        else:
            set_input_color(BSDF, 0, hex)
        # set_input_color(RGB, 0, hex)
        set_dif_color(material, hex)
    elif BSDF:
        set_bsdf(BSDF, hex, material, mat_name)
        if EC:
            set_input_color(EC, 0, hex)
    elif D_BSDF:
        set_bsdf(D_BSDF, hex, material, mat_name)
    elif EM:
        set_bsdf(EM, hex, material, mat_name)
    else:
        ShowMessageBox(no_bsdf, "Unable To Comply")


def set_bsdf(name, hex, material, mat_name):
    set_dif_color(material, hex)
    set_input_color(name, 0, hex)
    set_mat_name(material, mat_name)


def set_dif_color(thing, hex):
    thing.diffuse_color = hex_to_rgb(hex)


def set_input_color(node, num, hex):
    node.inputs[num].default_value = hex_to_rgb(hex)


def set_mat_name(thing, mat_name):
    mat_bool = bpy.context.scene.more_bool.rename_material_more
    if mat_bool == True:
        thing.name = mat_name
