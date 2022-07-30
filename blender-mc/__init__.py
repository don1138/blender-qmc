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
    "name"       : "More Colors (Ford, GE, Lick, Sherwin Williams)",
    "description": "Sets the Base Color of a Principled BSDF",
    "author"     : "Don Schnitzius",
    "version"    : (0, 9, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > More Colors",
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
        mat_bool = bpy.context.scene.more_bool.rename_material_more
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

# SHERWIN WILLIAMS - INTERIOR

class SMAppleBlossom(bpy.types.Operator):
    """Suburban Modern Apple Blossom"""
    bl_label = "Apple Blossom"
    bl_idname = 'color.sm_appleblossom'
    def execute(self, context):
        set_base_color(0xdab5b4, self.bl_label)
        return {'FINISHED'}

class SMAvocado(bpy.types.Operator):
    """Suburban Modern Avocado"""
    bl_label = "Avocado"
    bl_idname = 'color.sm_avocado'
    def execute(self, context):
        set_base_color(0x857c5d, self.bl_label)
        return {'FINISHED'}

class SMBeige(bpy.types.Operator):
    """Suburban Modern Beige"""
    bl_label = "Beige"
    bl_idname = 'color.sm_beige'
    def execute(self, context):
        set_base_color(0xdfc8b5, self.bl_label)
        return {'FINISHED'}

class SMCaribbeanCoral(bpy.types.Operator):
    """Suburban Modern Caribbean Coral"""
    bl_label = "Caribbean Coral"
    bl_idname = 'color.sm_caribbean_coral'
    def execute(self, context):
        set_base_color(0xbe795e, self.bl_label)
        return {'FINISHED'}

class SMChartreuse(bpy.types.Operator):
    """Suburban Modern Chartreuse"""
    bl_label = "Chartreuse"
    bl_idname = 'color.sm_chartreuse'
    def execute(self, context):
        set_base_color(0xe1d286, self.bl_label)
        return {'FINISHED'}

class SMChelseaGray(bpy.types.Operator):
    """Suburban Modern Chelsea Gray"""
    bl_label = "Chelsea Gray"
    bl_idname = 'color.sm_chelsea_gray'
    def execute(self, context):
        set_base_color(0xb6b7b0, self.bl_label)
        return {'FINISHED'}

class SMClassicFrenchGray(bpy.types.Operator):
    """Suburban Modern Classic French Gray"""
    bl_label = "Classic French Gray"
    bl_idname = 'color.sm_classic_french_gray'
    def execute(self, context):
        set_base_color(0x888782, self.bl_label)
        return {'FINISHED'}

class SMFairfaxBrown(bpy.types.Operator):
    """Suburban Modern Fairfax Brown"""
    bl_label = "Fairfax Brown"
    bl_idname = 'color.sm_fairfax_brown'
    def execute(self, context):
        set_base_color(0x61463a, self.bl_label)
        return {'FINISHED'}

class SMHarvestGold(bpy.types.Operator):
    """Suburban Modern Harvest Gold"""
    bl_label = "Harvest Gold"
    bl_idname = 'color.sm_harvest_gold'
    def execute(self, context):
        set_base_color(0xd9a06a, self.bl_label)
        return {'FINISHED'}

class SMHolidayTurquoise(bpy.types.Operator):
    """Suburban Modern Holiday Turquoise"""
    bl_label = "Holiday Turquoise"
    bl_idname = 'color.sm_holiday_turquoise'
    def execute(self, context):
        set_base_color(0x8ac6bd, self.bl_label)
        return {'FINISHED'}

class SMNewColonialYellow(bpy.types.Operator):
    """Suburban Modern New Colonial Yellow"""
    bl_label = "New Colonial Yellow"
    bl_idname = 'color.sm_new_colonial_yellow'
    def execute(self, context):
        set_base_color(0xe1bd99, self.bl_label)
        return {'FINISHED'}

class SMPeaceYellow(bpy.types.Operator):
    """Suburban Modern Peace Yellow"""
    bl_label = "Peace Yellow"
    bl_idname = 'color.sm_peace_yellow'
    def execute(self, context):
        set_base_color(0xeecf9e, self.bl_label)
        return {'FINISHED'}

class SMPinkFlamingo(bpy.types.Operator):
    """Suburban Modern Pink Flamingo"""
    bl_label = "Pink Flamingo"
    bl_idname = 'color.sm_pink_flamingo'
    def execute(self, context):
        set_base_color(0xcd717b, self.bl_label)
        return {'FINISHED'}

class SMPinkyBeige(bpy.types.Operator):
    """Suburban Modern Pinky Beige"""
    bl_label = "Pinky Beige"
    bl_idname = 'color.sm_pinky_beige'
    def execute(self, context):
        set_base_color(0xc9aa98, self.bl_label)
        return {'FINISHED'}

class SMPowderBlu(bpy.types.Operator):
    """Suburban Modern Powder Blu"""
    bl_label = "Powder Blu"
    bl_idname = 'color.sm_powder_blu'
    def execute(self, context):
        set_base_color(0x89a4ad, self.bl_label)
        return {'FINISHED'}

class SMRadiantLilac(bpy.types.Operator):
    """Suburban Modern Radiant Lilac"""
    bl_label = "Radiant Lilac"
    bl_idname = 'color.sm_radiant_lilac'
    def execute(self, context):
        set_base_color(0xa489a0, self.bl_label)
        return {'FINISHED'}

class SMSage(bpy.types.Operator):
    """Suburban Modern Sage"""
    bl_label = "Sage"
    bl_idname = 'color.sm_sage'
    def execute(self, context):
        set_base_color(0xb3ae95, self.bl_label)
        return {'FINISHED'}

class SMSageGreenLight(bpy.types.Operator):
    """Suburban Modern Sage Green Light"""
    bl_label = "Sage Green Light"
    bl_idname = 'color.sm_sage_green_light'
    def execute(self, context):
        set_base_color(0x73705e, self.bl_label)
        return {'FINISHED'}

class SMSunbeamYellow(bpy.types.Operator):
    """Suburban Modern Sunbeam Yellow"""
    bl_label = "Sunbeam Yellow"
    bl_idname = 'color.sm_sunbeam_yellow'
    def execute(self, context):
        set_base_color(0xf0d39d, self.bl_label)
        return {'FINISHED'}

class SMSycamoreTan(bpy.types.Operator):
    """Suburban Modern Sycamore Tan"""
    bl_label = "Sycamore Tan"
    bl_idname = 'color.sm_sycamore_tan'
    def execute(self, context):
        set_base_color(0x9c8a79, self.bl_label)
        return {'FINISHED'}

class SMWestchesterGray(bpy.types.Operator):
    """Suburban Modern Westchester Gray"""
    bl_label = "Westchester Gray"
    bl_idname = 'color.sm_westchester_gray'
    def execute(self, context):
        set_base_color(0x797978, self.bl_label)
        return {'FINISHED'}

# SHERWIN WILLIAMS - EXTERIOR

# class SMBirdseyeMaple(bpy.types.Operator):
#     """Suburban Modern Birdseye Maple"""
#     bl_label = "Birdseye Maple"
#     bl_idname = 'color.sm_birdseye_maple'
#     def execute(self, context):
#         set_base_color(0xe4c495, self.bl_label)
#         return {'FINISHED'}

# class SMCocoon(bpy.types.Operator):
#     """Suburban Modern Cocoon"""
#     bl_label = "Cocoon"
#     bl_idname = 'color.sm_cocoon'
#     def execute(self, context):
#         set_base_color(0x726b5b, self.bl_label)
#         return {'FINISHED'}

# class SMOldeWorldGold(bpy.types.Operator):
#     """Suburban Modern Olde World Gold"""
#     bl_label = "Olde World Gold"
#     bl_idname = 'color.sm_olde_world_gold'
#     def execute(self, context):
#         set_base_color(0x8f6c3e, self.bl_label)
#         return {'FINISHED'}

# class SMWoolSkein(bpy.types.Operator):
#     """Suburban Modern Wool Skein"""
#     bl_label = "Wool Skein"
#     bl_idname = 'color.sm_wool_skein'
#     def execute(self, context):
#         set_base_color(0xd9cfba, self.bl_label)
#         return {'FINISHED'}

# class SMArtisanTan(bpy.types.Operator):
#     """Suburban Modern Artisan Tan"""
#     bl_label = "Artisan Tan"
#     bl_idname = 'color.sm_artisan_tan'
#     def execute(self, context):
#         set_base_color(0xb09879, self.bl_label)
#         return {'FINISHED'}

# class SMStatusBronze(bpy.types.Operator):
#     """Suburban Modern Status Bronze"""
#     bl_label = "Status Bronze"
#     bl_idname = 'color.sm_status_bronze'
#     def execute(self, context):
#         set_base_color(0x5c4d3c, self.bl_label)
#         return {'FINISHED'}

# class SMTatamiTan(bpy.types.Operator):
#     """Suburban Modern Tatami Tan"""
#     bl_label = "Tatami Tan"
#     bl_idname = 'color.sm_tatami_tan'
#     def execute(self, context):
#         set_base_color(0xba8c64, self.bl_label)
#         return {'FINISHED'}

# class SMColonyBuff(bpy.types.Operator):
#     """Suburban Modern Colony Buff"""
#     bl_label = "Colony Buff"
#     bl_idname = 'color.sm_colony_buff'
#     def execute(self, context):
#         set_base_color(0xddc6ab, self.bl_label)
#         return {'FINISHED'}

# class SMHomburgGray(bpy.types.Operator):
#     """Suburban Modern Homburg Gray"""
#     bl_label = "Homburg Gray"
#     bl_idname = 'color.sm_homburg_gray'
#     def execute(self, context):
#         set_base_color(0x666d69, self.bl_label)
#         return {'FINISHED'}

# class SMMuslin(bpy.types.Operator):
#     """Suburban Modern Muslin"""
#     bl_label = "Muslin"
#     bl_idname = 'color.sm_muslin'
#     def execute(self, context):
#         set_base_color(0xeadfc9, self.bl_label)
#         return {'FINISHED'}

# class SMStrawHarvest(bpy.types.Operator):
#     """Suburban Modern Straw Harvest"""
#     bl_label = "Straw Harvest"
#     bl_idname = 'color.sm_straw_harvest'
#     def execute(self, context):
#         set_base_color(0xdbc8a2, self.bl_label)
#         return {'FINISHED'}

# class SMRuralGreen(bpy.types.Operator):
#     """Suburban Modern Rural Green"""
#     bl_label = "Rural Green"
#     bl_idname = 'color.sm_rural_green'
#     def execute(self, context):
#         set_base_color(0x8d844d, self.bl_label)
#         return {'FINISHED'}

# class SMExtraWhite(bpy.types.Operator):
#     """Suburban Modern Extra White"""
#     bl_label = "Extra White"
#     bl_idname = 'color.sm_extra_white'
#     def execute(self, context):
#         set_base_color(0xeeefea, self.bl_label)
#         return {'FINISHED'}

# class SMRushingRiver(bpy.types.Operator):
#     """Suburban Modern Rushing River"""
#     bl_label = "Rushing River"
#     bl_idname = 'color.sm_rushing_river'
#     def execute(self, context):
#         set_base_color(0xa19c8f, self.bl_label)
#         return {'FINISHED'}

# class SMSpicedCider(bpy.types.Operator):
#     """Suburban Modern Spiced Cider"""
#     bl_label = "Spiced Cider"
#     bl_idname = 'color.sm_spiced_cider'
#     def execute(self, context):
#         set_base_color(0xb0785c, self.bl_label)
#         return {'FINISHED'}

# class SMRetreat(bpy.types.Operator):
#     """Suburban Modern Retreat"""
#     bl_label = "Retreat"
#     bl_idname = 'color.sm_retreat'
#     def execute(self, context):
#         set_base_color(0x7a8076, self.bl_label)
#         return {'FINISHED'}

# class SMNetsuke(bpy.types.Operator):
#     """Suburban Modern Netsuke"""
#     bl_label = "Netsuke"
#     bl_idname = 'color.sm_netsuke'
#     def execute(self, context):
#         set_base_color(0xe0cfb0, self.bl_label)
#         return {'FINISHED'}

# class SMEdgyGold(bpy.types.Operator):
#     """Suburban Modern Edgy Gold"""
#     bl_label = "Edgy Gold"
#     bl_idname = 'color.sm_edgy_gold'
#     def execute(self, context):
#         set_base_color(0xb1975f, self.bl_label)
#         return {'FINISHED'}

# class SMJoggingPath(bpy.types.Operator):
#     """Suburban Modern Jogging Path"""
#     bl_label = "Jogging Path"
#     bl_idname = 'color.sm_jogging_path'
#     def execute(self, context):
#         set_base_color(0xc0b9a9, self.bl_label)
#         return {'FINISHED'}

# class SMIntellectualGray(bpy.types.Operator):
#     """Suburban Modern Intellectual Gray"""
#     bl_label = "Intellectual Gray"
#     bl_idname = 'color.sm_intellectual_gray'
#     def execute(self, context):
#         set_base_color(0xa8a093, self.bl_label)
#         return {'FINISHED'}

# class SMThunderGray(bpy.types.Operator):
#     """Suburban Modern Thunder Gray"""
#     bl_label = "Thunder Gray"
#     bl_idname = 'color.sm_thunder_gray'
#     def execute(self, context):
#         set_base_color(0x57534c, self.bl_label)
#         return {'FINISHED'}

# class SMAnjouPear(bpy.types.Operator):
#     """Suburban Modern Anjou Pear"""
#     bl_label = "Anjou Pear"
#     bl_idname = 'color.sm_anjou_pear'
#     def execute(self, context):
#         set_base_color(0xddac6d, self.bl_label)
#         return {'FINISHED'}

# class SMJerseyCream(bpy.types.Operator):
#     """Suburban Modern Jersey Cream"""
#     bl_label = "Jersey Cream"
#     bl_idname = 'color.sm_jersey_cream'
#     def execute(self, context):
#         set_base_color(0xf5debb, self.bl_label)
#         return {'FINISHED'}

# class SMWarmStone(bpy.types.Operator):
#     """Suburban Modern Warm Stone"""
#     bl_label = "Warm Stone"
#     bl_idname = 'color.sm_warm_stone'
#     def execute(self, context):
#         set_base_color(0x887b6c, self.bl_label)
#         return {'FINISHED'}

# class SMCorkWedge(bpy.types.Operator):
#     """Suburban Modern Cork Wedge"""
#     bl_label = "Cork Wedge"
#     bl_idname = 'color.sm_cork_wedge'
#     def execute(self, context):
#         set_base_color(0xc1a98a, self.bl_label)
#         return {'FINISHED'}

# class SMSmokehouse(bpy.types.Operator):
#     """Suburban Modern Smokehouse"""
#     bl_label = "Smokehouse"
#     bl_idname = 'color.sm_smokehouse'
#     def execute(self, context):
#         set_base_color(0x716354, self.bl_label)
#         return {'FINISHED'}

# class SMRusticRed(bpy.types.Operator):
#     """Suburban Modern Rustic Red"""
#     bl_label = "Rustic Red"
#     bl_idname = 'color.sm_rustic_red'
#     def execute(self, context):
#         set_base_color(0x703229, self.bl_label)
#         return {'FINISHED'}

# SHERWIN WILLIAMS - THE JAZZ AGE

class JAChineseRed(bpy.types.Operator):
    """Jazz Age Chinese Red"""
    bl_label = "Chinese Red"
    bl_idname = 'color.ja_chinese_red'
    def execute(self, context):
        set_base_color(0x9e3e33, self.bl_label)
        return {'FINISHED'}

class JAJazzAgeCoral(bpy.types.Operator):
    """Jazz Age Jazz Age Coral"""
    bl_label = "Jazz Age Coral"
    bl_idname = 'color.ja_jazz_age_coral'
    def execute(self, context):
        set_base_color(0xf1bfb1, self.bl_label)
        return {'FINISHED'}

class JAFrostwork(bpy.types.Operator):
    """Jazz Age Frostwork"""
    bl_label = "Frostwork"
    bl_idname = 'color.ja_frostwork'
    def execute(self, context):
        set_base_color(0xcbd0c2, self.bl_label)
        return {'FINISHED'}

class JAAlexandrite(bpy.types.Operator):
    """Jazz Age Alexandrite"""
    bl_label = "Alexandrite"
    bl_idname = 'color.ja_alexandrite'
    def execute(self, context):
        set_base_color(0x598c74, self.bl_label)
        return {'FINISHED'}

class JASalonRose(bpy.types.Operator):
    """Jazz Age Salon Rose"""
    bl_label = "Salon Rose"
    bl_idname = 'color.ja_salon_rose'
    def execute(self, context):
        set_base_color(0xab7878, self.bl_label)
        return {'FINISHED'}

class JAStudioMauve(bpy.types.Operator):
    """Jazz Age Studio Mauve"""
    bl_label = "Studio Mauve"
    bl_idname = 'color.ja_studio_mauve'
    def execute(self, context):
        set_base_color(0xc6b9b8, self.bl_label)
        return {'FINISHED'}

class JABlueSky(bpy.types.Operator):
    """Jazz Age Blue Sky"""
    bl_label = "Blue Sky"
    bl_idname = 'color.ja_blue_sky'
    def execute(self, context):
        set_base_color(0xabd1c9, self.bl_label)
        return {'FINISHED'}

class JABluePeacock(bpy.types.Operator):
    """Jazz Age Blue Peacock"""
    bl_label = "Blue Peacock"
    bl_idname = 'color.ja_blue_peacock'
    def execute(self, context):
        set_base_color(0x014e4c, self.bl_label)
        return {'FINISHED'}

# GENERAL ELECTRIC 1960S APPLIANCES

class GECoppertoneA(bpy.types.Operator):
    """General Electric Coppertone A"""
    bl_label = "Coppertone A"
    bl_idname = 'color.ge_coppertone_a'
    def execute(self, context):
        set_base_color(0x995b51, self.bl_label)
        return {'FINISHED'}

class GEDarkCoppertoneA(bpy.types.Operator):
    """General Electric Dark Coppertone A"""
    bl_label = "Dark Coppertone A"
    bl_idname = 'color.ge_dark_coppertone_a'
    def execute(self, context):
        set_base_color(0x683f36, self.bl_label)
        return {'FINISHED'}

class GECoppertoneB(bpy.types.Operator):
    """General Electric Coppertone B"""
    bl_label = "Coppertone B"
    bl_idname = 'color.ge_coppertone_b'
    def execute(self, context):
        set_base_color(0x6f4f4c, self.bl_label)
        return {'FINISHED'}

class GEDarkCoppertoneB(bpy.types.Operator):
    """General Electric Dark Coppertone B"""
    bl_label = "Dark Coppertone B"
    bl_idname = 'color.ge_dark_coppertone_b'
    def execute(self, context):
        set_base_color(0x462b29, self.bl_label)
        return {'FINISHED'}

class GEAvacado(bpy.types.Operator):
    """General Electric Avacado"""
    bl_label = "Avacado"
    bl_idname = 'color.ge_avacado'
    def execute(self, context):
        set_base_color(0xb3b280, self.bl_label)
        return {'FINISHED'}

class GEAvacadoLight(bpy.types.Operator):
    """General Electric Avacado Light"""
    bl_label = "Avacado Light"
    bl_idname = 'color.ge_avacado_light'
    def execute(self, context):
        set_base_color(0x99915d, self.bl_label)
        return {'FINISHED'}

class GEAvacadoDark(bpy.types.Operator):
    """General Electric Avacado Dark"""
    bl_label = "Avacado Dark"
    bl_idname = 'color.ge_avacado_dark'
    def execute(self, context):
        set_base_color(0x615b37, self.bl_label)
        return {'FINISHED'}

class GEHarvestGold(bpy.types.Operator):
    """General Electric Harvest Gold"""
    bl_label = "Harvest Gold"
    bl_idname = 'color.ge_harvest_gold'
    def execute(self, context):
        set_base_color(0xdcbc80, self.bl_label)
        return {'FINISHED'}

class GEHarvestDark(bpy.types.Operator):
    """General Electric Harvest Dark"""
    bl_label = "Harvest Dark"
    bl_idname = 'color.ge_harvest_dark'
    def execute(self, context):
        set_base_color(0xa68d56, self.bl_label)
        return {'FINISHED'}

class GEHarvestLight(bpy.types.Operator):
    """General Electric Harvest Light"""
    bl_label = "Harvest Light"
    bl_idname = 'color.ge_harvest_light'
    def execute(self, context):
        set_base_color(0xdebd80, self.bl_label)
        return {'FINISHED'}


# MOOD COLORS

class MoodsGreen02(bpy.types.Operator):
    """Soft sage green with a hint of blue"""
    bl_label = "Green 02"
    bl_idname = 'color.moods_green_02'
    def execute(self, context):
        set_base_color(0x8A9082, self.bl_label)
        return {'FINISHED'}

class MoodsBlue02(bpy.types.Operator):
    """Fresh clean minty blue"""
    bl_label = "Blue 02"
    bl_idname = 'color.moods_blue_02'
    def execute(self, context):
        set_base_color(0xd3dbd9, self.bl_label)
        return {'FINISHED'}

class MoodsBlue08(bpy.types.Operator):
    """Vibrant mid-tone sky blue"""
    bl_label = "Blue 08"
    bl_idname = 'color.moods_blue_08'
    def execute(self, context):
        set_base_color(0xabccd3, self.bl_label)
        return {'FINISHED'}

class MoodsPink04(bpy.types.Operator):
    """Muted pink with a touch of grey"""
    bl_label = "Pink 04"
    bl_idname = 'color.moods_pink_04'
    def execute(self, context):
        set_base_color(0xF3E0E4, self.bl_label)
        return {'FINISHED'}

class MoodsGreen07(bpy.types.Operator):
    """Foliage green with hint of blue & yellow"""
    bl_label = "Green 07"
    bl_idname = 'color.moods_green_07'
    def execute(self, context):
        set_base_color(0x698a66, self.bl_label)
        return {'FINISHED'}

class MoodsGreen08(bpy.types.Operator):
    """Fresh neo green"""
    bl_label = "Green 08"
    bl_idname = 'color.moods_green_08'
    def execute(self, context):
        set_base_color(0xa2c3af, self.bl_label)
        return {'FINISHED'}

class MoodsGreen13(bpy.types.Operator):
    """Sage green with added optimism"""
    bl_label = "Green 13"
    bl_idname = 'color.moods_green_13'
    def execute(self, context):
        set_base_color(0xb9ccae, self.bl_label)
        return {'FINISHED'}

class MoodsYellow06(bpy.types.Operator):
    """Daffodil yellow with a lemon tang"""
    bl_label = "Yellow 06"
    bl_idname = 'color.moods_yellow_06'
    def execute(self, context):
        set_base_color(0xffe887, self.bl_label)
        return {'FINISHED'}

class MoodsPink07(bpy.types.Operator):
    """A romantic, muted pink"""
    bl_label = "Pink 07"
    bl_idname = 'color.moods_pink_07'
    def execute(self, context):
        set_base_color(0xd2c5bc, self.bl_label)
        return {'FINISHED'}

class MoodsPink08(bpy.types.Operator):
    """Dusty pink on a distinctly earthy base"""
    bl_label = "Pink 08"
    bl_idname = 'color.moods_pink_08'
    def execute(self, context):
        set_base_color(0xc2a79c, self.bl_label)
        return {'FINISHED'}

class MoodsBeige02(bpy.types.Operator):
    """Light buff brown with touch of grey"""
    bl_label = "Beige 02"
    bl_idname = 'color.moods_beige_02'
    def execute(self, context):
        set_base_color(0xb6a18b, self.bl_label)
        return {'FINISHED'}

class MoodsBeige03(bpy.types.Operator):
    """Soft, earthy beige with notes of grey and yellow"""
    bl_label = "Beige 03"
    bl_idname = 'color.moods_beige_03'
    def execute(self, context):
        set_base_color(0xdfdbcf, self.bl_label)
        return {'FINISHED'}

class MoodsBlue06(bpy.types.Operator):
    """Deep slate blue"""
    bl_label = "Blue 06"
    bl_idname = 'color.moods_blue_06'
    def execute(self, context):
        set_base_color(0x4c5f6b, self.bl_label)
        return {'FINISHED'}

class MoodsBlue07(bpy.types.Operator):
    """Dark inky blue with touch of green"""
    bl_label = "Blue 07"
    bl_idname = 'color.moods_blue_07'
    def execute(self, context):
        set_base_color(0x3d4f56, self.bl_label)
        return {'FINISHED'}

class MoodsBlue17(bpy.types.Operator):
    """A grounded, muted blue"""
    bl_label = "Blue 17"
    bl_idname = 'color.moods_blue_17'
    def execute(self, context):
        set_base_color(0x8398a5, self.bl_label)
        return {'FINISHED'}

class MoodsBlue111(bpy.types.Operator):
    """Cobalt keyworker blue"""
    bl_label = "Blue1 11"
    bl_idname = 'color.moods_blue1_11'
    def execute(self, context):
        set_base_color(0x1a4677, self.bl_label)
        return {'FINISHED'}

class MoodsPurple03(bpy.types.Operator):
    """Deep, velvety purple with blue undertones"""
    bl_label = "Purple 03"
    bl_idname = 'color.moods_purple_03'
    def execute(self, context):
        set_base_color(0x432d2e, self.bl_label)
        return {'FINISHED'}

class MoodsTeal03(bpy.types.Operator):
    """Charcoal blue with grey undertones"""
    bl_label = "Teal 03"
    bl_idname = 'color.moods_teal_03'
    def execute(self, context):
        set_base_color(0x596869, self.bl_label)
        return {'FINISHED'}

class MoodsRed03(bpy.types.Operator):
    """Deep terracotta"""
    bl_label = "Red 03"
    bl_idname = 'color.moods_red_03'
    def execute(self, context):
        set_base_color(0xc3867b, self.bl_label)
        return {'FINISHED'}

class MoodsBlack01(bpy.types.Operator):
    """Graphite black with blue undertones"""
    bl_label = "Black 01"
    bl_idname = 'color.moods_black_01'
    def execute(self, context):
        set_base_color(0x444A4C, self.bl_label)
        return {'FINISHED'}

class MoodsWhite04(bpy.types.Operator):
    """Soft linen white with grey undertones"""
    bl_label = "White 04"
    bl_idname = 'color.moods_white_04'
    def execute(self, context):
        set_base_color(0xe4e2d7, self.bl_label)
        return {'FINISHED'}

class MoodsWhite03(bpy.types.Operator):
    """Soft creamy white with touch of yellow"""
    bl_label = "White 03"
    bl_idname = 'color.moods_white_03'
    def execute(self, context):
        set_base_color(0xf3f1e5, self.bl_label)
        return {'FINISHED'}

class MoodsWhite02(bpy.types.Operator):
    """Off-white with a touch of grey"""
    bl_label = "White 02"
    bl_idname = 'color.moods_white_02'
    def execute(self, context):
        set_base_color(0xeceae2, self.bl_label)
        return {'FINISHED'}

class MoodsWhite01(bpy.types.Operator):
    """Pure white with the lightest touch of grey"""
    bl_label = "White 01"
    bl_idname = 'color.moods_white_01'
    def execute(self, context):
        set_base_color(0xf2f2eb, self.bl_label)
        return {'FINISHED'}


# BOOLEAN FOR PANEL
class MORE_SETTINGS(bpy.types.PropertyGroup):
    rename_material_more: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )


