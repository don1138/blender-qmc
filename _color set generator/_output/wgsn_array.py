# WGSN COLORS SET

import bpy

from .globals import *
from .color_functions import *

# WGSN OPERATORS

class WGSN_NeoMint(bpy.types.Operator):
    """Neo Mint (Coloro 065-80-23)"""
    bl_label = "Neo Mint"
    bl_idname = 'color.wgsn_neo_mint'
    def execute(self, context):
        set_base_color(0xa6d3aa, self.bl_label)
        return {'FINISHED'}

class WGSN_Cantaloupe(bpy.types.Operator):
    """Cantaloupe (Coloro 020-72-30)"""
    bl_label = "Cantaloupe"
    bl_idname = 'color.wgsn_cantaloupe'
    def execute(self, context):
        set_base_color(0xf59f7e, self.bl_label)
        return {'FINISHED'}

class WGSN_Cassis(bpy.types.Operator):
    """Cassis (Coloro 145-58-21)"""
    bl_label = "Cassis"
    bl_idname = 'color.wgsn_cassis'
    def execute(self, context):
        set_base_color(0xac6f81, self.bl_label)
        return {'FINISHED'}

class WGSN_MellowYellow(bpy.types.Operator):
    """Mellow Yellow (Coloro 034-70-33)"""
    bl_label = "Mellow Yellow"
    bl_idname = 'color.wgsn_mellow_yellow'
    def execute(self, context):
        set_base_color(0xe2ab36, self.bl_label)
        return {'FINISHED'}

class WGSN_PuristBlue(bpy.types.Operator):
    """Purist Blue (Coloro 093-76-17)"""
    bl_label = "Purist Blue"
    bl_idname = 'color.wgsn_purist_blue'
    def execute(self, context):
        set_base_color(0x85c6cc, self.bl_label)
        return {'FINISHED'}

class WGSN_AIAqua(bpy.types.Operator):
    """A.I. Aqua (Coloro 098-59-30)"""
    bl_label = "A.I. Aqua"
    bl_idname = 'color.wgsn_ai_aqua'
    def execute(self, context):
        set_base_color(0x00a5b9, self.bl_label)
        return {'FINISHED'}

class WGSN_GoodGray(bpy.types.Operator):
    """Good Gray (Coloro 122-66-02)"""
    bl_label = "Good Gray"
    bl_idname = 'color.wgsn_good_gray'
    def execute(self, context):
        set_base_color(0xa0abb1, self.bl_label)
        return {'FINISHED'}

class WGSN_LemonSherbet(bpy.types.Operator):
    """Lemon Sherbet (Coloro 046-85-28)"""
    bl_label = "Lemon Sherbet"
    bl_idname = 'color.wgsn_lemon_sherbet'
    def execute(self, context):
        set_base_color(0xf2de6b, self.bl_label)
        return {'FINISHED'}

class WGSN_OxyFire(bpy.types.Operator):
    """Oxy Fire (Coloro 015-50-36)"""
    bl_label = "Oxy Fire"
    bl_idname = 'color.wgsn_oxy_fire'
    def execute(self, context):
        set_base_color(0xdc493f, self.bl_label)
        return {'FINISHED'}

class WGSN_QuietWave(bpy.types.Operator):
    """Quiet Wave (Coloro 072-69-24)"""
    bl_label = "Quiet Wave"
    bl_idname = 'color.wgsn_quiet_wave'
    def execute(self, context):
        set_base_color(0x75c095, self.bl_label)
        return {'FINISHED'}

class WGSN_GoldenHarvest(bpy.types.Operator):
    """Golden Harvest (Coloro 034-70-21)"""
    bl_label = "Golden Harvest"
    bl_idname = 'color.wgsn_golden_harvest'
    def execute(self, context):
        set_base_color(0xdaad6a, self.bl_label)
        return {'FINISHED'}

class WGSN_Bloodstone(bpy.types.Operator):
    """Bloodstone (Coloro 011-27-26)"""
    bl_label = "Bloodstone"
    bl_idname = 'color.wgsn_bloodstone'
    def execute(self, context):
        set_base_color(0x7f252e, self.bl_label)
        return {'FINISHED'}

class WGSN_DarkSprings(bpy.types.Operator):
    """Dark Springs (Coloro 087-20-02)"""
    bl_label = "Dark Springs"
    bl_idname = 'color.wgsn_dark_springs'
    def execute(self, context):
        set_base_color(0x2a3332, self.bl_label)
        return {'FINISHED'}

