# BSC COLORS SET

import bpy

from .globals import *
from .color_functions import *

# BSC OPERATORS

class BS0001_Canary(bpy.types.Operator):
    """0001 Canary"""
    bl_label = "0001 Canary"
    bl_idname = 'color.0001_canary'
    def execute(self, context):
        set_base_color(0xefc400, self.bl_label)
        return {'FINISHED'}

class BS0002_Oxlip(bpy.types.Operator):
    """0002 Oxlip"""
    bl_label = "0002 Oxlip"
    bl_idname = 'color.0002_oxlip'
    def execute(self, context):
        set_base_color(0xf3b100, self.bl_label)
        return {'FINISHED'}

class BS0003_Golden_Yellow(bpy.types.Operator):
    """0003 Golden Yellow"""
    bl_label = "0003 Golden Yellow"
    bl_idname = 'color.0003_golden_yellow'
    def execute(self, context):
        set_base_color(0xf3a500, self.bl_label)
        return {'FINISHED'}

class BS0004_Marigold(bpy.types.Operator):
    """0004 Marigold"""
    bl_label = "0004 Marigold"
    bl_idname = 'color.0004_marigold'
    def execute(self, context):
        set_base_color(0xe98128, self.bl_label)
        return {'FINISHED'}

class BS0005_Poppy_Red(bpy.types.Operator):
    """0005 Poppy Red"""
    bl_label = "0005 Poppy Red"
    bl_idname = 'color.0005_poppy_red'
    def execute(self, context):
        set_base_color(0xc7361e, self.bl_label)
        return {'FINISHED'}

class BS0006_Post_Office_Red(bpy.types.Operator):
    """0006 Post Office Red"""
    bl_label = "0006 Post Office Red"
    bl_idname = 'color.0006_post_office_red'
    def execute(self, context):
        set_base_color(0x922529, self.bl_label)
        return {'FINISHED'}

class BS0008_Chartreuse(bpy.types.Operator):
    """0008 Chartreuse"""
    bl_label = "0008 Chartreuse"
    bl_idname = 'color.0008_chartreuse'
    def execute(self, context):
        set_base_color(0xcccb00, self.bl_label)
        return {'FINISHED'}

class BS0009_Parakeet(bpy.types.Operator):
    """0009 Parakeet"""
    bl_label = "0009 Parakeet"
    bl_idname = 'color.0009_parakeet'
    def execute(self, context):
        set_base_color(0xacad13, self.bl_label)
        return {'FINISHED'}

class BS0010_Paris_Vir_Green(bpy.types.Operator):
    """0010 Paris / Vir. Green"""
    bl_label = "0010 Paris / Vir. Green"
    bl_idname = 'color.0010_paris_vir_green'
    def execute(self, context):
        set_base_color(0x008c51, self.bl_label)
        return {'FINISHED'}

class BS0011_Baltic_Blue(bpy.types.Operator):
    """0011 Baltic Blue"""
    bl_label = "0011 Baltic Blue"
    bl_idname = 'color.0011_baltic_blue'
    def execute(self, context):
        set_base_color(0x005d62, self.bl_label)
        return {'FINISHED'}

class BS0012_Pacific_Blue(bpy.types.Operator):
    """0012 Pacific Blue"""
    bl_label = "0012 Pacific Blue"
    bl_idname = 'color.0012_pacific_blue'
    def execute(self, context):
        set_base_color(0x137299, self.bl_label)
        return {'FINISHED'}

class BS0013_Anchusa(bpy.types.Operator):
    """0013 Anchusa"""
    bl_label = "0013 Anchusa"
    bl_idname = 'color.0013_anchusa'
    def execute(self, context):
        set_base_color(0x005a7b, self.bl_label)
        return {'FINISHED'}

class BS0014_Nightshade(bpy.types.Operator):
    """0014 Nightshade"""
    bl_label = "0014 Nightshade"
    bl_idname = 'color.0014_nightshade'
    def execute(self, context):
        set_base_color(0x554960, self.bl_label)
        return {'FINISHED'}

class BS1015_Zephyr(bpy.types.Operator):
    """1015 Zephyr"""
    bl_label = "1015 Zephyr"
    bl_idname = 'color.1015_zephyr'
    def execute(self, context):
        set_base_color(0xead4be, self.bl_label)
        return {'FINISHED'}

class BS1016_Pink_Haze(bpy.types.Operator):
    """1016 Pink Haze"""
    bl_label = "1016 Pink Haze"
    bl_idname = 'color.1016_pink_haze'
    def execute(self, context):
        set_base_color(0xc4a89e, self.bl_label)
        return {'FINISHED'}

class BS1017_Rose_Gray(bpy.types.Operator):
    """1017 Rose Gray"""
    bl_label = "1017 Rose Gray"
    bl_idname = 'color.1017_rose_gray'
    def execute(self, context):
        set_base_color(0xa28a88, self.bl_label)
        return {'FINISHED'}

class BS1018_Mecca_Red(bpy.types.Operator):
    """1018 Mecca Red"""
    bl_label = "1018 Mecca Red"
    bl_idname = 'color.1018_mecca_red'
    def execute(self, context):
        set_base_color(0x693c3c, self.bl_label)
        return {'FINISHED'}

class BS1019_Royal_Maroon(bpy.types.Operator):
    """1019 Royal Maroon"""
    bl_label = "1019 Royal Maroon"
    bl_idname = 'color.1019_royal_maroon'
    def execute(self, context):
        set_base_color(0x4a1f1e, self.bl_label)
        return {'FINISHED'}

class BS1020_Daybreak(bpy.types.Operator):
    """1020 Daybreak"""
    bl_label = "1020 Daybreak"
    bl_idname = 'color.1020_daybreak'
    def execute(self, context):
        set_base_color(0xddb3a6, self.bl_label)
        return {'FINISHED'}

class BS1021_Orchis(bpy.types.Operator):
    """1021 Orchis"""
    bl_label = "1021 Orchis"
    bl_idname = 'color.1021_orchis'
    def execute(self, context):
        set_base_color(0xe6998f, self.bl_label)
        return {'FINISHED'}

class BS1022_Reef_Red(bpy.types.Operator):
    """1022 Reef Red"""
    bl_label = "1022 Reef Red"
    bl_idname = 'color.1022_reef_red'
    def execute(self, context):
        set_base_color(0xe17a67, self.bl_label)
        return {'FINISHED'}

class BS1023_Tawney_Red(bpy.types.Operator):
    """1023 Tawney Red"""
    bl_label = "1023 Tawney Red"
    bl_idname = 'color.1023_tawney_red'
    def execute(self, context):
        set_base_color(0xba584c, self.bl_label)
        return {'FINISHED'}

class BS1024_Chestnut(bpy.types.Operator):
    """1024 Chestnut"""
    bl_label = "1024 Chestnut"
    bl_idname = 'color.1024_chestnut'
    def execute(self, context):
        set_base_color(0x803026, self.bl_label)
        return {'FINISHED'}

class BS1025_Crimson_Cherry(bpy.types.Operator):
    """1025 Crimson / Cherry"""
    bl_label = "1025 Crimson / Cherry"
    bl_idname = 'color.1025_crimson_cherry'
    def execute(self, context):
        set_base_color(0x6a2c31, self.bl_label)
        return {'FINISHED'}

class BS2026_Mellow_Buff(bpy.types.Operator):
    """2026 Mellow Buff"""
    bl_label = "2026 Mellow Buff"
    bl_idname = 'color.2026_mellow_buff'
    def execute(self, context):
        set_base_color(0xefcaa6, self.bl_label)
        return {'FINISHED'}

class BS2027_Cygnet(bpy.types.Operator):
    """2027 Cygnet"""
    bl_label = "2027 Cygnet"
    bl_idname = 'color.2027_cygnet'
    def execute(self, context):
        set_base_color(0xc0a691, self.bl_label)
        return {'FINISHED'}

class BS2028_Fallow(bpy.types.Operator):
    """2028 Fallow"""
    bl_label = "2028 Fallow"
    bl_idname = 'color.2028_fallow'
    def execute(self, context):
        set_base_color(0xa7806b, self.bl_label)
        return {'FINISHED'}

class BS2029_Copra(bpy.types.Operator):
    """2029 Copra"""
    bl_label = "2029 Copra"
    bl_idname = 'color.2029_copra'
    def execute(self, context):
        set_base_color(0x7f604e, self.bl_label)
        return {'FINISHED'}

class BS2030_Pink_Beige(bpy.types.Operator):
    """2030 Pink Beige"""
    bl_label = "2030 Pink Beige"
    bl_idname = 'color.2030_pink_beige'
    def execute(self, context):
        set_base_color(0xe2bea1, self.bl_label)
        return {'FINISHED'}

class BS2031_Aurora(bpy.types.Operator):
    """2031 Aurora"""
    bl_label = "2031 Aurora"
    bl_idname = 'color.2031_aurora'
    def execute(self, context):
        set_base_color(0xe0a081, self.bl_label)
        return {'FINISHED'}

class BS2032_Cocoa(bpy.types.Operator):
    """2032 Cocoa"""
    bl_label = "2032 Cocoa"
    bl_idname = 'color.2032_cocoa'
    def execute(self, context):
        set_base_color(0x9b614b, self.bl_label)
        return {'FINISHED'}

class BS3033_Magnolia(bpy.types.Operator):
    """3033 Magnolia"""
    bl_label = "3033 Magnolia"
    bl_idname = 'color.3033_magnolia'
    def execute(self, context):
        set_base_color(0xf0e7d0, self.bl_label)
        return {'FINISHED'}

class BS3034_Vanilla(bpy.types.Operator):
    """3034 Vanilla"""
    bl_label = "3034 Vanilla"
    bl_idname = 'color.3034_vanilla'
    def execute(self, context):
        set_base_color(0xf0dbb9, self.bl_label)
        return {'FINISHED'}

class BS3036_Cobweb(bpy.types.Operator):
    """3036 Cobweb"""
    bl_label = "3036 Cobweb"
    bl_idname = 'color.3036_cobweb'
    def execute(self, context):
        set_base_color(0x9d8a72, self.bl_label)
        return {'FINISHED'}

class BS3037_Buffalo(bpy.types.Operator):
    """3037 Buffalo"""
    bl_label = "3037 Buffalo"
    bl_idname = 'color.3037_buffalo'
    def execute(self, context):
        set_base_color(0x8b816b, self.bl_label)
        return {'FINISHED'}

class BS3038_Congo_Brown(bpy.types.Operator):
    """3038 Congo Brown"""
    bl_label = "3038 Congo Brown"
    bl_idname = 'color.3038_congo_brown'
    def execute(self, context):
        set_base_color(0x574635, self.bl_label)
        return {'FINISHED'}

class BS3039_Chocolate(bpy.types.Operator):
    """3039 Chocolate"""
    bl_label = "3039 Chocolate"
    bl_idname = 'color.3039_chocolate'
    def execute(self, context):
        set_base_color(0x342522, self.bl_label)
        return {'FINISHED'}

class BS3040_Manilla_Pale_Ivory(bpy.types.Operator):
    """3040 Manilla / Pale Ivory"""
    bl_label = "3040 Manilla / Pale Ivory"
    bl_idname = 'color.3040_manilla_pale_ivory'
    def execute(self, context):
        set_base_color(0xefd6ac, self.bl_label)
        return {'FINISHED'}

class BS3041_Maple(bpy.types.Operator):
    """3041 Maple"""
    bl_label = "3041 Maple"
    bl_idname = 'color.3041_maple'
    def execute(self, context):
        set_base_color(0xf0cb96, self.bl_label)
        return {'FINISHED'}

class BS3042_Rich_Cream(bpy.types.Operator):
    """3042 Rich Cream"""
    bl_label = "3042 Rich Cream"
    bl_idname = 'color.3042_rich_cream'
    def execute(self, context):
        set_base_color(0xe7c894, self.bl_label)
        return {'FINISHED'}

class BS3043_Light_Stone(bpy.types.Operator):
    """3043 Light Stone"""
    bl_label = "3043 Light Stone"
    bl_idname = 'color.3043_light_stone'
    def execute(self, context):
        set_base_color(0xbf9c6a, self.bl_label)
        return {'FINISHED'}

class BS3044_Golden_Brown(bpy.types.Operator):
    """3044 Golden Brown"""
    bl_label = "3044 Golden Brown"
    bl_idname = 'color.3044_golden_brown'
    def execute(self, context):
        set_base_color(0x935422, self.bl_label)
        return {'FINISHED'}

class BS3045_Middle_Brown(bpy.types.Operator):
    """3045 Middle Brown"""
    bl_label = "3045 Middle Brown"
    bl_idname = 'color.3045_middle_brown'
    def execute(self, context):
        set_base_color(0x744f33, self.bl_label)
        return {'FINISHED'}

class BS4046_Off_White(bpy.types.Operator):
    """4046 Off White"""
    bl_label = "4046 Off White"
    bl_idname = 'color.4046_off_white'
    def execute(self, context):
        set_base_color(0xf2e5cb, self.bl_label)
        return {'FINISHED'}

class BS4047_Silver_Gleam(bpy.types.Operator):
    """4047 Silver Gleam"""
    bl_label = "4047 Silver Gleam"
    bl_idname = 'color.4047_silver_gleam'
    def execute(self, context):
        set_base_color(0xcdc4a5, self.bl_label)
        return {'FINISHED'}

class BS4048_Stone_Grey(bpy.types.Operator):
    """4048 Stone Grey"""
    bl_label = "4048 Stone Grey"
    bl_idname = 'color.4048_stone_grey'
    def execute(self, context):
        set_base_color(0xb6ab92, self.bl_label)
        return {'FINISHED'}

class BS4049_Eddystone(bpy.types.Operator):
    """4049 Eddystone"""
    bl_label = "4049 Eddystone"
    bl_idname = 'color.4049_eddystone'
    def execute(self, context):
        set_base_color(0x9c9173, self.bl_label)
        return {'FINISHED'}

class BS4050_Olive(bpy.types.Operator):
    """4050 Olive"""
    bl_label = "4050 Olive"
    bl_idname = 'color.4050_olive'
    def execute(self, context):
        set_base_color(0x6e5d2e, self.bl_label)
        return {'FINISHED'}

class BS4051_Montella(bpy.types.Operator):
    """4051 Montella"""
    bl_label = "4051 Montella"
    bl_idname = 'color.4051_montella'
    def execute(self, context):
        set_base_color(0x464130, self.bl_label)
        return {'FINISHED'}

class BS4052_Buttermilk(bpy.types.Operator):
    """4052 Buttermilk"""
    bl_label = "4052 Buttermilk"
    bl_idname = 'color.4052_buttermilk'
    def execute(self, context):
        set_base_color(0xeadab1, self.bl_label)
        return {'FINISHED'}

class BS4053_Jonquil(bpy.types.Operator):
    """4053 Jonquil"""
    bl_label = "4053 Jonquil"
    bl_idname = 'color.4053_jonquil'
    def execute(self, context):
        set_base_color(0xe8e0a1, self.bl_label)
        return {'FINISHED'}

class BS4054_Mimosa_Yellow(bpy.types.Operator):
    """4054 Mimosa Yellow"""
    bl_label = "4054 Mimosa Yellow"
    bl_idname = 'color.4054_mimosa_yellow'
    def execute(self, context):
        set_base_color(0xf2dd84, self.bl_label)
        return {'FINISHED'}

class BS4055_Jasmine_Yellow(bpy.types.Operator):
    """4055 Jasmine Yellow"""
    bl_label = "4055 Jasmine Yellow"
    bl_idname = 'color.4055_jasmine_yellow'
    def execute(self, context):
        set_base_color(0xefdb5f, self.bl_label)
        return {'FINISHED'}

class BS4056_Mustard(bpy.types.Operator):
    """4056 Mustard"""
    bl_label = "4056 Mustard"
    bl_idname = 'color.4056_mustard'
    def execute(self, context):
        set_base_color(0xbfa154, self.bl_label)
        return {'FINISHED'}

class BS4057_Brass(bpy.types.Operator):
    """4057 Brass"""
    bl_label = "4057 Brass"
    bl_idname = 'color.4057_brass'
    def execute(self, context):
        set_base_color(0xdaa20f, self.bl_label)
        return {'FINISHED'}

class BS5058_Gossamer(bpy.types.Operator):
    """5058 Gossamer"""
    bl_label = "5058 Gossamer"
    bl_idname = 'color.5058_gossamer'
    def execute(self, context):
        set_base_color(0xcdcaa6, self.bl_label)
        return {'FINISHED'}

class BS5059_Sky(bpy.types.Operator):
    """5059 Sky"""
    bl_label = "5059 Sky"
    bl_idname = 'color.5059_sky'
    def execute(self, context):
        set_base_color(0xaeb394, self.bl_label)
        return {'FINISHED'}

class BS5050_Quarry_Grey(bpy.types.Operator):
    """5050 Quarry Grey"""
    bl_label = "5050 Quarry Grey"
    bl_idname = 'color.5050_quarry_grey'
    def execute(self, context):
        set_base_color(0x989976, self.bl_label)
        return {'FINISHED'}

class BS5061_Pine_Green(bpy.types.Operator):
    """5061 Pine Green"""
    bl_label = "5061 Pine Green"
    bl_idname = 'color.5061_pine_green'
    def execute(self, context):
        set_base_color(0x465643, self.bl_label)
        return {'FINISHED'}

class BS5062_Yaffie_Green(bpy.types.Operator):
    """5062 Yaffie Green"""
    bl_label = "5062 Yaffie Green"
    bl_idname = 'color.5062_yaffie_green'
    def execute(self, context):
        set_base_color(0xcfd072, self.bl_label)
        return {'FINISHED'}

class BS5063_Moss_Green(bpy.types.Operator):
    """5063 Moss Green"""
    bl_label = "5063 Moss Green"
    bl_idname = 'color.5063_moss_green'
    def execute(self, context):
        set_base_color(0x8e7f2f, self.bl_label)
        return {'FINISHED'}

class BS5064_Bredon_Green(bpy.types.Operator):
    """5064 Bredon Green"""
    bl_label = "5064 Bredon Green"
    bl_idname = 'color.5064_bredon_green'
    def execute(self, context):
        set_base_color(0x697e3f, self.bl_label)
        return {'FINISHED'}

class BS5_5065_Clover_Leaf(bpy.types.Operator):
    """5065 Clover Leaf"""
    bl_label = "5065 Clover Leaf"
    bl_idname = 'color.5065_clover_leaf'
    def execute(self, context):
        set_base_color(0x56653d, self.bl_label)
        return {'FINISHED'}

class BS5066_Grotto(bpy.types.Operator):
    """5066 Grotto"""
    bl_label = "5066 Grotto"
    bl_idname = 'color.5066_grotto'
    def execute(self, context):
        set_base_color(0x899e89, self.bl_label)
        return {'FINISHED'}

class BS5067_Atlantic_Green(bpy.types.Operator):
    """5067 Atlantic Green"""
    bl_label = "5067 Atlantic Green"
    bl_idname = 'color.5067_atlantic_green'
    def execute(self, context):
        set_base_color(0x71826d, self.bl_label)
        return {'FINISHED'}

class BS6068_Marble_Green(bpy.types.Operator):
    """6068 Marble Green"""
    bl_label = "6068 Marble Green"
    bl_idname = 'color.6068_marble_green'
    def execute(self, context):
        set_base_color(0x2b3e34, self.bl_label)
        return {'FINISHED'}

class BS6069_Glacier(bpy.types.Operator):
    """6069 Glacier"""
    bl_label = "6069 Glacier"
    bl_idname = 'color.6069_glacier'
    def execute(self, context):
        set_base_color(0xcad9b5, self.bl_label)
        return {'FINISHED'}

class BS6070_Pastel_Green(bpy.types.Operator):
    """6070 Pastel Green"""
    bl_label = "6070 Pastel Green"
    bl_idname = 'color.6070_pastel_green'
    def execute(self, context):
        set_base_color(0xcad8b1, self.bl_label)
        return {'FINISHED'}

class BS6071_Eau_De_Nil(bpy.types.Operator):
    """6071 Eau De Nil"""
    bl_label = "6071 Eau De Nil"
    bl_idname = 'color.6071_eau_de_nil'
    def execute(self, context):
        set_base_color(0x9ab777, self.bl_label)
        return {'FINISHED'}

class BS6073_Bottle_Green(bpy.types.Operator):
    """6073 Bottle Green"""
    bl_label = "6073 Bottle Green"
    bl_idname = 'color.6073_bottle_green'
    def execute(self, context):
        set_base_color(0x1f5644, self.bl_label)
        return {'FINISHED'}

class BS6074_Mid_Brunswick_Green(bpy.types.Operator):
    """6074 Mid Brunswick Green"""
    bl_label = "6074 Mid Brunswick Green"
    bl_idname = 'color.6074_mid_brunswick_green'
    def execute(self, context):
        set_base_color(0x18482a, self.bl_label)
        return {'FINISHED'}

class BS7075_Horizon_Blue(bpy.types.Operator):
    """7075 Horizon Blue"""
    bl_label = "7075 Horizon Blue"
    bl_idname = 'color.7075_horizon_blue'
    def execute(self, context):
        set_base_color(0xcee1ca, self.bl_label)
        return {'FINISHED'}

class BS7076_Court_Grey(bpy.types.Operator):
    """7076 Court Grey"""
    bl_label = "7076 Court Grey"
    bl_idname = 'color.7076_court_grey'
    def execute(self, context):
        set_base_color(0xa5b2a8, self.bl_label)
        return {'FINISHED'}

class BS7077_Shadow_Blue(bpy.types.Operator):
    """7077 Shadow Blue"""
    bl_label = "7077 Shadow Blue"
    bl_idname = 'color.7077_shadow_blue'
    def execute(self, context):
        set_base_color(0x8ba9a4, self.bl_label)
        return {'FINISHED'}

class BS7078_Light_Grey(bpy.types.Operator):
    """7078 Light Grey"""
    bl_label = "7078 Light Grey"
    bl_idname = 'color.7078_light_grey'
    def execute(self, context):
        set_base_color(0x8c9a94, self.bl_label)
        return {'FINISHED'}

class BS7080_Turquoise_Blue(bpy.types.Operator):
    """7080 Turquoise Blue"""
    bl_label = "7080 Turquoise Blue"
    bl_idname = 'color.7080_turquoise_blue'
    def execute(self, context):
        set_base_color(0x538a8e, self.bl_label)
        return {'FINISHED'}

class BS7081_Narvik(bpy.types.Operator):
    """7081 Narvik"""
    bl_label = "7081 Narvik"
    bl_idname = 'color.7081_narvik'
    def execute(self, context):
        set_base_color(0xccdece, self.bl_label)
        return {'FINISHED'}

class BS7082_Porcelain_Blue(bpy.types.Operator):
    """7082 Porcelain Blue"""
    bl_label = "7082 Porcelain Blue"
    bl_idname = 'color.7082_porcelain_blue'
    def execute(self, context):
        set_base_color(0xa6c8be, self.bl_label)
        return {'FINISHED'}

class BS7083_Ribbon_Blue(bpy.types.Operator):
    """7083 Ribbon Blue"""
    bl_label = "7083 Ribbon Blue"
    bl_idname = 'color.7083_ribbon_blue'
    def execute(self, context):
        set_base_color(0x8ebcbe, self.bl_label)
        return {'FINISHED'}

class BS7084_Fiesta_Blue(bpy.types.Operator):
    """7084 Fiesta Blue"""
    bl_label = "7084 Fiesta Blue"
    bl_idname = 'color.7084_fiesta_blue'
    def execute(self, context):
        set_base_color(0x5b9fad, self.bl_label)
        return {'FINISHED'}

class BS7085_Marine_Blue(bpy.types.Operator):
    """7085 Marine Blue"""
    bl_label = "7085 Marine Blue"
    bl_idname = 'color.7085_marine_blue'
    def execute(self, context):
        set_base_color(0x2c6474, self.bl_label)
        return {'FINISHED'}

class BS7086_Midnight_Blue(bpy.types.Operator):
    """7086 Midnight Blue"""
    bl_label = "7086 Midnight Blue"
    bl_idname = 'color.7086_midnight_blue'
    def execute(self, context):
        set_base_color(0x1d3c4e, self.bl_label)
        return {'FINISHED'}

class BS7087_Steel_Blue(bpy.types.Operator):
    """7087 Steel Blue"""
    bl_label = "7087 Steel Blue"
    bl_idname = 'color.7087_steel_blue'
    def execute(self, context):
        set_base_color(0xbec9cc, self.bl_label)
        return {'FINISHED'}

class BS7088_Wedgewood_Blue(bpy.types.Operator):
    """7088 Wedgewood Blue"""
    bl_label = "7088 Wedgewood Blue"
    bl_idname = 'color.7088_wedgewood_blue'
    def execute(self, context):
        set_base_color(0x7f9fae, self.bl_label)
        return {'FINISHED'}

class BS7089_Castle_Grey(bpy.types.Operator):
    """7089 Castle Grey"""
    bl_label = "7089 Castle Grey"
    bl_idname = 'color.7089_castle_grey'
    def execute(self, context):
        set_base_color(0x868c93, self.bl_label)
        return {'FINISHED'}