# PARENT PANEL
class MOREWPanel(bpy.types.Panel):
    bl_idname = "MORE_PT_Panel"
    bl_label = "More Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        more_bool = context.scene.more_bool

        col = layout.column(align=True)
        col.prop(more_bool, "rename_material_more")

# FORD COLORS 1958 PANEL
class F1958Panel(bpy.types.Panel):
    bl_idname = "F1958_PT_Panel"
    bl_label = "Ford 1958"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MORE_PT_Panel'
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

# GENERAL ELECTRIC 1960S APPLIANCES PANEL
class GEPanel(bpy.types.Panel):
    bl_idname = "GE_PT_Panel"
    bl_label = "General Electric"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MORE_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["ge_avacado"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_avacado_light"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_avacado_dark"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_coppertone_a"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_dark_coppertone_a"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_coppertone_b"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_dark_coppertone_b"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_harvest_gold"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_harvest_light"].icon_id)
        scol.label(text="", icon_value=c_icons["ge_harvest_dark"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.ge_avacado", text="Avacado")
        scol.operator("color.ge_avacado_light", text="Avacado Light")
        scol.operator("color.ge_avacado_dark", text="Avacado Dark")
        scol.operator("color.ge_coppertone_a", text="Coppertone A")
        scol.operator("color.ge_dark_coppertone_a", text="Dark Coppertone A")
        scol.operator("color.ge_coppertone_b", text="Coppertone B")
        scol.operator("color.ge_dark_coppertone_b", text="Dark Coppertone B")
        scol.operator("color.ge_harvest_gold", text="Harvest Gold")
        scol.operator("color.ge_harvest_light", text="Harvest Light")
        scol.operator("color.ge_harvest_dark", text="Harvest Dark")

# MOODS PANEL
class MOODSPanel(bpy.types.Panel):
    bl_idname = "MOODS_PT_Panel"
    bl_label = "Moods"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MORE_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

class MOODRELAXPanel(bpy.types.Panel):
    bl_idname = "MOODSRELAX_PT_Panel"
    bl_label = "Relaxed"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["moods_blue_02"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_blue_08"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_green_02"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_pink_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_blue_02", text="Blue 02")
        scol.operator("color.moods_blue_08", text="Blue 08")
        scol.operator("color.moods_green_02", text="Green 02")
        scol.operator("color.moods_pink_04", text="Pink 04")

class MOODENERGYPanel(bpy.types.Panel):
    bl_idname = "MOODENERGY_PT_Panel"
    bl_label = "Energy"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["moods_green_07"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_green_08"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_green_13"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_yellow_06"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_green_07", text="Green 07")
        scol.operator("color.moods_green_08", text="Green 08")
        scol.operator("color.moods_green_13", text="Green 13")
        scol.operator("color.moods_yellow_06", text="Yellow 06")

class MOODCOZYPanel(bpy.types.Panel):
    bl_idname = "MOODCOZY_PT_Panel"
    bl_label = "Cozy"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["moods_beige_02"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_beige_03"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_pink_07"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_pink_08"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_beige_02", text="Beige 02")
        scol.operator("color.moods_beige_03", text="Beige 03")
        scol.operator("color.moods_pink_07", text="Pink 07")
        scol.operator("color.moods_pink_08", text="Pink 08")

class MOODFOCUSPanel(bpy.types.Panel):
    bl_idname = "MOODFOCUS_PT_Panel"
    bl_label = "Focus"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["moods_blue_06"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_blue_07"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_blue_17"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_blue1_11"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_blue_06", text="Blue 06")
        scol.operator("color.moods_blue_07", text="Blue 07")
        scol.operator("color.moods_blue_17", text="Blue 17")
        scol.operator("color.moods_blue1_11", text="Blue 111")

class MOODMOODYPanel(bpy.types.Panel):
    bl_idname = "MOODMOODY_PT_Panel"
    bl_label = "Moody"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["moods_black_01"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_purple_03"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_red_03"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_teal_03"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_black_01", text="Black 01")
        scol.operator("color.moods_purple_03", text="Purple 03")
        scol.operator("color.moods_red_03", text="Red 03")
        scol.operator("color.moods_teal_03", text="Teal 03")

class MOODWHITESPanel(bpy.types.Panel):
    bl_idname = "MOODWHITES_PT_Panel"
    bl_label = "Whites"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MOODS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["moods_white_01"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_white_02"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_white_03"].icon_id)
        scol.label(text="", icon_value=c_icons["moods_white_04"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.moods_white_01", text="White 01")
        scol.operator("color.moods_white_02", text="White 02")
        scol.operator("color.moods_white_03", text="White 03")
        scol.operator("color.moods_white_04", text="White 04")

# SHERWIN WILLIAMS - INTERIOR PANEL
class SMIPanel(bpy.types.Panel):
    bl_idname = "SMI_PT_Panel"
    bl_label = "Suburban Modern"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MORE_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["sm_pink_flamingo"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_appleblossom"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_caribbean_coral"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_fairfax_brown"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_pinky_beige"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_beige"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_harvest_gold"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_new_colonial_yellow"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_sycamore_tan"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_peace_yellow"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_sunbeam_yellow"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_chartreuse"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_avocado"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_sage"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_sage_green_light"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_holiday_turquoise"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_powder_blu"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_radiant_lilac"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_chelsea_gray"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_westchester_gray"].icon_id)
        scol.label(text="", icon_value=c_icons["sm_classic_french_gray"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.sm_pink_flamingo", text="Pink Flamingo")
        scol.operator("color.sm_appleblossom", text="Apple Blossom")
        scol.operator("color.sm_caribbean_coral", text="Caribbean Coral")
        scol.operator("color.sm_fairfax_brown", text="Fairfax Brown")
        scol.operator("color.sm_pinky_beige", text="Pinky Beige")
        scol.operator("color.sm_beige", text="Beige")
        scol.operator("color.sm_harvest_gold", text="Harvest Gold")
        scol.operator("color.sm_new_colonial_yellow", text="New Colonial Yellow")
        scol.operator("color.sm_sycamore_tan", text="Sycamore Tan")
        scol.operator("color.sm_peace_yellow", text="Peace Yellow")
        scol.operator("color.sm_sunbeam_yellow", text="Sunbeam Yellow")
        scol.operator("color.sm_chartreuse", text="Chartreuse")
        scol.operator("color.sm_avocado", text="Avocado")
        scol.operator("color.sm_sage", text="Sage")
        scol.operator("color.sm_sage_green_light", text="Sage Green Light")
        scol.operator("color.sm_holiday_turquoise", text="Holiday Turquoise")
        scol.operator("color.sm_powder_blu", text="Powder Blu")
        scol.operator("color.sm_radiant_lilac", text="Radiant Lilac")
        scol.operator("color.sm_chelsea_gray", text="Chelsea Gray")
        scol.operator("color.sm_westchester_gray", text="Westchester Gray")
        scol.operator("color.sm_classic_french_gray", text="Classic French Gray")

# SHERWIN WILLIAMS - EXTERIOR PANEL
# class SMEPanel(bpy.types.Panel):
#     bl_idname = "SME_PT_Panel"
#     bl_label = "Suburban Modern Exterior"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "MAT"
#     bl_parent_id = 'MORE_PT_Panel'
#     bl_options = {'DEFAULT_CLOSED'}

#     def draw(self, context):
#         global c_icons
#         layout = self.layout

#         srow = layout.row()
#         scol = srow.column(align=True)
#         scol.scale_y = 1.25
#         scol.label(text="", icon_value=c_icons["sm_birdseye_maple"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_cocoon"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_olde_world_gold"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_wool_skein"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_artisan_tan"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_status_bronze"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_tatami_tan"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_colony_buff"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_homburg_gray"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_muslin"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_straw_harvest"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_rural_green"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_extra_white"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_rushing_river"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_spiced_cider"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_retreat"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_netsuke"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_edgy_gold"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_jogging_path"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_intellectual_gray"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_thunder_gray"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_anjou_pear"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_jersey_cream"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_warm_stone"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_cork_wedge"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_smokehouse"].icon_id)
#         scol.label(text="", icon_value=c_icons["sm_rustic_red"].icon_id)

#         scol = srow.column(align=True)
#         scol.scale_y = 1.25
#         scol.scale_x = 3.0
#         scol.operator("color.sm_birdseye_maple", text="Birdseye Maple")
#         scol.operator("color.sm_cocoon", text="Cocoon")
#         scol.operator("color.sm_olde_world_gold", text="Olde World Gold")
#         scol.operator("color.sm_wool_skein", text="Wool Skein")
#         scol.operator("color.sm_artisan_tan", text="Artisan Tan")
#         scol.operator("color.sm_status_bronze", text="Status Bronze")
#         scol.operator("color.sm_tatami_tan", text="Tatami Tan")
#         scol.operator("color.sm_colony_buff", text="Colony Buff")
#         scol.operator("color.sm_homburg_gray", text="Homburg Gray")
#         scol.operator("color.sm_muslin", text="Muslin")
#         scol.operator("color.sm_straw_harvest", text="Straw Harvest")
#         scol.operator("color.sm_rural_green", text="Rural Green")
#         scol.operator("color.sm_extra_white", text="Extra White")
#         scol.operator("color.sm_rushing_river", text="Rushing River")
#         scol.operator("color.sm_spiced_cider", text="Spiced Cider")
#         scol.operator("color.sm_retreat", text="Retreat")
#         scol.operator("color.sm_netsuke", text="Netsuke")
#         scol.operator("color.sm_edgy_gold", text="Edgy Gold")
#         scol.operator("color.sm_jogging_path", text="Jogging Path")
#         scol.operator("color.sm_intellectual_gray", text="Intellectual Gray")
#         scol.operator("color.sm_thunder_gray", text="Thunder Gray")
#         scol.operator("color.sm_anjou_pear", text="Anjou Pear")
#         scol.operator("color.sm_jersey_cream", text="Jersey Cream")
#         scol.operator("color.sm_warm_stone", text="Warm Stone")
#         scol.operator("color.sm_cork_wedge", text="Cork Wedge")
#         scol.operator("color.sm_smokehouse", text="Smokehouse")
#         scol.operator("color.sm_rustic_red", text="Rustic Red")


# SHERWIN WILLIAMS - THE JAZZ AGE PANEL
class JAPanel(bpy.types.Panel):
    bl_idname = "JA_PT_Panel"
    bl_label = "The Jazz Age"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'MORE_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=c_icons["ja_salon_rose"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_chinese_red"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_studio_mauve"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_jazz_age_coral"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_frostwork"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_alexandrite"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_blue_peacock"].icon_id)
        scol.label(text="", icon_value=c_icons["ja_blue_sky"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.ja_salon_rose", text="Salon Rose")
        scol.operator("color.ja_chinese_red", text="Chinese Red")
        scol.operator("color.ja_studio_mauve", text="Studio Mauve")
        scol.operator("color.ja_jazz_age_coral", text="Jazz Age Coral")
        scol.operator("color.ja_frostwork", text="Frostwork")
        scol.operator("color.ja_alexandrite", text="Alexandrite")
        scol.operator("color.ja_blue_peacock", text="Blue Peacock")
        scol.operator("color.ja_blue_sky", text="Blue Sky")


classes = [
    MORE_SETTINGS,
    MOREWPanel,
    F1958Panel,
    SMIPanel,
    # SMEPanel,
    JAPanel,
    GEPanel,
    MOODSPanel,
    MOODRELAXPanel,
    MOODENERGYPanel,
    MOODCOZYPanel,
    MOODFOCUSPanel,
    MOODMOODYPanel,
    MOODWHITESPanel,
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
    SMChartreuse,
    SMRadiantLilac,
    SMHolidayTurquoise,
    SMAppleBlossom,
    SMClassicFrenchGray,
    SMSunbeamYellow,
    SMPinkyBeige,
    SMPinkFlamingo,
    SMWestchesterGray,
    SMChelseaGray,
    SMSageGreenLight,
    SMNewColonialYellow,
    SMCaribbeanCoral,
    SMSycamoreTan,
    SMFairfaxBrown,
    SMPeaceYellow,
    SMHarvestGold,
    SMBeige,
    SMSage,
    SMAvocado,
    SMPowderBlu,
    # SMBirdseyeMaple,
    # SMCocoon,
    # SMOldeWorldGold,
    # SMWoolSkein,
    # SMArtisanTan,
    # SMStatusBronze,
    # SMTatamiTan,
    # SMColonyBuff,
    # SMHomburgGray,
    # SMMuslin,
    # SMStrawHarvest,
    # SMRuralGreen,
    # SMExtraWhite,
    # SMRushingRiver,
    # SMSpicedCider,
    # SMRetreat,
    # SMNetsuke,
    # SMEdgyGold,
    # SMJoggingPath,
    # SMIntellectualGray,
    # SMThunderGray,
    # SMAnjouPear,
    # SMJerseyCream,
    # SMWarmStone,
    # SMCorkWedge,
    # SMSmokehouse,
    # SMRusticRed,
    JAChineseRed,
    JAJazzAgeCoral,
    JAFrostwork,
    JAAlexandrite,
    JASalonRose,
    JAStudioMauve,
    JABlueSky,
    JABluePeacock,
    GECoppertoneA,
    GEDarkCoppertoneA,
    GECoppertoneB,
    GEDarkCoppertoneB,
    GEAvacado,
    GEAvacadoLight,
    GEAvacadoDark,
    GEHarvestGold,
    GEHarvestDark,
    GEHarvestLight,
    MoodsGreen02,
    MoodsBlue02,
    MoodsBlue08,
    MoodsPink04,
    MoodsGreen07,
    MoodsGreen08,
    MoodsGreen13,
    MoodsYellow06,
    MoodsPink07,
    MoodsPink08,
    MoodsBeige02,
    MoodsBeige03,
    MoodsBlue06,
    MoodsBlue07,
    MoodsBlue17,
    MoodsBlue111,
    MoodsPurple03,
    MoodsTeal03,
    MoodsRed03,
    MoodsBlack01,
    MoodsWhite04,
    MoodsWhite03,
    MoodsWhite02,
    MoodsWhite01,
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
        bpy.types.Scene.more_bool = bpy.props.PointerProperty(type=MORE_SETTINGS)


def unregister():
    # Addon updater unregister.
#    addon_updater_ops.unregister()
#   UNREGISTER ICONS
    global c_icons
    bpy.utils.previews.remove(c_icons)

    del bpy.types.Scene.more_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