class WGSN_ElectricMagenta(bpy.types.Operator):
    """Electric Magenta (Coloro 001-35-31)"""
    bl_label = "Electric Magenta"
    bl_idname = 'color.wgsn_electric_magenta'
    def execute(self, context):
        set_base_color(0xae1943, self.bl_label)
        return {'FINISHED'}

class WGSN_OrchidFlower(bpy.types.Operator):
    """Orchid Flower (Coloro 150-38-31)"""
    bl_label = "Orchid Flower"
    bl_idname = 'color.wgsn_orchid_flower'
    def execute(self, context):
        set_base_color(0xa1346d, self.bl_label)
        return {'FINISHED'}

class WGSN_Butter(bpy.types.Operator):
    """Butter (Coloro 040-86-20)"""
    bl_label = "Butter"
    bl_idname = 'color.wgsn_butter'
    def execute(self, context):
        set_base_color(0xebdf97, self.bl_label)
        return {'FINISHED'}

class WGSN_OliveOil(bpy.types.Operator):
    """Olive Oil (Coloro 044-52-13)"""
    bl_label = "Olive Oil"
    bl_idname = 'color.wgsn_olive_oil'
    def execute(self, context):
        set_base_color(0x8d8054, self.bl_label)
        return {'FINISHED'}

class WGSN_MangoSorbet(bpy.types.Operator):
    """Mango Sorbet (Coloro 030-67-34)"""
    bl_label = "Mango Sorbet"
    bl_idname = 'color.wgsn_mango_sorbet'
    def execute(self, context):
        set_base_color(0xec972d, self.bl_label)
        return {'FINISHED'}

class WGSN_AtlanticBlue(bpy.types.Operator):
    """Atlantic Blue (Coloro 115-35-20)"""
    bl_label = "Atlantic Blue"
    bl_idname = 'color.wgsn_atlantic_blue'
    def execute(self, context):
        set_base_color(0x375b7f, self.bl_label)
        return {'FINISHED'}

class WGSN_Honeycomb(bpy.types.Operator):
    """Honeycomb (Coloro 034-76-27)"""
    bl_label = "Honeycomb"
    bl_idname = 'color.wgsn_honeycomb'
    def execute(self, context):
        set_base_color(0xf8c761, self.bl_label)
        return {'FINISHED'}

class WGSN_Jade(bpy.types.Operator):
    """Jade (Coloro 062-57-10)"""
    bl_label = "Jade"
    bl_idname = 'color.wgsn_jade'
    def execute(self, context):
        set_base_color(0x839177, self.bl_label)
        return {'FINISHED'}

class WGSN_DarkOak(bpy.types.Operator):
    """Dark Oak (Coloro 017-23-07)"""
    bl_label = "Dark Oak"
    bl_idname = 'color.wgsn_dark_oak'
    def execute(self, context):
        set_base_color(0x413735, self.bl_label)
        return {'FINISHED'}

class WGSN_LazuliBlue(bpy.types.Operator):
    """Lazuli Blue (Coloro 122-25-24)"""
    bl_label = "Lazuli Blue"
    bl_idname = 'color.wgsn_lazuli_blue'
    def execute(self, context):
        set_base_color(0x32477c, self.bl_label)
        return {'FINISHED'}

class WGSN_DigitalLavender(bpy.types.Operator):
    """Digital Lavender (Coloro 134-67-16)"""
    bl_label = "Digital Lavender"
    bl_idname = 'color.wgsn_digital_lavender'
    def execute(self, context):
        set_base_color(0xb1a5cd, self.bl_label)
        return {'FINISHED'}

class WGSN_LusciousRed(bpy.types.Operator):
    """Luscious Red (Coloro 010-46-36)"""
    bl_label = "Luscious Red"
    bl_idname = 'color.wgsn_luscious_red'
    def execute(self, context):
        set_base_color(0xe33443, self.bl_label)
        return {'FINISHED'}

class WGSN_Sundial(bpy.types.Operator):
    """Sundial (Coloro 028-59-26)"""
    bl_label = "Sundial"
    bl_idname = 'color.wgsn_sundial'
    def execute(self, context):
        set_base_color(0xcc842f, self.bl_label)
        return {'FINISHED'}