class BS8090_Shell_Pink_Columbine(bpy.types.Operator):
    """8090 Shell Pink / Columbine"""
    bl_label = "8090 Shell Pink / Columbine"
    bl_idname = 'color.8090_shell_pink_columbine'
    def execute(self, context):
        set_base_color(0xe7c6bf, self.bl_label)
        return {'FINISHED'}

class BS8091_Cyclamen(bpy.types.Operator):
    """8091 Cyclamen"""
    bl_label = "8091 Cyclamen"
    bl_idname = 'color.8091_cyclamen'
    def execute(self, context):
        set_base_color(0xc16674, self.bl_label)
        return {'FINISHED'}

class BS8092_Regal_Red(bpy.types.Operator):
    """8092 Regal Red"""
    bl_label = "8092 Regal Red"
    bl_idname = 'color.8092_regal_red'
    def execute(self, context):
        set_base_color(0x683045, self.bl_label)
        return {'FINISHED'}

class BS9093_Silver(bpy.types.Operator):
    """9093 Silver"""
    bl_label = "9093 Silver"
    bl_idname = 'color.9093_silver'
    def execute(self, context):
        set_base_color(0xdddac9, self.bl_label)
        return {'FINISHED'}

class BS9094_Flake_Grey(bpy.types.Operator):
    """9094 Flake Grey"""
    bl_label = "9094 Flake Grey"
    bl_idname = 'color.9094_flake_grey'
    def execute(self, context):
        set_base_color(0xc3c2b7, self.bl_label)
        return {'FINISHED'}

class BS9095_Minerva_Grey(bpy.types.Operator):
    """9095 Minerva Grey"""
    bl_label = "9095 Minerva Grey"
    bl_idname = 'color.9095_minerva_grey'
    def execute(self, context):
        set_base_color(0xb2afa6, self.bl_label)
        return {'FINISHED'}

class BS9096_Shire_Grey(bpy.types.Operator):
    """9096 Shire Grey"""
    bl_label = "9096 Shire Grey"
    bl_idname = 'color.9096_shire_grey'
    def execute(self, context):
        set_base_color(0x918f88, self.bl_label)
        return {'FINISHED'}

class BS9097_Dark_Amiralty_Grey(bpy.types.Operator):
    """9097 Dark Amiralty Grey"""
    bl_label = "9097 Dark Amiralty Grey"
    bl_idname = 'color.9097_dark_amiralty_grey'
    def execute(self, context):
        set_base_color(0x5f6669, self.bl_label)
        return {'FINISHED'}

class BS9098_Blue_Grey(bpy.types.Operator):
    """9098 Blue Grey"""
    bl_label = "9098 Blue Grey"
    bl_idname = 'color.9098_blue_grey'
    def execute(self, context):
        set_base_color(0x333e45, self.bl_label)
        return {'FINISHED'}

class BS9100_Graphite(bpy.types.Operator):
    """9100 Graphite"""
    bl_label = "9100 Graphite"
    bl_idname = 'color.9100_graphite'
    def execute(self, context):
        set_base_color(0x8a8679, self.bl_label)
        return {'FINISHED'}

class BS9101_Charcoal(bpy.types.Operator):
    """9101 Charcoal"""
    bl_label = "9101 Charcoal"
    bl_idname = 'color.9101_charcoal'
    def execute(self, context):
        set_base_color(0x676660, self.bl_label)
        return {'FINISHED'}

class BS101_Sky_Blue(bpy.types.Operator):
    """101 Sky Blue"""
    bl_label = "101 Sky Blue"
    bl_idname = 'color.101_sky_blue'
    def execute(self, context):
        set_base_color(0x94bfac, self.bl_label)
        return {'FINISHED'}

class BS102_Turquoise_Blue(bpy.types.Operator):
    """ 102 Turquoise Blue"""
    bl_label = " 102 Turquoise Blue"
    bl_idname = 'color.102_turquoise_blue'
    def execute(self, context):
        set_base_color(0x5b9291, self.bl_label)
        return {'FINISHED'}

class BS103_Peacock_Blue(bpy.types.Operator):
    """ 103 Peacock Blue"""
    bl_label = " 103 Peacock Blue"
    bl_idname = 'color.103_peacock_blue'
    def execute(self, context):
        set_base_color(0x3b6879, self.bl_label)
        return {'FINISHED'}

class BS104_Azure_Blue(bpy.types.Operator):
    """104 Azure Blue"""
    bl_label = "104 Azure Blue"
    bl_idname = 'color.104_azure_blue'
    def execute(self, context):
        set_base_color(0x264d7e, self.bl_label)
        return {'FINISHED'}

class BS105_Oxford_Blue(bpy.types.Operator):
    """105 Oxford Blue"""
    bl_label = "105 Oxford Blue"
    bl_idname = 'color.105_oxford_blue'
    def execute(self, context):
        set_base_color(0x1f3057, self.bl_label)
        return {'FINISHED'}

class BS106_Royal_Blue(bpy.types.Operator):
    """106 Royal Blue"""
    bl_label = "106 Royal Blue"
    bl_idname = 'color.106_royal_blue'
    def execute(self, context):
        set_base_color(0x2a283d, self.bl_label)
        return {'FINISHED'}

class BS107_Strong_Blue_Pacific_Blue(bpy.types.Operator):
    """107 Strong Blue / Pacific Blue"""
    bl_label = "107 Strong Blue / Pacific Blue"
    bl_idname = 'color.107_strong_blue_pacific_blue'
    def execute(self, context):
        set_base_color(0x3a73a9, self.bl_label)
        return {'FINISHED'}

class BS108_Aircraft_Blue(bpy.types.Operator):
    """108 Aircraft Blue"""
    bl_label = "108 Aircraft Blue"
    bl_idname = 'color.108_aircraft_blue'
    def execute(self, context):
        set_base_color(0x173679, self.bl_label)
        return {'FINISHED'}

class BS109_Middle_Blue_Anchusa(bpy.types.Operator):
    """109 Middle Blue / Anchusa"""
    bl_label = "109 Middle Blue / Anchusa"
    bl_idname = 'color.109_middle_blue_anchusa'
    def execute(self, context):
        set_base_color(0x1c5680, self.bl_label)
        return {'FINISHED'}

class BS110_Roundel_Blue(bpy.types.Operator):
    """110 Roundel Blue"""
    bl_label = "110 Roundel Blue"
    bl_idname = 'color.110_roundel_blue'
    def execute(self, context):
        set_base_color(0x2c3e75, self.bl_label)
        return {'FINISHED'}

class BS111_Sky_Blue(bpy.types.Operator):
    """111 Sky Blue"""
    bl_label = "111 Sky Blue"
    bl_idname = 'color.111_sky_blue'
    def execute(self, context):
        set_base_color(0x8cc5bb, self.bl_label)
        return {'FINISHED'}

class BS112_Arctic_Blue_Fiesta_Blue(bpy.types.Operator):
    """112 Arctic Blue / Fiesta Blue"""
    bl_label = "112 Arctic Blue / Fiesta Blue"
    bl_idname = 'color.112_arctic_blue_fiesta_blue'
    def execute(self, context):
        set_base_color(0x78adc2, self.bl_label)
        return {'FINISHED'}

class BS113_Deep_Saxe_Blue(bpy.types.Operator):
    """113 Deep Saxe Blue"""
    bl_label = "113 Deep Saxe Blue"
    bl_idname = 'color.113_deep_saxe_blue'
    def execute(self, context):
        set_base_color(0x3f687d, self.bl_label)
        return {'FINISHED'}

class BS114_Rail_Blue(bpy.types.Operator):
    """114 Rail Blue"""
    bl_label = "114 Rail Blue"
    bl_idname = 'color.114_rail_blue'
    def execute(self, context):
        set_base_color(0x1f4b61, self.bl_label)
        return {'FINISHED'}

class BS115_Cobalt_Blue(bpy.types.Operator):
    """115 Cobalt Blue"""
    bl_label = "115 Cobalt Blue"
    bl_idname = 'color.115_cobalt_blue'
    def execute(self, context):
        set_base_color(0x5f88c1, self.bl_label)
        return {'FINISHED'}

class BS166_French_Blue(bpy.types.Operator):
    """166 French Blue"""
    bl_label = "166 French Blue"
    bl_idname = 'color.166_french_blue'
    def execute(self, context):
        set_base_color(0x2458af, self.bl_label)
        return {'FINISHED'}

class BS172_Pale_Rundel_Blue(bpy.types.Operator):
    """172 Pale Rundel Blue"""
    bl_label = "172 Pale Rundel Blue"
    bl_idname = 'color.172_pale_rundel_blue'
    def execute(self, context):
        set_base_color(0xa7c6eb, self.bl_label)
        return {'FINISHED'}

class BS174_Orient_Blue(bpy.types.Operator):
    """174 Orient Blue"""
    bl_label = "174 Orient Blue"
    bl_idname = 'color.174_orient_blue'
    def execute(self, context):
        set_base_color(0x64a0aa, self.bl_label)
        return {'FINISHED'}

class BS175_Light_French_Blue(bpy.types.Operator):
    """175 Light French Blue"""
    bl_label = "175 Light French Blue"
    bl_idname = 'color.175_light_french_blue'
    def execute(self, context):
        set_base_color(0x4f81c5, self.bl_label)
        return {'FINISHED'}

class BS210_Sky(bpy.types.Operator):
    """210 Sky"""
    bl_label = "210 Sky"
    bl_idname = 'color.210_sky'
    def execute(self, context):
        set_base_color(0xbbc9a5, self.bl_label)
        return {'FINISHED'}

class BS216_Eau_De_Nil(bpy.types.Operator):
    """216 Eau De Nil"""
    bl_label = "216 Eau De Nil"
    bl_idname = 'color.216_eau_de_nil'
    def execute(self, context):
        set_base_color(0xbcd890, self.bl_label)
        return {'FINISHED'}

class BS217_Sea_Green(bpy.types.Operator):
    """217 Sea Green"""
    bl_label = "217 Sea Green"
    bl_idname = 'color.217_sea_green'
    def execute(self, context):
        set_base_color(0x96bf65, self.bl_label)
        return {'FINISHED'}

class BS218_Grass_Green(bpy.types.Operator):
    """218 Grass Green"""
    bl_label = "218 Grass Green"
    bl_idname = 'color.218_grass_green'
    def execute(self, context):
        set_base_color(0x698b47, self.bl_label)
        return {'FINISHED'}

class BS220_Olive_Green(bpy.types.Operator):
    """220 Olive Green"""
    bl_label = "220 Olive Green"
    bl_idname = 'color.220_olive_green'
    def execute(self, context):
        set_base_color(0x4b5729, self.bl_label)
        return {'FINISHED'}

class BS221_Brilliant_Green(bpy.types.Operator):
    """221 Brilliant Green"""
    bl_label = "221 Brilliant Green"
    bl_idname = 'color.221_brilliant_green'
    def execute(self, context):
        set_base_color(0x507d3a, self.bl_label)
        return {'FINISHED'}

class BS222_Light_Bronze_Green(bpy.types.Operator):
    """222 Light Bronze Green"""
    bl_label = "222 Light Bronze Green"
    bl_idname = 'color.222_light_bronze_green'
    def execute(self, context):
        set_base_color(0x6a7031, self.bl_label)
        return {'FINISHED'}

class BS223_Middle_Bronze_Green(bpy.types.Operator):
    """223 Middle Bronze Green"""
    bl_label = "223 Middle Bronze Green"
    bl_idname = 'color.223_middle_bronze_green'
    def execute(self, context):
        set_base_color(0x49523a, self.bl_label)
        return {'FINISHED'}

class BS224_Deep_Bronze_Green(bpy.types.Operator):
    """224 Deep Bronze Green"""
    bl_label = "224 Deep Bronze Green"
    bl_idname = 'color.224_deep_bronze_green'
    def execute(self, context):
        set_base_color(0x3e4630, self.bl_label)
        return {'FINISHED'}

class BS225_Light_Brunswick_Green(bpy.types.Operator):
    """225 Light Brunswick Green"""
    bl_label = "225 Light Brunswick Green"
    bl_idname = 'color.225_light_brunswick_green'
    def execute(self, context):
        set_base_color(0x406a28, self.bl_label)
        return {'FINISHED'}

class BS226_Mid_Brunswick_Green(bpy.types.Operator):
    """226 Mid Brunswick Green"""
    bl_label = "226 Mid Brunswick Green"
    bl_idname = 'color.226_mid_brunswick_green'
    def execute(self, context):
        set_base_color(0x33533b, self.bl_label)
        return {'FINISHED'}

class BS227_Deep_Brunswick_Green(bpy.types.Operator):
    """227 Deep Brunswick Green"""
    bl_label = "227 Deep Brunswick Green"
    bl_idname = 'color.227_deep_brunswick_green'
    def execute(self, context):
        set_base_color(0x254432, self.bl_label)
        return {'FINISHED'}

class BS228_Emerald_Green_Viridian(bpy.types.Operator):
    """228 Emerald Green / Viridian"""
    bl_label = "228 Emerald Green / Viridian"
    bl_idname = 'color.228_emerald_green_viridian'
    def execute(self, context):
        set_base_color(0x428b64, self.bl_label)
        return {'FINISHED'}

class BS241_Dark_Green(bpy.types.Operator):
    """241 Dark Green"""
    bl_label = "241 Dark Green"
    bl_idname = 'color.241_dark_green'
    def execute(self, context):
        set_base_color(0x4f5241, self.bl_label)
        return {'FINISHED'}

class BS262_Bold_Green(bpy.types.Operator):
    """262 Bold Green"""
    bl_label = "262 Bold Green"
    bl_idname = 'color.262_bold_green'
    def execute(self, context):
        set_base_color(0x44945e, self.bl_label)
        return {'FINISHED'}

class BS267_Deep_Chrome_Green_Traffic_Green(bpy.types.Operator):
    """267 Deep Chrome Green / Traffic Green"""
    bl_label = "267 Deep Chrome Green / Traffic Green"
    bl_idname = 'color.267_deep_chrome_green_traffic_green'
    def execute(self, context):
        set_base_color(0x476a4c, self.bl_label)
        return {'FINISHED'}

class BS275_Opaline_Green(bpy.types.Operator):
    """275 Opaline Green"""
    bl_label = "275 Opaline Green"
    bl_idname = 'color.275_opaline_green'
    def execute(self, context):
        set_base_color(0x8fc693, self.bl_label)
        return {'FINISHED'}

class BS278_Light_Olive_Green(bpy.types.Operator):
    """278 Light Olive Green"""
    bl_label = "278 Light Olive Green"
    bl_idname = 'color.278_light_olive_green'
    def execute(self, context):
        set_base_color(0x87965a, self.bl_label)
        return {'FINISHED'}

class BS280_Verdigris_Green(bpy.types.Operator):
    """280 Verdigris Green"""
    bl_label = "280 Verdigris Green"
    bl_idname = 'color.280_verdigris_green'
    def execute(self, context):
        set_base_color(0x68ab77, self.bl_label)
        return {'FINISHED'}

class BS282_Forest_Green(bpy.types.Operator):
    """282 Forest Green"""
    bl_label = "282 Forest Green"
    bl_idname = 'color.282_forest_green'
    def execute(self, context):
        set_base_color(0x506b52, self.bl_label)
        return {'FINISHED'}

class BS283_Aircraft_Grey_Green(bpy.types.Operator):
    """283 Aircraft Grey Green"""
    bl_label = "283 Aircraft Grey Green"
    bl_idname = 'color.283_aircraft_grey_green'
    def execute(self, context):
        set_base_color(0x7e8f6e, self.bl_label)
        return {'FINISHED'}

class BS284_Spruce_Green(bpy.types.Operator):
    """284 Spruce Green"""
    bl_label = "284 Spruce Green"
    bl_idname = 'color.284_spruce_green'
    def execute(self, context):
        set_base_color(0x6b6f5a, self.bl_label)
        return {'FINISHED'}

class BS285_Nato_Green(bpy.types.Operator):
    """285 Nato Green"""
    bl_label = "285 Nato Green"
    bl_idname = 'color.285_nato_green'
    def execute(self, context):
        set_base_color(0x5f5c4b, self.bl_label)
        return {'FINISHED'}

class BS298_Olive_Drab(bpy.types.Operator):
    """298 Olive Drab"""
    bl_label = "298 Olive Drab"
    bl_idname = 'color.298_olive_drab'
    def execute(self, context):
        set_base_color(0x4f5138, self.bl_label)
        return {'FINISHED'}

class BS309_Canary_Yellow(bpy.types.Operator):
    """309 Canary Yellow"""
    bl_label = "309 Canary Yellow"
    bl_idname = 'color.309_canary_yellow'
    def execute(self, context):
        set_base_color(0xfeec04, self.bl_label)
        return {'FINISHED'}

class BS310_Primrose(bpy.types.Operator):
    """310 Primrose"""
    bl_label = "310 Primrose"
    bl_idname = 'color.310_primrose'
    def execute(self, context):
        set_base_color(0xfef963, self.bl_label)
        return {'FINISHED'}

class BS315_Grapefruit(bpy.types.Operator):
    """315 Grapefruit"""
    bl_label = "315 Grapefruit"
    bl_idname = 'color.315_grapefruit'
    def execute(self, context):
        set_base_color(0xfef96a, self.bl_label)
        return {'FINISHED'}

class BS320_Light_Brown(bpy.types.Operator):
    """320 Light Brown"""
    bl_label = "320 Light Brown"
    bl_idname = 'color.320_light_brown'
    def execute(self, context):
        set_base_color(0x9e7339, self.bl_label)
        return {'FINISHED'}

class BS337_Very_Dark_Drab(bpy.types.Operator):
    """337 Very Dark Drab"""
    bl_label = "337 Very Dark Drab"
    bl_idname = 'color.337_very_dark_drab'
    def execute(self, context):
        set_base_color(0x4c4a3c, self.bl_label)
        return {'FINISHED'}

class BS350_Dark_Earth(bpy.types.Operator):
    """350 Dark Earth"""
    bl_label = "350 Dark Earth"
    bl_idname = 'color.350_dark_earth'
    def execute(self, context):
        set_base_color(0x7b6b4f, self.bl_label)
        return {'FINISHED'}

class BS352_Pale_Cream(bpy.types.Operator):
    """352 Pale Cream"""
    bl_label = "352 Pale Cream"
    bl_idname = 'color.352_pale_cream'
    def execute(self, context):
        set_base_color(0xfced96, self.bl_label)
        return {'FINISHED'}

class BS353_Deep_Cream(bpy.types.Operator):
    """353 Deep Cream"""
    bl_label = "353 Deep Cream"
    bl_idname = 'color.353_deep_cream'
    def execute(self, context):
        set_base_color(0xfdf07a, self.bl_label)
        return {'FINISHED'}

class BS355_Lemon(bpy.types.Operator):
    """355 Lemon"""
    bl_label = "355 Lemon"
    bl_idname = 'color.355_lemon'
    def execute(self, context):
        set_base_color(0xfdd906, self.bl_label)
        return {'FINISHED'}

class BS356_Golden_Yellow(bpy.types.Operator):
    """356 Golden Yellow"""
    bl_label = "356 Golden Yellow"
    bl_idname = 'color.356_golden_yellow'
    def execute(self, context):
        set_base_color(0xfcc808, self.bl_label)
        return {'FINISHED'}

class BS358_Light_Buff(bpy.types.Operator):
    """358 Light Buff"""
    bl_label = "358 Light Buff"
    bl_idname = 'color.358_light_buff'
    def execute(self, context):
        set_base_color(0xf6c870, self.bl_label)
        return {'FINISHED'}

class BS359_Middle_Buff(bpy.types.Operator):
    """359 Middle Buff"""
    bl_label = "359 Middle Buff"
    bl_idname = 'color.359_middle_buff'
    def execute(self, context):
        set_base_color(0xdbac50, self.bl_label)
        return {'FINISHED'}

class BS361_Light_Stone(bpy.types.Operator):
    """361 Light Stone"""
    bl_label = "361 Light Stone"
    bl_idname = 'color.361_light_stone'
    def execute(self, context):
        set_base_color(0xd4b97d, self.bl_label)
        return {'FINISHED'}

class BS363_Bold_Yellow(bpy.types.Operator):
    """363 Bold Yellow"""
    bl_label = "363 Bold Yellow"
    bl_idname = 'color.363_bold_yellow'
    def execute(self, context):
        set_base_color(0xeec200, self.bl_label)
        return {'FINISHED'}

class BS365_Vellum(bpy.types.Operator):
    """365 Vellum"""
    bl_label = "365 Vellum"
    bl_idname = 'color.365_vellum'
    def execute(self, context):
        set_base_color(0xf4f0bd, self.bl_label)
        return {'FINISHED'}

class BS366_Light_Beige(bpy.types.Operator):
    """366 Light Beige"""
    bl_label = "366 Light Beige"
    bl_idname = 'color.366_light_beige'
    def execute(self, context):
        set_base_color(0xf5e7a1, self.bl_label)
        return {'FINISHED'}

class BS367_Manilla(bpy.types.Operator):
    """367 Manilla"""
    bl_label = "367 Manilla"
    bl_idname = 'color.367_manilla'
    def execute(self, context):
        set_base_color(0xfef6bf, self.bl_label)
        return {'FINISHED'}

class BS369_Biscuit(bpy.types.Operator):
    """369 Biscuit"""
    bl_label = "369 Biscuit"
    bl_idname = 'color.369_biscuit'
    def execute(self, context):
        set_base_color(0xfeeba8, self.bl_label)
        return {'FINISHED'}

class BS380_Camouflage_Desert_Sand(bpy.types.Operator):
    """380 Camouflage Desert Sand"""
    bl_label = "380 Camouflage Desert Sand"
    bl_idname = 'color.380_camouflage_desert_sand'
    def execute(self, context):
        set_base_color(0xbba38a, self.bl_label)
        return {'FINISHED'}

class BS384_Light_Straw(bpy.types.Operator):
    """384 Light Straw"""
    bl_label = "384 Light Straw"
    bl_idname = 'color.384_light_straw'
    def execute(self, context):
        set_base_color(0xeedfa5, self.bl_label)
        return {'FINISHED'}

class BS388_Beige(bpy.types.Operator):
    """388 Beige"""
    bl_label = "388 Beige"
    bl_idname = 'color.388_beige'
    def execute(self, context):
        set_base_color(0xe4cf93, self.bl_label)
        return {'FINISHED'}

class BS389_Camouflage_Beige(bpy.types.Operator):
    """389 Camouflage Beige"""
    bl_label = "389 Camouflage Beige"
    bl_idname = 'color.389_camouflage_beige'
    def execute(self, context):
        set_base_color(0xb2a788, self.bl_label)
        return {'FINISHED'}

class BS411_Middle_Brown(bpy.types.Operator):
    """411 Middle Brown"""
    bl_label = "411 Middle Brown"
    bl_idname = 'color.411_middle_brown'
    def execute(self, context):
        set_base_color(0x74542f, self.bl_label)
        return {'FINISHED'}

class BS412_Dark_Brown(bpy.types.Operator):
    """412 Dark Brown"""
    bl_label = "412 Dark Brown"
    bl_idname = 'color.412_dark_brown'
    def execute(self, context):
        set_base_color(0x5c422e, self.bl_label)
        return {'FINISHED'}

class BS414_Golden_Brown(bpy.types.Operator):
    """414 Golden Brown"""
    bl_label = "414 Golden Brown"
    bl_idname = 'color.414_golden_brown'
    def execute(self, context):
        set_base_color(0xa86c29, self.bl_label)
        return {'FINISHED'}

class BS420_Dark_Camouflage_Desert_Sand(bpy.types.Operator):
    """420 Dark Camouflage Desert Sand"""
    bl_label = "420 Dark Camouflage Desert Sand"
    bl_idname = 'color.420_dark_camouflage_desert_sand'
    def execute(self, context):
        set_base_color(0xa89177, self.bl_label)
        return {'FINISHED'}

class BS435_Camouflage_Red(bpy.types.Operator):
    """435 Camouflage Red"""
    bl_label = "435 Camouflage Red"
    bl_idname = 'color.435_camouflage_red'
    def execute(self, context):
        set_base_color(0x845b4d, self.bl_label)
        return {'FINISHED'}

class BS436_Dark_Camouflage_Brown(bpy.types.Operator):
    """436 Dark Camouflage Brown"""
    bl_label = "436 Dark Camouflage Brown"
    bl_idname = 'color.436_dark_camouflage_brown'
    def execute(self, context):
        set_base_color(0x564b47, self.bl_label)
        return {'FINISHED'}

class BS444_Terracotta(bpy.types.Operator):
    """444 Terracotta"""
    bl_label = "444 Terracotta"
    bl_idname = 'color.444_terracotta'
    def execute(self, context):
        set_base_color(0xa65341, self.bl_label)
        return {'FINISHED'}

class BS445_Venetian_Red(bpy.types.Operator):
    """445 Venetian Red"""
    bl_label = "445 Venetian Red"
    bl_idname = 'color.445_venetian_red'
    def execute(self, context):
        set_base_color(0x83422b, self.bl_label)
        return {'FINISHED'}

class BS446_Red_Oxide(bpy.types.Operator):
    """446 Red Oxide"""
    bl_label = "446 Red Oxide"
    bl_idname = 'color.446_red_oxide'
    def execute(self, context):
        set_base_color(0x774430, self.bl_label)
        return {'FINISHED'}

