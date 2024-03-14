# ECC COLORS SET

import bpy

from .globals import *
from .color_functions import *

# ECC OPERATORS

class Audi_Nardo_Grey(bpy.types.Operator):
    """Audi's classic grey color"""
    bl_label = "Nardo Grey"
    bl_idname = 'color.audi_nardo_grey'
    def execute(self, context):
        set_base_color(0xC0C6C8, self.bl_label)
        return {'FINISHED'}

class Ferrari_Argento_Nurburgring(bpy.types.Operator):
    """Ferrari's metallic silver color"""
    bl_label = "Argento Nurburgring"
    bl_idname = 'color.ferrari_argento_nurburgring'
    def execute(self, context):
        set_base_color(0xCACBCE, self.bl_label)
        return {'FINISHED'}

class Ferrari_Bianco_Avorio(bpy.types.Operator):
    """Ferrari's cream white color"""
    bl_label = "Bianco Avorio"
    bl_idname = 'color.ferrari_bianco_avorio'
    def execute(self, context):
        set_base_color(0xE5DEDC, self.bl_label)
        return {'FINISHED'}

class Ferrari_Bianco_Avus(bpy.types.Operator):
    """Ferrari's classic white color"""
    bl_label = "Bianco Avus"
    bl_idname = 'color.ferrari_bianco_avus'
    def execute(self, context):
        set_base_color(0xF2F3F6, self.bl_label)
        return {'FINISHED'}

class Ferrari_Blu_Abu_Dhabi(bpy.types.Operator):
    """Ferrari's light blue color"""
    bl_label = "Blu Abu Dhabi"
    bl_idname = 'color.ferrari_blu_abu_dhabi'
    def execute(self, context):
        set_base_color(0x2885B5, self.bl_label)
        return {'FINISHED'}

class Ferrari_Blu_Pozzi(bpy.types.Operator):
    """Ferrari's deep blue color"""
    bl_label = "Blu Pozzi"
    bl_idname = 'color.ferrari_blu_pozzi'
    def execute(self, context):
        set_base_color(0x2C3970, self.bl_label)
        return {'FINISHED'}

class Ferrari_Blu_Scozia(bpy.types.Operator):
    """Ferrari's dark blue color"""
    bl_label = "Blu Scozia"
    bl_idname = 'color.ferrari_blu_scozia'
    def execute(self, context):
        set_base_color(0x505C77, self.bl_label)
        return {'FINISHED'}

class Ferrari_Blu_Swaters(bpy.types.Operator):
    """Ferrari's royal blue color"""
    bl_label = "Blu Swaters"
    bl_idname = 'color.ferrari_blu_swaters'
    def execute(self, context):
        set_base_color(0x163166, self.bl_label)
        return {'FINISHED'}

class Ferrari_Blu_Tour_De_France(bpy.types.Operator):
    """Ferrari's classic blue color"""
    bl_label = "Blu Tour De France"
    bl_idname = 'color.ferrari_blu_tour_de_france'
    def execute(self, context):
        set_base_color(0x2243AA, self.bl_label)
        return {'FINISHED'}

class Ferrari_Canna_Di_Fucile(bpy.types.Operator):
    """Ferrari's metallic grey color"""
    bl_label = "Canna Di Fucile"
    bl_idname = 'color.ferrari_canna_di_fucile'
    def execute(self, context):
        set_base_color(0x7E8792, self.bl_label)
        return {'FINISHED'}

class Ferrari_Giallo_Modena(bpy.types.Operator):
    """Ferrari's triple layer yellow color"""
    bl_label = "Giallo Modena"
    bl_idname = 'color.ferrari_giallo_modena'
    def execute(self, context):
        set_base_color(0xFCE903, self.bl_label)
        return {'FINISHED'}

class Ferrari_Grigio_Alloy(bpy.types.Operator):
    """Ferrari's light grey (blue) color"""
    bl_label = "Grigio Alloy"
    bl_idname = 'color.ferrari_grigio_alloy'
    def execute(self, context):
        set_base_color(0xA3C7E9, self.bl_label)
        return {'FINISHED'}

class Ferrari_Grigio_Ferro(bpy.types.Operator):
    """Ferrari's light grey color"""
    bl_label = "Grigio Ferro"
    bl_idname = 'color.ferrari_grigio_ferro'
    def execute(self, context):
        set_base_color(0x626062, self.bl_label)
        return {'FINISHED'}

class Ferrari_Grigio_Ingrid(bpy.types.Operator):
    """Ferrari's beige grey color"""
    bl_label = "Grigio Ingrid"
    bl_idname = 'color.ferrari_grigio_ingrid'
    def execute(self, context):
        set_base_color(0x756D62, self.bl_label)
        return {'FINISHED'}

class Ferrari_Grigio_Scuro(bpy.types.Operator):
    """Ferrari's deep grey color"""
    bl_label = "Grigio Scuro"
    bl_idname = 'color.ferrari_grigio_scuro'
    def execute(self, context):
        set_base_color(0x4C4E4D, self.bl_label)
        return {'FINISHED'}

class Ferrari_Grigio_Silverstone(bpy.types.Operator):
    """Ferrari's dark grey color"""
    bl_label = "Grigio Silverstone"
    bl_idname = 'color.ferrari_grigio_silverstone'
    def execute(self, context):
        set_base_color(0x585C64, self.bl_label)
        return {'FINISHED'}

class Ferrari_Grigio_Titanio(bpy.types.Operator):
    """Ferrari's classic grey color"""
    bl_label = "Grigio Titanio"
    bl_idname = 'color.ferrari_grigio_titanio'
    def execute(self, context):
        set_base_color(0xA8B8C0, self.bl_label)
        return {'FINISHED'}