class WGSN_TranquilBlue(bpy.types.Operator):
    """Tranquil Blue (Coloro 72-29-717)"""
    bl_label = "Tranquil Blue"
    bl_idname = 'color.wgsn_tranquil_blue'
    def execute(self, context):
        set_base_color(0x528ccc, self.bl_label)
        return {'FINISHED'}

class WGSN_Verdigris(bpy.types.Operator):
    """Verdigris (Coloro 092-38-21)"""
    bl_label = "Verdigris"
    bl_idname = 'color.wgsn_verdigris'
    def execute(self, context):
        set_base_color(0x016d6d, self.bl_label)
        return {'FINISHED'}

class WGSN_AstroDust(bpy.types.Operator):
    """Astro Dust (Coloro 010-42-20)"""
    bl_label = "Astro Dust"
    bl_idname = 'color.wgsn_astro_dust'
    def execute(self, context):
        set_base_color(0xa34e51, self.bl_label)
        return {'FINISHED'}

class WGSN_GalacticCobalt(bpy.types.Operator):
    """Galactic Cobalt (Coloro 120-28-32)"""
    bl_label = "Galactic Cobalt"
    bl_idname = 'color.wgsn_galactic_cobalt'
    def execute(self, context):
        set_base_color(0x274585, self.bl_label)
        return {'FINISHED'}

class WGSN_SageLeaf(bpy.types.Operator):
    """Sage Leaf (Coloro 072-45-06)"""
    bl_label = "Sage Leaf"
    bl_idname = 'color.wgsn_sage_leaf'
    def execute(self, context):
        set_base_color(0x66786c, self.bl_label)
        return {'FINISHED'}

class WGSN_ApricotCrush(bpy.types.Operator):
    """Apricot Crush (Coloro 024-65-27)"""
    bl_label = "Apricot Crush"
    bl_idname = 'color.wgsn_apricot_crush'
    def execute(self, context):
        set_base_color(0xe39360, self.bl_label)
        return {'FINISHED'}

class WGSN_ApricotCrush(bpy.types.Operator):
    """Apricot Crush (Coloro 024-65-27)"""
    bl_label = "Apricot Crush"
    bl_idname = 'color.wgsn_apricot_crush'
    def execute(self, context):
        set_base_color(0xf39154, self.bl_label)
        return {'FINISHED'}

class WGSN_CyberLime(bpy.types.Operator):
    """Cyber Lime (Coloro 051-76-36)"""
    bl_label = "Cyber Lime"
    bl_idname = 'color.wgsn_cyber_lime'
    def execute(self, context):
        set_base_color(0xd0c81d, self.bl_label)
        return {'FINISHED'}

class WGSN_ElementalBlue(bpy.types.Operator):
    """Elemental Blue (Coloro 117-47-13)"""
    bl_label = "Elemental Blue"
    bl_idname = 'color.wgsn_elemental_blue'
    def execute(self, context):
        set_base_color(0x5a7a91, self.bl_label)
        return {'FINISHED'}

class WGSN_FondantPink(bpy.types.Operator):
    """Fondant Pink (Coloro 147-70-20)"""
    bl_label = "Fondant Pink"
    bl_idname = 'color.wgsn_fondant_pink'
    def execute(self, context):
        set_base_color(0xd8a2c2, self.bl_label)
        return {'FINISHED'}

class WGSN_Nutshell(bpy.types.Operator):
    """Nutshell (Coloro 024-37-20)"""
    bl_label = "Nutshell"
    bl_idname = 'color.wgsn_nutshell'
    def execute(self, context):
        set_base_color(0x865132, self.bl_label)
        return {'FINISHED'}

class WGSN_RadiantRed(bpy.types.Operator):
    """Radiant Red (Coloro 011-50-32)"""
    bl_label = "Radiant Red"
    bl_idname = 'color.wgsn_radiant_red'
    def execute(self, context):
        set_base_color(0xdb4c50, self.bl_label)
        return {'FINISHED'}

class WGSN_CoolMatcha(bpy.types.Operator):
    """Cool Matcha (Coloro 055-85-20)"""
    bl_label = "Cool Matcha"
    bl_idname = 'color.wgsn_cool_matcha'
    def execute(self, context):
        set_base_color(0xdff4b3, self.bl_label)
        return {'FINISHED'}