class BS447_Salmon_Pink(bpy.types.Operator):
    """447 Salmon Pink"""
    bl_label = "447 Salmon Pink"
    bl_idname = 'color.447_salmon_pink'
    def execute(self, context):
        set_base_color(0xf3b28b, self.bl_label)
        return {'FINISHED'}

class BS448_Deep_Indian_Red(bpy.types.Operator):
    """448 Deep Indian Red"""
    bl_label = "448 Deep Indian Red"
    bl_idname = 'color.448_deep_indian_red'
    def execute(self, context):
        set_base_color(0x67403a, self.bl_label)
        return {'FINISHED'}

class BS449_Light_Purple_Brown(bpy.types.Operator):
    """449 Light Purple Brown"""
    bl_label = "449 Light Purple Brown"
    bl_idname = 'color.449_light_purple_brown'
    def execute(self, context):
        set_base_color(0x693b3f, self.bl_label)
        return {'FINISHED'}

class BS452_Dark_Crimson(bpy.types.Operator):
    """452 Dark Crimson"""
    bl_label = "452 Dark Crimson"
    bl_idname = 'color.452_dark_crimson'
    def execute(self, context):
        set_base_color(0x613339, self.bl_label)
        return {'FINISHED'}

class BS453_Shell_Pink(bpy.types.Operator):
    """453 Shell Pink"""
    bl_label = "453 Shell Pink"
    bl_idname = 'color.453_shell_pink'
    def execute(self, context):
        set_base_color(0xfbded6, self.bl_label)
        return {'FINISHED'}

class BS454_Pale_Roundel_Red(bpy.types.Operator):
    """454 Pale Roundel Red"""
    bl_label = "454 Pale Roundel Red"
    bl_idname = 'color.454_pale_roundel_red'
    def execute(self, context):
        set_base_color(0xe8a1a2, self.bl_label)
        return {'FINISHED'}

class BS460_Deep_Buff(bpy.types.Operator):
    """460 Deep Buff"""
    bl_label = "460 Deep Buff"
    bl_idname = 'color.460_deep_buff'
    def execute(self, context):
        set_base_color(0xbd8f56, self.bl_label)
        return {'FINISHED'}

class BS473_Gulf_Red(bpy.types.Operator):
    """473 Gulf Red"""
    bl_label = "473 Gulf Red"
    bl_idname = 'color.473_gulf_red'
    def execute(self, context):
        set_base_color(0x793932, self.bl_label)
        return {'FINISHED'}

class BS489_Leaf_Brown(bpy.types.Operator):
    """489 Leaf Brown"""
    bl_label = "489 Leaf Brown"
    bl_idname = 'color.489_leaf_brown'
    def execute(self, context):
        set_base_color(0x8d5b41, self.bl_label)
        return {'FINISHED'}

class BS499_Service_Brown(bpy.types.Operator):
    """499 Service Brown"""
    bl_label = "499 Service Brown"
    bl_idname = 'color.499_service_brown'
    def execute(self, context):
        set_base_color(0x59493e, self.bl_label)
        return {'FINISHED'}

class BS537_Signal_Red(bpy.types.Operator):
    """537 Signal Red"""
    bl_label = "537 Signal Red"
    bl_idname = 'color.537_signal_red'
    def execute(self, context):
        set_base_color(0xdd3420, self.bl_label)
        return {'FINISHED'}

class BS538_Post_Office_Red_Cherry(bpy.types.Operator):
    """538 Post Office Red / Cherry"""
    bl_label = "538 Post Office Red / Cherry"
    bl_idname = 'color.538_post_office_red_cherry'
    def execute(self, context):
        set_base_color(0xc41c22, self.bl_label)
        return {'FINISHED'}

class BS539_Currant_Red(bpy.types.Operator):
    """539 Currant Red"""
    bl_label = "539 Currant Red"
    bl_idname = 'color.539_currant_red'
    def execute(self, context):
        set_base_color(0xd21e2b, self.bl_label)
        return {'FINISHED'}

class BS540_Crimson(bpy.types.Operator):
    """540 Crimson"""
    bl_label = "540 Crimson"
    bl_idname = 'color.540_crimson'
    def execute(self, context):
        set_base_color(0x8b1a32, self.bl_label)
        return {'FINISHED'}

class BS541_Maroon(bpy.types.Operator):
    """541 Maroon"""
    bl_label = "541 Maroon"
    bl_idname = 'color.541_maroon'
    def execute(self, context):
        set_base_color(0x471b21, self.bl_label)
        return {'FINISHED'}

class BS542_Ruby(bpy.types.Operator):
    """542 Ruby"""
    bl_label = "542 Ruby"
    bl_idname = 'color.542_ruby'
    def execute(self, context):
        set_base_color(0x982d57, self.bl_label)
        return {'FINISHED'}

class BS557_Light_Orange(bpy.types.Operator):
    """557 Light Orange"""
    bl_label = "557 Light Orange"
    bl_idname = 'color.557_light_orange'
    def execute(self, context):
        set_base_color(0xef841e, self.bl_label)
        return {'FINISHED'}

class BS564_Bold_Red(bpy.types.Operator):
    """564 Bold Red"""
    bl_label = "564 Bold Red"
    bl_idname = 'color.564_bold_red'
    def execute(self, context):
        set_base_color(0xdd3524, self.bl_label)
        return {'FINISHED'}

class BS568_Apricot(bpy.types.Operator):
    """568 Apricot"""
    bl_label = "568 Apricot"
    bl_idname = 'color.568_apricot'
    def execute(self, context):
        set_base_color(0xfb9c06, self.bl_label)
        return {'FINISHED'}

class BS592_International_Orange(bpy.types.Operator):
    """592 International Orange"""
    bl_label = "592 International Orange"
    bl_idname = 'color.592_international_orange'
    def execute(self, context):
        set_base_color(0xe45523, self.bl_label)
        return {'FINISHED'}

class BS593_Rail_Red_Azo_Orange(bpy.types.Operator):
    """593 Rail Red / Azo Orange"""
    bl_label = "593 Rail Red / Azo Orange"
    bl_idname = 'color.593_rail_red_azo_orange'
    def execute(self, context):
        set_base_color(0xf24816, self.bl_label)
        return {'FINISHED'}

class BS626_Camouflage_Grey(bpy.types.Operator):
    """626 Camouflage Grey"""
    bl_label = "626 Camouflage Grey"
    bl_idname = 'color.626_camouflage_grey'
    def execute(self, context):
        set_base_color(0xa0a9aa, self.bl_label)
        return {'FINISHED'}

class BS627_Light_Aircraft_Grey(bpy.types.Operator):
    """627 Light Aircraft Grey"""
    bl_label = "627 Light Aircraft Grey"
    bl_idname = 'color.627_light_aircraft_grey'
    def execute(self, context):
        set_base_color(0xbec0b8, self.bl_label)
        return {'FINISHED'}

class BS629_Dark_Camouflage_Grey_Quaker_Grey(bpy.types.Operator):
    """629 Dark Camouflage Grey / Quaker Grey"""
    bl_label = "629 Dark Camouflage Grey / Quaker Grey"
    bl_idname = 'color.629_dark_camouflage_grey_quacker_grey'
    def execute(self, context):
        set_base_color(0x7a838b, self.bl_label)
        return {'FINISHED'}

class BS630_French_Grey(bpy.types.Operator):
    """630 French Grey"""
    bl_label = "630 French Grey"
    bl_idname = 'color.630_french_grey'
    def execute(self, context):
        set_base_color(0xa5ad98, self.bl_label)
        return {'FINISHED'}

class BS631_Light_Grey(bpy.types.Operator):
    """631 Light Grey"""
    bl_label = "631 Light Grey"
    bl_idname = 'color.631_light_grey'
    def execute(self, context):
        set_base_color(0x9aaa9f, self.bl_label)
        return {'FINISHED'}

class BS632_Dark_Admiralty_Grey(bpy.types.Operator):
    """632 Dark Admiralty Grey"""
    bl_label = "632 Dark Admiralty Grey"
    bl_idname = 'color.632_dark_admiralty_grey'
    def execute(self, context):
        set_base_color(0x6b7477, self.bl_label)
        return {'FINISHED'}

class BS633_Raf_Blue_Grey(bpy.types.Operator):
    """633 Raf Blue Grey"""
    bl_label = "633 Raf Blue Grey"
    bl_idname = 'color.633_raf_blue_grey'
    def execute(self, context):
        set_base_color(0x424c53, self.bl_label)
        return {'FINISHED'}

class BS634_Slate(bpy.types.Operator):
    """634 Slate"""
    bl_label = "634 Slate"
    bl_idname = 'color.634_slate'
    def execute(self, context):
        set_base_color(0x6f7264, self.bl_label)
        return {'FINISHED'}

class BS635_Lead(bpy.types.Operator):
    """635 Lead"""
    bl_label = "635 Lead"
    bl_idname = 'color.635_lead'
    def execute(self, context):
        set_base_color(0x525b55, self.bl_label)
        return {'FINISHED'}

class BS636_Pru_Blue(bpy.types.Operator):
    """636 Pru Blue"""
    bl_label = "636 Pru Blue"
    bl_idname = 'color.636_pru_blue'
    def execute(self, context):
        set_base_color(0x5f7682, self.bl_label)
        return {'FINISHED'}

class BS637_Medium_Sea_Grey(bpy.types.Operator):
    """637 Medium Sea Grey"""
    bl_label = "637 Medium Sea Grey"
    bl_idname = 'color.637_medium_sea_grey'
    def execute(self, context):
        set_base_color(0x8e9b9c, self.bl_label)
        return {'FINISHED'}

class BS638_Dark_Sea_Grey(bpy.types.Operator):
    """638 Dark Sea Grey"""
    bl_label = "638 Dark Sea Grey"
    bl_idname = 'color.638_dark_sea_grey'
    def execute(self, context):
        set_base_color(0x6c7377, self.bl_label)
        return {'FINISHED'}

class BS639_Light_Slate_Grey(bpy.types.Operator):
    """639 Light Slate Grey"""
    bl_label = "639 Light Slate Grey"
    bl_idname = 'color.639_light_slate_grey'
    def execute(self, context):
        set_base_color(0x667563, self.bl_label)
        return {'FINISHED'}

class BS640_Extra_Dark_Sea_Grey(bpy.types.Operator):
    """640 Extra Dark Sea Grey"""
    bl_label = "640 Extra Dark Sea Grey"
    bl_idname = 'color.640_extra_dark_sea_grey'
    def execute(self, context):
        set_base_color(0x566164, self.bl_label)
        return {'FINISHED'}

class BS642_Night(bpy.types.Operator):
    """642 Night"""
    bl_label = "642 Night"
    bl_idname = 'color.642_night'
    def execute(self, context):
        set_base_color(0x282b2f, self.bl_label)
        return {'FINISHED'}

class BS671_Middle_Graphite(bpy.types.Operator):
    """671 Middle Graphite"""
    bl_label = "671 Middle Graphite"
    bl_idname = 'color.671_middle_graphite'
    def execute(self, context):
        set_base_color(0x4e5355, self.bl_label)
        return {'FINISHED'}

class BS676_Light_Weatherwork_Grey(bpy.types.Operator):
    """676 Light Weatherwork Grey"""
    bl_label = "676 Light Weatherwork Grey"
    bl_idname = 'color.676_light_weatherwork_grey'
    def execute(self, context):
        set_base_color(0xa9b7b9, self.bl_label)
        return {'FINISHED'}

class BS677_Dark_Weatherwork_Grey(bpy.types.Operator):
    """677 Dark Weatherwork Grey"""
    bl_label = "677 Dark Weatherwork Grey"
    bl_idname = 'color.677_dark_weatherwork_grey'
    def execute(self, context):
        set_base_color(0x676f76, self.bl_label)
        return {'FINISHED'}

class BS692_Smoke_Grey(bpy.types.Operator):
    """692 Smoke Grey"""
    bl_label = "692 Smoke Grey"
    bl_idname = 'color.692_smoke_grey'
    def execute(self, context):
        set_base_color(0x7b93a3, self.bl_label)
        return {'FINISHED'}

class BS693_Aircraft_Grey(bpy.types.Operator):
    """693 Aircraft Grey"""
    bl_label = "693 Aircraft Grey"
    bl_idname = 'color.693_aircraft_grey'
    def execute(self, context):
        set_base_color(0x88918d, self.bl_label)
        return {'FINISHED'}

class BS694_Dove_Grey(bpy.types.Operator):
    """694 Dove Grey"""
    bl_label = "694 Dove Grey"
    bl_idname = 'color.694_dove_grey'
    def execute(self, context):
        set_base_color(0x909a92, self.bl_label)
        return {'FINISHED'}

class BS697_Light_Admiralty_Grey(bpy.types.Operator):
    """697 Light Admiralty Grey"""
    bl_label = "697 Light Admiralty Grey"
    bl_idname = 'color.697_light_admiralty_grey'
    def execute(self, context):
        set_base_color(0xb6d3cc, self.bl_label)
        return {'FINISHED'}

class BS796_Dark_Violet(bpy.types.Operator):
    """796 Dark Violet"""
    bl_label = "796 Dark Violet"
    bl_idname = 'color.796_dark_violet'
    def execute(self, context):
        set_base_color(0x6e4a75, self.bl_label)
        return {'FINISHED'}

class BS797_Light_Violet(bpy.types.Operator):
    """797 Light Violet"""
    bl_label = "797 Light Violet"
    bl_idname = 'color.797_light_violet'
    def execute(self, context):
        set_base_color(0xc9a8ce, self.bl_label)
        return {'FINISHED'}

class BS00_A_01_Ash_Grey_Oyster_Grey_Portland(bpy.types.Operator):
    """00-A-01 Ash Grey / Oyster Grey / Portland"""
    bl_label = "00-A-01 Ash Grey / Oyster Grey / Portland"
    bl_idname = 'color.00_a_01_ash_grey_oyster_grey_portland'
    def execute(self, context):
        set_base_color(0xdeded2, self.bl_label)
        return {'FINISHED'}

class BS00_A_03_Grey(bpy.types.Operator):
    """00-A-03 Grey"""
    bl_label = "00-A-03 Grey"
    bl_idname = 'color.00_a_03_grey'
    def execute(self, context):
        set_base_color(0xbeb7a7, self.bl_label)
        return {'FINISHED'}

class BS00_A_05_Goose_Grey_Sea_Mist_Goosewing(bpy.types.Operator):
    """00-A-05 Goose Grey / Sea Mist / Goosewing"""
    bl_label = "00-A-05 Goose Grey / Sea Mist / Goosewing"
    bl_idname = 'color.00_a_05_goose_grey_sea_mist_goosewing'
    def execute(self, context):
        set_base_color(0x848889, self.bl_label)
        return {'FINISHED'}

class BS00_A_07_Grey(bpy.types.Operator):
    """00-A-07 Grey"""
    bl_label = "00-A-07 Grey"
    bl_idname = 'color.00_a_07_grey'
    def execute(self, context):
        set_base_color(0x7c7e81, self.bl_label)
        return {'FINISHED'}

class BS00_A_09_Flint_Grey_Flint(bpy.types.Operator):
    """00-A-09 Flint Grey / Flint"""
    bl_label = "00-A-09 Flint Grey / Flint"
    bl_idname = 'color.00_a_09_flint_grey_flint'
    def execute(self, context):
        set_base_color(0x555f68, self.bl_label)
        return {'FINISHED'}

class BS00_A_11_Grey(bpy.types.Operator):
    """00-A-11 Grey"""
    bl_label = "00-A-11 Grey"
    bl_idname = 'color.00_a_11_grey'
    def execute(self, context):
        set_base_color(0x414549, self.bl_label)
        return {'FINISHED'}

class BS00_A_13_Storm_Grey_Greyfriar(bpy.types.Operator):
    """00-A-13 Storm Grey / Greyfriar"""
    bl_label = "00-A-13 Storm Grey / Greyfriar"
    bl_idname = 'color.00_a_13_storm_grey_greyfriar'
    def execute(self, context):
        set_base_color(0x363e42, self.bl_label)
        return {'FINISHED'}

class BS00_E_53_Black(bpy.types.Operator):
    """00-E-53 Black"""
    bl_label = "00-E-53 Black"
    bl_idname = 'color.00_e_53_black'
    def execute(self, context):
        set_base_color(0x0b0e10, self.bl_label)
        return {'FINISHED'}

class BS00_E_55_White(bpy.types.Operator):
    """00-E-55 White"""
    bl_label = "00-E-55 White"
    bl_idname = 'color.00_e_55_white'
    def execute(self, context):
        set_base_color(0xffffff, self.bl_label)
        return {'FINISHED'}

class BS02_A_03_Grey(bpy.types.Operator):
    """02-A-03 Grey"""
    bl_label = "02-A-03 Grey"
    bl_idname = 'color.02_a_03_grey'
    def execute(self, context):
        set_base_color(0xd2d2d2, self.bl_label)
        return {'FINISHED'}

class BS02_A_07_Grey(bpy.types.Operator):
    """02-A-07 Grey"""
    bl_label = "02-A-07 Grey"
    bl_idname = 'color.02_a_07_grey'
    def execute(self, context):
        set_base_color(0x92969b, self.bl_label)
        return {'FINISHED'}

class BS02_A_11_Grey(bpy.types.Operator):
    """02-A-11 Grey"""
    bl_label = "02-A-11 Grey"
    bl_idname = 'color.02_a_11_grey'
    def execute(self, context):
        set_base_color(0x4d4e51, self.bl_label)
        return {'FINISHED'}

class BS02_C_33_Lupin_Pink_Candy_Floss_Pink_Wafer(bpy.types.Operator):
    """02-C-33 Lupin Pink / Candy Floss / Pink Wafer"""
    bl_label = "02-C-33 Lupin Pink / Candy Floss / Pink Wafer"
    bl_idname = 'color.02_c_33_lupin_pink_candy_floss_pink_wafer'
    def execute(self, context):
        set_base_color(0xe4c0c4, self.bl_label)
        return {'FINISHED'}

class BS02_C_35_Pink(bpy.types.Operator):
    """02-C-35 Pink"""
    bl_label = "02-C-35 Pink"
    bl_idname = 'color.02_c_35_pink'
    def execute(self, context):
        set_base_color(0xf9bbcb, self.bl_label)
        return {'FINISHED'}

class BS02_C_37_Clover_Pink_Corinth_Fontana(bpy.types.Operator):
    """02-C-37 Clover Pink / Corinth / Fontana"""
    bl_label = "02-C-37 Clover Pink / Corinth / Fontana"
    bl_idname = 'color.02_c_37_clover_pink_corinth_fontana'
    def execute(self, context):
        set_base_color(0x8c5367, self.bl_label)
        return {'FINISHED'}

class BS02_C_39_Victoria_Plum_Aubergine_Plum(bpy.types.Operator):
    """02-C-39 Victoria Plum / Aubergine / Plum"""
    bl_label = "02-C-39 Victoria Plum / Aubergine / Plum"
    bl_idname = 'color.02_c_39_victoria_plum_aubergine_plum'
    def execute(self, context):
        set_base_color(0x764a57, self.bl_label)
        return {'FINISHED'}

class BS02_C_40_Deep_Plum_Loganberry(bpy.types.Operator):
    """02-C-40 Deep Plum / Loganberry"""
    bl_label = "02-C-40 Deep Plum / Loganberry"
    bl_idname = 'color.02_c_40_deep_plum_loganberry'
    def execute(self, context):
        set_base_color(0x3e3035, self.bl_label)
        return {'FINISHED'}

class BS02_D_41_Pink(bpy.types.Operator):
    """02-D-41 Pink"""
    bl_label = "02-D-41 Pink"
    bl_idname = 'color.02_d_41_pink'
    def execute(self, context):
        set_base_color(0xde776f, self.bl_label)
        return {'FINISHED'}

class BS02_D_43_Pink(bpy.types.Operator):
    """02-D-43 Pink"""
    bl_label = "02-D-43 Pink"
    bl_idname = 'color.02_d_43_pink'
    def execute(self, context):
        set_base_color(0xc44a5e, self.bl_label)
        return {'FINISHED'}

class BS02_D_44_Pink(bpy.types.Operator):
    """02-D-44 Pink"""
    bl_label = "02-D-44 Pink"
    bl_idname = 'color.02_d_44_pink'
    def execute(self, context):
        set_base_color(0x9a2a41, self.bl_label)
        return {'FINISHED'}

class BS02_D_45_Purple(bpy.types.Operator):
    """02-D-45 Purple"""
    bl_label = "02-D-45 Purple"
    bl_idname = 'color.02_d_45_purple'
    def execute(self, context):
        set_base_color(0x62172b, self.bl_label)
        return {'FINISHED'}

class BS02_E_53_Purple(bpy.types.Operator):
    """02-E-53 Purple"""
    bl_label = "02-E-53 Purple"
    bl_idname = 'color.02_e_53_purple'
    def execute(self, context):
        set_base_color(0xbf3e50, self.bl_label)
        return {'FINISHED'}

class BS02_E_56_Deep_Pink(bpy.types.Operator):
    """02-E-56 Deep Pink"""
    bl_label = "02-E-56 Deep Pink"
    bl_idname = 'color.02_e_56_deep_pink'
    def execute(self, context):
        set_base_color(0x8f2437, self.bl_label)
        return {'FINISHED'}

class BS02_E_58_Bordeaux(bpy.types.Operator):
    """02-E-58 Bordeaux"""
    bl_label = "02-E-58 Bordeaux"
    bl_idname = 'color.02_e_58_bordeaux'
    def execute(self, context):
        set_base_color(0x440b19, self.bl_label)
        return {'FINISHED'}

class BS04_B_15_Rosepetal_Pastel_Pink_Dawn_Pink(bpy.types.Operator):
    """04-B-15 Rosepetal / Pastel Pink / Dawn Pink"""
    bl_label = "04-B-15 Rosepetal / Pastel Pink / Dawn Pink"
    bl_idname = 'color.04_b_15_rosepetal_pastel_pink_dawn_pink'
    def execute(self, context):
        set_base_color(0xd5b59a, self.bl_label)
        return {'FINISHED'}

class BS04_B_15_Dawn_Pink(bpy.types.Operator):
    """04-B-15 Dawn Pink"""
    bl_label = "04-B-15 Dawn Pink"
    bl_idname = 'color.04_b_15_dawn_pink'
    def execute(self, context):
        set_base_color(0xdab69c, self.bl_label)
        return {'FINISHED'}

class BS04_B_17_Tea_Rose(bpy.types.Operator):
    """04-B-17 Tea Rose"""
    bl_label = "04-B-17 Tea Rose"
    bl_idname = 'color.04_b_17_tea_rose'
    def execute(self, context):
        set_base_color(0xc89c82, self.bl_label)
        return {'FINISHED'}

class BS04_B_19_Beige(bpy.types.Operator):
    """04-B-19 Beige"""
    bl_label = "04-B-19 Beige"
    bl_idname = 'color.04_b_19_beige'
    def execute(self, context):
        set_base_color(0xae8568, self.bl_label)
        return {'FINISHED'}

class BS04_B_21_Sierra(bpy.types.Operator):
    """04-B-21 Sierra"""
    bl_label = "04-B-21 Sierra"
    bl_idname = 'color.04_b_21_sierra'
    def execute(self, context):
        set_base_color(0x84604b, self.bl_label)
        return {'FINISHED'}

class BS04_B_23_Brown(bpy.types.Operator):
    """04-B-23 Brown"""
    bl_label = "04-B-23 Brown"
    bl_idname = 'color.04_b_23_brown'
    def execute(self, context):
        set_base_color(0x7d594d, self.bl_label)
        return {'FINISHED'}

class BS04_B_25_Saracen(bpy.types.Operator):
    """04-B-25 Saracen"""
    bl_label = "04-B-25 Saracen"
    bl_idname = 'color.04_b_25_saracen'
    def execute(self, context):
        set_base_color(0x36312d, self.bl_label)
        return {'FINISHED'}

class BS04_B_27_Brown(bpy.types.Operator):
    """04-B-27 Brown"""
    bl_label = "04-B-27 Brown"
    bl_idname = 'color.04_b_27_brown'
    def execute(self, context):
        set_base_color(0x553c35, self.bl_label)
        return {'FINISHED'}

class BS04_B_29_Brown(bpy.types.Operator):
    """04-B-29 Brown"""
    bl_label = "04-B-29 Brown"
    bl_idname = 'color.04_b_29_brown'
    def execute(self, context):
        set_base_color(0x2c1e1a, self.bl_label)
        return {'FINISHED'}

class BS04_C_31_Pink(bpy.types.Operator):
    """04-C-31 Pink"""
    bl_label = "04-C-31 Pink"
    bl_idname = 'color.04_c_31_pink'
    def execute(self, context):
        set_base_color(0xf4e7e0, self.bl_label)
        return {'FINISHED'}

class BS04_C_33_Parisian_Pink(bpy.types.Operator):
    """04-C-33 Parisian Pink"""
    bl_label = "04-C-33 Parisian Pink"
    bl_idname = 'color.04_c_33_parisian_pink'
    def execute(self, context):
        set_base_color(0xe7bdb4, self.bl_label)
        return {'FINISHED'}

