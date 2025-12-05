# Color Functions v.2.1
# Revised: 25-12-05

import bpy

# Constants
NO_ACTIVE = "No Compatible Node Found"
NO_BSDF = "No Principled BSDF Shader Found"
NO_MATERIAL = "No Compatible Material Found"
NO_WORLD = "No World Found"
NO_WORLD_BG = 'World Background Shader Named "Background" Required'
ENERGY_CONSERVATION = 'Energy Conservation'

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


# RECURSIVE NODE ITERATOR (SEARCH INSIDE GROUPS)


def iter_nodes_recursive(node_tree, include_groups=True, _visited=None):
    """Yield all nodes in a node tree, optionally diving into groups."""
    if not node_tree:
        return
    if _visited is None:
        _visited = set()
    if node_tree in _visited:
        return

    _visited.add(node_tree)

    for node in node_tree.nodes:
        yield node

        # Dive into groups if allowed
        if include_groups and node.bl_idname == "ShaderNodeGroup":
            sub_tree = getattr(node, "node_tree", None)
            if sub_tree:
                yield from iter_nodes_recursive(sub_tree, include_groups, _visited)


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


def get_first_node_by_bl_idname(nodes, bl_idname):
    """Return the first node whose bl_idname matches."""
    for node in nodes:
        if node.bl_idname == bl_idname:
            return node
    return None


def set_base_color(hex, mat_name):
    wor_bool = bpy.context.scene.qmc_settings.world_color_more

    if wor_bool:
        world = bpy.context.scene.world
        if world:
            world_name = world.name
            curr_world = bpy.data.worlds.get(world_name)
            world_bg = get_first_node_by_bl_idname(
                curr_world.node_tree.nodes,
                "ShaderNodeBackground",
            )
            if world_bg:
                set_input_color(world_bg, 0, hex)
                bpy.context.scene.world.color = hex_to_rgb(hex)
                set_mat_name(world, mat_name)
            else:
                show_message_box(NO_WORLD_BG, "Unable To Comply")
        else:
            show_message_box(NO_WORLD, "Unable To Comply")
    else:
        active_object = bpy.context.object

        if active_object:
            material = active_object.active_material
            if material:
                set_material(material, hex, mat_name)
            else:
                show_message_box(NO_MATERIAL, "Unable To Comply")
        else:
            show_message_box("No Active Object Found", "Unable To Comply")

    return {'FINISHED'}


def set_material(material, hex, mat_name):
    include_groups = not bpy.context.scene.qmc_settings.group_more
    
    nodes = material.node_tree.nodes
    all_nodes = list(iter_nodes_recursive(material.node_tree, include_groups))
    
    bsdf_node = None
    color_ramp_node = None
    d_bsdf_node = None
    em_node = None
    
    for n in all_nodes:
        if n.bl_idname == "ShaderNodeBsdfPrincipled":
            bsdf_node = n
        elif n.bl_idname == "ShaderNodeValToRGB":
            color_ramp_node = n
        elif n.bl_idname == "ShaderNodeBsdfDiffuse":
            d_bsdf_node = n
        elif n.bl_idname == "ShaderNodeEmission":
            em_node = n
            
    ec_node = nodes.get(ENERGY_CONSERVATION)
    plaster = bpy.data.materials.get('QMM Plaster')

    an_bool = bpy.context.scene.qmc_settings.active_node_more
    
    if an_bool:
        changed = False

        for n in iter_nodes_recursive(material.node_tree, include_groups):
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
    if bpy.context.scene.qmc_settings.diffuse_more:
        thing.diffuse_color = hex_to_rgb(hex)


def set_mat_name(thing, mat_name):
    if bpy.context.scene.qmc_settings.rename_material_more:
        thing.name = mat_name