class WGSN_SustainedGrey(bpy.types.Operator):
    """Sustained Grey (Coloro 035-73-04)"""
    bl_label = "Sustained Grey"
    bl_idname = 'color.wgsn_sustained_grey'
    def execute(self, context):
        set_base_color(0xbabbb5, self.bl_label)
        return {'FINISHED'}

class WGSN_MidnightPlum(bpy.types.Operator):
    """Midnight Plum (Coloro 151-22-09)"""
    bl_label = "Midnight Plum"
    bl_idname = 'color.wgsn_midnight_plum'
    def execute(self, context):
        set_base_color(0x4a3343, self.bl_label)
        return {'FINISHED'}

class WGSN_IntenseRust(bpy.types.Operator):
    """Intense Rust (Coloro 015-33-25)"""
    bl_label = "Intense Rust"
    bl_idname = 'color.wgsn_intense_rust'
    def execute(self, context):
        set_base_color(0x78291a, self.bl_label)
        return {'FINISHED'}

class WGSN_FutureDusk(bpy.types.Operator):
    """Future Dusk (Coloro 129-35-18)"""
    bl_label = "Future Dusk"
    bl_idname = 'color.wgsn_future_dusk'
    def execute(self, context):
        set_base_color(0x4C5578, self.bl_label)
        return {'FINISHED'}

class WGSN_AquaticAwe(bpy.types.Operator):
    """Aquatic Awe (Coloro 086-70-25)"""
    bl_label = "Aquatic Awe"
    bl_idname = 'color.wgsn_aquatic_awe'
    def execute(self, context):
        set_base_color(0x5DC7B7, self.bl_label)
        return {'FINISHED'}

class WGSN_RayFlower(bpy.types.Operator):
    """Ray Flower (Coloro 037-82-32)"""
    bl_label = "Ray Flower"
    bl_idname = 'color.wgsn_ray_flower'
    def execute(self, context):
        set_base_color(0xFFCA5C, self.bl_label)
        return {'FINISHED'}

class WGSN_SunsetCoral(bpy.types.Operator):
    """Sunset Coral (Coloro 009-58-31)"""
    bl_label = "Sunset Coral"
    bl_idname = 'color.wgsn_sunset_coral'
    def execute(self, context):
        set_base_color(0xF0686C, self.bl_label)
        return {'FINISHED'}

class WGSN_TranscendentPink(bpy.types.Operator):
    """Transcendent Pink (Coloro 021-80-08)"""
    bl_label = "Transcendent Pink"
    bl_idname = 'color.wgsn_transcendent_pink'
    def execute(self, context):
        set_base_color(0xE3B8C9, self.bl_label)
        return {'FINISHED'}

class WGSN_CelestialYellow(bpy.types.Operator):
    """Celestial Yellow (Coloro 048-90-17)"""
    bl_label = "Celestial Yellow"
    bl_idname = 'color.wgsn_celestial_yellow'
    def execute(self, context):
        set_base_color(0xEDEAB1, self.bl_label)
        return {'FINISHED'}

class WGSN_CherryLacquer(bpy.types.Operator):
    """Cherry Lacquer (Coloro 159-23-15)"""
    bl_label = "Cherry Lacquer"
    bl_idname = 'color.wgsn_cherry_lacquer'
    def execute(self, context):
        set_base_color(0x512C3A, self.bl_label)
        return {'FINISHED'}

class WGSN_RetroBlue(bpy.types.Operator):
    """Retro Blue (Coloro 100-64-14)"""
    bl_label = "Retro Blue"
    bl_idname = 'color.wgsn_retro_blue'
    def execute(self, context):
        set_base_color(0x71ADBA, self.bl_label)
        return {'FINISHED'}

class WGSN_NeonFlare(bpy.types.Operator):
    """Neon Flare (Coloro 014-68-51)"""
    bl_label = "Neon Flare"
    bl_idname = 'color.wgsn_neon_flare'
    def execute(self, context):
        set_base_color(0xFF654F, self.bl_label)
        return {'FINISHED'}

class WGSN_TransformativeTeal(bpy.types.Operator):
    """Transformative Teal (Coloro 092-357-14)"""
    bl_label = "Transformative Teal"
    bl_idname = 'color.wgsn_transformative_teal'
    def execute(self, context):
        set_base_color(0x366f70, self.bl_label)
        return {'FINISHED'}