class BS04_C_35_Soft_Red(bpy.types.Operator):
    """04-C-35 Soft Red"""
    bl_label = "04-C-35 Soft Red"
    bl_idname = 'color.04_c_35_soft_red'
    def execute(self, context):
        set_base_color(0xe09371, self.bl_label)
        return {'FINISHED'}

class BS04_C_37_Red(bpy.types.Operator):
    """04-C-37 Red"""
    bl_label = "04-C-37 Red"
    bl_idname = 'color.04_c_37_red'
    def execute(self, context):
        set_base_color(0xa66f67, self.bl_label)
        return {'FINISHED'}

class BS04_C_39_Copperbeech(bpy.types.Operator):
    """04-C-39 Copperbeech"""
    bl_label = "04-C-39 Copperbeech"
    bl_idname = 'color.04_c_39_copperbeech'
    def execute(self, context):
        set_base_color(0x7b4945, self.bl_label)
        return {'FINISHED'}

class BS04_C_40_Maroon(bpy.types.Operator):
    """04-C-40 Maroon"""
    bl_label = "04-C-40 Maroon"
    bl_idname = 'color.04_c_40_maroon'
    def execute(self, context):
        set_base_color(0x493230, self.bl_label)
        return {'FINISHED'}

class BS04_D_41_Pink(bpy.types.Operator):
    """04-D-41 Pink"""
    bl_label = "04-D-41 Pink"
    bl_idname = 'color.04_d_41_pink'
    def execute(self, context):
        set_base_color(0xe18c6a, self.bl_label)
        return {'FINISHED'}

class BS04_D_43_Robin(bpy.types.Operator):
    """04-D-43 Robin"""
    bl_label = "04-D-43 Robin"
    bl_idname = 'color.04_d_43_robin'
    def execute(self, context):
        set_base_color(0xcb5952, self.bl_label)
        return {'FINISHED'}

class BS04_D_44_Tawny(bpy.types.Operator):
    """04-D-44 Tawny"""
    bl_label = "04-D-44 Tawny"
    bl_idname = 'color.04_d_44_tawny'
    def execute(self, context):
        set_base_color(0xa1514d, self.bl_label)
        return {'FINISHED'}

class BS04_D_45_Russet(bpy.types.Operator):
    """04-D-45 Russet"""
    bl_label = "04-D-45 Russet"
    bl_idname = 'color.04_d_45_russet'
    def execute(self, context):
        set_base_color(0x873f3d, self.bl_label)
        return {'FINISHED'}

class BS04_E_49_Petal(bpy.types.Operator):
    """04-E-49 Petal"""
    bl_label = "04-E-49 Petal"
    bl_idname = 'color.04_e_49_petal'
    def execute(self, context):
        set_base_color(0xf5dbd4, self.bl_label)
        return {'FINISHED'}

class BS04_E_50_Pink(bpy.types.Operator):
    """04-E-50 Pink"""
    bl_label = "04-E-50 Pink"
    bl_idname = 'color.04_e_50_pink'
    def execute(self, context):
        set_base_color(0xf1a17d, self.bl_label)
        return {'FINISHED'}

class BS04_E_51_Salmon_Red_Lobster_Azalea(bpy.types.Operator):
    """04-E-51 Salmon Red / Lobster / Azalea"""
    bl_label = "04-E-51 Salmon Red / Lobster / Azalea"
    bl_idname = 'color.04_e_51_salmon_red_lobster_azalea'
    def execute(self, context):
        set_base_color(0xdc1e04, self.bl_label)
        return {'FINISHED'}

class BS04_E_53_Carnival_Red_Poppy(bpy.types.Operator):
    """04-E-53 Carnival Red / Poppy"""
    bl_label = "04-E-53 Carnival Red / Poppy"
    bl_idname = 'color.04_e_53_carnival_red_poppy'
    def execute(self, context):
        set_base_color(0xff1801, self.bl_label)
        return {'FINISHED'}

class BS04_E_55_Red(bpy.types.Operator):
    """04-E-55 Red"""
    bl_label = "04-E-55 Red"
    bl_idname = 'color.04_e_55_red'
    def execute(self, context):
        set_base_color(0xff0000, self.bl_label)
        return {'FINISHED'}

class BS04_E_56_Carnival_Red(bpy.types.Operator):
    """04-E-56 Carnival Red"""
    bl_label = "04-E-56 Carnival Red"
    bl_idname = 'color.04_e_56_carnival_red'
    def execute(self, context):
        set_base_color(0xbb0000, self.bl_label)
        return {'FINISHED'}

class BS04_E_58_Red(bpy.types.Operator):
    """04-E-58 Red"""
    bl_label = "04-E-58 Red"
    bl_idname = 'color.04_e_58_red'
    def execute(self, context):
        set_base_color(0x6d211f, self.bl_label)
        return {'FINISHED'}

class BS06_A_03_Grey(bpy.types.Operator):
    """06-A-03 Grey"""
    bl_label = "06-A-03 Grey"
    bl_idname = 'color.06_a_03_grey'
    def execute(self, context):
        set_base_color(0xdac9af, self.bl_label)
        return {'FINISHED'}

class BS06_A_07_Grey(bpy.types.Operator):
    """06-A-07 Grey"""
    bl_label = "06-A-07 Grey"
    bl_idname = 'color.06_a_07_grey'
    def execute(self, context):
        set_base_color(0x908473, self.bl_label)
        return {'FINISHED'}

class BS06_A_11_Grey(bpy.types.Operator):
    """06-A-11 Grey"""
    bl_label = "06-A-11 Grey"
    bl_idname = 'color.06_a_11_grey'
    def execute(self, context):
        set_base_color(0x363f32, self.bl_label)
        return {'FINISHED'}

class BS06_C_33_Cameo(bpy.types.Operator):
    """06-C-33 Cameo"""
    bl_label = "06-C-33 Cameo"
    bl_idname = 'color.06_c_33_cameo'
    def execute(self, context):
        set_base_color(0xe4ac74, self.bl_label)
        return {'FINISHED'}

class BS06_C_35_Light_Orange(bpy.types.Operator):
    """06-C-35 Light Orange"""
    bl_label = "06-C-35 Light Orange"
    bl_idname = 'color.06_c_35_light_orange'
    def execute(self, context):
        set_base_color(0xdc9542, self.bl_label)
        return {'FINISHED'}

class BS06_C_37_Brownstone(bpy.types.Operator):
    """06-C-37 Brownstone"""
    bl_label = "06-C-37 Brownstone"
    bl_idname = 'color.06_c_37_brownstone'
    def execute(self, context):
        set_base_color(0xb67a36, self.bl_label)
        return {'FINISHED'}

class BS06_C_39_Saddle(bpy.types.Operator):
    """06-C-39 Saddle"""
    bl_label = "06-C-39 Saddle"
    bl_idname = 'color.06_c_39_saddle'
    def execute(self, context):
        set_base_color(0x663300, self.bl_label)
        return {'FINISHED'}

class BS06_C_40_Brown(bpy.types.Operator):
    """06-C-40 Brown"""
    bl_label = "06-C-40 Brown"
    bl_idname = 'color.06_c_40_brown'
    def execute(self, context):
        set_base_color(0x472300, self.bl_label)
        return {'FINISHED'}

class BS06_D_41_Orange(bpy.types.Operator):
    """06-D-41 Orange"""
    bl_label = "06-D-41 Orange"
    bl_idname = 'color.06_d_41_orange'
    def execute(self, context):
        set_base_color(0xf2aa4c, self.bl_label)
        return {'FINISHED'}

class BS06_D_43_Kalahari(bpy.types.Operator):
    """06-D-43 Kalahari"""
    bl_label = "06-D-43 Kalahari"
    bl_idname = 'color.06_d_43_kalahari'
    def execute(self, context):
        set_base_color(0xd76b00, self.bl_label)
        return {'FINISHED'}

class BS06_D_44_Orange(bpy.types.Operator):
    """06-D-44 Orange"""
    bl_label = "06-D-44 Orange"
    bl_idname = 'color.06_d_44_orange'
    def execute(self, context):
        set_base_color(0xfe6800, self.bl_label)
        return {'FINISHED'}

class BS06_D_45_Mace(bpy.types.Operator):
    """06-D-45 Mace"""
    bl_label = "06-D-45 Mace"
    bl_idname = 'color.06_d_45_mace'
    def execute(self, context):
        set_base_color(0xae3a00, self.bl_label)
        return {'FINISHED'}

class BS06_E_50_Apricot(bpy.types.Operator):
    """06-E-50 Apricot"""
    bl_label = "06-E-50 Apricot"
    bl_idname = 'color.06_e_50_apricot'
    def execute(self, context):
        set_base_color(0xffac30, self.bl_label)
        return {'FINISHED'}

class BS06_E_51_Clementine(bpy.types.Operator):
    """06-E-51 Clementine"""
    bl_label = "06-E-51 Clementine"
    bl_idname = 'color.06_e_51_clementine'
    def execute(self, context):
        set_base_color(0xff6d1c, self.bl_label)
        return {'FINISHED'}

class BS06_E_53_Orange(bpy.types.Operator):
    """06-E-53 Orange"""
    bl_label = "06-E-53 Orange"
    bl_idname = 'color.06_e_53_orange'
    def execute(self, context):
        set_base_color(0xff6600, self.bl_label)
        return {'FINISHED'}

class BS06_E_55_Orange(bpy.types.Operator):
    """06-E-55 Orange"""
    bl_label = "06-E-55 Orange"
    bl_idname = 'color.06_e_55_orange'
    def execute(self, context):
        set_base_color(0xff380c, self.bl_label)
        return {'FINISHED'}

class BS06_E_56_Yellow(bpy.types.Operator):
    """06-E-56 Yellow"""
    bl_label = "06-E-56 Yellow"
    bl_idname = 'color.06_e_56_yellow'
    def execute(self, context):
        set_base_color(0xa15904, self.bl_label)
        return {'FINISHED'}

class BS08_A_14_Black(bpy.types.Operator):
    """08-A-14 Black"""
    bl_label = "08-A-14 Black"
    bl_idname = 'color.08_a_14_black'
    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}

class BS08_B_15_Magnolia(bpy.types.Operator):
    """08-B-15 Magnolia"""
    bl_label = "08-B-15 Magnolia"
    bl_idname = 'color.08_b_15_magnolia'
    def execute(self, context):
        set_base_color(0xefe970, self.bl_label)
        return {'FINISHED'}

class BS08_B_17_Fawn(bpy.types.Operator):
    """08-B-17 Fawn"""
    bl_label = "08-B-17 Fawn"
    bl_idname = 'color.08_b_17_fawn'
    def execute(self, context):
        set_base_color(0xddb158, self.bl_label)
        return {'FINISHED'}

class BS08_B_19_Beige(bpy.types.Operator):
    """08-B-19 Beige"""
    bl_label = "08-B-19 Beige"
    bl_idname = 'color.08_b_19_beige'
    def execute(self, context):
        set_base_color(0xbd984b, self.bl_label)
        return {'FINISHED'}

class BS08_B_21_Antelope(bpy.types.Operator):
    """08-B-21 Antelope"""
    bl_label = "08-B-21 Antelope"
    bl_idname = 'color.08_b_21_antelope'
    def execute(self, context):
        set_base_color(0xac8a44, self.bl_label)
        return {'FINISHED'}

class BS08_B_23_Brown(bpy.types.Operator):
    """08-B-23 Brown"""
    bl_label = "08-B-23 Brown"
    bl_idname = 'color.08_b_23_brown'
    def execute(self, context):
        set_base_color(0x97793b, self.bl_label)
        return {'FINISHED'}

class BS08_B_25_Beaver(bpy.types.Operator):
    """08-B-25 Beaver"""
    bl_label = "08-B-25 Beaver"
    bl_idname = 'color.08_b_25_beaver'
    def execute(self, context):
        set_base_color(0x856b34, self.bl_label)
        return {'FINISHED'}

class BS08_B_27_Brown(bpy.types.Operator):
    """08-B-27 Brown"""
    bl_label = "08-B-27 Brown"
    bl_idname = 'color.08_b_27_brown'
    def execute(self, context):
        set_base_color(0x624e25, self.bl_label)
        return {'FINISHED'}

class BS08_B_29_Vandye(bpy.types.Operator):
    """08-B-29 Vandye"""
    bl_label = "08-B-29 Vandye"
    bl_idname = 'color.08_b_29_vandye'
    def execute(self, context):
        set_base_color(0x46381a, self.bl_label)
        return {'FINISHED'}

class BS08_C_31_Blush_Stone(bpy.types.Operator):
    """08-C-31 Blush Stone"""
    bl_label = "08-C-31 Blush Stone"
    bl_idname = 'color.08_c_31_blush_stone'
    def execute(self, context):
        set_base_color(0xf0bc56, self.bl_label)
        return {'FINISHED'}

class BS08_C_33_Beige(bpy.types.Operator):
    """08-C-33 Beige"""
    bl_label = "08-C-33 Beige"
    bl_idname = 'color.08_c_33_beige'
    def execute(self, context):
        set_base_color(0xd3a54c, self.bl_label)
        return {'FINISHED'}

class BS08_C_35_Butterscoth(bpy.types.Operator):
    """08-C-35 Butterscoth"""
    bl_label = "08-C-35 Butterscoth"
    bl_idname = 'color.08_c_35_butterscoth'
    def execute(self, context):
        set_base_color(0xac812b, self.bl_label)
        return {'FINISHED'}

class BS08_C_37_Bracken(bpy.types.Operator):
    """08-C-37 Bracken"""
    bl_label = "08-C-37 Bracken"
    bl_idname = 'color.08_c_37_bracken'
    def execute(self, context):
        set_base_color(0xc46200, self.bl_label)
        return {'FINISHED'}

class BS08_C_39_Bison(bpy.types.Operator):
    """08-C-39 Bison"""
    bl_label = "08-C-39 Bison"
    bl_idname = 'color.08_c_39_bison'
    def execute(self, context):
        set_base_color(0x703800, self.bl_label)
        return {'FINISHED'}

class BS08_C_40_Brown(bpy.types.Operator):
    """08-C-40 Brown"""
    bl_label = "08-C-40 Brown"
    bl_idname = 'color.08_c_40_brown'
    def execute(self, context):
        set_base_color(0x482400, self.bl_label)
        return {'FINISHED'}

class BS08_D_41_Yellow(bpy.types.Operator):
    """08-D-41 Yellow"""
    bl_label = "08-D-41 Yellow"
    bl_idname = 'color.08_d_41_yellow'
    def execute(self, context):
        set_base_color(0xfcaf3d, self.bl_label)
        return {'FINISHED'}

class BS08_D_43_Yellow(bpy.types.Operator):
    """08-D-43 Yellow"""
    bl_label = "08-D-43 Yellow"
    bl_idname = 'color.08_d_43_yellow'
    def execute(self, context):
        set_base_color(0xce7f08, self.bl_label)
        return {'FINISHED'}

class BS08_D_44_Brown(bpy.types.Operator):
    """08-D-44 Brown"""
    bl_label = "08-D-44 Brown"
    bl_idname = 'color.08_d_44_brown'
    def execute(self, context):
        set_base_color(0xbb4a00, self.bl_label)
        return {'FINISHED'}

class BS08_D_45_Brown(bpy.types.Operator):
    """08-D-45 Brown"""
    bl_label = "08-D-45 Brown"
    bl_idname = 'color.08_d_45_brown'
    def execute(self, context):
        set_base_color(0x7c3100, self.bl_label)
        return {'FINISHED'}

class BS08_E_51_Golden_Ambar(bpy.types.Operator):
    """08-E-51 Golden Ambar"""
    bl_label = "08-E-51 Golden Ambar"
    bl_idname = 'color.08_e_51_golden_ambar'
    def execute(self, context):
        set_base_color(0xff8311, self.bl_label)
        return {'FINISHED'}

class BS08_E_53_Yellow(bpy.types.Operator):
    """08-E-53 Yellow"""
    bl_label = "08-E-53 Yellow"
    bl_idname = 'color.08_e_53_yellow'
    def execute(self, context):
        set_base_color(0xffaf15, self.bl_label)
        return {'FINISHED'}

class BS08_E_55_Orange(bpy.types.Operator):
    """08-E-55 Orange"""
    bl_label = "08-E-55 Orange"
    bl_idname = 'color.08_e_55_orange'
    def execute(self, context):
        set_base_color(0xff932b, self.bl_label)
        return {'FINISHED'}

class BS08_E_56_Yellow(bpy.types.Operator):
    """08-E-56 Yellow"""
    bl_label = "08-E-56 Yellow"
    bl_idname = 'color.08_e_56_yellow'
    def execute(self, context):
        set_base_color(0xdc6e00, self.bl_label)
        return {'FINISHED'}

class BS10_A_01_White(bpy.types.Operator):
    """10-A-01 White"""
    bl_label = "10-A-01 White"
    bl_idname = 'color.10_a_01_white'
    def execute(self, context):
        set_base_color(0xe2e2e1, self.bl_label)
        return {'FINISHED'}

class BS10_A_03_Sink_Grey(bpy.types.Operator):
    """10-A-03 Sink Grey"""
    bl_label = "10-A-03 Sink Grey"
    bl_idname = 'color.10_a_03_sink_grey'
    def execute(self, context):
        set_base_color(0xa9a9a8, self.bl_label)
        return {'FINISHED'}

class BS10_A_05_Grey(bpy.types.Operator):
    """10-A-05 Grey"""
    bl_label = "10-A-05 Grey"
    bl_idname = 'color.10_a_05_grey'
    def execute(self, context):
        set_base_color(0x8a8a89, self.bl_label)
        return {'FINISHED'}

class BS10_A_07_Wood_Ash(bpy.types.Operator):
    """10-A-07 Wood Ash"""
    bl_label = "10-A-07 Wood Ash"
    bl_idname = 'color.10_a_07_wood_ash'
    def execute(self, context):
        set_base_color(0xaa9358, self.bl_label)
        return {'FINISHED'}

class BS10_A_09_Grey(bpy.types.Operator):
    """10-A-09 Grey"""
    bl_label = "10-A-09 Grey"
    bl_idname = 'color.10_a_09_grey'
    def execute(self, context):
        set_base_color(0x6c5d38, self.bl_label)
        return {'FINISHED'}

class BS10_A_11_Storm_Rhino(bpy.types.Operator):
    """10-A-11 Storm / Rhino"""
    bl_label = "10-A-11 Storm / Rhino"
    bl_idname = 'color.10_a_11_storm_rhino'
    def execute(self, context):
        set_base_color(0x51462a, self.bl_label)
        return {'FINISHED'}

class BS10_B_15_Ivory(bpy.types.Operator):
    """10-B-15 Ivory"""
    bl_label = "10-B-15 Ivory"
    bl_idname = 'color.10_b_15_ivory'
    def execute(self, context):
        set_base_color(0xfcf3a8, self.bl_label)
        return {'FINISHED'}

class BS10_B_17_Greystone(bpy.types.Operator):
    """10-B-17 Greystone"""
    bl_label = "10-B-17 Greystone"
    bl_idname = 'color.10_b_17_greystone'
    def execute(self, context):
        set_base_color(0xcac387, self.bl_label)
        return {'FINISHED'}

class BS10_B_19_Beige(bpy.types.Operator):
    """10-B-19 Beige"""
    bl_label = "10-B-19 Beige"
    bl_idname = 'color.10_b_19_beige'
    def execute(self, context):
        set_base_color(0xaaa472, self.bl_label)
        return {'FINISHED'}

class BS10_B_21_Lizard(bpy.types.Operator):
    """10-B-21 Lizard"""
    bl_label = "10-B-21 Lizard"
    bl_idname = 'color.10_b_21_lizard'
    def execute(self, context):
        set_base_color(0x958758, self.bl_label)
        return {'FINISHED'}

class BS10_B_23_Brown(bpy.types.Operator):
    """10-B-23 Brown"""
    bl_label = "10-B-23 Brown"
    bl_idname = 'color.10_b_23_brown'
    def execute(self, context):
        set_base_color(0x897749, self.bl_label)
        return {'FINISHED'}

class BS10_B_25_Turtle(bpy.types.Operator):
    """10-B-25 Turtle"""
    bl_label = "10-B-25 Turtle"
    bl_idname = 'color.10_b_25_turtle'
    def execute(self, context):
        set_base_color(0x5a4e2f, self.bl_label)
        return {'FINISHED'}

class BS10_B_27_Brown(bpy.types.Operator):
    """10-B-27 Brown"""
    bl_label = "10-B-27 Brown"
    bl_idname = 'color.10_b_27_brown'
    def execute(self, context):
        set_base_color(0x433a23, self.bl_label)
        return {'FINISHED'}

class BS10_B_29_Ironstone(bpy.types.Operator):
    """10-B-29 Ironstone"""
    bl_label = "10-B-29 Ironstone"
    bl_idname = 'color.10_b_29_ironstone'
    def execute(self, context):
        set_base_color(0x2c2617, self.bl_label)
        return {'FINISHED'}

class BS10_C_31_Champagne(bpy.types.Operator):
    """10-C-31 Champagne"""
    bl_label = "10-C-31 Champagne"
    bl_idname = 'color.10_c_31_champagne'
    def execute(self, context):
        set_base_color(0xffe268, self.bl_label)
        return {'FINISHED'}

class BS10_C_33_Pollen(bpy.types.Operator):
    """10-C-33 Pollen"""
    bl_label = "10-C-33 Pollen"
    bl_idname = 'color.10_c_33_pollen'
    def execute(self, context):
        set_base_color(0xe2c95c, self.bl_label)
        return {'FINISHED'}

class BS10_C_35_Golden_Bronze(bpy.types.Operator):
    """10-C-35 Golden Bronze"""
    bl_label = "10-C-35 Golden Bronze"
    bl_idname = 'color.10_c_35_golden_bronze'
    def execute(self, context):
        set_base_color(0xae9b46, self.bl_label)
        return {'FINISHED'}

class BS10_C_37_Yellow_Brown(bpy.types.Operator):
    """10-C-37 Yellow Brown"""
    bl_label = "10-C-37 Yellow Brown"
    bl_idname = 'color.10_c_37_yellow_brown'
    def execute(self, context):
        set_base_color(0x9a7b1e, self.bl_label)
        return {'FINISHED'}

class BS10_C_39_Saluki(bpy.types.Operator):
    """10-C-39 Saluki"""
    bl_label = "10-C-39 Saluki"
    bl_idname = 'color.10_c_39_saluki'
    def execute(self, context):
        set_base_color(0x3e310c, self.bl_label)
        return {'FINISHED'}

class BS10_D_41_Yellow(bpy.types.Operator):
    """10-D-41 Yellow"""
    bl_label = "10-D-41 Yellow"
    bl_idname = 'color.10_d_41_yellow'
    def execute(self, context):
        set_base_color(0xffcc32, self.bl_label)
        return {'FINISHED'}

class BS10_D_43_Banana(bpy.types.Operator):
    """10-D-43 Banana"""
    bl_label = "10-D-43 Banana"
    bl_idname = 'color.10_d_43_banana'
    def execute(self, context):
        set_base_color(0xd3a929, self.bl_label)
        return {'FINISHED'}

class BS10_D_44_Light_Olive(bpy.types.Operator):
    """10-D-44 Light Olive"""
    bl_label = "10-D-44 Light Olive"
    bl_idname = 'color.10_d_44_light_olive'
    def execute(self, context):
        set_base_color(0xb18d22, self.bl_label)
        return {'FINISHED'}

class BS10_D_45_Florida(bpy.types.Operator):
    """10-D-45 Florida"""
    bl_label = "10-D-45 Florida"
    bl_idname = 'color.10_d_45_florida'
    def execute(self, context):
        set_base_color(0x6b5514, self.bl_label)
        return {'FINISHED'}

class BS10_E_49_Pale_Lemon(bpy.types.Operator):
    """10-E-49 Pale Lemon"""
    bl_label = "10-E-49 Pale Lemon"
    bl_idname = 'color.10_e_49_pale_lemon'
    def execute(self, context):
        set_base_color(0xfdd93f, self.bl_label)
        return {'FINISHED'}

class BS10_E_50_Forsythia(bpy.types.Operator):
    """10-E-50 Forsythia"""
    bl_label = "10-E-50 Forsythia"
    bl_idname = 'color.10_e_50_forsythia'
    def execute(self, context):
        set_base_color(0xfdef41, self.bl_label)
        return {'FINISHED'}

class BS10_E_51_Yellow(bpy.types.Operator):
    """10-E-51 Yellow"""
    bl_label = "10-E-51 Yellow"
    bl_idname = 'color.10_e_51_yellow'
    def execute(self, context):
        set_base_color(0xffcc00, self.bl_label)
        return {'FINISHED'}

class BS10_E_53_Canary(bpy.types.Operator):
    """10-E-53 Canary"""
    bl_label = "10-E-53 Canary"
    bl_idname = 'color.10_e_53_canary'
    def execute(self, context):
        set_base_color(0xe8b900, self.bl_label)
        return {'FINISHED'}

class BS10_E_55_Camery_Yellow(bpy.types.Operator):
    """10-E-55 Camery Yellow"""
    bl_label = "10-E-55 Camery Yellow"
    bl_idname = 'color.10_e_55_camery_yellow'
    def execute(self, context):
        set_base_color(0xdfb606, self.bl_label)
        return {'FINISHED'}

