import bpy



# MESSAGE BOX

no_active = "No Compatable Shader Node Found"
no_bsdf = "No Principled BSDF Shader Found"
no_material = "No Compatable Material Found"
no_world = "No World Found"
no_world_bg = "World Background Shader Named \"Background\" Required"
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

def hex_to_rgb_sm(h):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)])



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
    "ShaderNodeSubsurfaceScattering",
    "ShaderNodeVolumeAbsorption",
    "ShaderNodeVolumePrincipled",
    "ShaderNodeVolumeScatter",
}



# COLOR SWITCHER

def set_base_color(hex, mat_name):
    material = bpy.context.object.active_material
    world = bpy.context.scene.world
    an_bool = bpy.context.scene.active_bool.active_node_more
    mat_bool = bpy.context.scene.more_bool.rename_material_more
    wor_bool = bpy.context.scene.world_bool.world_color_more

    if wor_bool == True:
        if world:
            world_name = world.name
            curr_world = bpy.data.worlds.get(world_name)
            world_bg = curr_world.node_tree.nodes.get("Background")
            if world_bg:
                world_bg.inputs[0].default_value = hex_to_rgb(hex)
                bpy.context.scene.world.color = hex_to_rgb_sm(hex)
                if mat_bool == True:
                    world.name = mat_name
            else:
                ShowMessageBox(no_world_bg, "Unable To Comply")
        else:
            ShowMessageBox(no_world, "Unable To Comply")
    else:
        if material:
            plaster = bpy.data.materials.get('QMM Plaster')
            AN = material.node_tree.nodes
            BSDF = material.node_tree.nodes.get('Principled BSDF')
            ColorRamp = material.node_tree.nodes.get('ColorRamp')
            D_BSDF = material.node_tree.nodes.get('Diffuse BSDF')
            RGB = material.node_tree.nodes.get('RGB')

            if an_bool == True:
                changed = False
                for n in AN:
                    if n.select and n.bl_idname in node_bl_idnames:
                        n.inputs[0].default_value = hex_to_rgb(hex)
                        material.diffuse_color = hex_to_rgb(hex)
                        changed = True
                if changed == False:
                    ShowMessageBox(no_active, "Unable To Comply")
            else:
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
        else:
            ShowMessageBox(no_material, "Unable To Comply")
    return {'FINISHED'}