class WGSN_BlueAura(bpy.types.Operator):
    """Blue Aura (Coloro 117-77-06)"""
    bl_label = "Blue Aura"
    bl_idname = 'color.wgsn_blue_aura'
    def execute(self, context):
        set_base_color(0xbed0dc, self.bl_label)
        return {'FINISHED'}

class WGSN_ElectricFuchsia(bpy.types.Operator):
    """Electric Fuchsia (Coloro 144-57-41)"""
    bl_label = "Electric Fuchsia"
    bl_idname = 'color.wgsn_electric_fuchsia'
    def execute(self, context):
        set_base_color(0xee67db, self.bl_label)
        return {'FINISHED'}

class WGSN_JellyMint(bpy.types.Operator):
    """Jelly Mint (Coloro 078-80-22)"""
    bl_label = "Jelly Mint"
    bl_idname = 'color.wgsn_jelly_mint'
    def execute(self, context):
        set_base_color(0x9ddbc9, self.bl_label)
        return {'FINISHED'}

class WGSN_AmberHaze(bpy.types.Operator):
    """Amber Haze (Coloro 043-65-31)"""
    bl_label = "Amber Haze"
    bl_idname = 'color.wgsn_amber_haze'
    def execute(self, context):
        set_base_color(0xdbb62f, self.bl_label)
        return {'FINISHED'}

class WGSN_WaxPaper(bpy.types.Operator):
    """Wax Paper (Coloro 035-88-12)"""
    bl_label = "Wax Paper"
    bl_idname = 'color.wgsn_wax_paper'
    def execute(self, context):
        set_base_color(0xf7e4c5, self.bl_label)
        return {'FINISHED'}

class WGSN_FreshPurple(bpy.types.Operator):
    """Fresh Purple (Coloro 136-32-33)"""
    bl_label = "Fresh Purple"
    bl_idname = 'color.wgsn_fresh_purple'
    def execute(self, context):
        set_base_color(0x724e9a, self.bl_label)
        return {'FINISHED'}

class WGSN_CocoaPowder(bpy.types.Operator):
    """Cocoa Powder (Coloro 008-35-06)"""
    bl_label = "Cocoa Powder"
    bl_idname = 'color.wgsn_cocoa_powder'
    def execute(self, context):
        set_base_color(0x735b5f, self.bl_label)
        return {'FINISHED'}

class WGSN_GreenGlow(bpy.types.Operator):
    """Green Glow (Coloro 057-82-32)"""
    bl_label = "Green Glow"
    bl_idname = 'color.wgsn_green_glow'
    def execute(self, context):
        set_base_color(0xcee270, self.bl_label)
        return {'FINISHED'}

class WGSN_LuminousBlue(bpy.types.Operator):
    """Luminous Blue (Coloro 125-28-38)"""
    bl_label = "Luminous Blue"
    bl_idname = 'color.wgsn_luminous_blue'
    def execute(self, context):
        set_base_color(0x193f8f, self.bl_label)
        return {'FINISHED'}

class WGSN_EnergyOrange(bpy.types.Operator):
    """Energy Orange (Coloro 018-57-34)"""
    bl_label = "Energy Orange"
    bl_idname = 'color.wgsn_energy_orange'
    def execute(self, context):
        set_base_color(0xee6643, self.bl_label)
        return {'FINISHED'}

class WGSN_MeadowlandGreen(bpy.types.Operator):
    """Meadowland Green (Coloro 050-61-19)"""
    bl_label = "Meadowland Green"
    bl_idname = 'color.wgsn_meadowland_green'
    def execute(self, context):
        set_base_color(0xa39e58, self.bl_label)
        return {'FINISHED'}

class WGSN_Clay(bpy.types.Operator):
    """Clay (Coloro 014-60-13)"""
    bl_label = "Clay"
    bl_idname = 'color.wgsn_clay'
    def execute(self, context):
        set_base_color(0xc38b84, self.bl_label)
        return {'FINISHED'}

class WGSN_PopPink(bpy.types.Operator):
    """Pop Pink (Coloro 151-73-22)"""
    bl_label = "Pop Pink"
    bl_idname = 'color.wgsn_pop_pink'
    def execute(self, context):
        set_base_color(0xeaa6c5, self.bl_label)
        return {'FINISHED'}


# WGSN PANEL