class BS10_E_56_Yellow(bpy.types.Operator):
    """10-E-56 Yellow"""
    bl_label = "10-E-56 Yellow"
    bl_idname = 'color.10_e_56_yellow'
    def execute(self, context):
        set_base_color(0xb79605, self.bl_label)
        return {'FINISHED'}

class BS12_B_15_Seafoam(bpy.types.Operator):
    """12-B-15 Seafoam"""
    bl_label = "12-B-15 Seafoam"
    bl_idname = 'color.12_b_15_seafoam'
    def execute(self, context):
        set_base_color(0xe5e4d0, self.bl_label)
        return {'FINISHED'}

class BS12_B_17_Willow(bpy.types.Operator):
    """12-B-17 Willow"""
    bl_label = "12-B-17 Willow"
    bl_idname = 'color.12_b_17_willow'
    def execute(self, context):
        set_base_color(0xd2d1bf, self.bl_label)
        return {'FINISHED'}

class BS12_B_19_Beige(bpy.types.Operator):
    """12-B-19 Beige"""
    bl_label = "12-B-19 Beige"
    bl_idname = 'color.12_b_19_beige'
    def execute(self, context):
        set_base_color(0xb8b7a8, self.bl_label)
        return {'FINISHED'}

class BS12_B_21_Opaline(bpy.types.Operator):
    """12-B-21 Opaline"""
    bl_label = "12-B-21 Opaline"
    bl_idname = 'color.12_b_21_opaline'
    def execute(self, context):
        set_base_color(0x8fa878, self.bl_label)
        return {'FINISHED'}

class BS12_B_23_Green(bpy.types.Operator):
    """12-B-23 Green"""
    bl_label = "12-B-23 Green"
    bl_idname = 'color.12_b_23_green'
    def execute(self, context):
        set_base_color(0x7d9369, self.bl_label)
        return {'FINISHED'}

class BS12_B_25_Thyme(bpy.types.Operator):
    """12-B-25 Thyme"""
    bl_label = "12-B-25 Thyme"
    bl_idname = 'color.12_b_25_thyme'
    def execute(self, context):
        set_base_color(0x5e5f50, self.bl_label)
        return {'FINISHED'}

class BS12_B_27_Green(bpy.types.Operator):
    """12-B-27 Green"""
    bl_label = "12-B-27 Green"
    bl_idname = 'color.12_b_27_green'
    def execute(self, context):
        set_base_color(0x5e7550, self.bl_label)
        return {'FINISHED'}

class BS12_B_29_Juniper(bpy.types.Operator):
    """12-B-29 Juniper"""
    bl_label = "12-B-29 Juniper"
    bl_idname = 'color.12_b_29_juniper'
    def execute(self, context):
        set_base_color(0x263021, self.bl_label)
        return {'FINISHED'}

class BS12_C_31_Light_Yellow(bpy.types.Operator):
    """12-C-31 Light Yellow"""
    bl_label = "12-C-31 Light Yellow"
    bl_idname = 'color.12_c_31_light_yellow'
    def execute(self, context):
        set_base_color(0xf7f994, self.bl_label)
        return {'FINISHED'}

class BS12_C_33_Catkin(bpy.types.Operator):
    """12-C-33 Catkin"""
    bl_label = "12-C-33 Catkin"
    bl_idname = 'color.12_c_33_catkin'
    def execute(self, context):
        set_base_color(0xcccd7a, self.bl_label)
        return {'FINISHED'}

class BS12_C_35_Green(bpy.types.Operator):
    """12-C-35 Green"""
    bl_label = "12-C-35 Green"
    bl_idname = 'color.12_c_35_green'
    def execute(self, context):
        set_base_color(0xbabb6f, self.bl_label)
        return {'FINISHED'}

class BS12_C_37_Green(bpy.types.Operator):
    """12-C-37 Green"""
    bl_label = "12-C-37 Green"
    bl_idname = 'color.12_c_37_green'
    def execute(self, context):
        set_base_color(0x778d47, self.bl_label)
        return {'FINISHED'}

class BS12_C_39_Orchard(bpy.types.Operator):
    """12-C-39 Orchard"""
    bl_label = "12-C-39 Orchard"
    bl_idname = 'color.12_c_39_orchard'
    def execute(self, context):
        set_base_color(0x4d5b2e, self.bl_label)
        return {'FINISHED'}

class BS12_C_40_Green(bpy.types.Operator):
    """12-C-40 Green"""
    bl_label = "12-C-40 Green"
    bl_idname = 'color.12_c_40_green'
    def execute(self, context):
        set_base_color(0x1e2311, self.bl_label)
        return {'FINISHED'}

class BS12_C_41_Green(bpy.types.Operator):
    """12-C-41 Green"""
    bl_label = "12-C-41 Green"
    bl_idname = 'color.12_c_41_green'
    def execute(self, context):
        set_base_color(0xb6d06b, self.bl_label)
        return {'FINISHED'}

class BS12_D_43_Sapling(bpy.types.Operator):
    """12-D-43 Sapling"""
    bl_label = "12-D-43 Sapling"
    bl_idname = 'color.12_d_43_sapling'
    def execute(self, context):
        set_base_color(0x91953e, self.bl_label)
        return {'FINISHED'}

class BS12_D_44_Green(bpy.types.Operator):
    """12-D-44 Green"""
    bl_label = "12-D-44 Green"
    bl_idname = 'color.12_d_44_green'
    def execute(self, context):
        set_base_color(0x7f8336, self.bl_label)
        return {'FINISHED'}

class BS12_D_45_Tundra(bpy.types.Operator):
    """12-D-45 Tundra"""
    bl_label = "12-D-45 Tundra"
    bl_idname = 'color.12_d_45_tundra'
    def execute(self, context):
        set_base_color(0x565730, self.bl_label)
        return {'FINISHED'}

class BS12_E_51_Citrine(bpy.types.Operator):
    """12-E-51 Citrine"""
    bl_label = "12-E-51 Citrine"
    bl_idname = 'color.12_e_51_citrine'
    def execute(self, context):
        set_base_color(0xc8c83e, self.bl_label)
        return {'FINISHED'}

class BS12_E_53_Linden(bpy.types.Operator):
    """12-E-53 Linden"""
    bl_label = "12-E-53 Linden"
    bl_idname = 'color.12_e_53_linden'
    def execute(self, context):
        set_base_color(0x99b03f, self.bl_label)
        return {'FINISHED'}

class BS12_E_55_Green(bpy.types.Operator):
    """12-E-55 Green"""
    bl_label = "12-E-55 Green"
    bl_idname = 'color.12_e_55_green'
    def execute(self, context):
        set_base_color(0x7ba044, self.bl_label)
        return {'FINISHED'}

class BS14_C_31_Green_Alpine(bpy.types.Operator):
    """14-C-31 Green / Alpine"""
    bl_label = "14-C-31 Green / Alpine"
    bl_idname = 'color.14_c_31_green_alpine'
    def execute(self, context):
        set_base_color(0xd9e7d7, self.bl_label)
        return {'FINISHED'}

class BS14_C_33_Green(bpy.types.Operator):
    """14-C-33 Green"""
    bl_label = "14-C-33 Green"
    bl_idname = 'color.14_c_33_green'
    def execute(self, context):
        set_base_color(0xaae7a7, self.bl_label)
        return {'FINISHED'}

class BS14_C_35_Breamer(bpy.types.Operator):
    """14-C-35 Breamer"""
    bl_label = "14-C-35 Breamer"
    bl_idname = 'color.14_c_35_breamer'
    def execute(self, context):
        set_base_color(0x85b582, self.bl_label)
        return {'FINISHED'}

class BS14_C_37_Green(bpy.types.Operator):
    """14-C-37 Green"""
    bl_label = "14-C-37 Green"
    bl_idname = 'color.14_c_37_green'
    def execute(self, context):
        set_base_color(0x678d65, self.bl_label)
        return {'FINISHED'}

class BS14_C_39_Hollybush(bpy.types.Operator):
    """14-C-39 Hollybush"""
    bl_label = "14-C-39 Hollybush"
    bl_idname = 'color.14_c_39_hollybush'
    def execute(self, context):
        set_base_color(0x364b35, self.bl_label)
        return {'FINISHED'}

class BS14_C_40_Green(bpy.types.Operator):
    """14-C-40 Green"""
    bl_label = "14-C-40 Green"
    bl_idname = 'color.14_c_40_green'
    def execute(self, context):
        set_base_color(0x1d281c, self.bl_label)
        return {'FINISHED'}

class BS14_D_41_Green(bpy.types.Operator):
    """14-D-41 Green"""
    bl_label = "14-D-41 Green"
    bl_idname = 'color.14_d_41_green'
    def execute(self, context):
        set_base_color(0x739f6f, self.bl_label)
        return {'FINISHED'}

class BS14_D_43_Green(bpy.types.Operator):
    """14-D-43 Green"""
    bl_label = "14-D-43 Green"
    bl_idname = 'color.14_d_43_green'
    def execute(self, context):
        set_base_color(0x599759, self.bl_label)
        return {'FINISHED'}

class BS14_D_44_Green(bpy.types.Operator):
    """14-D-44 Green"""
    bl_label = "14-D-44 Green"
    bl_idname = 'color.14_d_44_green'
    def execute(self, context):
        set_base_color(0x4c824c, self.bl_label)
        return {'FINISHED'}

class BS14_D_45_Green(bpy.types.Operator):
    """14-D-45 Green"""
    bl_label = "14-D-45 Green"
    bl_idname = 'color.14_d_45_green'
    def execute(self, context):
        set_base_color(0x273f29, self.bl_label)
        return {'FINISHED'}

class BS14_E_49_Light_Green(bpy.types.Operator):
    """14-E-49 Light Green"""
    bl_label = "14-E-49 Light Green"
    bl_idname = 'color.14_e_49_light_green'
    def execute(self, context):
        set_base_color(0x9dfda5, self.bl_label)
        return {'FINISHED'}

class BS14_E_50_Green(bpy.types.Operator):
    """14-E-50 Green"""
    bl_label = "14-E-50 Green"
    bl_idname = 'color.14_e_50_green'
    def execute(self, context):
        set_base_color(0x80ce86, self.bl_label)
        return {'FINISHED'}

class BS14_E_51_Goblin(bpy.types.Operator):
    """14-E-51 Goblin"""
    bl_label = "14-E-51 Goblin"
    bl_idname = 'color.14_e_51_goblin'
    def execute(self, context):
        set_base_color(0x18ad53, self.bl_label)
        return {'FINISHED'}

class BS14_E_53_Avarice(bpy.types.Operator):
    """14-E-53 Avarice"""
    bl_label = "14-E-53 Avarice"
    bl_idname = 'color.14_e_53_avarice'
    def execute(self, context):
        set_base_color(0x0e6932, self.bl_label)
        return {'FINISHED'}

class BS14_E_56_Green(bpy.types.Operator):
    """14-E-56 Green"""
    bl_label = "14-E-56 Green"
    bl_idname = 'color.14_e_56_green'
    def execute(self, context):
        set_base_color(0x0c661d, self.bl_label)
        return {'FINISHED'}

class BS14_E_58_Green(bpy.types.Operator):
    """14-E-58 Green"""
    bl_label = "14-E-58 Green"
    bl_idname = 'color.14_e_58_green'
    def execute(self, context):
        set_base_color(0x06330e, self.bl_label)
        return {'FINISHED'}

class BS16_A_03_Grey(bpy.types.Operator):
    """16-A-03 Grey"""
    bl_label = "16-A-03 Grey"
    bl_idname = 'color.16_a_03_grey'
    def execute(self, context):
        set_base_color(0xcccccc, self.bl_label)
        return {'FINISHED'}

class BS16_A_07_Mid_Grey(bpy.types.Operator):
    """16-A-07 Mid Grey"""
    bl_label = "16-A-07 Mid Grey"
    bl_idname = 'color.16_a_07_mid_grey'
    def execute(self, context):
        set_base_color(0x939393, self.bl_label)
        return {'FINISHED'}

class BS16_A_11_Grey(bpy.types.Operator):
    """16-A-11 Grey"""
    bl_label = "16-A-11 Grey"
    bl_idname = 'color.16_a_11_grey'
    def execute(self, context):
        set_base_color(0x444444, self.bl_label)
        return {'FINISHED'}

class BS16_C_33_Duckegg(bpy.types.Operator):
    """16-C-33 Duckegg"""
    bl_label = "16-C-33 Duckegg"
    bl_idname = 'color.16_c_33_duckegg'
    def execute(self, context):
        set_base_color(0xd0ebe6, self.bl_label)
        return {'FINISHED'}

class BS16_C_35_Green(bpy.types.Operator):
    """16-C-35 Green"""
    bl_label = "16-C-35 Green"
    bl_idname = 'color.16_c_35_green'
    def execute(self, context):
        set_base_color(0xa0bf92, self.bl_label)
        return {'FINISHED'}

class BS16_C_37_Green(bpy.types.Operator):
    """16-C-37 Green"""
    bl_label = "16-C-37 Green"
    bl_idname = 'color.16_c_37_green'
    def execute(self, context):
        set_base_color(0x829b76, self.bl_label)
        return {'FINISHED'}

class BS16_C_39_Green(bpy.types.Operator):
    """16-C-39 Green"""
    bl_label = "16-C-39 Green"
    bl_idname = 'color.16_c_39_green'
    def execute(self, context):
        set_base_color(0x3a4635, self.bl_label)
        return {'FINISHED'}

class BS16_C_40_Deep_Green(bpy.types.Operator):
    """16-C-40 Deep Green"""
    bl_label = "16-C-40 Deep Green"
    bl_idname = 'color.16_c_40_deep_green'
    def execute(self, context):
        set_base_color(0x1f261c, self.bl_label)
        return {'FINISHED'}

class BS16_D_41_Green(bpy.types.Operator):
    """16-D-41 Green"""
    bl_label = "16-D-41 Green"
    bl_idname = 'color.16_d_41_green'
    def execute(self, context):
        set_base_color(0x9edca3, self.bl_label)
        return {'FINISHED'}

class BS16_D_43_Green(bpy.types.Operator):
    """16-D-43 Green"""
    bl_label = "16-D-43 Green"
    bl_idname = 'color.16_d_43_green'
    def execute(self, context):
        set_base_color(0x40925e, self.bl_label)
        return {'FINISHED'}

class BS16_D_44_Green(bpy.types.Operator):
    """16-D-44 Green"""
    bl_label = "16-D-44 Green"
    bl_idname = 'color.16_d_44_green'
    def execute(self, context):
        set_base_color(0x387f52, self.bl_label)
        return {'FINISHED'}

class BS16_D_45_Green_Blue(bpy.types.Operator):
    """16-D-45 Green Blue"""
    bl_label = "16-D-45 Green Blue"
    bl_idname = 'color.16_d_45_green_blue'
    def execute(self, context):
        set_base_color(0x234f33, self.bl_label)
        return {'FINISHED'}

class BS16_E_50_Turquoise(bpy.types.Operator):
    """16-E-50 Turquoise"""
    bl_label = "16-E-50 Turquoise"
    bl_idname = 'color.16_e_50_turquoise'
    def execute(self, context):
        set_base_color(0xa3e4a9, self.bl_label)
        return {'FINISHED'}

class BS16_E_53_Seafarer(bpy.types.Operator):
    """16-E-53 Seafarer"""
    bl_label = "16-E-53 Seafarer"
    bl_idname = 'color.16_e_53_seafarer'
    def execute(self, context):
        set_base_color(0x5da07a, self.bl_label)
        return {'FINISHED'}

class BS16_E_56_Green(bpy.types.Operator):
    """16-E-56 Green"""
    bl_label = "16-E-56 Green"
    bl_idname = 'color.16_e_56_green'
    def execute(self, context):
        set_base_color(0x468863, self.bl_label)
        return {'FINISHED'}

class BS18_A_14_Black(bpy.types.Operator):
    """18-A-14 Black"""
    bl_label = "18-A-14 Black"
    bl_idname = 'color.18_a_14_black'
    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}

class BS18_B_15_White(bpy.types.Operator):
    """18-B-15 White"""
    bl_label = "18-B-15 White"
    bl_idname = 'color.18_b_15_white'
    def execute(self, context):
        set_base_color(0xffffff, self.bl_label)
        return {'FINISHED'}

class BS18_B_17_Silver_Haze(bpy.types.Operator):
    """18-B-17 Silver Haze"""
    bl_label = "18-B-17 Silver Haze"
    bl_idname = 'color.18_b_17_silver_haze'
    def execute(self, context):
        set_base_color(0xbfbfbf, self.bl_label)
        return {'FINISHED'}

class BS18_B_19_Grey(bpy.types.Operator):
    """18-B-19 Grey"""
    bl_label = "18-B-19 Grey"
    bl_idname = 'color.18_b_19_grey'
    def execute(self, context):
        set_base_color(0xb6b6b6, self.bl_label)
        return {'FINISHED'}

class BS18_B_21_Blue(bpy.types.Operator):
    """18-B-21 Blue"""
    bl_label = "18-B-21 Blue"
    bl_idname = 'color.18_b_21_blue'
    def execute(self, context):
        set_base_color(0xa3a3a3, self.bl_label)
        return {'FINISHED'}

class BS18_B_23_Grey(bpy.types.Operator):
    """18-B-23 Grey"""
    bl_label = "18-B-23 Grey"
    bl_idname = 'color.18_b_23_grey'
    def execute(self, context):
        set_base_color(0x8e8e8e, self.bl_label)
        return {'FINISHED'}

class BS18_B_25_Dark_Admiral_Grey(bpy.types.Operator):
    """18-B-25 Dark Admiral Grey"""
    bl_label = "18-B-25 Dark Admiral Grey"
    bl_idname = 'color.18_b_25_dark_admiral_grey'
    def execute(self, context):
        set_base_color(0x545b5e, self.bl_label)
        return {'FINISHED'}

class BS18_B_27_Grey(bpy.types.Operator):
    """18-B-27 Grey"""
    bl_label = "18-B-27 Grey"
    bl_idname = 'color.18_b_27_grey'
    def execute(self, context):
        set_base_color(0x323638, self.bl_label)
        return {'FINISHED'}

class BS18_B_29_Blue(bpy.types.Operator):
    """18-B-29 Blue"""
    bl_label = "18-B-29 Blue"
    bl_idname = 'color.18_b_29_blue'
    def execute(self, context):
        set_base_color(0x191a1c, self.bl_label)
        return {'FINISHED'}

class BS18_C_31_Ice_Blue(bpy.types.Operator):
    """18-C-31 Ice Blue"""
    bl_label = "18-C-31 Ice Blue"
    bl_idname = 'color.18_c_31_ice_blue'
    def execute(self, context):
        set_base_color(0xe4e8e1, self.bl_label)
        return {'FINISHED'}

class BS18_C_33_Blue(bpy.types.Operator):
    """18-C-33 Blue"""
    bl_label = "18-C-33 Blue"
    bl_idname = 'color.18_c_33_blue'
    def execute(self, context):
        set_base_color(0xced2cc, self.bl_label)
        return {'FINISHED'}

class BS18_C_35_Blue(bpy.types.Operator):
    """18-C-35 Blue"""
    bl_label = "18-C-35 Blue"
    bl_idname = 'color.18_c_35_blue'
    def execute(self, context):
        set_base_color(0x6ba3ba, self.bl_label)
        return {'FINISHED'}

class BS18_C_37_Blue(bpy.types.Operator):
    """18-C-37 Blue"""
    bl_label = "18-C-37 Blue"
    bl_idname = 'color.18_c_37_blue'
    def execute(self, context):
        set_base_color(0x486d7c, self.bl_label)
        return {'FINISHED'}

class BS18_C_39_Deep_River(bpy.types.Operator):
    """18-C-39 Deep River"""
    bl_label = "18-C-39 Deep River"
    bl_idname = 'color.18_c_39_deep_river'
    def execute(self, context):
        set_base_color(0x2b4149, self.bl_label)
        return {'FINISHED'}

class BS18_C_40_Black(bpy.types.Operator):
    """18-C-40 Black"""
    bl_label = "18-C-40 Black"
    bl_idname = 'color.18_c_40_black'
    def execute(self, context):
        set_base_color(0x0f1619, self.bl_label)
        return {'FINISHED'}

class BS18_D_41_Blue(bpy.types.Operator):
    """18-D-41 Blue"""
    bl_label = "18-D-41 Blue"
    bl_idname = 'color.18_d_41_blue'
    def execute(self, context):
        set_base_color(0x68b6a5, self.bl_label)
        return {'FINISHED'}

class BS18_D_43_Dresden_Blue(bpy.types.Operator):
    """18-D-43 Dresden Blue"""
    bl_label = "18-D-43 Dresden Blue"
    bl_idname = 'color.18_d_43_dresden_blue'
    def execute(self, context):
        set_base_color(0x559587, self.bl_label)
        return {'FINISHED'}

class BS18_D_44_Blue(bpy.types.Operator):
    """18-D-44 Blue"""
    bl_label = "18-D-44 Blue"
    bl_idname = 'color.18_d_44_blue'
    def execute(self, context):
        set_base_color(0x3d6c62, self.bl_label)
        return {'FINISHED'}

class BS18_D_45_Blue(bpy.types.Operator):
    """18-D-45 Blue"""
    bl_label = "18-D-45 Blue"
    bl_idname = 'color.18_d_45_blue'
    def execute(self, context):
        set_base_color(0x2e514a, self.bl_label)
        return {'FINISHED'}

class BS18_E_49_Astral_Blue(bpy.types.Operator):
    """18-E-49 Astral Blue"""
    bl_label = "18-E-49 Astral Blue"
    bl_idname = 'color.18_e_49_astral_blue'
    def execute(self, context):
        set_base_color(0xd4e6e2, self.bl_label)
        return {'FINISHED'}

class BS18_E_50_Blue(bpy.types.Operator):
    """18-E-50 Blue"""
    bl_label = "18-E-50 Blue"
    bl_idname = 'color.18_e_50_blue'
    def execute(self, context):
        set_base_color(0xadd4da, self.bl_label)
        return {'FINISHED'}

class BS18_E_51_Mermaid(bpy.types.Operator):
    """18-E-51 Mermaid"""
    bl_label = "18-E-51 Mermaid"
    bl_idname = 'color.18_e_51_mermaid'
    def execute(self, context):
        set_base_color(0x03978e, self.bl_label)
        return {'FINISHED'}

class BS18_E_53_Cobalt_Blue(bpy.types.Operator):
    """18-E-53 Cobalt Blue"""
    bl_label = "18-E-53 Cobalt Blue"
    bl_idname = 'color.18_e_53_cobalt_blue'
    def execute(self, context):
        set_base_color(0x028a82, self.bl_label)
        return {'FINISHED'}

class BS18_E_58_Blue(bpy.types.Operator):
    """18-E-58 Blue"""
    bl_label = "18-E-58 Blue"
    bl_idname = 'color.18_e_58_blue'
    def execute(self, context):
        set_base_color(0x233e39, self.bl_label)
        return {'FINISHED'}

class BS20_C_33_Pompadour(bpy.types.Operator):
    """20-C-33 Pompadour"""
    bl_label = "20-C-33 Pompadour"
    bl_idname = 'color.20_c_33_pompadour'
    def execute(self, context):
        set_base_color(0xbbcedb, self.bl_label)
        return {'FINISHED'}

class BS20_C_35_Blue(bpy.types.Operator):
    """20-C-35 Blue"""
    bl_label = "20-C-35 Blue"
    bl_idname = 'color.20_c_35_blue'
    def execute(self, context):
        set_base_color(0xa9bbc6, self.bl_label)
        return {'FINISHED'}

class BS20_C_37_Viking(bpy.types.Operator):
    """20-C-37 Viking"""
    bl_label = "20-C-37 Viking"
    bl_idname = 'color.20_c_37_viking'
    def execute(self, context):
        set_base_color(0x6d88a0, self.bl_label)
        return {'FINISHED'}

class BS20_C_39_Blue(bpy.types.Operator):
    """20-C-39 Blue"""
    bl_label = "20-C-39 Blue"
    bl_idname = 'color.20_c_39_blue'
    def execute(self, context):
        set_base_color(0x54697b, self.bl_label)
        return {'FINISHED'}

class BS20_C_40_Midnight(bpy.types.Operator):
    """20-C-40 Midnight"""
    bl_label = "20-C-40 Midnight"
    bl_idname = 'color.20_c_40_midnight'
    def execute(self, context):
        set_base_color(0x3d4d5a, self.bl_label)
        return {'FINISHED'}

class BS20_D_41_Powder_Blue(bpy.types.Operator):
    """20-D-41 Powder Blue"""
    bl_label = "20-D-41 Powder Blue"
    bl_idname = 'color.20_d_41_powder_blue'
    def execute(self, context):
        set_base_color(0xa9c6e2, self.bl_label)
        return {'FINISHED'}

class BS20_D_43_Blue(bpy.types.Operator):
    """20-D-43 Blue"""
    bl_label = "20-D-43 Blue"
    bl_idname = 'color.20_d_43_blue'
    def execute(self, context):
        set_base_color(0x7e94a9, self.bl_label)
        return {'FINISHED'}

