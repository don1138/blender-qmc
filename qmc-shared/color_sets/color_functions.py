# Color Functions v.2.0.2
# Revised: 26-07-14

import bpy

# Messages
NO_ACTIVE = "No Compatible Selected Node Found"
NO_ACTIVE_OBJECT = "No Active Object Found"
NO_BSDF = "No Compatible Shader Node Found"
NO_MATERIAL = "No Compatible Material Found"
NO_WORLD = "No World Found"
NO_WORLD_BG = "No World Background Shader Found"

ENERGY_CONSERVATION = "Energy Conservation"


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
    b = h & 0x0000ff
    rgb = tuple(srgb_to_linearrgb(c / 0xff) for c in (r, g, b))
    return rgb + (alpha,)


def set_input_color(node, num, hex_value):
    node.inputs[num].default_value = hex_to_rgb(hex_value)


# NODE HELPERS

def get_first_node_by_bl_idname(nodes, bl_idname):
    for node in nodes:
        if node.bl_idname == bl_idname:
            return node
    return None


# SELECTED NODE COLOR HELPERS

def is_writable_color_socket(socket):
    """Return True for an enabled, unlinked RGBA input socket."""
    return (
        getattr(socket, "enabled", True)
        and not getattr(socket, "is_linked", False)
        and getattr(socket, "type", None) == 'RGBA'
        and hasattr(socket, "default_value")
    )


def set_socket_color(socket, hex_value):
    try:
        socket.default_value = hex_to_rgb(hex_value)
        return True
    except (AttributeError, TypeError, ValueError):
        return False


def set_selected_node_color(node, hex_value):
    """Set the most appropriate color value on one selected node."""

    # The RGB node stores its color on an output socket.
    if node.bl_idname == "ShaderNodeRGB":
        try:
            node.outputs[0].default_value = hex_to_rgb(hex_value)
            return True
        except (AttributeError, IndexError, TypeError, ValueError):
            return False

    color_inputs = [
        socket for socket in node.inputs
        if is_writable_color_socket(socket)
    ]

    if not color_inputs:
        return False

    # Mix nodes preserve A and replace B by extension convention.
    if node.bl_idname in {"ShaderNodeMix", "ShaderNodeMixRGB"}:
        preferred_names = {"B", "Color2"}

        for socket in color_inputs:
            if socket.name in preferred_names:
                return set_socket_color(socket, hex_value)

        # Socket names can vary between Blender releases. The second
        # available color input is the safest fallback for Mix nodes.
        if len(color_inputs) > 1:
            return set_socket_color(color_inputs[1], hex_value)

    # All other supported nodes use their first writable color input.
    return set_socket_color(color_inputs[0], hex_value)


# COLOR SWITCHER

def set_base_color(hex_value, mat_name):
    world_mode = bpy.context.scene.world_bool.world_color_more

    if world_mode:
        world = bpy.context.scene.world

        if world is None:
            show_message_box(NO_WORLD, "Unable To Comply")
            return {'FINISHED'}

        if not world.use_nodes or world.node_tree is None:
            show_message_box(NO_WORLD_BG, "Unable To Comply")
            return {'FINISHED'}

        world_bg = get_first_node_by_bl_idname(
            world.node_tree.nodes,
            "ShaderNodeBackground",
        )

        if world_bg is None:
            show_message_box(NO_WORLD_BG, "Unable To Comply")
            return {'FINISHED'}

        set_input_color(world_bg, 0, hex_value)
        world.color = hex_to_rgb(hex_value)[:3]
        set_mat_name(world, mat_name)
        return {'FINISHED'}

    active_object = bpy.context.active_object

    if active_object is None:
        show_message_box(NO_ACTIVE_OBJECT, "Unable To Comply")
        return {'FINISHED'}

    material = getattr(active_object, "active_material", None)

    if material is None:
        show_message_box(NO_MATERIAL, "Unable To Comply")
        return {'FINISHED'}

    set_material(material, hex_value, mat_name)
    return {'FINISHED'}


def set_material(material, hex_value, mat_name):
    if not material.use_nodes or material.node_tree is None:
        show_message_box(NO_BSDF, "Unable To Comply")
        return

    nodes = material.node_tree.nodes

    bsdf_node = get_first_node_by_bl_idname(
        nodes,
        "ShaderNodeBsdfPrincipled",
    )
    color_ramp_node = get_first_node_by_bl_idname(
        nodes,
        "ShaderNodeValToRGB",
    )
    diffuse_bsdf_node = get_first_node_by_bl_idname(
        nodes,
        "ShaderNodeBsdfDiffuse",
    )
    emission_node = get_first_node_by_bl_idname(
        nodes,
        "ShaderNodeEmission",
    )
    energy_conservation_node = nodes.get(ENERGY_CONSERVATION)
    plaster = bpy.data.materials.get("QMM Plaster")

    selected_nodes_only = bpy.context.scene.active_bool.active_node_more

    if selected_nodes_only:
        changed = False

        for node in nodes:
            if not node.select:
                continue

            node_changed = set_selected_node_color(node, hex_value)

            if node.name == ENERGY_CONSERVATION:
                try:
                    set_input_color(node, 0, hex_value)
                    node_changed = True
                except (AttributeError, IndexError, TypeError, ValueError):
                    pass

            changed = node_changed or changed

        if changed:
            set_dif_color(material, hex_value)
            set_mat_name(material, mat_name)
        else:
            show_message_box(NO_ACTIVE, "Unable To Comply")

    elif material == plaster:
        if color_ramp_node is None or bsdf_node is None:
            show_message_box(NO_BSDF, "Unable To Comply")
            return

        color_ramp_node.color_ramp.elements[0].color = hex_to_rgb(hex_value)
        set_input_color(bsdf_node, 0, hex_value)
        set_dif_color(material, hex_value)
        set_mat_name(material, mat_name)

    elif bsdf_node:
        set_bsdf(bsdf_node, hex_value, material, mat_name)

        if energy_conservation_node:
            set_input_color(energy_conservation_node, 0, hex_value)

    elif diffuse_bsdf_node:
        set_bsdf(diffuse_bsdf_node, hex_value, material, mat_name)

    elif emission_node:
        set_bsdf(emission_node, hex_value, material, mat_name)

    else:
        show_message_box(NO_BSDF, "Unable To Comply")


def set_bsdf(node, hex_value, material, mat_name):
    set_dif_color(material, hex_value)
    set_input_color(node, 0, hex_value)
    set_mat_name(material, mat_name)


def set_dif_color(thing, hex_value):
    if bpy.context.scene.diffuse_bool.diffuse_more:
        thing.diffuse_color = hex_to_rgb(hex_value)


def set_mat_name(thing, mat_name):
    if bpy.context.scene.more_bool.rename_material_more:
        thing.name = mat_name