class WGSNPanel(bpy.types.Panel):
    bl_idname = "WGSN_PT_Panel"
    bl_label = "WGSN"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["wgsn_neo_mint"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_cantaloupe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_cassis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_mellow_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_purist_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_ai_aqua"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_good_gray"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_lemon_sherbet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_oxy_fire"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_quiet_wave"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_golden_harvest"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_bloodstone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_dark_springs"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_electric_magenta"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_orchid_flower"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_butter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_olive_oil"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_mango_sorbet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_atlantic_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_honeycomb"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_jade"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_dark_oak"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_lazuli_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_digital_lavender"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_luscious_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_sundial"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_tranquil_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_verdigris"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_astro_dust"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_galactic_cobalt"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_sage_leaf"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_apricot_crush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_apricot_crush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_cyber_lime"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_elemental_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_fondant_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_nutshell"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_radiant_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_cool_matcha"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_sustained_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_midnight_plum"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_intense_rust"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_future_dusk"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_aquatic_awe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_ray_flower"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_sunset_coral"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_transcendent_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_celestial_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_cherry_lacquer"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_retro_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_neon_flare"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_transformative_teal"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_blue_aura"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_electric_fuchsia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_jelly_mint"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_amber_haze"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_wax_paper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_fresh_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_cocoa_powder"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_green_glow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_luminous_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_energy_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_meadowland_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_clay"].icon_id)
        scol.label(text="", icon_value=g.c_icons["wgsn_pop_pink"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.wgsn_neo_mint", text="Neo Mint")
        scol.operator("color.wgsn_cantaloupe", text="Cantaloupe")
        scol.operator("color.wgsn_cassis", text="Cassis")
        scol.operator("color.wgsn_mellow_yellow", text="Mellow Yellow")
        scol.operator("color.wgsn_purist_blue", text="Purist Blue")
        scol.operator("color.wgsn_ai_aqua", text="A.I. Aqua")
        scol.operator("color.wgsn_good_gray", text="Good Gray")
        scol.operator("color.wgsn_lemon_sherbet", text="Lemon Sherbet")
        scol.operator("color.wgsn_oxy_fire", text="Oxy Fire")
        scol.operator("color.wgsn_quiet_wave", text="Quiet Wave")
        scol.operator("color.wgsn_golden_harvest", text="Golden Harvest")
        scol.operator("color.wgsn_bloodstone", text="Bloodstone")
        scol.operator("color.wgsn_dark_springs", text="Dark Springs")
        scol.operator("color.wgsn_electric_magenta", text="Electric Magenta")
        scol.operator("color.wgsn_orchid_flower", text="Orchid Flower")
        scol.operator("color.wgsn_butter", text="Butter")
        scol.operator("color.wgsn_olive_oil", text="Olive Oil")
        scol.operator("color.wgsn_mango_sorbet", text="Mango Sorbet")
        scol.operator("color.wgsn_atlantic_blue", text="Atlantic Blue")
        scol.operator("color.wgsn_honeycomb", text="Honeycomb")
        scol.operator("color.wgsn_jade", text="Jade")
        scol.operator("color.wgsn_dark_oak", text="Dark Oak")
        scol.operator("color.wgsn_lazuli_blue", text="Lazuli Blue")
        scol.operator("color.wgsn_digital_lavender", text="Digital Lavender")
        scol.operator("color.wgsn_luscious_red", text="Luscious Red")
        scol.operator("color.wgsn_sundial", text="Sundial")
        scol.operator("color.wgsn_tranquil_blue", text="Tranquil Blue")
        scol.operator("color.wgsn_verdigris", text="Verdigris")
        scol.operator("color.wgsn_astro_dust", text="Astro Dust")
        scol.operator("color.wgsn_galactic_cobalt", text="Galactic Cobalt")
        scol.operator("color.wgsn_sage_leaf", text="Sage Leaf")
        scol.operator("color.wgsn_apricot_crush", text="Apricot Crush")
        scol.operator("color.wgsn_apricot_crush", text="Apricot Crush")
        scol.operator("color.wgsn_cyber_lime", text="Cyber Lime")
        scol.operator("color.wgsn_elemental_blue", text="Elemental Blue")
        scol.operator("color.wgsn_fondant_pink", text="Fondant Pink")
        scol.operator("color.wgsn_nutshell", text="Nutshell")
        scol.operator("color.wgsn_radiant_red", text="Radiant Red")
        scol.operator("color.wgsn_cool_matcha", text="Cool Matcha")
        scol.operator("color.wgsn_sustained_grey", text="Sustained Grey")
        scol.operator("color.wgsn_midnight_plum", text="Midnight Plum")
        scol.operator("color.wgsn_intense_rust", text="Intense Rust")
        scol.operator("color.wgsn_future_dusk", text="Future Dusk")
        scol.operator("color.wgsn_aquatic_awe", text="Aquatic Awe")
        scol.operator("color.wgsn_ray_flower", text="Ray Flower")
        scol.operator("color.wgsn_sunset_coral", text="Sunset Coral")
        scol.operator("color.wgsn_transcendent_pink", text="Transcendent Pink")
        scol.operator("color.wgsn_celestial_yellow", text="Celestial Yellow")
        scol.operator("color.wgsn_cherry_lacquer", text="Cherry Lacquer")
        scol.operator("color.wgsn_retro_blue", text="Retro Blue")
        scol.operator("color.wgsn_neon_flare", text="Neon Flare")
        scol.operator("color.wgsn_transformative_teal", text="Transformative Teal")
        scol.operator("color.wgsn_blue_aura", text="Blue Aura")
        scol.operator("color.wgsn_electric_fuchsia", text="Electric Fuchsia")
        scol.operator("color.wgsn_jelly_mint", text="Jelly Mint")
        scol.operator("color.wgsn_amber_haze", text="Amber Haze")
        scol.operator("color.wgsn_wax_paper", text="Wax Paper")
        scol.operator("color.wgsn_fresh_purple", text="Fresh Purple")
        scol.operator("color.wgsn_cocoa_powder", text="Cocoa Powder")
        scol.operator("color.wgsn_green_glow", text="Green Glow")
        scol.operator("color.wgsn_luminous_blue", text="Luminous Blue")
        scol.operator("color.wgsn_energy_orange", text="Energy Orange")
        scol.operator("color.wgsn_meadowland_green", text="Meadowland Green")
        scol.operator("color.wgsn_clay", text="Clay")
        scol.operator("color.wgsn_pop_pink", text="Pop Pink")


# WGSN CLASSES
array_wgsn = [
    WGSNPanel,
    WGSN_NeoMint,
    WGSN_Cantaloupe,
    WGSN_Cassis,
    WGSN_MellowYellow,
    WGSN_PuristBlue,
    WGSN_AIAqua,
    WGSN_GoodGray,
    WGSN_LemonSherbet,
    WGSN_OxyFire,
    WGSN_QuietWave,
    WGSN_GoldenHarvest,
    WGSN_Bloodstone,
    WGSN_DarkSprings,
    WGSN_ElectricMagenta,
    WGSN_OrchidFlower,
    WGSN_Butter,
    WGSN_OliveOil,
    WGSN_MangoSorbet,
    WGSN_AtlanticBlue,
    WGSN_Honeycomb,
    WGSN_Jade,
    WGSN_DarkOak,
    WGSN_LazuliBlue,
    WGSN_DigitalLavender,
    WGSN_LusciousRed,
    WGSN_Sundial,
    WGSN_TranquilBlue,
    WGSN_Verdigris,
    WGSN_AstroDust,
    WGSN_GalacticCobalt,
    WGSN_SageLeaf,
    WGSN_ApricotCrush,
    WGSN_ApricotCrush,
    WGSN_CyberLime,
    WGSN_ElementalBlue,
    WGSN_FondantPink,
    WGSN_Nutshell,
    WGSN_RadiantRed,
    WGSN_CoolMatcha,
    WGSN_SustainedGrey,
    WGSN_MidnightPlum,
    WGSN_IntenseRust,
    WGSN_FutureDusk,
    WGSN_AquaticAwe,
    WGSN_RayFlower,
    WGSN_SunsetCoral,
    WGSN_TranscendentPink,
    WGSN_CelestialYellow,
    WGSN_CherryLacquer,
    WGSN_RetroBlue,
    WGSN_NeonFlare,
    WGSN_TransformativeTeal,
    WGSN_BlueAura,
    WGSN_ElectricFuchsia,
    WGSN_JellyMint,
    WGSN_AmberHaze,
    WGSN_WaxPaper,
    WGSN_FreshPurple,
    WGSN_CocoaPowder,
    WGSN_GreenGlow,
    WGSN_LuminousBlue,
    WGSN_EnergyOrange,
    WGSN_MeadowlandGreen,
    WGSN_Clay,
    WGSN_PopPink,
]