class BS20_D_44_Blue(bpy.types.Operator):
    """20-D-44 Blue"""
    bl_label = "20-D-44 Blue"
    bl_idname = 'color.20_d_44_blue'
    def execute(self, context):
        set_base_color(0x697c8d, self.bl_label)
        return {'FINISHED'}

class BS20_D_45_Maritime(bpy.types.Operator):
    """20-D-45 Maritime"""
    bl_label = "20-D-45 Maritime"
    bl_idname = 'color.20_d_45_maritime'
    def execute(self, context):
        set_base_color(0x4b5966, self.bl_label)
        return {'FINISHED'}

class BS20_E_50_Blue(bpy.types.Operator):
    """20-E-50 Blue"""
    bl_label = "20-E-50 Blue"
    bl_idname = 'color.20_e_50_blue'
    def execute(self, context):
        set_base_color(0x81c6fd, self.bl_label)
        return {'FINISHED'}

class BS20_E_51_Corfu_Purple(bpy.types.Operator):
    """20-E-51 Corfu / Purple"""
    bl_label = "20-E-51 Corfu / Purple"
    bl_idname = 'color.20_e_51_corfu_purple'
    def execute(self, context):
        set_base_color(0x6ca5d3, self.bl_label)
        return {'FINISHED'}

class BS20_E_53_Blue(bpy.types.Operator):
    """20-E-53 Blue"""
    bl_label = "20-E-53 Blue"
    bl_idname = 'color.20_e_53_blue'
    def execute(self, context):
        set_base_color(0x3876ab, self.bl_label)
        return {'FINISHED'}

class BS20_E_56_Blue(bpy.types.Operator):
    """20-E-56 Blue"""
    bl_label = "20-E-56 Blue"
    bl_idname = 'color.20_e_56_blue'
    def execute(self, context):
        set_base_color(0x266492, self.bl_label)
        return {'FINISHED'}

class BS22_B_15_Swansdown(bpy.types.Operator):
    """22-B-15 Swansdown"""
    bl_label = "22-B-15 Swansdown"
    bl_idname = 'color.22_b_15_swansdown'
    def execute(self, context):
        set_base_color(0xe3e3df, self.bl_label)
        return {'FINISHED'}

class BS22_B_17_Lavender_Haze(bpy.types.Operator):
    """22-B-17 Lavender Haze"""
    bl_label = "22-B-17 Lavender Haze"
    bl_idname = 'color.22_b_17_lavender_haze'
    def execute(self, context):
        set_base_color(0xd8d7dd, self.bl_label)
        return {'FINISHED'}

class BS22_B_19_Soft_Bleu(bpy.types.Operator):
    """22-B-19 Soft Bleu"""
    bl_label = "22-B-19 Soft Bleu"
    bl_idname = 'color.22_b_19_soft_bleu'
    def execute(self, context):
        set_base_color(0xc4c3c9, self.bl_label)
        return {'FINISHED'}

class BS22_B_21_Kashmir(bpy.types.Operator):
    """22-B-21 Kashmir"""
    bl_label = "22-B-21 Kashmir"
    bl_idname = 'color.22_b_21_kashmir'
    def execute(self, context):
        set_base_color(0xaeadb2, self.bl_label)
        return {'FINISHED'}

class BS22_B_23_Purple(bpy.types.Operator):
    """22-B-23 Purple"""
    bl_label = "22-B-23 Purple"
    bl_idname = 'color.22_b_23_purple'
    def execute(self, context):
        set_base_color(0x89888c, self.bl_label)
        return {'FINISHED'}

class BS22_B_25_Nightshade(bpy.types.Operator):
    """22-B-25 Nightshade"""
    bl_label = "22-B-25 Nightshade"
    bl_idname = 'color.22_b_25_nightshade'
    def execute(self, context):
        set_base_color(0x6a696c, self.bl_label)
        return {'FINISHED'}

class BS22_B_27_Violet(bpy.types.Operator):
    """22-B-27 Violet"""
    bl_label = "22-B-27 Violet"
    bl_idname = 'color.22_b_27_violet'
    def execute(self, context):
        set_base_color(0x443f39, self.bl_label)
        return {'FINISHED'}

class BS22_B_29_Deep_Purple(bpy.types.Operator):
    """22-B-29 Deep Purple"""
    bl_label = "22-B-29 Deep Purple"
    bl_idname = 'color.22_b_29_deep_purple'
    def execute(self, context):
        set_base_color(0x221f1c, self.bl_label)
        return {'FINISHED'}

class BS22_C_31_White(bpy.types.Operator):
    """22-C-31 White"""
    bl_label = "22-C-31 White"
    bl_idname = 'color.22_c_31_white'
    def execute(self, context):
        set_base_color(0xffffff, self.bl_label)
        return {'FINISHED'}

class BS22_C_33_Soft_Purple(bpy.types.Operator):
    """22-C-33 Soft Purple"""
    bl_label = "22-C-33 Soft Purple"
    bl_idname = 'color.22_c_33_soft_purple'
    def execute(self, context):
        set_base_color(0xe5e5e5, self.bl_label)
        return {'FINISHED'}

class BS22_C_35_Purple(bpy.types.Operator):
    """22-C-35 Purple"""
    bl_label = "22-C-35 Purple"
    bl_idname = 'color.22_c_35_purple'
    def execute(self, context):
        set_base_color(0xbdbdbd, self.bl_label)
        return {'FINISHED'}

class BS22_C_37_Violet(bpy.types.Operator):
    """22-C-37 Violet"""
    bl_label = "22-C-37 Violet"
    bl_idname = 'color.22_c_37_violet'
    def execute(self, context):
        set_base_color(0x7d7b9b, self.bl_label)
        return {'FINISHED'}

class BS22_C_39_Purple(bpy.types.Operator):
    """22-C-39 Purple"""
    bl_label = "22-C-39 Purple"
    bl_idname = 'color.22_c_39_purple'
    def execute(self, context):
        set_base_color(0x5d5c74, self.bl_label)
        return {'FINISHED'}

class BS22_C_40_Purple(bpy.types.Operator):
    """22-C-40 Purple"""
    bl_label = "22-C-40 Purple"
    bl_idname = 'color.22_c_40_purple'
    def execute(self, context):
        set_base_color(0x474659, self.bl_label)
        return {'FINISHED'}

class BS22_D_41_Violet(bpy.types.Operator):
    """22-D-41 Violet"""
    bl_label = "22-D-41 Violet"
    bl_idname = 'color.22_d_41_violet'
    def execute(self, context):
        set_base_color(0xb0b3d4, self.bl_label)
        return {'FINISHED'}

class BS22_D_43_Violet(bpy.types.Operator):
    """22-D-43 Violet"""
    bl_label = "22-D-43 Violet"
    bl_idname = 'color.22_d_43_violet'
    def execute(self, context):
        set_base_color(0x888aa4, self.bl_label)
        return {'FINISHED'}

class BS22_D_44_Purple(bpy.types.Operator):
    """22-D-44 Purple"""
    bl_label = "22-D-44 Purple"
    bl_idname = 'color.22_d_44_purple'
    def execute(self, context):
        set_base_color(0x7a7c93, self.bl_label)
        return {'FINISHED'}

class BS22_D_45_Purple(bpy.types.Operator):
    """22-D-45 Purple"""
    bl_label = "22-D-45 Purple"
    bl_idname = 'color.22_d_45_purple'
    def execute(self, context):
        set_base_color(0x5c5485, self.bl_label)
        return {'FINISHED'}

class BS22_E_53_Purple(bpy.types.Operator):
    """22-E-53 Purple"""
    bl_label = "22-E-53 Purple"
    bl_idname = 'color.22_e_53_purple'
    def execute(self, context):
        set_base_color(0x685f96, self.bl_label)
        return {'FINISHED'}

class BS22_E_58_Purple(bpy.types.Operator):
    """22-E-58 Purple"""
    bl_label = "22-E-58 Purple"
    bl_idname = 'color.22_e_58_purple'
    def execute(self, context):
        set_base_color(0x443e62, self.bl_label)
        return {'FINISHED'}

class BS24_C_33_Lilac(bpy.types.Operator):
    """24-C-33 Lilac"""
    bl_label = "24-C-33 Lilac"
    bl_idname = 'color.24_c_33_lilac'
    def execute(self, context):
        set_base_color(0xebdae7, self.bl_label)
        return {'FINISHED'}

class BS24_C_35_Pink(bpy.types.Operator):
    """24-C-35 Pink"""
    bl_label = "24-C-35 Pink"
    bl_idname = 'color.24_c_35_pink'
    def execute(self, context):
        set_base_color(0xd5afbb, self.bl_label)
        return {'FINISHED'}

class BS24_C_37_Purple(bpy.types.Operator):
    """24-C-37 Purple"""
    bl_label = "24-C-37 Purple"
    bl_idname = 'color.24_c_37_purple'
    def execute(self, context):
        set_base_color(0xaa8c95, self.bl_label)
        return {'FINISHED'}

class BS24_C_38_Amethyst(bpy.types.Operator):
    """24-C-38 Amethyst"""
    bl_label = "24-C-38 Amethyst"
    bl_idname = 'color.24_c_38_amethyst'
    def execute(self, context):
        set_base_color(0x8c6991, self.bl_label)
        return {'FINISHED'}

class BS24_C_39_Regalia(bpy.types.Operator):
    """24-C-39 Regalia"""
    bl_label = "24-C-39 Regalia"
    bl_idname = 'color.24_c_39_regalia'
    def execute(self, context):
        set_base_color(0x6a506e, self.bl_label)
        return {'FINISHED'}

class BS24_C_40_Purple(bpy.types.Operator):
    """24-C-40 Purple"""
    bl_label = "24-C-40 Purple"
    bl_idname = 'color.24_c_40_purple'
    def execute(self, context):
        set_base_color(0x67555a, self.bl_label)
        return {'FINISHED'}

class BS24_E_50_Pink(bpy.types.Operator):
    """24-E-50 Pink"""
    bl_label = "24-E-50 Pink"
    bl_idname = 'color.24_e_50_pink'
    def execute(self, context):
        set_base_color(0xf98cc7, self.bl_label)
        return {'FINISHED'}

class BS24_E_53_Purple(bpy.types.Operator):
    """24-E-53 Purple"""
    bl_label = "24-E-53 Purple"
    bl_idname = 'color.24_e_53_purple'
    def execute(self, context):
        set_base_color(0xae638b, self.bl_label)
        return {'FINISHED'}

class BS24_E_56_Violet(bpy.types.Operator):
    """24-E-56 Violet"""
    bl_label = "24-E-56 Violet"
    bl_idname = 'color.24_e_56_violet'
    def execute(self, context):
        set_base_color(0x965579, self.bl_label)
        return {'FINISHED'}

class BS24_E_58_Purple(bpy.types.Operator):
    """24-E-58 Purple"""
    bl_label = "24-E-58 Purple"
    bl_idname = 'color.24_e_58_purple'
    def execute(self, context):
        set_base_color(0x5e354b, self.bl_label)
        return {'FINISHED'}


# BSC PANEL

class BSCPanel(bpy.types.Panel):
    bl_idname = "BSC_PT_Panel"
    bl_label = "British Standard"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