class Ferrari_Nero_Daytona(bpy.types.Operator):
    """Ferrari's classic black color"""
    bl_label = "Nero Daytona"
    bl_idname = 'color.ferrari_nero_daytona'
    def execute(self, context):
        set_base_color(0x231F1C, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_70_Anni(bpy.types.Operator):
    """Ferrari's 70th anniversary celebration color"""
    bl_label = "Rosso 70 Anni"
    bl_idname = 'color.ferrari_rosso_70_anni'
    def execute(self, context):
        set_base_color(0xC40C19, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_Corsa(bpy.types.Operator):
    """Ferrari's classic red color"""
    bl_label = "Rosso Corsa"
    bl_idname = 'color.ferrari_rosso_corsa'
    def execute(self, context):
        set_base_color(0xD40000, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_Dino(bpy.types.Operator):
    """Ferrari's red/orange color"""
    bl_label = "Rosso Dino"
    bl_idname = 'color.ferrari_rosso_dino'
    def execute(self, context):
        set_base_color(0xFC652E, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_Fiorano(bpy.types.Operator):
    """Ferrari's ruby red color"""
    bl_label = "Rosso Fiorano"
    bl_idname = 'color.ferrari_rosso_fiorano'
    def execute(self, context):
        set_base_color(0x5D0001, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_Fuoco(bpy.types.Operator):
    """Ferrari's triple layer red color"""
    bl_label = "Rosso Fuoco"
    bl_idname = 'color.ferrari_rosso_fuoco'
    def execute(self, context):
        set_base_color(0xD13442, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_Mugello(bpy.types.Operator):
    """Ferrari's dark red color"""
    bl_label = "Rosso Mugello"
    bl_idname = 'color.ferrari_rosso_mugello'
    def execute(self, context):
        set_base_color(0x7A212A, self.bl_label)
        return {'FINISHED'}

class Ferrari_Rosso_Scuderia(bpy.types.Operator):
    """Ferrari's bright red color"""
    bl_label = "Rosso Scuderia"
    bl_idname = 'color.ferrari_rosso_scuderia'
    def execute(self, context):
        set_base_color(0xff2800, self.bl_label)
        return {'FINISHED'}

class Ferrari_Verde_British(bpy.types.Operator):
    """Ferrari's British racing green color"""
    bl_label = "Verde British"
    bl_idname = 'color.ferrari_verde_british'
    def execute(self, context):
        set_base_color(0x004225, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Arancia_Atlas(bpy.types.Operator):
    """Lamborghini's shiny orange color"""
    bl_label = "Arancia Atlas"
    bl_idname = 'color.lamborghini_arancia_atlas'
    def execute(self, context):
        set_base_color(0xFC9303, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Arancio_Argos(bpy.types.Operator):
    """Lamborghini's Ad Personam fire red color"""
    bl_label = "Arancio Argos"
    bl_idname = 'color.lamborghini_arancio_argos'
    def execute(self, context):
        set_base_color(0xFB6445, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Arancio_Borealis(bpy.types.Operator):
    """Lamborghini's Ad Personam orange color"""
    bl_label = "Arancio Borealis"
    bl_idname = 'color.lamborghini_arancio_borealis'
    def execute(self, context):
        set_base_color(0xFBA400, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Arancio_Bruciato(bpy.types.Operator):
    """Lamborghini's contemporary orange color"""
    bl_label = "Arancio Bruciato"
    bl_idname = 'color.lamborghini_arancio_bruciato'
    def execute(self, context):
        set_base_color(0xD74C10, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Arancio_Xanto(bpy.types.Operator):
    """Lamborghini's sportiva orange color"""
    bl_label = "Arancio Xanto"
    bl_idname = 'color.lamborghini_arancio_xanto'
    def execute(self, context):
        set_base_color(0xE64A37, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Azzurro_Thetys(bpy.types.Operator):
    """Lamborghini's Ad Personam light blue color"""
    bl_label = "Azzurro Thetys"
    bl_idname = 'color.lamborghini_azzurro_thetys'
    def execute(self, context):
        set_base_color(0x8CA0B8, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Balloon_White(bpy.types.Operator):
    """Lamborghini's contemporary white color"""
    bl_label = "Balloon White"
    bl_idname = 'color.lamborghini_balloon_white'
    def execute(self, context):
        set_base_color(0xE8E8E8, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Bianco_Asopo(bpy.types.Operator):
    """Lamborghini's sportiva white color"""
    bl_label = "Bianco Asopo"
    bl_idname = 'color.lamborghini_bianco_asopo'
    def execute(self, context):
        set_base_color(0xF3FAFD, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Bianco_Comes(bpy.types.Operator):
    """Lamborghini's pearl white color"""
    bl_label = "Bianco Comes"
    bl_idname = 'color.lamborghini_bianco_comes'
    def execute(self, context):
        set_base_color(0xFBFBFB, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Bianco_Isi(bpy.types.Operator):
    """Lamborghini's shiny white color"""
    bl_label = "Bianco Isi"
    bl_idname = 'color.lamborghini_bianco_isi'
    def execute(self, context):
        set_base_color(0xC0CBCD, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Bianco_Monocerus(bpy.types.Operator):
    """Lamborghini's Ad Personam white color"""
    bl_label = "Bianco Monocerus"
    bl_idname = 'color.lamborghini_bianco_monocerus'
    def execute(self, context):
        set_base_color(0xEDEDED, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Aegir(bpy.types.Operator):
    """Lamborghini's contemporary blue color"""
    bl_label = "Blu Aegir"
    bl_idname = 'color.lamborghini_blu_aegir'
    def execute(self, context):
        set_base_color(0x2CAEFE, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Astraeus(bpy.types.Operator):
    """Lamborghini's Ad Personam deep blue color"""
    bl_label = "Blu Astraeus"
    bl_idname = 'color.lamborghini_blu_astraeus'
    def execute(self, context):
        set_base_color(0x00024C, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Caelum(bpy.types.Operator):
    """Lamborghini's Ad Personam royal blue color"""
    bl_label = "Blu Caelum"
    bl_idname = 'color.lamborghini_blu_caelum'
    def execute(self, context):
        set_base_color(0x054AE3, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Cepheus(bpy.types.Operator):
    """Lamborghini's pearl blue color"""
    bl_label = "Blu Cepheus"
    bl_idname = 'color.lamborghini_blu_cepheus'
    def execute(self, context):
        set_base_color(0x39BFFE, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Eleos(bpy.types.Operator):
    """Lamborghini's Ad Personam shiny blue color"""
    bl_label = "Blu Eleos"
    bl_idname = 'color.lamborghini_blu_eleos'
    def execute(self, context):
        set_base_color(0x418DD8, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Fontus(bpy.types.Operator):
    """Lamborghini's Ad Personam dark blue color"""
    bl_label = "Blu Fontus"
    bl_idname = 'color.lamborghini_blu_fontus'
    def execute(self, context):
        set_base_color(0x313247, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Glauco(bpy.types.Operator):
    """Lamborghini's Ad Personam teal color"""
    bl_label = "Blu Glauco"
    bl_idname = 'color.lamborghini_blu_glauco'
    def execute(self, context):
        set_base_color(0x08C7E3, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Le_Mans(bpy.types.Operator):
    """Lamborghini's Ad Personam bright blue color"""
    bl_label = "Blu Le Mans"
    bl_idname = 'color.lamborghini_blu_le_mans'
    def execute(self, context):
        set_base_color(0x0690FF, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Nereid(bpy.types.Operator):
    """Lamborghini's Ad Personam metallic blue color"""
    bl_label = "Blu Nereid"
    bl_idname = 'color.lamborghini_blu_nereid'
    def execute(self, context):
        set_base_color(0x2539BC, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Nethuns(bpy.types.Operator):
    """Lamborghini's sportiva blue color"""
    bl_label = "Blu Nethuns"
    bl_idname = 'color.lamborghini_blu_nethuns'
    def execute(self, context):
        set_base_color(0x1336EA, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Nila(bpy.types.Operator):
    """Lamborghini's shiny blue color"""
    bl_label = "Blu Nila"
    bl_idname = 'color.lamborghini_blu_nila'
    def execute(self, context):
        set_base_color(0x017EF4, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Notte(bpy.types.Operator):
    """Lamborghini's classic blue color"""
    bl_label = "Blu Notte"
    bl_idname = 'color.lamborghini_blu_notte'
    def execute(self, context):
        set_base_color(0x212E58, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Blu_Uranus(bpy.types.Operator):
    """Lamborghini's pearl ocean color"""
    bl_label = "Blu Uranus"
    bl_idname = 'color.lamborghini_blu_uranus'
    def execute(self, context):
        set_base_color(0x0177A4, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Bronzo_Zante(bpy.types.Operator):
    """Lamborghini's contemporary bronze color"""
    bl_label = "Bronzo Zante"
    bl_idname = 'color.lamborghini_bronzo_zante'
    def execute(self, context):
        set_base_color(0xB08D57, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Giallo_Auge(bpy.types.Operator):
    """Lamborghini's Ad Personam yellow color"""
    bl_label = "Giallo Auge"
    bl_idname = 'color.lamborghini_giallo_auge'
    def execute(self, context):
        set_base_color(0xFEBE05, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Giallo_Evros(bpy.types.Operator):
    """Lamborghini's Ad Personam dark yellow color"""
    bl_label = "Giallo Evros"
    bl_idname = 'color.lamborghini_giallo_evros'
    def execute(self, context):
        set_base_color(0xE28F01, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Giallo_Inti(bpy.types.Operator):
    """Lamborghini's Ad Personam bright yellow color"""
    bl_label = "Giallo Inti"
    bl_idname = 'color.lamborghini_giallo_inti'
    def execute(self, context):
        set_base_color(0xFED136, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Giallo_Orion(bpy.types.Operator):
    """Lamborghini's shiny yellow color"""
    bl_label = "Giallo Orion"
    bl_idname = 'color.lamborghini_giallo_orion'
    def execute(self, context):
        set_base_color(0xFEA700, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Giallo_Spica(bpy.types.Operator):
    """Lamborghini's Ad Personam pearl yellow color"""
    bl_label = "Giallo Spica"
    bl_idname = 'color.lamborghini_giallo_spica'
    def execute(self, context):
        set_base_color(0xF2C32F, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Giallo_Tenerife(bpy.types.Operator):
    """Lamborghini's Ad Personam pale yellow color"""
    bl_label = "Giallo Tenerife"
    bl_idname = 'color.lamborghini_giallo_tenerife'
    def execute(self, context):
        set_base_color(0xF2F427, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Antares(bpy.types.Operator):
    """Lamborghini's Ad Personam metallic grey color"""
    bl_label = "Grigio Antares"
    bl_idname = 'color.lamborghini_grigio_antares'
    def execute(self, context):
        set_base_color(0xA6ADB7, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Ater(bpy.types.Operator):
    """Lamborghini's Ad Personam dark grey color"""
    bl_label = "Grigio Ater"
    bl_idname = 'color.lamborghini_grigio_ater'
    def execute(self, context):
        set_base_color(0x727274, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Estoque(bpy.types.Operator):
    """Lamborghini's Ad Personam metallic grey color"""
    bl_label = "Grigio Estoque"
    bl_idname = 'color.lamborghini_grigio_estoque'
    def execute(self, context):
        set_base_color(0xACACAE, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Hati(bpy.types.Operator):
    """Lamborghini's Ad Personam light grey color"""
    bl_label = "Grigio Hati"
    bl_idname = 'color.lamborghini_grigio_hati'
    def execute(self, context):
        set_base_color(0xC7D7E7, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Keres(bpy.types.Operator):
    """Lamborghini's Ad Personam metallic grey color"""
    bl_label = "Grigio Keres"
    bl_idname = 'color.lamborghini_grigio_keres'
    def execute(self, context):
        set_base_color(0x6F6F6F, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Liqueo(bpy.types.Operator):
    """Lamborghini's Ad Personam light metallic grey color"""
    bl_label = "Grigio Liqueo"
    bl_idname = 'color.lamborghini_grigio_liqueo'
    def execute(self, context):
        set_base_color(0x85898D, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Lynx(bpy.types.Operator):
    """Lamborghini's Ad Personam grey color"""
    bl_label = "Grigio Lynx"
    bl_idname = 'color.lamborghini_grigio_lynx'
    def execute(self, context):
        set_base_color(0x707176, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Nimbus(bpy.types.Operator):
    """Lamborghini's Ad Personam bright light grey color"""
    bl_label = "Grigio Nimbus"
    bl_idname = 'color.lamborghini_grigio_nimbus'
    def execute(self, context):
        set_base_color(0x6B7278, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Grigio_Telesto(bpy.types.Operator):
    """Lamborghini's sportiva grey color"""
    bl_label = "Grigio Telesto"
    bl_idname = 'color.lamborghini_grigio_telesto'
    def execute(self, context):
        set_base_color(0x7692A5, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Nero_Aldebaran(bpy.types.Operator):
    """Lamborghini's shiny black color"""
    bl_label = "Nero Aldebaran"
    bl_idname = 'color.lamborghini_nero_aldebaran'
    def execute(self, context):
        set_base_color(0x0D1015, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Nero_Granatus(bpy.types.Operator):
    """Lamborghini's contemporary black color"""
    bl_label = "Nero Granatus"
    bl_idname = 'color.lamborghini_nero_granatus'
    def execute(self, context):
        set_base_color(0x92555D, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Nero_Helene(bpy.types.Operator):
    """Lamborghini's Ad Personam black color"""
    bl_label = "Nero Helene"
    bl_idname = 'color.lamborghini_nero_helene'
    def execute(self, context):
        set_base_color(0x151618, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Nero_Nemesis(bpy.types.Operator):
    """Lamborghini's Ad Personam matte black color"""
    bl_label = "Nero Nemesis"
    bl_idname = 'color.lamborghini_nero_nemesis'
    def execute(self, context):
        set_base_color(0x312F30, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Nero_Noctis(bpy.types.Operator):
    """Lamborghini's Ad Personam metallic black color"""
    bl_label = "Nero Noctis"
    bl_idname = 'color.lamborghini_nero_noctis'
    def execute(self, context):
        set_base_color(0x292927, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Nero_Pegaso(bpy.types.Operator):
    """Lamborghini's Ad Personam dark black color"""
    bl_label = "Nero Pegaso"
    bl_idname = 'color.lamborghini_nero_pegaso'
    def execute(self, context):
        set_base_color(0x080D10, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Oros_Elios(bpy.types.Operator):
    """Lamborghini's pearl bronze color"""
    bl_label = "Oros Elios"
    bl_idname = 'color.lamborghini_oros_elios'
    def execute(self, context):
        set_base_color(0xB88B60, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Rosso_Arancio(bpy.types.Operator):
    """Lamborghini's classic red color"""
    bl_label = "Rosso Arancio"
    bl_idname = 'color.lamborghini_rosso_arancio'
    def execute(self, context):
        set_base_color(0xDD3D0D, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Rosso_Bia(bpy.types.Operator):
    """Lamborghini's Ad Personam cherry red color"""
    bl_label = "Rosso Bia"
    bl_idname = 'color.lamborghini_rosso_bia'
    def execute(self, context):
        set_base_color(0xC10001, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Rosso_Efesto(bpy.types.Operator):
    """Lamborghini's contemporary red color"""
    bl_label = "Rosso Efesto"
    bl_idname = 'color.lamborghini_rosso_efesto'
    def execute(self, context):
        set_base_color(0xF4221F, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Rosso_Leto(bpy.types.Operator):
    """Lamborghini's Ad Personam deep red color"""
    bl_label = "Rosso Leto"
    bl_idname = 'color.lamborghini_rosso_leto'
    def execute(self, context):
        set_base_color(0xB60035, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Rosso_Mars(bpy.types.Operator):
    """Lamborghini's shiny red color"""
    bl_label = "Rosso Mars"
    bl_idname = 'color.lamborghini_rosso_mars'
    def execute(self, context):
        set_base_color(0xD40000, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Citrea(bpy.types.Operator):
    """Lamborghini's pearl green color"""
    bl_label = "Verde Citrea"
    bl_idname = 'color.lamborghini_verde_citrea'
    def execute(self, context):
        set_base_color(0x9AF95D, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Ermes(bpy.types.Operator):
    """Lamborghini's Ad Personam dark green color"""
    bl_label = "Verde Ermes"
    bl_idname = 'color.lamborghini_verde_ermes'
    def execute(self, context):
        set_base_color(0x546E51, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Gea_Lucido(bpy.types.Operator):
    """Lamborghini's contemporary green color"""
    bl_label = "Verde Gea Lucido"
    bl_idname = 'color.lamborghini_verde_gea_lucido'
    def execute(self, context):
        set_base_color(0x8B8970, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Ithaca(bpy.types.Operator):
    """Lamborghini's Ad Personam bright green color"""
    bl_label = "Verde Ithaca"
    bl_idname = 'color.lamborghini_verde_ithaca'
    def execute(self, context):
        set_base_color(0xAEFF7E, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Mantis(bpy.types.Operator):
    """Lamborghini's shiny green color"""
    bl_label = "Verde Mantis"
    bl_idname = 'color.lamborghini_verde_mantis'
    def execute(self, context):
        set_base_color(0x7DC23B, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Metallic(bpy.types.Operator):
    """Lamborghini's classic british racing green color"""
    bl_label = "Verde Metallic"
    bl_idname = 'color.lamborghini_verde_metallic'
    def execute(self, context):
        set_base_color(0x8FC028, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Scandal(bpy.types.Operator):
    """Lamborghini's classic green color"""
    bl_label = "Verde Scandal"
    bl_idname = 'color.lamborghini_verde_scandal'
    def execute(self, context):
        set_base_color(0x84E12E, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Verde_Selvans(bpy.types.Operator):
    """Lamborghini's sportiva green color"""
    bl_label = "Verde Selvans"
    bl_idname = 'color.lamborghini_verde_selvans'
    def execute(self, context):
        set_base_color(0x67C52F, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Viola_30(bpy.types.Operator):
    """Lamborghini's classic purple color"""
    bl_label = "Viola 30"
    bl_idname = 'color.lamborghini_viola_30'
    def execute(self, context):
        set_base_color(0xB27CB6, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Viola_Aletheia(bpy.types.Operator):
    """Lamborghini's Ad Personam deep purple color"""
    bl_label = "Viola Aletheia"
    bl_idname = 'color.lamborghini_viola_aletheia'
    def execute(self, context):
        set_base_color(0x492AC5, self.bl_label)
        return {'FINISHED'}

class Lamborghini_Viola_Pasifae(bpy.types.Operator):
    """Lamborghini's sportiva purple color"""
    bl_label = "Viola Pasifae"
    bl_idname = 'color.lamborghini_viola_pasifae'
    def execute(self, context):
        set_base_color(0x6B0686, self.bl_label)
        return {'FINISHED'}

class McLaren_Aurora_Blue(bpy.types.Operator):
    """McLaren's deep blue color"""
    bl_label = "Aurora Blue"
    bl_idname = 'color.mclaren_aurora_blue'
    def execute(self, context):
        set_base_color(0x172375, self.bl_label)
        return {'FINISHED'}

class McLaren_Cobalt_Violet(bpy.types.Operator):
    """McLaren's dark purple color"""
    bl_label = "Cobalt Violet"
    bl_idname = 'color.mclaren_cobalt_violet'
    def execute(self, context):
        set_base_color(0xC8659E, self.bl_label)
        return {'FINISHED'}

class McLaren_Curacao_Blue(bpy.types.Operator):
    """McLaren's bright blue color"""
    bl_label = "Curacao Blue"
    bl_idname = 'color.mclaren_curacao_blue'
    def execute(self, context):
        set_base_color(0x00B8EE, self.bl_label)
        return {'FINISHED'}

class McLaren_Fire_Black(bpy.types.Operator):
    """McLaren's metallic black color"""
    bl_label = "Fire Black"
    bl_idname = 'color.mclaren_fire_black'
    def execute(self, context):
        set_base_color(0x191A1E, self.bl_label)
        return {'FINISHED'}

class McLaren_Ice_Silver(bpy.types.Operator):
    """McLaren's bright silver color"""
    bl_label = "Ice Silver"
    bl_idname = 'color.mclaren_ice_silver'
    def execute(self, context):
        set_base_color(0xC4C8D4, self.bl_label)
        return {'FINISHED'}

class McLaren_Lantana_Purple(bpy.types.Operator):
    """McLaren's deep purple color"""
    bl_label = "Lantana Purple"
    bl_idname = 'color.mclaren_lantana_purple'
    def execute(self, context):
        set_base_color(0x351175, self.bl_label)
        return {'FINISHED'}

class McLaren_Lime_Green(bpy.types.Operator):
    """McLaren's bright green color"""
    bl_label = "Lime Green"
    bl_idname = 'color.mclaren_lime_green'
    def execute(self, context):
        set_base_color(0xC2ED3E, self.bl_label)
        return {'FINISHED'}

class McLaren_Mantis_Green(bpy.types.Operator):
    """McLaren's bright green color"""
    bl_label = "Mantis Green"
    bl_idname = 'color.mclaren_mantis_green'
    def execute(self, context):
        set_base_color(0x63EA2E, self.bl_label)
        return {'FINISHED'}

class McLaren_McLaren_Argon(bpy.types.Operator):
    """McLaren's classic dark grey color"""
    bl_label = "McLaren Argon"
    bl_idname = 'color.mclaren_mclaren_argon'
    def execute(self, context):
        set_base_color(0x626876, self.bl_label)
        return {'FINISHED'}

class McLaren_Mclaren_Orange(bpy.types.Operator):
    """McLaren's classic orange color"""
    bl_label = "Mclaren Orange"
    bl_idname = 'color.mclaren_mclaren_orange'
    def execute(self, context):
        set_base_color(0xFFC43D, self.bl_label)
        return {'FINISHED'}

class McLaren_Mercury_Red(bpy.types.Operator):
    """McLaren's dark red color"""
    bl_label = "Mercury Red"
    bl_idname = 'color.mclaren_mercury_red'
    def execute(self, context):
        set_base_color(0x9B0E1F, self.bl_label)
        return {'FINISHED'}

class McLaren_Pearl_White(bpy.types.Operator):
    """McLaren's flat white color"""
    bl_label = "Pearl White"
    bl_idname = 'color.mclaren_pearl_white'
    def execute(self, context):
        set_base_color(0xEBEBEB, self.bl_label)
        return {'FINISHED'}

class McLaren_Racing_Green(bpy.types.Operator):
    """McLaren's British racing green color"""
    bl_label = "Racing Green"
    bl_idname = 'color.mclaren_racing_green'
    def execute(self, context):
        set_base_color(0x2F473A, self.bl_label)
        return {'FINISHED'}

class McLaren_Sapphire_Black(bpy.types.Operator):
    """McLaren's classic black color"""
    bl_label = "Sapphire Black"
    bl_idname = 'color.mclaren_sapphire_black'
    def execute(self, context):
        set_base_color(0x29324E, self.bl_label)
        return {'FINISHED'}

class McLaren_Storm_Grey(bpy.types.Operator):
    """McLaren's classic grey color"""
    bl_label = "Storm Grey"
    bl_idname = 'color.mclaren_storm_grey'
    def execute(self, context):
        set_base_color(0x8C8D92, self.bl_label)
        return {'FINISHED'}

class McLaren_Titanium_Silver(bpy.types.Operator):
    """McLaren's classic silver color"""
    bl_label = "Titanium Silver"
    bl_idname = 'color.mclaren_titanium_silver'
    def execute(self, context):
        set_base_color(0x9BA2B4, self.bl_label)
        return {'FINISHED'}

class McLaren_Vegas_Blue(bpy.types.Operator):
    """McLaren's classic blue color"""
    bl_label = "Vegas Blue"
    bl_idname = 'color.mclaren_vegas_blue'
    def execute(self, context):
        set_base_color(0x0149D3, self.bl_label)
        return {'FINISHED'}

class McLaren_Volcano_Orange(bpy.types.Operator):
    """McLaren's fire orange color"""
    bl_label = "Volcano Orange"
    bl_idname = 'color.mclaren_volcano_orange'
    def execute(self, context):
        set_base_color(0xC82504, self.bl_label)
        return {'FINISHED'}

class McLaren_Volcano_Red(bpy.types.Operator):
    """McLaren's fire red color"""
    bl_label = "Volcano Red"
    bl_idname = 'color.mclaren_volcano_red'
    def execute(self, context):
        set_base_color(0xA80115, self.bl_label)
        return {'FINISHED'}

class Porsche_Acid_Green(bpy.types.Operator):
    """Porsche's electric green color"""
    bl_label = "Acid Green"
    bl_idname = 'color.porsche_acid_green'
    def execute(self, context):
        set_base_color(0xCBE800, self.bl_label)
        return {'FINISHED'}

class Porsche_Agate_Grey_Metallic(bpy.types.Operator):
    """Porsche's metallic grey color"""
    bl_label = "Agate Grey Metallic"
    bl_idname = 'color.porsche_agate_grey_metallic'
    def execute(self, context):
        set_base_color(0xAAB1B9, self.bl_label)
        return {'FINISHED'}

class Porsche_Arrow_Blue(bpy.types.Operator):
    """Porsche's bright blue color"""
    bl_label = "Arrow Blue"
    bl_idname = 'color.porsche_arrow_blue'
    def execute(self, context):
        set_base_color(0x0459DA, self.bl_label)
        return {'FINISHED'}

class Porsche_Aventurine_Green_Metallic(bpy.types.Operator):
    """Porsche's metallic dark green color"""
    bl_label = "Aventurine Green Metallic"
    bl_idname = 'color.porsche_aventurine_green_metallic'
    def execute(self, context):
        set_base_color(0x605E51, self.bl_label)
        return {'FINISHED'}

class Porsche_Azure_Blue(bpy.types.Operator):
    """Porsche's classic blue color"""
    bl_label = "Azure Blue"
    bl_idname = 'color.porsche_azure_blue'
    def execute(self, context):
        set_base_color(0x3C566F, self.bl_label)
        return {'FINISHED'}

class Porsche_Bahama_Blue(bpy.types.Operator):
    """Porsche's bright metallic blue color"""
    bl_label = "Bahama Blue"
    bl_idname = 'color.porsche_bahama_blue'
    def execute(self, context):
        set_base_color(0x2971EA, self.bl_label)
        return {'FINISHED'}

class Porsche_Carbon_Black_Metallic(bpy.types.Operator):
    """Porsche's bright metallic black color"""
    bl_label = "Carbon Black Metallic"
    bl_idname = 'color.porsche_carbon_black_metallic'
    def execute(self, context):
        set_base_color(0x74828B, self.bl_label)
        return {'FINISHED'}

class Porsche_Carmine_Red(bpy.types.Operator):
    """Porsche's deep red color"""
    bl_label = "Carmine Red"
    bl_idname = 'color.porsche_carmine_red'
    def execute(self, context):
        set_base_color(0x9D0620, self.bl_label)
        return {'FINISHED'}

class Porsche_Chalk(bpy.types.Operator):
    """Porsche's light grey color"""
    bl_label = "Chalk"
    bl_idname = 'color.porsche_chalk'
    def execute(self, context):
        set_base_color(0xA5A4AC, self.bl_label)
        return {'FINISHED'}

class Porsche_Dolomite_Silver_Metallic(bpy.types.Operator):
    """Porsche's metallic silver color"""
    bl_label = "Dolomite Silver Metallic"
    bl_idname = 'color.porsche_dolomite_silver_metallic'
    def execute(self, context):
        set_base_color(0x9FB1BC, self.bl_label)
        return {'FINISHED'}

class Porsche_Emerald_Green_Metalli(bpy.types.Operator):
    """Porsche's British racing green color"""
    bl_label = "Emerald Green Metalli"
    bl_idname = 'color.porsche_emerald_green_metalli'
    def execute(self, context):
        set_base_color(0x328983, self.bl_label)
        return {'FINISHED'}

class Porsche_Gentian_Blue_Metallic(bpy.types.Operator):
    """Porsche's metallic blue color"""
    bl_label = "Gentian Blue Metallic"
    bl_idname = 'color.porsche_gentian_blue_metallic'
    def execute(self, context):
        set_base_color(0x09203F, self.bl_label)
        return {'FINISHED'}

class Porsche_Graphite_Grey(bpy.types.Operator):
    """Porsche's classic grey color"""
    bl_label = "Graphite Grey"
    bl_idname = 'color.porsche_graphite_grey'
    def execute(self, context):
        set_base_color(0x748795, self.bl_label)
        return {'FINISHED'}

class Porsche_Graphite_Metallic(bpy.types.Operator):
    """Porsche's bright grey color"""
    bl_label = "Graphite Metallic"
    bl_idname = 'color.porsche_graphite_metallic'
    def execute(self, context):
        set_base_color(0x546A78, self.bl_label)
        return {'FINISHED'}

class Porsche_GT_Silver_Metallic(bpy.types.Operator):
    """Porsche's light metallic grey color"""
    bl_label = "GT Silver Metallic"
    bl_idname = 'color.porsche_gt_silver_metallic'
    def execute(self, context):
        set_base_color(0xA3ACB3, self.bl_label)
        return {'FINISHED'}

class Porsche_Guards_Red(bpy.types.Operator):
    """Porsche's classic red color"""
    bl_label = "Guards Red"
    bl_idname = 'color.porsche_guards_red'
    def execute(self, context):
        set_base_color(0xFA2223, self.bl_label)
        return {'FINISHED'}

class Porsche_Ice_Blue_Metallic(bpy.types.Operator):
    """Porsche's light metallic blue color"""
    bl_label = "Ice Blue Metallic"
    bl_idname = 'color.porsche_ice_blue_metallic'
    def execute(self, context):
        set_base_color(0x8C969F, self.bl_label)
        return {'FINISHED'}

class Porsche_Jade_Green(bpy.types.Operator):
    """Porsche's bright teal color"""
    bl_label = "Jade Green"
    bl_idname = 'color.porsche_jade_green'
    def execute(self, context):
        set_base_color(0x00BC96, self.bl_label)
        return {'FINISHED'}

class Porsche_Jet_Black_Metallic(bpy.types.Operator):
    """Porsche's metallic black color"""
    bl_label = "Jet Black Metallic"
    bl_idname = 'color.porsche_jet_black_metallic'
    def execute(self, context):
        set_base_color(0x201A1E, self.bl_label)
        return {'FINISHED'}

class Porsche_Lava_Orange(bpy.types.Operator):
    """Porsche's classic orange color"""
    bl_label = "Lava Orange"
    bl_idname = 'color.porsche_lava_orange'
    def execute(self, context):
        set_base_color(0xFF2600, self.bl_label)
        return {'FINISHED'}

class Porsche_Metallic_Blue(bpy.types.Operator):
    """Porsche's classic metallic blue color"""
    bl_label = "Metallic Blue"
    bl_idname = 'color.porsche_metallic_blue'
    def execute(self, context):
        set_base_color(0x0387D9, self.bl_label)
        return {'FINISHED'}

class Porsche_Miami_Blue(bpy.types.Operator):
    """Porsche's light blue color"""
    bl_label = "Miami Blue"
    bl_idname = 'color.porsche_miami_blue'
    def execute(self, context):
        set_base_color(0x00B5C8, self.bl_label)
        return {'FINISHED'}

class Porsche_Moonlight_Blue_Metallic(bpy.types.Operator):
    """Porsche's dark metallic blue color"""
    bl_label = "Moonlight Blue Metallic"
    bl_idname = 'color.porsche_moonlight_blue_metallic'
    def execute(self, context):
        set_base_color(0x153149, self.bl_label)
        return {'FINISHED'}

class Porsche_Night_Blue_Metallic(bpy.types.Operator):
    """Porsche's dark metallic blue color"""
    bl_label = "Night Blue Metallic"
    bl_idname = 'color.porsche_night_blue_metallic'
    def execute(self, context):
        set_base_color(0x385D89, self.bl_label)
        return {'FINISHED'}

class Porsche_Pastel_blue(bpy.types.Operator):
    """Porsche's light pastel blue color"""
    bl_label = "Pastel blue"
    bl_idname = 'color.porsche_pastel_blue'
    def execute(self, context):
        set_base_color(0xA0D8FB, self.bl_label)
        return {'FINISHED'}

class Porsche_Polo_Red(bpy.types.Operator):
    """Porsche's classic red color"""
    bl_label = "Polo Red"
    bl_idname = 'color.porsche_polo_red'
    def execute(self, context):
        set_base_color(0x980611, self.bl_label)
        return {'FINISHED'}

class Porsche_Python_Green(bpy.types.Operator):
    """Porsche's bright green color"""
    bl_label = "Python Green"
    bl_idname = 'color.porsche_python_green'
    def execute(self, context):
        set_base_color(0x1FF497, self.bl_label)
        return {'FINISHED'}

class Porsche_Racing_Yellow(bpy.types.Operator):
    """Porsche's classic yellow color"""
    bl_label = "Racing Yellow"
    bl_idname = 'color.porsche_racing_yellow'
    def execute(self, context):
        set_base_color(0xF8CD02, self.bl_label)
        return {'FINISHED'}

class Porsche_Red_Metallic(bpy.types.Operator):
    """Porsche's metallic red color"""
    bl_label = "Red Metallic"
    bl_idname = 'color.porsche_red_metallic'
    def execute(self, context):
        set_base_color(0xA72241, self.bl_label)
        return {'FINISHED'}

class Porsche_Riviera_Blue(bpy.types.Operator):
    """Porsche's bright blue color"""
    bl_label = "Riviera Blue"
    bl_idname = 'color.porsche_riviera_blue'
    def execute(self, context):
        set_base_color(0x018ADA, self.bl_label)
        return {'FINISHED'}

class Porsche_Rubystone_Red(bpy.types.Operator):
    """Porsche's pink ruby color"""
    bl_label = "Rubystone Red"
    bl_idname = 'color.porsche_rubystone_red'
    def execute(self, context):
        set_base_color(0xF3037E, self.bl_label)
        return {'FINISHED'}

class Porsche_Sand_Beige(bpy.types.Operator):
    """Porsche's flat beige color"""
    bl_label = "Sand Beige"
    bl_idname = 'color.porsche_sand_beige'
    def execute(self, context):
        set_base_color(0xC9AC80, self.bl_label)
        return {'FINISHED'}

class Porsche_Scarlet_Red(bpy.types.Operator):
    """Porsche's red/orange color"""
    bl_label = "Scarlet Red"
    bl_idname = 'color.porsche_scarlet_red'
    def execute(self, context):
        set_base_color(0xF82100, self.bl_label)
        return {'FINISHED'}

class Porsche_Viper_Green(bpy.types.Operator):
    """Porsche's classic green color"""
    bl_label = "Viper Green"
    bl_idname = 'color.porsche_viper_green'
    def execute(self, context):
        set_base_color(0x029220, self.bl_label)
        return {'FINISHED'}


# ECC PANEL

class ECCPanel(bpy.types.Panel):
    bl_idname = "ECC_PT_Panel"
    bl_label = "Exotic Car Colors"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

class AUDIPanel(bpy.types.Panel):
    bl_idname = "AUDI_PT_Panel"
    bl_label = "    Audi"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'ECC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["audi_nardo_grey"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.audi_nardo_grey", text="Nardo Grey")

class FERRARIPanel(bpy.types.Panel):
    bl_idname = "FERRARI_PT_Panel"
    bl_label = "    Ferrari"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'ECC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["ferrari_argento_nurburgring"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_bianco_avorio"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_bianco_avus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_blu_abu_dhabi"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_blu_pozzi"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_blu_scozia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_blu_swaters"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_blu_tour_de_france"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_canna_di_fucile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_giallo_modena"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_grigio_alloy"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_grigio_ferro"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_grigio_ingrid"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_grigio_scuro"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_grigio_silverstone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_grigio_titanio"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_nero_daytona"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_70_anni"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_corsa"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_dino"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_fiorano"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_fuoco"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_mugello"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_rosso_scuderia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ferrari_verde_british"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.ferrari_argento_nurburgring", text="Argento Nurburgring")
        scol.operator("color.ferrari_bianco_avorio", text="Bianco Avorio")
        scol.operator("color.ferrari_bianco_avus", text="Bianco Avus")
        scol.operator("color.ferrari_blu_abu_dhabi", text="Blu Abu Dhabi")
        scol.operator("color.ferrari_blu_pozzi", text="Blu Pozzi")
        scol.operator("color.ferrari_blu_scozia", text="Blu Scozia")
        scol.operator("color.ferrari_blu_swaters", text="Blu Swaters")
        scol.operator("color.ferrari_blu_tour_de_france", text="Blu Tour De France")
        scol.operator("color.ferrari_canna_di_fucile", text="Canna Di Fucile")
        scol.operator("color.ferrari_giallo_modena", text="Giallo Modena")
        scol.operator("color.ferrari_grigio_alloy", text="Grigio Alloy")
        scol.operator("color.ferrari_grigio_ferro", text="Grigio Ferro")
        scol.operator("color.ferrari_grigio_ingrid", text="Grigio Ingrid")
        scol.operator("color.ferrari_grigio_scuro", text="Grigio Scuro")
        scol.operator("color.ferrari_grigio_silverstone", text="Grigio Silverstone")
        scol.operator("color.ferrari_grigio_titanio", text="Grigio Titanio")
        scol.operator("color.ferrari_nero_daytona", text="Nero Daytona")
        scol.operator("color.ferrari_rosso_70_anni", text="Rosso 70 Anni")
        scol.operator("color.ferrari_rosso_corsa", text="Rosso Corsa")
        scol.operator("color.ferrari_rosso_dino", text="Rosso Dino")
        scol.operator("color.ferrari_rosso_fiorano", text="Rosso Fiorano")
        scol.operator("color.ferrari_rosso_fuoco", text="Rosso Fuoco")
        scol.operator("color.ferrari_rosso_mugello", text="Rosso Mugello")
        scol.operator("color.ferrari_rosso_scuderia", text="Rosso Scuderia")
        scol.operator("color.ferrari_verde_british", text="Verde British")

class LAMBORGHINIPanel(bpy.types.Panel):
    bl_idname = "LAMBORGHINI_PT_Panel"
    bl_label = "    Lamborghini"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'ECC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["lamborghini_arancia_atlas"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_arancio_argos"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_arancio_borealis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_arancio_bruciato"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_arancio_xanto"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_azzurro_thetys"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_balloon_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_bianco_asopo"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_bianco_comes"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_bianco_isi"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_bianco_monocerus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_aegir"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_astraeus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_caelum"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_cepheus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_eleos"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_fontus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_glauco"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_le_mans"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_nereid"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_nethuns"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_nila"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_notte"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_blu_uranus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_bronzo_zante"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_giallo_auge"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_giallo_evros"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_giallo_inti"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_giallo_orion"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_giallo_spica"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_giallo_tenerife"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_antares"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_ater"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_estoque"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_hati"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_keres"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_liqueo"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_lynx"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_nimbus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_grigio_telesto"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_nero_aldebaran"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_nero_granatus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_nero_helene"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_nero_nemesis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_nero_noctis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_nero_pegaso"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_oros_elios"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_rosso_arancio"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_rosso_bia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_rosso_efesto"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_rosso_leto"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_rosso_mars"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_citrea"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_ermes"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_gea_lucido"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_ithaca"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_mantis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_scandal"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_verde_selvans"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_viola_30"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_viola_aletheia"].icon_id)
        scol.label(text="", icon_value=g.c_icons["lamborghini_viola_pasifae"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.lamborghini_arancia_atlas", text="Arancia Atlas")
        scol.operator("color.lamborghini_arancio_argos", text="Arancio Argos")
        scol.operator("color.lamborghini_arancio_borealis", text="Arancio Borealis")
        scol.operator("color.lamborghini_arancio_bruciato", text="Arancio Bruciato")
        scol.operator("color.lamborghini_arancio_xanto", text="Arancio Xanto")
        scol.operator("color.lamborghini_azzurro_thetys", text="Azzurro Thetys")
        scol.operator("color.lamborghini_balloon_white", text="Balloon White")
        scol.operator("color.lamborghini_bianco_asopo", text="Bianco Asopo")
        scol.operator("color.lamborghini_bianco_comes", text="Bianco Comes")
        scol.operator("color.lamborghini_bianco_isi", text="Bianco Isi")
        scol.operator("color.lamborghini_bianco_monocerus", text="Bianco Monocerus")
        scol.operator("color.lamborghini_blu_aegir", text="Blu Aegir")
        scol.operator("color.lamborghini_blu_astraeus", text="Blu Astraeus")
        scol.operator("color.lamborghini_blu_caelum", text="Blu Caelum")
        scol.operator("color.lamborghini_blu_cepheus", text="Blu Cepheus")
        scol.operator("color.lamborghini_blu_eleos", text="Blu Eleos")
        scol.operator("color.lamborghini_blu_fontus", text="Blu Fontus")
        scol.operator("color.lamborghini_blu_glauco", text="Blu Glauco")
        scol.operator("color.lamborghini_blu_le_mans", text="Blu Le Mans")
        scol.operator("color.lamborghini_blu_nereid", text="Blu Nereid")
        scol.operator("color.lamborghini_blu_nethuns", text="Blu Nethuns")
        scol.operator("color.lamborghini_blu_nila", text="Blu Nila")
        scol.operator("color.lamborghini_blu_notte", text="Blu Notte")
        scol.operator("color.lamborghini_blu_uranus", text="Blu Uranus")
        scol.operator("color.lamborghini_bronzo_zante", text="Bronzo Zante")
        scol.operator("color.lamborghini_giallo_auge", text="Giallo Auge")
        scol.operator("color.lamborghini_giallo_evros", text="Giallo Evros")
        scol.operator("color.lamborghini_giallo_inti", text="Giallo Inti")
        scol.operator("color.lamborghini_giallo_orion", text="Giallo Orion")
        scol.operator("color.lamborghini_giallo_spica", text="Giallo Spica")
        scol.operator("color.lamborghini_giallo_tenerife", text="Giallo Tenerife")
        scol.operator("color.lamborghini_grigio_antares", text="Grigio Antares")
        scol.operator("color.lamborghini_grigio_ater", text="Grigio Ater")
        scol.operator("color.lamborghini_grigio_estoque", text="Grigio Estoque")
        scol.operator("color.lamborghini_grigio_hati", text="Grigio Hati")
        scol.operator("color.lamborghini_grigio_keres", text="Grigio Keres")
        scol.operator("color.lamborghini_grigio_liqueo", text="Grigio Liqueo")
        scol.operator("color.lamborghini_grigio_lynx", text="Grigio Lynx")
        scol.operator("color.lamborghini_grigio_nimbus", text="Grigio Nimbus")
        scol.operator("color.lamborghini_grigio_telesto", text="Grigio Telesto")
        scol.operator("color.lamborghini_nero_aldebaran", text="Nero Aldebaran")
        scol.operator("color.lamborghini_nero_granatus", text="Nero Granatus")
        scol.operator("color.lamborghini_nero_helene", text="Nero Helene")
        scol.operator("color.lamborghini_nero_nemesis", text="Nero Nemesis")
        scol.operator("color.lamborghini_nero_noctis", text="Nero Noctis")
        scol.operator("color.lamborghini_nero_pegaso", text="Nero Pegaso")
        scol.operator("color.lamborghini_oros_elios", text="Oros Elios")
        scol.operator("color.lamborghini_rosso_arancio", text="Rosso Arancio")
        scol.operator("color.lamborghini_rosso_bia", text="Rosso Bia")
        scol.operator("color.lamborghini_rosso_efesto", text="Rosso Efesto")
        scol.operator("color.lamborghini_rosso_leto", text="Rosso Leto")
        scol.operator("color.lamborghini_rosso_mars", text="Rosso Mars")
        scol.operator("color.lamborghini_verde_citrea", text="Verde Citrea")
        scol.operator("color.lamborghini_verde_ermes", text="Verde Ermes")
        scol.operator("color.lamborghini_verde_gea_lucido", text="Verde Gea Lucido")
        scol.operator("color.lamborghini_verde_ithaca", text="Verde Ithaca")
        scol.operator("color.lamborghini_verde_mantis", text="Verde Mantis")
        scol.operator("color.lamborghini_verde_metallic", text="Verde Metallic")
        scol.operator("color.lamborghini_verde_scandal", text="Verde Scandal")
        scol.operator("color.lamborghini_verde_selvans", text="Verde Selvans")
        scol.operator("color.lamborghini_viola_30", text="Viola 30")
        scol.operator("color.lamborghini_viola_aletheia", text="Viola Aletheia")
        scol.operator("color.lamborghini_viola_pasifae", text="Viola Pasifae")

class MCLARENPanel(bpy.types.Panel):
    bl_idname = "MCLAREN_PT_Panel"
    bl_label = "    McLaren"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'ECC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["mclaren_aurora_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_cobalt_violet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_curacao_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_fire_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_ice_silver"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_lantana_purple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_lime_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_mantis_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_mclaren_argon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_mclaren_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_mercury_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_pearl_white"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_racing_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_sapphire_black"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_storm_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_titanium_silver"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_vegas_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_volcano_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["mclaren_volcano_red"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.mclaren_aurora_blue", text="Aurora Blue")
        scol.operator("color.mclaren_cobalt_violet", text="Cobalt Violet")
        scol.operator("color.mclaren_curacao_blue", text="Curacao Blue")
        scol.operator("color.mclaren_fire_black", text="Fire Black")
        scol.operator("color.mclaren_ice_silver", text="Ice Silver")
        scol.operator("color.mclaren_lantana_purple", text="Lantana Purple")
        scol.operator("color.mclaren_lime_green", text="Lime Green")
        scol.operator("color.mclaren_mantis_green", text="Mantis Green")
        scol.operator("color.mclaren_mclaren_argon", text="McLaren Argon")
        scol.operator("color.mclaren_mclaren_orange", text="Mclaren Orange")
        scol.operator("color.mclaren_mercury_red", text="Mercury Red")
        scol.operator("color.mclaren_pearl_white", text="Pearl White")
        scol.operator("color.mclaren_racing_green", text="Racing Green")
        scol.operator("color.mclaren_sapphire_black", text="Sapphire Black")
        scol.operator("color.mclaren_storm_grey", text="Storm Grey")
        scol.operator("color.mclaren_titanium_silver", text="Titanium Silver")
        scol.operator("color.mclaren_vegas_blue", text="Vegas Blue")
        scol.operator("color.mclaren_volcano_orange", text="Volcano Orange")
        scol.operator("color.mclaren_volcano_red", text="Volcano Red")

class PORSCHEPanel(bpy.types.Panel):
    bl_idname = "PORSCHE_PT_Panel"
    bl_label = "    Porsche"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'ECC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["porsche_acid_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_agate_grey_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_arrow_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_aventurine_green_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_azure_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_bahama_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_carbon_black_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_carmine_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_chalk"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_dolomite_silver_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_emerald_green_metalli"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_gentian_blue_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_graphite_grey"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_graphite_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_gt_silver_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_guards_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_ice_blue_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_jade_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_jet_black_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_lava_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_metallic_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_miami_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_moonlight_blue_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_night_blue_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_pastel_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_polo_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_python_green"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_racing_yellow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_red_metallic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_riviera_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_rubystone_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_sand_beige"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_scarlet_red"].icon_id)
        scol.label(text="", icon_value=g.c_icons["porsche_viper_green"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.porsche_acid_green", text="Acid Green")
        scol.operator("color.porsche_agate_grey_metallic", text="Agate Grey Metallic")
        scol.operator("color.porsche_arrow_blue", text="Arrow Blue")
        scol.operator("color.porsche_aventurine_green_metallic", text="Aventurine Green Metallic")
        scol.operator("color.porsche_azure_blue", text="Azure Blue")
        scol.operator("color.porsche_bahama_blue", text="Bahama Blue")
        scol.operator("color.porsche_carbon_black_metallic", text="Carbon Black Metallic")
        scol.operator("color.porsche_carmine_red", text="Carmine Red")
        scol.operator("color.porsche_chalk", text="Chalk")
        scol.operator("color.porsche_dolomite_silver_metallic", text="Dolomite Silver Metallic")
        scol.operator("color.porsche_emerald_green_metalli", text="Emerald Green Metalli")
        scol.operator("color.porsche_gentian_blue_metallic", text="Gentian Blue Metallic")
        scol.operator("color.porsche_graphite_grey", text="Graphite Grey")
        scol.operator("color.porsche_graphite_metallic", text="Graphite Metallic")
        scol.operator("color.porsche_gt_silver_metallic", text="GT Silver Metallic")
        scol.operator("color.porsche_guards_red", text="Guards Red")
        scol.operator("color.porsche_ice_blue_metallic", text="Ice Blue Metallic")
        scol.operator("color.porsche_jade_green", text="Jade Green")
        scol.operator("color.porsche_jet_black_metallic", text="Jet Black Metallic")
        scol.operator("color.porsche_lava_orange", text="Lava Orange")
        scol.operator("color.porsche_metallic_blue", text="Metallic Blue")
        scol.operator("color.porsche_miami_blue", text="Miami Blue")
        scol.operator("color.porsche_moonlight_blue_metallic", text="Moonlight Blue Metallic")
        scol.operator("color.porsche_night_blue_metallic", text="Night Blue Metallic")
        scol.operator("color.porsche_pastel_blue", text="Pastel blue")
        scol.operator("color.porsche_polo_red", text="Polo Red")
        scol.operator("color.porsche_python_green", text="Python Green")
        scol.operator("color.porsche_racing_yellow", text="Racing Yellow")
        scol.operator("color.porsche_red_metallic", text="Red Metallic")
        scol.operator("color.porsche_riviera_blue", text="Riviera Blue")
        scol.operator("color.porsche_rubystone_red", text="Rubystone Red")
        scol.operator("color.porsche_sand_beige", text="Sand Beige")
        scol.operator("color.porsche_scarlet_red", text="Scarlet Red")
        scol.operator("color.porsche_viper_green", text="Viper Green")


# ECC CLASSES
array_ecc = [
    ECCPanel,
    AUDIPanel,
    FERRARIPanel,
    LAMBORGHINIPanel,
    MCLARENPanel,
    PORSCHEPanel,
    Audi_Nardo_Grey,
    Ferrari_Argento_Nurburgring,
    Ferrari_Bianco_Avorio,
    Ferrari_Bianco_Avus,
    Ferrari_Blu_Abu_Dhabi,
    Ferrari_Blu_Pozzi,
    Ferrari_Blu_Scozia,
    Ferrari_Blu_Swaters,
    Ferrari_Blu_Tour_De_France,
    Ferrari_Canna_Di_Fucile,
    Ferrari_Giallo_Modena,
    Ferrari_Grigio_Alloy,
    Ferrari_Grigio_Ferro,
    Ferrari_Grigio_Ingrid,
    Ferrari_Grigio_Scuro,
    Ferrari_Grigio_Silverstone,
    Ferrari_Grigio_Titanio,
    Ferrari_Nero_Daytona,
    Ferrari_Rosso_70_Anni,
    Ferrari_Rosso_Corsa,
    Ferrari_Rosso_Dino,
    Ferrari_Rosso_Fiorano,
    Ferrari_Rosso_Fuoco,
    Ferrari_Rosso_Mugello,
    Ferrari_Rosso_Scuderia,
    Ferrari_Verde_British,
    Lamborghini_Arancia_Atlas,
    Lamborghini_Arancio_Argos,
    Lamborghini_Arancio_Borealis,
    Lamborghini_Arancio_Bruciato,
    Lamborghini_Arancio_Xanto,
    Lamborghini_Azzurro_Thetys,
    Lamborghini_Balloon_White,
    Lamborghini_Bianco_Asopo,
    Lamborghini_Bianco_Comes,
    Lamborghini_Bianco_Isi,
    Lamborghini_Bianco_Monocerus,
    Lamborghini_Blu_Aegir,
    Lamborghini_Blu_Astraeus,
    Lamborghini_Blu_Caelum,
    Lamborghini_Blu_Cepheus,
    Lamborghini_Blu_Eleos,
    Lamborghini_Blu_Fontus,
    Lamborghini_Blu_Glauco,
    Lamborghini_Blu_Le_Mans,
    Lamborghini_Blu_Nereid,
    Lamborghini_Blu_Nethuns,
    Lamborghini_Blu_Nila,
    Lamborghini_Blu_Notte,
    Lamborghini_Blu_Uranus,
    Lamborghini_Bronzo_Zante,
    Lamborghini_Giallo_Auge,
    Lamborghini_Giallo_Evros,
    Lamborghini_Giallo_Inti,
    Lamborghini_Giallo_Orion,
    Lamborghini_Giallo_Spica,
    Lamborghini_Giallo_Tenerife,
    Lamborghini_Grigio_Antares,
    Lamborghini_Grigio_Ater,
    Lamborghini_Grigio_Estoque,
    Lamborghini_Grigio_Hati,
    Lamborghini_Grigio_Keres,
    Lamborghini_Grigio_Liqueo,
    Lamborghini_Grigio_Lynx,
    Lamborghini_Grigio_Nimbus,
    Lamborghini_Grigio_Telesto,
    Lamborghini_Nero_Aldebaran,
    Lamborghini_Nero_Granatus,
    Lamborghini_Nero_Helene,
    Lamborghini_Nero_Nemesis,
    Lamborghini_Nero_Noctis,
    Lamborghini_Nero_Pegaso,
    Lamborghini_Oros_Elios,
    Lamborghini_Rosso_Arancio,
    Lamborghini_Rosso_Bia,
    Lamborghini_Rosso_Efesto,
    Lamborghini_Rosso_Leto,
    Lamborghini_Rosso_Mars,
    Lamborghini_Verde_Citrea,
    Lamborghini_Verde_Ermes,
    Lamborghini_Verde_Gea_Lucido,
    Lamborghini_Verde_Ithaca,
    Lamborghini_Verde_Mantis,
    Lamborghini_Verde_Metallic,
    Lamborghini_Verde_Scandal,
    Lamborghini_Verde_Selvans,
    Lamborghini_Viola_30,
    Lamborghini_Viola_Aletheia,
    Lamborghini_Viola_Pasifae,
    McLaren_Aurora_Blue,
    McLaren_Cobalt_Violet,
    McLaren_Curacao_Blue,
    McLaren_Fire_Black,
    McLaren_Ice_Silver,
    McLaren_Lantana_Purple,
    McLaren_Lime_Green,
    McLaren_Mantis_Green,
    McLaren_McLaren_Argon,
    McLaren_Mclaren_Orange,
    McLaren_Mercury_Red,
    McLaren_Pearl_White,
    McLaren_Racing_Green,
    McLaren_Sapphire_Black,
    McLaren_Storm_Grey,
    McLaren_Titanium_Silver,
    McLaren_Vegas_Blue,
    McLaren_Volcano_Orange,
    McLaren_Volcano_Red,
    Porsche_Acid_Green,
    Porsche_Agate_Grey_Metallic,
    Porsche_Arrow_Blue,
    Porsche_Aventurine_Green_Metallic,
    Porsche_Azure_Blue,
    Porsche_Bahama_Blue,
    Porsche_Carbon_Black_Metallic,
    Porsche_Carmine_Red,
    Porsche_Chalk,
    Porsche_Dolomite_Silver_Metallic,
    Porsche_Emerald_Green_Metalli,
    Porsche_Gentian_Blue_Metallic,
    Porsche_Graphite_Grey,
    Porsche_Graphite_Metallic,
    Porsche_GT_Silver_Metallic,
    Porsche_Guards_Red,
    Porsche_Ice_Blue_Metallic,
    Porsche_Jade_Green,
    Porsche_Jet_Black_Metallic,
    Porsche_Lava_Orange,
    Porsche_Metallic_Blue,
    Porsche_Miami_Blue,
    Porsche_Moonlight_Blue_Metallic,
    Porsche_Night_Blue_Metallic,
    Porsche_Pastel_blue,
    Porsche_Polo_Red,
    Porsche_Python_Green,
    Porsche_Racing_Yellow,
    Porsche_Red_Metallic,
    Porsche_Riviera_Blue,
    Porsche_Rubystone_Red,
    Porsche_Sand_Beige,
    Porsche_Scarlet_Red,
    Porsche_Viper_Green,
]