class BSC2660Panel(bpy.types.Panel):
    bl_idname = "BSC2660_PT_Panel"
    bl_label = "    BS2660 (1964)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'BSC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["0001_canary"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0002_oxlip"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0003_golden_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0004_marigold"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0005_poppy_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0006_post_office_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0008_chartreuse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0009_parakeet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0010_paris_vir_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0011_baltic_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0012_pacific_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0013_anchusa"].icon_id)
        scol.label(text="", icon_value=g.c_icons["0014_nightshade"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1015_zephyr"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1016_pink_haze"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1017_rose_gray"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1018_mecca_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1019_royal_maroon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1020_daybreak"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1021_orchis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1022_reef_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1023_tawney_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1024_chestnut"].icon_id)
        scol.label(text="", icon_value=g.c_icons["1025_crimson_cherry"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2026_mellow_buff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2027_cygnet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2028_fallow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2029_copra"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2030_pink_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2031_aurora"].icon_id)
        scol.label(text="", icon_value=g.c_icons["2032_cocoa"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3033_magnolia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3034_vanilla"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3036_cobweb"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3037_buffalo"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3038_congo_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3039_chocolate"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3040_manilla_pale_ivory"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3041_maple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3042_rich_cream"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3043_light_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3044_golden_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["3045_middle_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4046_off_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4047_silver_gleam"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4048_stone_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4049_eddystone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4050_olive"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4051_montella"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4052_buttermilk"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4053_jonquil"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4054_mimosa_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4055_jasmine_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4056_mustard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["4057_brass"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5058_gossamer"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5059_sky"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5050_quarry_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5061_pine_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5062_yaffie_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5063_moss_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5064_bredon_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5065_clover_leaf"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5066_grotto"].icon_id)
        scol.label(text="", icon_value=g.c_icons["5067_atlantic_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["6068_marble_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["6069_glacier"].icon_id)
        scol.label(text="", icon_value=g.c_icons["6070_pastel_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["6071_eau_de_nil"].icon_id)
        scol.label(text="", icon_value=g.c_icons["6073_bottle_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["6074_mid_brunswick_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7075_horizon_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7076_court_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7077_shadow_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7078_light_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7080_turquoise_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7081_narvik"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7082_porcelain_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7083_ribbon_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7084_fiesta_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7085_marine_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7086_midnight_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7087_steel_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7088_wedgewood_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["7089_castle_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["8090_shell_pink_columbine"].icon_id)
        scol.label(text="", icon_value=g.c_icons["8091_cyclamen"].icon_id)
        scol.label(text="", icon_value=g.c_icons["8092_regal_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9093_silver"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9094_flake_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9095_minerva_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9096_shire_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9097_dark_amiralty_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9098_blue_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9100_graphite"].icon_id)
        scol.label(text="", icon_value=g.c_icons["9101_charcoal"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.0001_canary", text="0001 Canary")
        scol.operator("color.0002_oxlip", text="0002 Oxlip")
        scol.operator("color.0003_golden_yellow", text="0003 Golden Yellow")
        scol.operator("color.0004_marigold", text="0004 Marigold")
        scol.operator("color.0005_poppy_red", text="0005 Poppy Red")
        scol.operator("color.0006_post_office_red", text="0006 Post Office Red")
        scol.operator("color.0008_chartreuse", text="0008 Chartreuse")
        scol.operator("color.0009_parakeet", text="0009 Parakeet")
        scol.operator("color.0010_paris_vir_green", text="0010 Paris / Vir. Green")
        scol.operator("color.0011_baltic_blue", text="0011 Baltic Blue")
        scol.operator("color.0012_pacific_blue", text="0012 Pacific Blue")
        scol.operator("color.0013_anchusa", text="0013 Anchusa")
        scol.operator("color.0014_nightshade", text="0014 Nightshade")
        scol.operator("color.1015_zephyr", text="1015 Zephyr")
        scol.operator("color.1016_pink_haze", text="1016 Pink Haze")
        scol.operator("color.1017_rose_gray", text="1017 Rose Gray")
        scol.operator("color.1018_mecca_red", text="1018 Mecca Red")
        scol.operator("color.1019_royal_maroon", text="1019 Royal Maroon")
        scol.operator("color.1020_daybreak", text="1020 Daybreak")
        scol.operator("color.1021_orchis", text="1021 Orchis")
        scol.operator("color.1022_reef_red", text="1022 Reef Red")
        scol.operator("color.1023_tawney_red", text="1023 Tawney Red")
        scol.operator("color.1024_chestnut", text="1024 Chestnut")
        scol.operator("color.1025_crimson_cherry", text="1025 Crimson / Cherry")
        scol.operator("color.2026_mellow_buff", text="2026 Mellow Buff")
        scol.operator("color.2027_cygnet", text="2027 Cygnet")
        scol.operator("color.2028_fallow", text="2028 Fallow")
        scol.operator("color.2029_copra", text="2029 Copra")
        scol.operator("color.2030_pink_beige", text="2030 Pink Beige")
        scol.operator("color.2031_aurora", text="2031 Aurora")
        scol.operator("color.2032_cocoa", text="2032 Cocoa")
        scol.operator("color.3033_magnolia", text="3033 Magnolia")
        scol.operator("color.3034_vanilla", text="3034 Vanilla")
        scol.operator("color.3036_cobweb", text="3036 Cobweb")
        scol.operator("color.3037_buffalo", text="3037 Buffalo")
        scol.operator("color.3038_congo_brown", text="3038 Congo Brown")
        scol.operator("color.3039_chocolate", text="3039 Chocolate")
        scol.operator("color.3040_manilla_pale_ivory", text="3040 Manilla / Pale Ivory")
        scol.operator("color.3041_maple", text="3041 Maple")
        scol.operator("color.3042_rich_cream", text="3042 Rich Cream")
        scol.operator("color.3043_light_stone", text="3043 Light Stone")
        scol.operator("color.3044_golden_brown", text="3044 Golden Brown")
        scol.operator("color.3045_middle_brown", text="3045 Middle Brown")
        scol.operator("color.4046_off_white", text="4046 Off White")
        scol.operator("color.4047_silver_gleam", text="4047 Silver Gleam")
        scol.operator("color.4048_stone_grey", text="4048 Stone Grey")
        scol.operator("color.4049_eddystone", text="4049 Eddystone")
        scol.operator("color.4050_olive", text="4050 Olive")
        scol.operator("color.4051_montella", text="4051 Montella")
        scol.operator("color.4052_buttermilk", text="4052 Buttermilk")
        scol.operator("color.4053_jonquil", text="4053 Jonquil")
        scol.operator("color.4054_mimosa_yellow", text="4054 Mimosa Yellow")
        scol.operator("color.4055_jasmine_yellow", text="4055 Jasmine Yellow")
        scol.operator("color.4056_mustard", text="4056 Mustard")
        scol.operator("color.4057_brass", text="4057 Brass")
        scol.operator("color.5058_gossamer", text="5058 Gossamer")
        scol.operator("color.5059_sky", text="5059 Sky")
        scol.operator("color.5050_quarry_grey", text="5050 Quarry Grey")
        scol.operator("color.5061_pine_green", text="5061 Pine Green")
        scol.operator("color.5062_yaffie_green", text="5062 Yaffie Green")
        scol.operator("color.5063_moss_green", text="5063 Moss Green")
        scol.operator("color.5064_bredon_green", text="5064 Bredon Green")
        scol.operator("color.5065_clover_leaf", text="5065 Clover Leaf")
        scol.operator("color.5066_grotto", text="5066 Grotto")
        scol.operator("color.5067_atlantic_green", text="5067 Atlantic Green")
        scol.operator("color.6068_marble_green", text="6068 Marble Green")
        scol.operator("color.6069_glacier", text="6069 Glacier")
        scol.operator("color.6070_pastel_green", text="6070 Pastel Green")
        scol.operator("color.6071_eau_de_nil", text="6071 Eau De Nil")
        scol.operator("color.6073_bottle_green", text="6073 Bottle Green")
        scol.operator("color.6074_mid_brunswick_green", text="6074 Mid Brunswick Green")
        scol.operator("color.7075_horizon_blue", text="7075 Horizon Blue")
        scol.operator("color.7076_court_grey", text="7076 Court Grey")
        scol.operator("color.7077_shadow_blue", text="7077 Shadow Blue")
        scol.operator("color.7078_light_grey", text="7078 Light Grey")
        scol.operator("color.7080_turquoise_blue", text="7080 Turquoise Blue")
        scol.operator("color.7081_narvik", text="7081 Narvik")
        scol.operator("color.7082_porcelain_blue", text="7082 Porcelain Blue")
        scol.operator("color.7083_ribbon_blue", text="7083 Ribbon Blue")
        scol.operator("color.7084_fiesta_blue", text="7084 Fiesta Blue")
        scol.operator("color.7085_marine_blue", text="7085 Marine Blue")
        scol.operator("color.7086_midnight_blue", text="7086 Midnight Blue")
        scol.operator("color.7087_steel_blue", text="7087 Steel Blue")
        scol.operator("color.7088_wedgewood_blue", text="7088 Wedgewood Blue")
        scol.operator("color.7089_castle_grey", text="7089 Castle Grey")
        scol.operator("color.8090_shell_pink_columbine", text="8090 Shell Pink / Columbine")
        scol.operator("color.8091_cyclamen", text="8091 Cyclamen")
        scol.operator("color.8092_regal_red", text="8092 Regal Red")
        scol.operator("color.9093_silver", text="9093 Silver")
        scol.operator("color.9094_flake_grey", text="9094 Flake Grey")
        scol.operator("color.9095_minerva_grey", text="9095 Minerva Grey")
        scol.operator("color.9096_shire_grey", text="9096 Shire Grey")
        scol.operator("color.9097_dark_amiralty_grey", text="9097 Dark Amiralty Grey")
        scol.operator("color.9098_blue_grey", text="9098 Blue Grey")
        scol.operator("color.9100_graphite", text="9100 Graphite")
        scol.operator("color.9101_charcoal", text="9101 Charcoal")

class BSC381CPanel(bpy.types.Panel):
    bl_idname = "BSC381C_PT_Panel"
    bl_label = "    BS381C (1930)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'BSC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["101_sky_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["102_turquoise_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["103_peacock_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["104_azure_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["105_oxford_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["106_royal_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["107_strong_blue_pacific_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["108_aircraft_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["109_middle_blue_anchusa"].icon_id)
        scol.label(text="", icon_value=g.c_icons["110_roundel_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["111_sky_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["112_arctic_blue_fiesta_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["113_deep_saxe_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["114_rail_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["115_cobalt_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["166_french_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["172_pale_rundel_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["174_orient_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["175_light_french_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["210_sky"].icon_id)
        scol.label(text="", icon_value=g.c_icons["216_eau_de_nil"].icon_id)
        scol.label(text="", icon_value=g.c_icons["217_sea_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["218_grass_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["220_olive_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["221_brilliant_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["222_light_bronze_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["223_middle_bronze_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["224_deep_bronze_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["225_light_brunswick_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["226_mid_brunswick_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["227_deep_brunswick_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["228_emerald_green_viridian"].icon_id)
        scol.label(text="", icon_value=g.c_icons["241_dark_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["262_bold_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["267_deep_chrome_green_traffic_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["275_opaline_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["278_light_olive_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["280_verdigris_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["282_forest_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["283_aircraft_grey_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["284_spruce_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["285_nato_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["298_olive_drab"].icon_id)
        scol.label(text="", icon_value=g.c_icons["309_canary_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["310_primrose"].icon_id)
        scol.label(text="", icon_value=g.c_icons["315_grapefruit"].icon_id)
        scol.label(text="", icon_value=g.c_icons["320_light_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["337_very_dark_drab"].icon_id)
        scol.label(text="", icon_value=g.c_icons["350_dark_earth"].icon_id)
        scol.label(text="", icon_value=g.c_icons["352_pale_cream"].icon_id)
        scol.label(text="", icon_value=g.c_icons["353_deep_cream"].icon_id)
        scol.label(text="", icon_value=g.c_icons["355_lemon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["356_golden_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["358_light_buff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["359_middle_buff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["361_light_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["363_bold_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["365_vellum"].icon_id)
        scol.label(text="", icon_value=g.c_icons["366_light_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["367_manilla"].icon_id)
        scol.label(text="", icon_value=g.c_icons["369_biscuit"].icon_id)
        scol.label(text="", icon_value=g.c_icons["380_camouflage_desert_sand"].icon_id)
        scol.label(text="", icon_value=g.c_icons["384_light_straw"].icon_id)
        scol.label(text="", icon_value=g.c_icons["388_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["389_camouflage_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["411_middle_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["412_dark_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["414_golden_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["420_dark_camouflage_desert_sand"].icon_id)
        scol.label(text="", icon_value=g.c_icons["435_camouflage_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["436_dark_camouflage_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["444_terracotta"].icon_id)
        scol.label(text="", icon_value=g.c_icons["445_venetian_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["446_red_oxide"].icon_id)
        scol.label(text="", icon_value=g.c_icons["447_salmon_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["448_deep_indian_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["449_light_purple_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["452_dark_crimson"].icon_id)
        scol.label(text="", icon_value=g.c_icons["453_shell_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["454_pale_roundel_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["460_deep_buff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["473_gulf_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["489_leaf_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["499_service_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["537_signal_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["538_post_office_red_cherry"].icon_id)
        scol.label(text="", icon_value=g.c_icons["539_currant_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["540_crimson"].icon_id)
        scol.label(text="", icon_value=g.c_icons["541_maroon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["542_ruby"].icon_id)
        scol.label(text="", icon_value=g.c_icons["557_light_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["564_bold_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["568_apricot"].icon_id)
        scol.label(text="", icon_value=g.c_icons["592_international_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["593_rail_red_azo_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["626_camouflage_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["627_light_aircraft_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["629_dark_camouflage_grey_quacker_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["630_french_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["631_light_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["632_dark_admiralty_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["633_raf_blue_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["634_slate"].icon_id)
        scol.label(text="", icon_value=g.c_icons["635_lead"].icon_id)
        scol.label(text="", icon_value=g.c_icons["636_pru_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["637_medium_sea_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["638_dark_sea_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["639_light_slate_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["640_extra_dark_sea_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["642_night"].icon_id)
        scol.label(text="", icon_value=g.c_icons["671_middle_graphite"].icon_id)
        scol.label(text="", icon_value=g.c_icons["676_light_weatherwork_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["677_dark_weatherwork_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["692_smoke_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["693_aircraft_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["694_dove_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["697_light_admiralty_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["796_dark_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["797_light_violet"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.101_sky_blue", text="101 Sky Blue")
        scol.operator("color.102_turquoise_blue", text=" 102 Turquoise Blue")
        scol.operator("color.103_peacock_blue", text=" 103 Peacock Blue")
        scol.operator("color.104_azure_blue", text="104 Azure Blue")
        scol.operator("color.105_oxford_blue", text="105 Oxford Blue")
        scol.operator("color.106_royal_blue", text="106 Royal Blue")
        scol.operator("color.107_strong_blue_pacific_blue", text="107 Strong Blue / Pacific Blue")
        scol.operator("color.108_aircraft_blue", text="108 Aircraft Blue")
        scol.operator("color.109_middle_blue_anchusa", text="109 Middle Blue / Anchusa")
        scol.operator("color.110_roundel_blue", text="110 Roundel Blue")
        scol.operator("color.111_sky_blue", text="111 Sky Blue")
        scol.operator("color.112_arctic_blue_fiesta_blue", text="112 Arctic Blue / Fiesta Blue")
        scol.operator("color.113_deep_saxe_blue", text="113 Deep Saxe Blue")
        scol.operator("color.114_rail_blue", text="114 Rail Blue")
        scol.operator("color.115_cobalt_blue", text="115 Cobalt Blue")
        scol.operator("color.166_french_blue", text="166 French Blue")
        scol.operator("color.172_pale_rundel_blue", text="172 Pale Rundel Blue")
        scol.operator("color.174_orient_blue", text="174 Orient Blue")
        scol.operator("color.175_light_french_blue", text="175 Light French Blue")
        scol.operator("color.210_sky", text="210 Sky")
        scol.operator("color.216_eau_de_nil", text="216 Eau De Nil")
        scol.operator("color.217_sea_green", text="217 Sea Green")
        scol.operator("color.218_grass_green", text="218 Grass Green")
        scol.operator("color.220_olive_green", text="220 Olive Green")
        scol.operator("color.221_brilliant_green", text="221 Brilliant Green")
        scol.operator("color.222_light_bronze_green", text="222 Light Bronze Green")
        scol.operator("color.223_middle_bronze_green", text="223 Middle Bronze Green")
        scol.operator("color.224_deep_bronze_green", text="224 Deep Bronze Green")
        scol.operator("color.225_light_brunswick_green", text="225 Light Brunswick Green")
        scol.operator("color.226_mid_brunswick_green", text="226 Mid Brunswick Green")
        scol.operator("color.227_deep_brunswick_green", text="227 Deep Brunswick Green")
        scol.operator("color.228_emerald_green_viridian", text="228 Emerald Green / Viridian")
        scol.operator("color.241_dark_green", text="241 Dark Green")
        scol.operator("color.262_bold_green", text="262 Bold Green")
        scol.operator("color.267_deep_chrome_green_traffic_green", text="267 Deep Chrome Green / Traffic Green")
        scol.operator("color.275_opaline_green", text="275 Opaline Green")
        scol.operator("color.278_light_olive_green", text="278 Light Olive Green")
        scol.operator("color.280_verdigris_green", text="280 Verdigris Green")
        scol.operator("color.282_forest_green", text="282 Forest Green")
        scol.operator("color.283_aircraft_grey_green", text="283 Aircraft Grey Green")
        scol.operator("color.284_spruce_green", text="284 Spruce Green")
        scol.operator("color.285_nato_green", text="285 Nato Green")
        scol.operator("color.298_olive_drab", text="298 Olive Drab")
        scol.operator("color.309_canary_yellow", text="309 Canary Yellow")
        scol.operator("color.310_primrose", text="310 Primrose")
        scol.operator("color.315_grapefruit", text="315 Grapefruit")
        scol.operator("color.320_light_brown", text="320 Light Brown")
        scol.operator("color.337_very_dark_drab", text="337 Very Dark Drab")
        scol.operator("color.350_dark_earth", text="350 Dark Earth")
        scol.operator("color.352_pale_cream", text="352 Pale Cream")
        scol.operator("color.353_deep_cream", text="353 Deep Cream")
        scol.operator("color.355_lemon", text="355 Lemon")
        scol.operator("color.356_golden_yellow", text="356 Golden Yellow")
        scol.operator("color.358_light_buff", text="358 Light Buff")
        scol.operator("color.359_middle_buff", text="359 Middle Buff")
        scol.operator("color.361_light_stone", text="361 Light Stone")
        scol.operator("color.363_bold_yellow", text="363 Bold Yellow")
        scol.operator("color.365_vellum", text="365 Vellum")
        scol.operator("color.366_light_beige", text="366 Light Beige")
        scol.operator("color.367_manilla", text="367 Manilla")
        scol.operator("color.369_biscuit", text="369 Biscuit")
        scol.operator("color.380_camouflage_desert_sand", text="380 Camouflage Desert Sand")
        scol.operator("color.384_light_straw", text="384 Light Straw")
        scol.operator("color.388_beige", text="388 Beige")
        scol.operator("color.389_camouflage_beige", text="389 Camouflage Beige")
        scol.operator("color.411_middle_brown", text="411 Middle Brown")
        scol.operator("color.412_dark_brown", text="412 Dark Brown")
        scol.operator("color.414_golden_brown", text="414 Golden Brown")
        scol.operator("color.420_dark_camouflage_desert_sand", text="420 Dark Camouflage Desert Sand")
        scol.operator("color.435_camouflage_red", text="435 Camouflage Red")
        scol.operator("color.436_dark_camouflage_brown", text="436 Dark Camouflage Brown")
        scol.operator("color.444_terracotta", text="444 Terracotta")
        scol.operator("color.445_venetian_red", text="445 Venetian Red")
        scol.operator("color.446_red_oxide", text="446 Red Oxide")
        scol.operator("color.447_salmon_pink", text="447 Salmon Pink")
        scol.operator("color.448_deep_indian_red", text="448 Deep Indian Red")
        scol.operator("color.449_light_purple_brown", text="449 Light Purple Brown")
        scol.operator("color.452_dark_crimson", text="452 Dark Crimson")
        scol.operator("color.453_shell_pink", text="453 Shell Pink")
        scol.operator("color.454_pale_roundel_red", text="454 Pale Roundel Red")
        scol.operator("color.460_deep_buff", text="460 Deep Buff")
        scol.operator("color.473_gulf_red", text="473 Gulf Red")
        scol.operator("color.489_leaf_brown", text="489 Leaf Brown")
        scol.operator("color.499_service_brown", text="499 Service Brown")
        scol.operator("color.537_signal_red", text="537 Signal Red")
        scol.operator("color.538_post_office_red_cherry", text="538 Post Office Red / Cherry")
        scol.operator("color.539_currant_red", text="539 Currant Red")
        scol.operator("color.540_crimson", text="540 Crimson")
        scol.operator("color.541_maroon", text="541 Maroon")
        scol.operator("color.542_ruby", text="542 Ruby")
        scol.operator("color.557_light_orange", text="557 Light Orange")
        scol.operator("color.564_bold_red", text="564 Bold Red")
        scol.operator("color.568_apricot", text="568 Apricot")
        scol.operator("color.592_international_orange", text="592 International Orange")
        scol.operator("color.593_rail_red_azo_orange", text="593 Rail Red / Azo Orange")
        scol.operator("color.626_camouflage_grey", text="626 Camouflage Grey")
        scol.operator("color.627_light_aircraft_grey", text="627 Light Aircraft Grey")
        scol.operator("color.629_dark_camouflage_grey_quacker_grey", text="629 Dark Camouflage Grey / Quaker Grey")
        scol.operator("color.630_french_grey", text="630 French Grey")
        scol.operator("color.631_light_grey", text="631 Light Grey")
        scol.operator("color.632_dark_admiralty_grey", text="632 Dark Admiralty Grey")
        scol.operator("color.633_raf_blue_grey", text="633 Raf Blue Grey")
        scol.operator("color.634_slate", text="634 Slate")
        scol.operator("color.635_lead", text="635 Lead")
        scol.operator("color.636_pru_blue", text="636 Pru Blue")
        scol.operator("color.637_medium_sea_grey", text="637 Medium Sea Grey")
        scol.operator("color.638_dark_sea_grey", text="638 Dark Sea Grey")
        scol.operator("color.639_light_slate_grey", text="639 Light Slate Grey")
        scol.operator("color.640_extra_dark_sea_grey", text="640 Extra Dark Sea Grey")
        scol.operator("color.642_night", text="642 Night")
        scol.operator("color.671_middle_graphite", text="671 Middle Graphite")
        scol.operator("color.676_light_weatherwork_grey", text="676 Light Weatherwork Grey")
        scol.operator("color.677_dark_weatherwork_grey", text="677 Dark Weatherwork Grey")
        scol.operator("color.692_smoke_grey", text="692 Smoke Grey")
        scol.operator("color.693_aircraft_grey", text="693 Aircraft Grey")
        scol.operator("color.694_dove_grey", text="694 Dove Grey")
        scol.operator("color.697_light_admiralty_grey", text="697 Light Admiralty Grey")
        scol.operator("color.796_dark_violet", text="796 Dark Violet")
        scol.operator("color.797_light_violet", text="797 Light Violet")

class BSC5252Panel(bpy.types.Panel):
    bl_idname = "BSC5252_PT_Panel"
    bl_label = "    BS5252 (1976)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'BSC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["00_a_01_ash_grey_oyster_grey_portland"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_a_03_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_a_05_goose_grey_sea_mist_goosewing"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_a_07_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_a_09_flint_grey_flint"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_a_11_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_a_13_storm_grey_greyfriar"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_e_53_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["00_e_55_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_a_03_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_a_07_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_a_11_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_c_33_lupin_pink_candy_floss_pink_wafer"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_c_35_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_c_37_clover_pink_corinth_fontana"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_c_39_victoria_plum_aubergine_plum"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_c_40_deep_plum_loganberry"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_d_41_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_d_43_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_d_44_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_d_45_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_e_53_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_e_56_deep_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["02_e_58_bordeaux"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_15_rosepetal_pastel_pink_dawn_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_15_dawn_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_17_tea_rose"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_19_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_21_sierra"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_23_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_25_saracen"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_27_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_b_29_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_c_31_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_c_33_parisian_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_c_35_soft_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_c_37_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_c_39_copperbeech"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_c_40_maroon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_d_41_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_d_43_robin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_d_44_tawny"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_d_45_russet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_49_petal"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_50_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_51_salmon_red_lobster_azalea"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_53_carnival_red_poppy"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_55_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_56_carnival_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["04_e_58_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_a_03_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_a_07_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_a_11_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_c_33_cameo"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_c_35_light_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_c_37_brownstone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_c_39_saddle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_c_40_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_d_41_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_d_43_kalahari"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_d_44_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_d_45_mace"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_e_50_apricot"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_e_51_clementine"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_e_53_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_e_55_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["06_e_56_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_a_14_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_15_magnolia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_17_fawn"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_19_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_21_antelope"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_23_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_25_beaver"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_27_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_b_29_vandye"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_c_31_blush_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_c_33_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_c_35_butterscoth"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_c_37_bracken"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_c_39_bison"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_c_40_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_d_41_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_d_43_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_d_44_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_d_45_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_e_51_golden_ambar"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_e_53_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_e_55_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["08_e_56_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_a_01_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_a_03_sink_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_a_05_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_a_07_wood_ash"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_a_09_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_a_11_storm_rhino"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_15_ivory"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_17_greystone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_19_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_21_lizard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_23_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_25_turtle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_27_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_b_29_ironstone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_c_31_champagne"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_c_33_pollen"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_c_35_golden_bronze"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_c_37_yellow_brown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_c_39_saluki"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_d_41_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_d_43_banana"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_d_44_light_olive"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_d_45_florida"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_e_49_pale_lemon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_e_50_forsythia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_e_51_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_e_53_canary"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_e_55_camery_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["10_e_56_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_15_seafoam"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_17_willow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_19_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_21_opaline"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_23_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_25_thyme"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_27_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_b_29_juniper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_31_light_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_33_catkin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_35_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_37_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_39_orchard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_40_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_c_41_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_d_43_sapling"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_d_44_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_d_45_tundra"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_e_51_citrine"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_e_53_linden"].icon_id)
        scol.label(text="", icon_value=g.c_icons["12_e_55_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_c_31_green_alpine"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_c_33_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_c_35_breamer"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_c_37_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_c_39_hollybush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_c_40_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_d_41_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_d_43_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_d_44_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_d_45_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_e_49_light_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_e_50_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_e_51_goblin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_e_53_avarice"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_e_56_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["14_e_58_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_a_03_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_a_07_mid_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_a_11_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_c_33_duckegg"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_c_35_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_c_37_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_c_39_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_c_40_deep_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_d_41_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_d_43_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_d_44_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_d_45_green_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_e_50_turquoise"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_e_53_seafarer"].icon_id)
        scol.label(text="", icon_value=g.c_icons["16_e_56_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_a_14_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_15_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_17_silver_haze"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_19_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_21_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_23_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_25_dark_admiral_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_27_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_b_29_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_c_31_ice_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_c_33_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_c_35_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_c_37_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_c_39_deep_river"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_c_40_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_d_41_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_d_43_dresden_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_d_44_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_d_45_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_e_49_astral_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_e_50_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_e_51_mermaid"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_e_53_cobalt_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["18_e_58_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_c_33_pompadour"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_c_35_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_c_37_viking"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_c_39_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_c_40_midnight"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_d_41_powder_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_d_43_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_d_44_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_d_45_maritime"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_e_50_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_e_51_corfu_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_e_53_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["20_e_56_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_15_swansdown"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_17_lavender_haze"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_19_soft_bleu"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_21_kashmir"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_23_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_25_nightshade"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_27_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_b_29_deep_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_c_31_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_c_33_soft_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_c_35_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_c_37_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_c_39_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_c_40_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_d_41_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_d_43_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_d_44_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_d_45_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_e_53_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["22_e_58_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_c_33_lilac"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_c_35_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_c_37_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_c_38_amethyst"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_c_39_regalia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_c_40_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_e_50_pink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_e_53_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_e_56_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["24_e_58_purple"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.00_a_01_ash_grey_oyster_grey_portland", text="00-A-01 Ash Grey / Oyster Grey / Portland")
        scol.operator("color.00_a_03_grey", text="00-A-03 Grey")
        scol.operator("color.00_a_05_goose_grey_sea_mist_goosewing", text="00-A-05 Goose Grey / Sea Mist / Goosewing")
        scol.operator("color.00_a_07_grey", text="00-A-07 Grey")
        scol.operator("color.00_a_09_flint_grey_flint", text="00-A-09 Flint Grey / Flint")
        scol.operator("color.00_a_11_grey", text="00-A-11 Grey")
        scol.operator("color.00_a_13_storm_grey_greyfriar", text="00-A-13 Storm Grey / Greyfriar")
        scol.operator("color.00_e_53_black", text="00-E-53 Black")
        scol.operator("color.00_e_55_white", text="00-E-55 White")
        scol.operator("color.02_a_03_grey", text="02-A-03 Grey")
        scol.operator("color.02_a_07_grey", text="02-A-07 Grey")
        scol.operator("color.02_a_11_grey", text="02-A-11 Grey")
        scol.operator("color.02_c_33_lupin_pink_candy_floss_pink_wafer", text="02-C-33 Lupin Pink / Candy Floss / Pink Wafer")
        scol.operator("color.02_c_35_pink", text="02-C-35 Pink")
        scol.operator("color.02_c_37_clover_pink_corinth_fontana", text="02-C-37 Clover Pink / Corinth / Fontana")
        scol.operator("color.02_c_39_victoria_plum_aubergine_plum", text="02-C-39 Victoria Plum / Aubergine / Plum")
        scol.operator("color.02_c_40_deep_plum_loganberry", text="02-C-40 Deep Plum / Loganberry")
        scol.operator("color.02_d_41_pink", text="02-D-41 Pink")
        scol.operator("color.02_d_43_pink", text="02-D-43 Pink")
        scol.operator("color.02_d_44_pink", text="02-D-44 Pink")
        scol.operator("color.02_d_45_purple", text="02-D-45 Purple")
        scol.operator("color.02_e_53_purple", text="02-E-53 Purple")
        scol.operator("color.02_e_56_deep_pink", text="02-E-56 Deep Pink")
        scol.operator("color.02_e_58_bordeaux", text="02-E-58 Bordeaux")
        scol.operator("color.04_b_15_rosepetal_pastel_pink_dawn_pink", text="04-B-15 Rosepetal / Pastel Pink / Dawn Pink")
        scol.operator("color.04_b_15_dawn_pink", text="04-B-15 Dawn Pink")
        scol.operator("color.04_b_17_tea_rose", text="04-B-17 Tea Rose")
        scol.operator("color.04_b_19_beige", text="04-B-19 Beige")
        scol.operator("color.04_b_21_sierra", text="04-B-21 Sierra")
        scol.operator("color.04_b_23_brown", text="04-B-23 Brown")
        scol.operator("color.04_b_25_saracen", text="04-B-25 Saracen")
        scol.operator("color.04_b_27_brown", text="04-B-27 Brown")
        scol.operator("color.04_b_29_brown", text="04-B-29 Brown")
        scol.operator("color.04_c_31_pink", text="04-C-31 Pink")
        scol.operator("color.04_c_33_parisian_pink", text="04-C-33 Parisian Pink")
        scol.operator("color.04_c_35_soft_red", text="04-C-35 Soft Red")
        scol.operator("color.04_c_37_red", text="04-C-37 Red")
        scol.operator("color.04_c_39_copperbeech", text="04-C-39 Copperbeech")
        scol.operator("color.04_c_40_maroon", text="04-C-40 Maroon")
        scol.operator("color.04_d_41_pink", text="04-D-41 Pink")
        scol.operator("color.04_d_43_robin", text="04-D-43 Robin")
        scol.operator("color.04_d_44_tawny", text="04-D-44 Tawny")
        scol.operator("color.04_d_45_russet", text="04-D-45 Russet")
        scol.operator("color.04_e_49_petal", text="04-E-49 Petal")
        scol.operator("color.04_e_50_pink", text="04-E-50 Pink")
        scol.operator("color.04_e_51_salmon_red_lobster_azalea", text="04-E-51 Salmon Red / Lobster / Azalea")
        scol.operator("color.04_e_53_carnival_red_poppy", text="04-E-53 Carnival Red / Poppy")
        scol.operator("color.04_e_55_red", text="04-E-55 Red")
        scol.operator("color.04_e_56_carnival_red", text="04-E-56 Carnival Red")
        scol.operator("color.04_e_58_red", text="04-E-58 Red")
        scol.operator("color.06_a_03_grey", text="06-A-03 Grey")
        scol.operator("color.06_a_07_grey", text="06-A-07 Grey")
        scol.operator("color.06_a_11_grey", text="06-A-11 Grey")
        scol.operator("color.06_c_33_cameo", text="06-C-33 Cameo")
        scol.operator("color.06_c_35_light_orange", text="06-C-35 Light Orange")
        scol.operator("color.06_c_37_brownstone", text="06-C-37 Brownstone")
        scol.operator("color.06_c_39_saddle", text="06-C-39 Saddle")
        scol.operator("color.06_c_40_brown", text="06-C-40 Brown")
        scol.operator("color.06_d_41_orange", text="06-D-41 Orange")
        scol.operator("color.06_d_43_kalahari", text="06-D-43 Kalahari")
        scol.operator("color.06_d_44_orange", text="06-D-44 Orange")
        scol.operator("color.06_d_45_mace", text="06-D-45 Mace")
        scol.operator("color.06_e_50_apricot", text="06-E-50 Apricot")
        scol.operator("color.06_e_51_clementine", text="06-E-51 Clementine")
        scol.operator("color.06_e_53_orange", text="06-E-53 Orange")
        scol.operator("color.06_e_55_orange", text="06-E-55 Orange")
        scol.operator("color.06_e_56_yellow", text="06-E-56 Yellow")
        scol.operator("color.08_a_14_black", text="08-A-14 Black")
        scol.operator("color.08_b_15_magnolia", text="08-B-15 Magnolia")
        scol.operator("color.08_b_17_fawn", text="08-B-17 Fawn")
        scol.operator("color.08_b_19_beige", text="08-B-19 Beige")
        scol.operator("color.08_b_21_antelope", text="08-B-21 Antelope")
        scol.operator("color.08_b_23_brown", text="08-B-23 Brown")
        scol.operator("color.08_b_25_beaver", text="08-B-25 Beaver")
        scol.operator("color.08_b_27_brown", text="08-B-27 Brown")
        scol.operator("color.08_b_29_vandye", text="08-B-29 Vandye")
        scol.operator("color.08_c_31_blush_stone", text="08-C-31 Blush Stone")
        scol.operator("color.08_c_33_beige", text="08-C-33 Beige")
        scol.operator("color.08_c_35_butterscoth", text="08-C-35 Butterscoth")
        scol.operator("color.08_c_37_bracken", text="08-C-37 Bracken")
        scol.operator("color.08_c_39_bison", text="08-C-39 Bison")
        scol.operator("color.08_c_40_brown", text="08-C-40 Brown")
        scol.operator("color.08_d_41_yellow", text="08-D-41 Yellow")
        scol.operator("color.08_d_43_yellow", text="08-D-43 Yellow")
        scol.operator("color.08_d_44_brown", text="08-D-44 Brown")
        scol.operator("color.08_d_45_brown", text="08-D-45 Brown")
        scol.operator("color.08_e_51_golden_ambar", text="08-E-51 Golden Ambar")
        scol.operator("color.08_e_53_yellow", text="08-E-53 Yellow")
        scol.operator("color.08_e_55_orange", text="08-E-55 Orange")
        scol.operator("color.08_e_56_yellow", text="08-E-56 Yellow")
        scol.operator("color.10_a_01_white", text="10-A-01 White")
        scol.operator("color.10_a_03_sink_grey", text="10-A-03 Sink Grey")
        scol.operator("color.10_a_05_grey", text="10-A-05 Grey")
        scol.operator("color.10_a_07_wood_ash", text="10-A-07 Wood Ash")
        scol.operator("color.10_a_09_grey", text="10-A-09 Grey")
        scol.operator("color.10_a_11_storm_rhino", text="10-A-11 Storm / Rhino")
        scol.operator("color.10_b_15_ivory", text="10-B-15 Ivory")
        scol.operator("color.10_b_17_greystone", text="10-B-17 Greystone")
        scol.operator("color.10_b_19_beige", text="10-B-19 Beige")
        scol.operator("color.10_b_21_lizard", text="10-B-21 Lizard")
        scol.operator("color.10_b_23_brown", text="10-B-23 Brown")
        scol.operator("color.10_b_25_turtle", text="10-B-25 Turtle")
        scol.operator("color.10_b_27_brown", text="10-B-27 Brown")
        scol.operator("color.10_b_29_ironstone", text="10-B-29 Ironstone")
        scol.operator("color.10_c_31_champagne", text="10-C-31 Champagne")
        scol.operator("color.10_c_33_pollen", text="10-C-33 Pollen")
        scol.operator("color.10_c_35_golden_bronze", text="10-C-35 Golden Bronze")
        scol.operator("color.10_c_37_yellow_brown", text="10-C-37 Yellow Brown")
        scol.operator("color.10_c_39_saluki", text="10-C-39 Saluki")
        scol.operator("color.10_d_41_yellow", text="10-D-41 Yellow")
        scol.operator("color.10_d_43_banana", text="10-D-43 Banana")
        scol.operator("color.10_d_44_light_olive", text="10-D-44 Light Olive")
        scol.operator("color.10_d_45_florida", text="10-D-45 Florida")
        scol.operator("color.10_e_49_pale_lemon", text="10-E-49 Pale Lemon")
        scol.operator("color.10_e_50_forsythia", text="10-E-50 Forsythia")
        scol.operator("color.10_e_51_yellow", text="10-E-51 Yellow")
        scol.operator("color.10_e_53_canary", text="10-E-53 Canary")
        scol.operator("color.10_e_55_camery_yellow", text="10-E-55 Camery Yellow")
        scol.operator("color.10_e_56_yellow", text="10-E-56 Yellow")
        scol.operator("color.12_b_15_seafoam", text="12-B-15 Seafoam")
        scol.operator("color.12_b_17_willow", text="12-B-17 Willow")
        scol.operator("color.12_b_19_beige", text="12-B-19 Beige")
        scol.operator("color.12_b_21_opaline", text="12-B-21 Opaline")
        scol.operator("color.12_b_23_green", text="12-B-23 Green")
        scol.operator("color.12_b_25_thyme", text="12-B-25 Thyme")
        scol.operator("color.12_b_27_green", text="12-B-27 Green")
        scol.operator("color.12_b_29_juniper", text="12-B-29 Juniper")
        scol.operator("color.12_c_31_light_yellow", text="12-C-31 Light Yellow")
        scol.operator("color.12_c_33_catkin", text="12-C-33 Catkin")
        scol.operator("color.12_c_35_green", text="12-C-35 Green")
        scol.operator("color.12_c_37_green", text="12-C-37 Green")
        scol.operator("color.12_c_39_orchard", text="12-C-39 Orchard")
        scol.operator("color.12_c_40_green", text="12-C-40 Green")
        scol.operator("color.12_c_41_green", text="12-C-41 Green")
        scol.operator("color.12_d_43_sapling", text="12-D-43 Sapling")
        scol.operator("color.12_d_44_green", text="12-D-44 Green")
        scol.operator("color.12_d_45_tundra", text="12-D-45 Tundra")
        scol.operator("color.12_e_51_citrine", text="12-E-51 Citrine")
        scol.operator("color.12_e_53_linden", text="12-E-53 Linden")
        scol.operator("color.12_e_55_green", text="12-E-55 Green")
        scol.operator("color.14_c_31_green_alpine", text="14-C-31 Green / Alpine")
        scol.operator("color.14_c_33_green", text="14-C-33 Green")
        scol.operator("color.14_c_35_breamer", text="14-C-35 Breamer")
        scol.operator("color.14_c_37_green", text="14-C-37 Green")
        scol.operator("color.14_c_39_hollybush", text="14-C-39 Hollybush")
        scol.operator("color.14_c_40_green", text="14-C-40 Green")
        scol.operator("color.14_d_41_green", text="14-D-41 Green")
        scol.operator("color.14_d_43_green", text="14-D-43 Green")
        scol.operator("color.14_d_44_green", text="14-D-44 Green")
        scol.operator("color.14_d_45_green", text="14-D-45 Green")
        scol.operator("color.14_e_49_light_green", text="14-E-49 Light Green")
        scol.operator("color.14_e_50_green", text="14-E-50 Green")
        scol.operator("color.14_e_51_goblin", text="14-E-51 Goblin")
        scol.operator("color.14_e_53_avarice", text="14-E-53 Avarice")
        scol.operator("color.14_e_56_green", text="14-E-56 Green")
        scol.operator("color.14_e_58_green", text="14-E-58 Green")
        scol.operator("color.16_a_03_grey", text="16-A-03 Grey")
        scol.operator("color.16_a_07_mid_grey", text="16-A-07 Mid Grey")
        scol.operator("color.16_a_11_grey", text="16-A-11 Grey")
        scol.operator("color.16_c_33_duckegg", text="16-C-33 Duckegg")
        scol.operator("color.16_c_35_green", text="16-C-35 Green")
        scol.operator("color.16_c_37_green", text="16-C-37 Green")
        scol.operator("color.16_c_39_green", text="16-C-39 Green")
        scol.operator("color.16_c_40_deep_green", text="16-C-40 Deep Green")
        scol.operator("color.16_d_41_green", text="16-D-41 Green")
        scol.operator("color.16_d_43_green", text="16-D-43 Green")
        scol.operator("color.16_d_44_green", text="16-D-44 Green")
        scol.operator("color.16_d_45_green_blue", text="16-D-45 Green Blue")
        scol.operator("color.16_e_50_turquoise", text="16-E-50 Turquoise")
        scol.operator("color.16_e_53_seafarer", text="16-E-53 Seafarer")
        scol.operator("color.16_e_56_green", text="16-E-56 Green")
        scol.operator("color.18_a_14_black", text="18-A-14 Black")
        scol.operator("color.18_b_15_white", text="18-B-15 White")
        scol.operator("color.18_b_17_silver_haze", text="18-B-17 Silver Haze")
        scol.operator("color.18_b_19_grey", text="18-B-19 Grey")
        scol.operator("color.18_b_21_blue", text="18-B-21 Blue")
        scol.operator("color.18_b_23_grey", text="18-B-23 Grey")
        scol.operator("color.18_b_25_dark_admiral_grey", text="18-B-25 Dark Admiral Grey")
        scol.operator("color.18_b_27_grey", text="18-B-27 Grey")
        scol.operator("color.18_b_29_blue", text="18-B-29 Blue")
        scol.operator("color.18_c_31_ice_blue", text="18-C-31 Ice Blue")
        scol.operator("color.18_c_33_blue", text="18-C-33 Blue")
        scol.operator("color.18_c_35_blue", text="18-C-35 Blue")
        scol.operator("color.18_c_37_blue", text="18-C-37 Blue")
        scol.operator("color.18_c_39_deep_river", text="18-C-39 Deep River")
        scol.operator("color.18_c_40_black", text="18-C-40 Black")
        scol.operator("color.18_d_41_blue", text="18-D-41 Blue")
        scol.operator("color.18_d_43_dresden_blue", text="18-D-43 Dresden Blue")
        scol.operator("color.18_d_44_blue", text="18-D-44 Blue")
        scol.operator("color.18_d_45_blue", text="18-D-45 Blue")
        scol.operator("color.18_e_49_astral_blue", text="18-E-49 Astral Blue")
        scol.operator("color.18_e_50_blue", text="18-E-50 Blue")
        scol.operator("color.18_e_51_mermaid", text="18-E-51 Mermaid")
        scol.operator("color.18_e_53_cobalt_blue", text="18-E-53 Cobalt Blue")
        scol.operator("color.18_e_58_blue", text="18-E-58 Blue")
        scol.operator("color.20_c_33_pompadour", text="20-C-33 Pompadour")
        scol.operator("color.20_c_35_blue", text="20-C-35 Blue")
        scol.operator("color.20_c_37_viking", text="20-C-37 Viking")
        scol.operator("color.20_c_39_blue", text="20-C-39 Blue")
        scol.operator("color.20_c_40_midnight", text="20-C-40 Midnight")
        scol.operator("color.20_d_41_powder_blue", text="20-D-41 Powder Blue")
        scol.operator("color.20_d_43_blue", text="20-D-43 Blue")
        scol.operator("color.20_d_44_blue", text="20-D-44 Blue")
        scol.operator("color.20_d_45_maritime", text="20-D-45 Maritime")
        scol.operator("color.20_e_50_blue", text="20-E-50 Blue")
        scol.operator("color.20_e_51_corfu_purple", text="20-E-51 Corfu / Purple")
        scol.operator("color.20_e_53_blue", text="20-E-53 Blue")
        scol.operator("color.20_e_56_blue", text="20-E-56 Blue")
        scol.operator("color.22_b_15_swansdown", text="22-B-15 Swansdown")
        scol.operator("color.22_b_17_lavender_haze", text="22-B-17 Lavender Haze")
        scol.operator("color.22_b_19_soft_bleu", text="22-B-19 Soft Bleu")
        scol.operator("color.22_b_21_kashmir", text="22-B-21 Kashmir")
        scol.operator("color.22_b_23_purple", text="22-B-23 Purple")
        scol.operator("color.22_b_25_nightshade", text="22-B-25 Nightshade")
        scol.operator("color.22_b_27_violet", text="22-B-27 Violet")
        scol.operator("color.22_b_29_deep_purple", text="22-B-29 Deep Purple")
        scol.operator("color.22_c_31_white", text="22-C-31 White")
        scol.operator("color.22_c_33_soft_purple", text="22-C-33 Soft Purple")
        scol.operator("color.22_c_35_purple", text="22-C-35 Purple")
        scol.operator("color.22_c_37_violet", text="22-C-37 Violet")
        scol.operator("color.22_c_39_purple", text="22-C-39 Purple")
        scol.operator("color.22_c_40_purple", text="22-C-40 Purple")
        scol.operator("color.22_d_41_violet", text="22-D-41 Violet")
        scol.operator("color.22_d_43_violet", text="22-D-43 Violet")
        scol.operator("color.22_d_44_purple", text="22-D-44 Purple")
        scol.operator("color.22_d_45_purple", text="22-D-45 Purple")
        scol.operator("color.22_e_53_purple", text="22-E-53 Purple")
        scol.operator("color.22_e_58_purple", text="22-E-58 Purple")
        scol.operator("color.24_c_33_lilac", text="24-C-33 Lilac")
        scol.operator("color.24_c_35_pink", text="24-C-35 Pink")
        scol.operator("color.24_c_37_purple", text="24-C-37 Purple")
        scol.operator("color.24_c_38_amethyst", text="24-C-38 Amethyst")
        scol.operator("color.24_c_39_regalia", text="24-C-39 Regalia")
        scol.operator("color.24_c_40_purple", text="24-C-40 Purple")
        scol.operator("color.24_e_50_pink", text="24-E-50 Pink")
        scol.operator("color.24_e_53_purple", text="24-E-53 Purple")
        scol.operator("color.24_e_56_violet", text="24-E-56 Violet")
        scol.operator("color.24_e_58_purple", text="24-E-58 Purple")


# BSC CLASSES
array_bsc = [
    BSCPanel,
    BSC2660Panel,
    BSC381CPanel,
    BSC5252Panel,
    BS0001_Canary,
    BS0002_Oxlip,
    BS0003_Golden_Yellow,
    BS0004_Marigold,
    BS0005_Poppy_Red,
    BS0006_Post_Office_Red,
    BS0008_Chartreuse,
    BS0009_Parakeet,
    BS0010_Paris_Vir_Green,
    BS0011_Baltic_Blue,
    BS0012_Pacific_Blue,
    BS0013_Anchusa,
    BS0014_Nightshade,
    BS1015_Zephyr,
    BS1016_Pink_Haze,
    BS1017_Rose_Gray,
    BS1018_Mecca_Red,
    BS1019_Royal_Maroon,
    BS1020_Daybreak,
    BS1021_Orchis,
    BS1022_Reef_Red,
    BS1023_Tawney_Red,
    BS1024_Chestnut,
    BS1025_Crimson_Cherry,
    BS2026_Mellow_Buff,
    BS2027_Cygnet,
    BS2028_Fallow,
    BS2029_Copra,
    BS2030_Pink_Beige,
    BS2031_Aurora,
    BS2032_Cocoa,
    BS3033_Magnolia,
    BS3034_Vanilla,
    BS3036_Cobweb,
    BS3037_Buffalo,
    BS3038_Congo_Brown,
    BS3039_Chocolate,
    BS3040_Manilla_Pale_Ivory,
    BS3041_Maple,
    BS3042_Rich_Cream,
    BS3043_Light_Stone,
    BS3044_Golden_Brown,
    BS3045_Middle_Brown,
    BS4046_Off_White,
    BS4047_Silver_Gleam,
    BS4048_Stone_Grey,
    BS4049_Eddystone,
    BS4050_Olive,
    BS4051_Montella,
    BS4052_Buttermilk,
    BS4053_Jonquil,
    BS4054_Mimosa_Yellow,
    BS4055_Jasmine_Yellow,
    BS4056_Mustard,
    BS4057_Brass,
    BS5058_Gossamer,
    BS5059_Sky,
    BS5050_Quarry_Grey,
    BS5061_Pine_Green,
    BS5062_Yaffie_Green,
    BS5063_Moss_Green,
    BS5064_Bredon_Green,
    BS5_5065_Clover_Leaf,
    BS5066_Grotto,
    BS5067_Atlantic_Green,
    BS6068_Marble_Green,
    BS6069_Glacier,
    BS6070_Pastel_Green,
    BS6071_Eau_De_Nil,
    BS6073_Bottle_Green,
    BS6074_Mid_Brunswick_Green,
    BS7075_Horizon_Blue,
    BS7076_Court_Grey,
    BS7077_Shadow_Blue,
    BS7078_Light_Grey,
    BS7080_Turquoise_Blue,
    BS7081_Narvik,
    BS7082_Porcelain_Blue,
    BS7083_Ribbon_Blue,
    BS7084_Fiesta_Blue,
    BS7085_Marine_Blue,
    BS7086_Midnight_Blue,
    BS7087_Steel_Blue,
    BS7088_Wedgewood_Blue,
    BS7089_Castle_Grey,
    BS8090_Shell_Pink_Columbine,
    BS8091_Cyclamen,
    BS8092_Regal_Red,
    BS9093_Silver,
    BS9094_Flake_Grey,
    BS9095_Minerva_Grey,
    BS9096_Shire_Grey,
    BS9097_Dark_Amiralty_Grey,
    BS9098_Blue_Grey,
    BS9100_Graphite,
    BS9101_Charcoal,
    BS101_Sky_Blue,
    BS102_Turquoise_Blue,
    BS103_Peacock_Blue,
    BS104_Azure_Blue,
    BS105_Oxford_Blue,
    BS106_Royal_Blue,
    BS107_Strong_Blue_Pacific_Blue,
    BS108_Aircraft_Blue,
    BS109_Middle_Blue_Anchusa,
    BS110_Roundel_Blue,
    BS111_Sky_Blue,
    BS112_Arctic_Blue_Fiesta_Blue,
    BS113_Deep_Saxe_Blue,
    BS114_Rail_Blue,
    BS115_Cobalt_Blue,
    BS166_French_Blue,
    BS172_Pale_Rundel_Blue,
    BS174_Orient_Blue,
    BS175_Light_French_Blue,
    BS210_Sky,
    BS216_Eau_De_Nil,
    BS217_Sea_Green,
    BS218_Grass_Green,
    BS220_Olive_Green,
    BS221_Brilliant_Green,
    BS222_Light_Bronze_Green,
    BS223_Middle_Bronze_Green,
    BS224_Deep_Bronze_Green,
    BS225_Light_Brunswick_Green,
    BS226_Mid_Brunswick_Green,
    BS227_Deep_Brunswick_Green,
    BS228_Emerald_Green_Viridian,
    BS241_Dark_Green,
    BS262_Bold_Green,
    BS267_Deep_Chrome_Green_Traffic_Green,
    BS275_Opaline_Green,
    BS278_Light_Olive_Green,
    BS280_Verdigris_Green,
    BS282_Forest_Green,
    BS283_Aircraft_Grey_Green,
    BS284_Spruce_Green,
    BS285_Nato_Green,
    BS298_Olive_Drab,
    BS309_Canary_Yellow,
    BS310_Primrose,
    BS315_Grapefruit,
    BS320_Light_Brown,
    BS337_Very_Dark_Drab,
    BS350_Dark_Earth,
    BS352_Pale_Cream,
    BS353_Deep_Cream,
    BS355_Lemon,
    BS356_Golden_Yellow,
    BS358_Light_Buff,
    BS359_Middle_Buff,
    BS361_Light_Stone,
    BS363_Bold_Yellow,
    BS365_Vellum,
    BS366_Light_Beige,
    BS367_Manilla,
    BS369_Biscuit,
    BS380_Camouflage_Desert_Sand,
    BS384_Light_Straw,
    BS388_Beige,
    BS389_Camouflage_Beige,
    BS411_Middle_Brown,
    BS412_Dark_Brown,
    BS414_Golden_Brown,
    BS420_Dark_Camouflage_Desert_Sand,
    BS435_Camouflage_Red,
    BS436_Dark_Camouflage_Brown,
    BS444_Terracotta,
    BS445_Venetian_Red,
    BS446_Red_Oxide,
    BS447_Salmon_Pink,
    BS448_Deep_Indian_Red,
    BS449_Light_Purple_Brown,
    BS452_Dark_Crimson,
    BS453_Shell_Pink,
    BS454_Pale_Roundel_Red,
    BS460_Deep_Buff,
    BS473_Gulf_Red,
    BS489_Leaf_Brown,
    BS499_Service_Brown,
    BS537_Signal_Red,
    BS538_Post_Office_Red_Cherry,
    BS539_Currant_Red,
    BS540_Crimson,
    BS541_Maroon,
    BS542_Ruby,
    BS557_Light_Orange,
    BS564_Bold_Red,
    BS568_Apricot,
    BS592_International_Orange,
    BS593_Rail_Red_Azo_Orange,
    BS626_Camouflage_Grey,
    BS627_Light_Aircraft_Grey,
    BS629_Dark_Camouflage_Grey_Quaker_Grey,
    BS630_French_Grey,
    BS631_Light_Grey,
    BS632_Dark_Admiralty_Grey,
    BS633_Raf_Blue_Grey,
    BS634_Slate,
    BS635_Lead,
    BS636_Pru_Blue,
    BS637_Medium_Sea_Grey,
    BS638_Dark_Sea_Grey,
    BS639_Light_Slate_Grey,
    BS640_Extra_Dark_Sea_Grey,
    BS642_Night,
    BS671_Middle_Graphite,
    BS676_Light_Weatherwork_Grey,
    BS677_Dark_Weatherwork_Grey,
    BS692_Smoke_Grey,
    BS693_Aircraft_Grey,
    BS694_Dove_Grey,
    BS697_Light_Admiralty_Grey,
    BS796_Dark_Violet,
    BS797_Light_Violet,
    BS00_A_01_Ash_Grey_Oyster_Grey_Portland,
    BS00_A_03_Grey,
    BS00_A_05_Goose_Grey_Sea_Mist_Goosewing,
    BS00_A_07_Grey,
    BS00_A_09_Flint_Grey_Flint,
    BS00_A_11_Grey,
    BS00_A_13_Storm_Grey_Greyfriar,
    BS00_E_53_Black,
    BS00_E_55_White,
    BS02_A_03_Grey,
    BS02_A_07_Grey,
    BS02_A_11_Grey,
    BS02_C_33_Lupin_Pink_Candy_Floss_Pink_Wafer,
    BS02_C_35_Pink,
    BS02_C_37_Clover_Pink_Corinth_Fontana,
    BS02_C_39_Victoria_Plum_Aubergine_Plum,
    BS02_C_40_Deep_Plum_Loganberry,
    BS02_D_41_Pink,
    BS02_D_43_Pink,
    BS02_D_44_Pink,
    BS02_D_45_Purple,
    BS02_E_53_Purple,
    BS02_E_56_Deep_Pink,
    BS02_E_58_Bordeaux,
    BS04_B_15_Rosepetal_Pastel_Pink_Dawn_Pink,
    BS04_B_15_Dawn_Pink,
    BS04_B_17_Tea_Rose,
    BS04_B_19_Beige,
    BS04_B_21_Sierra,
    BS04_B_23_Brown,
    BS04_B_25_Saracen,
    BS04_B_27_Brown,
    BS04_B_29_Brown,
    BS04_C_31_Pink,
    BS04_C_33_Parisian_Pink,
    BS04_C_35_Soft_Red,
    BS04_C_37_Red,
    BS04_C_39_Copperbeech,
    BS04_C_40_Maroon,
    BS04_D_41_Pink,
    BS04_D_43_Robin,
    BS04_D_44_Tawny,
    BS04_D_45_Russet,
    BS04_E_49_Petal,
    BS04_E_50_Pink,
    BS04_E_51_Salmon_Red_Lobster_Azalea,
    BS04_E_53_Carnival_Red_Poppy,
    BS04_E_55_Red,
    BS04_E_56_Carnival_Red,
    BS04_E_58_Red,
    BS06_A_03_Grey,
    BS06_A_07_Grey,
    BS06_A_11_Grey,
    BS06_C_33_Cameo,
    BS06_C_35_Light_Orange,
    BS06_C_37_Brownstone,
    BS06_C_39_Saddle,
    BS06_C_40_Brown,
    BS06_D_41_Orange,
    BS06_D_43_Kalahari,
    BS06_D_44_Orange,
    BS06_D_45_Mace,
    BS06_E_50_Apricot,
    BS06_E_51_Clementine,
    BS06_E_53_Orange,
    BS06_E_55_Orange,
    BS06_E_56_Yellow,
    BS08_A_14_Black,
    BS08_B_15_Magnolia,
    BS08_B_17_Fawn,
    BS08_B_19_Beige,
    BS08_B_21_Antelope,
    BS08_B_23_Brown,
    BS08_B_25_Beaver,
    BS08_B_27_Brown,
    BS08_B_29_Vandye,
    BS08_C_31_Blush_Stone,
    BS08_C_33_Beige,
    BS08_C_35_Butterscoth,
    BS08_C_37_Bracken,
    BS08_C_39_Bison,
    BS08_C_40_Brown,
    BS08_D_41_Yellow,
    BS08_D_43_Yellow,
    BS08_D_44_Brown,
    BS08_D_45_Brown,
    BS08_E_51_Golden_Ambar,
    BS08_E_53_Yellow,
    BS08_E_55_Orange,
    BS08_E_56_Yellow,
    BS10_A_01_White,
    BS10_A_03_Sink_Grey,
    BS10_A_05_Grey,
    BS10_A_07_Wood_Ash,
    BS10_A_09_Grey,
    BS10_A_11_Storm_Rhino,
    BS10_B_15_Ivory,
    BS10_B_17_Greystone,
    BS10_B_19_Beige,
    BS10_B_21_Lizard,
    BS10_B_23_Brown,
    BS10_B_25_Turtle,
    BS10_B_27_Brown,
    BS10_B_29_Ironstone,
    BS10_C_31_Champagne,
    BS10_C_33_Pollen,
    BS10_C_35_Golden_Bronze,
    BS10_C_37_Yellow_Brown,
    BS10_C_39_Saluki,
    BS10_D_41_Yellow,
    BS10_D_43_Banana,
    BS10_D_44_Light_Olive,
    BS10_D_45_Florida,
    BS10_E_49_Pale_Lemon,
    BS10_E_50_Forsythia,
    BS10_E_51_Yellow,
    BS10_E_53_Canary,
    BS10_E_55_Camery_Yellow,
    BS10_E_56_Yellow,
    BS12_B_15_Seafoam,
    BS12_B_17_Willow,
    BS12_B_19_Beige,
    BS12_B_21_Opaline,
    BS12_B_23_Green,
    BS12_B_25_Thyme,
    BS12_B_27_Green,
    BS12_B_29_Juniper,
    BS12_C_31_Light_Yellow,
    BS12_C_33_Catkin,
    BS12_C_35_Green,
    BS12_C_37_Green,
    BS12_C_39_Orchard,
    BS12_C_40_Green,
    BS12_C_41_Green,
    BS12_D_43_Sapling,
    BS12_D_44_Green,
    BS12_D_45_Tundra,
    BS12_E_51_Citrine,
    BS12_E_53_Linden,
    BS12_E_55_Green,
    BS14_C_31_Green_Alpine,
    BS14_C_33_Green,
    BS14_C_35_Breamer,
    BS14_C_37_Green,
    BS14_C_39_Hollybush,
    BS14_C_40_Green,
    BS14_D_41_Green,
    BS14_D_43_Green,
    BS14_D_44_Green,
    BS14_D_45_Green,
    BS14_E_49_Light_Green,
    BS14_E_50_Green,
    BS14_E_51_Goblin,
    BS14_E_53_Avarice,
    BS14_E_56_Green,
    BS14_E_58_Green,
    BS16_A_03_Grey,
    BS16_A_07_Mid_Grey,
    BS16_A_11_Grey,
    BS16_C_33_Duckegg,
    BS16_C_35_Green,
    BS16_C_37_Green,
    BS16_C_39_Green,
    BS16_C_40_Deep_Green,
    BS16_D_41_Green,
    BS16_D_43_Green,
    BS16_D_44_Green,
    BS16_D_45_Green_Blue,
    BS16_E_50_Turquoise,
    BS16_E_53_Seafarer,
    BS16_E_56_Green,
    BS18_A_14_Black,
    BS18_B_15_White,
    BS18_B_17_Silver_Haze,
    BS18_B_19_Grey,
    BS18_B_21_Blue,
    BS18_B_23_Grey,
    BS18_B_25_Dark_Admiral_Grey,
    BS18_B_27_Grey,
    BS18_B_29_Blue,
    BS18_C_31_Ice_Blue,
    BS18_C_33_Blue,
    BS18_C_35_Blue,
    BS18_C_37_Blue,
    BS18_C_39_Deep_River,
    BS18_C_40_Black,
    BS18_D_41_Blue,
    BS18_D_43_Dresden_Blue,
    BS18_D_44_Blue,
    BS18_D_45_Blue,
    BS18_E_49_Astral_Blue,
    BS18_E_50_Blue,
    BS18_E_51_Mermaid,
    BS18_E_53_Cobalt_Blue,
    BS18_E_58_Blue,
    BS20_C_33_Pompadour,
    BS20_C_35_Blue,
    BS20_C_37_Viking,
    BS20_C_39_Blue,
    BS20_C_40_Midnight,
    BS20_D_41_Powder_Blue,
    BS20_D_43_Blue,
    BS20_D_44_Blue,
    BS20_D_45_Maritime,
    BS20_E_50_Blue,
    BS20_E_51_Corfu_Purple,
    BS20_E_53_Blue,
    BS20_E_56_Blue,
    BS22_B_15_Swansdown,
    BS22_B_17_Lavender_Haze,
    BS22_B_19_Soft_Bleu,
    BS22_B_21_Kashmir,
    BS22_B_23_Purple,
    BS22_B_25_Nightshade,
    BS22_B_27_Violet,
    BS22_B_29_Deep_Purple,
    BS22_C_31_White,
    BS22_C_33_Soft_Purple,
    BS22_C_35_Purple,
    BS22_C_37_Violet,
    BS22_C_39_Purple,
    BS22_C_40_Purple,
    BS22_D_41_Violet,
    BS22_D_43_Violet,
    BS22_D_44_Purple,
    BS22_D_45_Purple,
    BS22_E_53_Purple,
    BS22_E_58_Purple,
    BS24_C_33_Lilac,
    BS24_C_35_Pink,
    BS24_C_37_Purple,
    BS24_C_38_Amethyst,
    BS24_C_39_Regalia,
    BS24_C_40_Purple,
    BS24_E_50_Pink,
    BS24_E_53_Purple,
    BS24_E_56_Violet,
    BS24_E_58_Purple,
]
