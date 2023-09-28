# AMS COLORS SET

import bpy

from .globals import *
from .color_functions import *

# AMS OPERATORS

class AMS10045(bpy.types.Operator):
    """AMS10045 - Brown"""
    bl_label = "10045 Brown"
    bl_idname = 'color.ams_10045'
    def execute(self, context):
        set_base_color(0x5F5453, self.bl_label)
        return {'FINISHED'}

class AMS10049(bpy.types.Operator):
    """AMS10049 - Maroon 81352 / ANA 510"""
    bl_label = "10049 Maroon 81352 / ANA 510"
    bl_idname = 'color.ams_10049'
    def execute(self, context):
        set_base_color(0x544141, self.bl_label)
        return {'FINISHED'}

class AMS10055(bpy.types.Operator):
    """AMS10055 - DoT Highway Brown"""
    bl_label = "10055 DoT Highway Brown"
    bl_idname = 'color.ams_10055'
    def execute(self, context):
        set_base_color(0x6C4D40, self.bl_label)
        return {'FINISHED'}

class AMS10059(bpy.types.Operator):
    """AMS10059 - Brown"""
    bl_label = "10059 Brown"
    bl_idname = 'color.ams_10059'
    def execute(self, context):
        set_base_color(0x5F504C, self.bl_label)
        return {'FINISHED'}

class AMS10070(bpy.types.Operator):
    """AMS10070 - Brown"""
    bl_label = "10070 Brown"
    bl_idname = 'color.ams_10070'
    def execute(self, context):
        set_base_color(0x5A4843, self.bl_label)
        return {'FINISHED'}

class AMS10075(bpy.types.Operator):
    """AMS10075 - Brown"""
    bl_label = "10075 Brown"
    bl_idname = 'color.ams_10075'
    def execute(self, context):
        set_base_color(0x625248, self.bl_label)
        return {'FINISHED'}

class AMS10076(bpy.types.Operator):
    """AMS10076 - Coast Guard Deck Red / Metallic Red-Brown"""
    bl_label = "10076 Coast Guard Deck Red / Metallic Red-Brown"
    bl_idname = 'color.ams_10076'
    def execute(self, context):
        set_base_color(0x794640, self.bl_label)
        return {'FINISHED'}

class AMS10080(bpy.types.Operator):
    """AMS10080 - Seal Brown / NASA Safety Brown"""
    bl_label = "10080 Seal Brown / NASA Safety Brown"
    bl_idname = 'color.ams_10080'
    def execute(self, context):
        set_base_color(0x625147, self.bl_label)
        return {'FINISHED'}

class AMS10091(bpy.types.Operator):
    """AMS10091 - Dark Oak"""
    bl_label = "10091 Dark Oak"
    bl_idname = 'color.ams_10091'
    def execute(self, context):
        set_base_color(0x7D4C3F, self.bl_label)
        return {'FINISHED'}

class AMS10115(bpy.types.Operator):
    """AMS10115 - Brown"""
    bl_label = "10115 Brown"
    bl_idname = 'color.ams_10115'
    def execute(self, context):
        set_base_color(0x9B684C, self.bl_label)
        return {'FINISHED'}

class AMS10219(bpy.types.Operator):
    """AMS10219 - Brown"""
    bl_label = "10219 Brown"
    bl_idname = 'color.ams_10219'
    def execute(self, context):
        set_base_color(0x937968, self.bl_label)
        return {'FINISHED'}

class AMS10233(bpy.types.Operator):
    """AMS10233 - Cocoa Brown / National Parks Service"""
    bl_label = "10233 Cocoa Brown / National Parks Service"
    bl_idname = 'color.ams_10233'
    def execute(self, context):
        set_base_color(0xA1766B, self.bl_label)
        return {'FINISHED'}

class AMS10260(bpy.types.Operator):
    """AMS10260 - Brown"""
    bl_label = "10260 Brown"
    bl_idname = 'color.ams_10260'
    def execute(self, context):
        set_base_color(0xC4A46F, self.bl_label)
        return {'FINISHED'}

class AMS10266(bpy.types.Operator):
    """AMS10266 - Middlestone"""
    bl_label = "10266 Middlestone"
    bl_idname = 'color.ams_10266'
    def execute(self, context):
        set_base_color(0xA6865D, self.bl_label)
        return {'FINISHED'}

class AMS10324(bpy.types.Operator):
    """AMS10324 - Brown"""
    bl_label = "10324 Brown"
    bl_idname = 'color.ams_10324'
    def execute(self, context):
        set_base_color(0xAD9484, self.bl_label)
        return {'FINISHED'}

class AMS10371(bpy.types.Operator):
    """AMS10371 - Buff / TT-E-489"""
    bl_label = "10371 Buff / TT-E-489"
    bl_idname = 'color.ams_10371'
    def execute(self, context):
        set_base_color(0xC29063, self.bl_label)
        return {'FINISHED'}

class AMS11086(bpy.types.Operator):
    """AMS11086 - DoT Highway Red"""
    bl_label = "11086 DoT Highway Red"
    bl_idname = 'color.ams_11086'
    def execute(self, context):
        set_base_color(0x914042, self.bl_label)
        return {'FINISHED'}

class AMS11105(bpy.types.Operator):
    """AMS11105 - OSHA Safety Red / DoT Highway Red"""
    bl_label = "11105 OSHA Safety Red / DoT Highway Red"
    bl_idname = 'color.ams_11105'
    def execute(self, context):
        set_base_color(0x9F3B40, self.bl_label)
        return {'FINISHED'}

class AMS11120(bpy.types.Operator):
    """AMS11120 - OSHA Safety Red"""
    bl_label = "11120 OSHA Safety Red"
    bl_idname = 'color.ams_11120'
    def execute(self, context):
        set_base_color(0xB04343, self.bl_label)
        return {'FINISHED'}

class AMS11136(bpy.types.Operator):
    """AMS11136 - Insignia Red / Carmine Red"""
    bl_label = "11136 Insignia Red / Carmine Red"
    bl_idname = 'color.ams_11136'
    def execute(self, context):
        set_base_color(0x914042, self.bl_label)
        return {'FINISHED'}

class AMS11140(bpy.types.Operator):
    """AMS11140 - OSHA Safety Red"""
    bl_label = "11140 OSHA Safety Red"
    bl_idname = 'color.ams_11140'
    def execute(self, context):
        set_base_color(0x9E3C3F, self.bl_label)
        return {'FINISHED'}

class AMS11302(bpy.types.Operator):
    """AMS11302 - Red"""
    bl_label = "11302 Red"
    bl_idname = 'color.ams_11302'
    def execute(self, context):
        set_base_color(0xBB4D4A, self.bl_label)
        return {'FINISHED'}

class AMS11310(bpy.types.Operator):
    """AMS11310 - Post Office Red"""
    bl_label = "11310 Post Office Red"
    bl_idname = 'color.ams_11310'
    def execute(self, context):
        set_base_color(0xB74441, self.bl_label)
        return {'FINISHED'}

class AMS11328(bpy.types.Operator):
    """AMS11328 - Red"""
    bl_label = "11328 Red"
    bl_idname = 'color.ams_11328'
    def execute(self, context):
        set_base_color(0xB04E56, self.bl_label)
        return {'FINISHED'}

class AMS11330(bpy.types.Operator):
    """AMS11330 - RCAF Snowbird Red I-4147"""
    bl_label = "11330 RCAF Snowbird Red I-4147"
    bl_idname = 'color.ams_11330'
    def execute(self, context):
        set_base_color(0xAC4044, self.bl_label)
        return {'FINISHED'}

class AMS11350(bpy.types.Operator):
    """AMS11350 - Coast Guard Buoy Red"""
    bl_label = "11350 Coast Guard Buoy Red"
    bl_idname = 'color.ams_11350'
    def execute(self, context):
        set_base_color(0xAD3E43, self.bl_label)
        return {'FINISHED'}

class AMS11400(bpy.types.Operator):
    """AMS11400 - Red"""
    bl_label = "11400 Red"
    bl_idname = 'color.ams_11400'
    def execute(self, context):
        set_base_color(0xC95246, self.bl_label)
        return {'FINISHED'}

class AMS11630(bpy.types.Operator):
    """AMS11630 - Red"""
    bl_label = "11630 Red"
    bl_idname = 'color.ams_11630'
    def execute(self, context):
        set_base_color(0xDCB7B2, self.bl_label)
        return {'FINISHED'}

class AMS11670(bpy.types.Operator):
    """AMS11670 - Peach"""
    bl_label = "11670 Peach"
    bl_idname = 'color.ams_11670'
    def execute(self, context):
        set_base_color(0xEFCBB4, self.bl_label)
        return {'FINISHED'}

class AMS12160(bpy.types.Operator):
    """AMS12160 - Orange-Brown"""
    bl_label = "12160 Orange-Brown"
    bl_idname = 'color.ams_12160'
    def execute(self, context):
        set_base_color(0xA96350, self.bl_label)
        return {'FINISHED'}

class AMS12197(bpy.types.Operator):
    """AMS12197 - International Orange / ANA 508"""
    bl_label = "12197 International Orange / ANA 508"
    bl_idname = 'color.ams_12197'
    def execute(self, context):
        set_base_color(0xC24F3C, self.bl_label)
        return {'FINISHED'}

class AMS12199(bpy.types.Operator):
    """AMS12199 - Coast Guard Red #40"""
    bl_label = "12199 Coast Guard Red #40"
    bl_idname = 'color.ams_12199'
    def execute(self, context):
        set_base_color(0xDB473C, self.bl_label)
        return {'FINISHED'}

class AMS12215(bpy.types.Operator):
    """AMS12215 - Orange"""
    bl_label = "12215 Orange"
    bl_idname = 'color.ams_12215'
    def execute(self, context):
        set_base_color(0xCA5E3E, self.bl_label)
        return {'FINISHED'}

class AMS12243(bpy.types.Operator):
    """AMS12243 - DoT Highway Orange"""
    bl_label = "12243 DoT Highway Orange"
    bl_idname = 'color.ams_12243'
    def execute(self, context):
        set_base_color(0xD26C3A, self.bl_label)
        return {'FINISHED'}

class AMS12246(bpy.types.Operator):
    """AMS12246 - OSHA Safety Orange"""
    bl_label = "12246 OSHA Safety Orange"
    bl_idname = 'color.ams_12246'
    def execute(self, context):
        set_base_color(0xD35C3C, self.bl_label)
        return {'FINISHED'}

class AMS12250(bpy.types.Operator):
    """AMS12250 - Coast Guard Orange"""
    bl_label = "12250 Coast Guard Orange"
    bl_idname = 'color.ams_12250'
    def execute(self, context):
        set_base_color(0xD24F39, self.bl_label)
        return {'FINISHED'}

class AMS12300(bpy.types.Operator):
    """AMS12300 - OSHA Safety Orange"""
    bl_label = "12300 OSHA Safety Orange"
    bl_idname = 'color.ams_12300'
    def execute(self, context):
        set_base_color(0xDB7B31, self.bl_label)
        return {'FINISHED'}

class AMS12473(bpy.types.Operator):
    """AMS12473 - Orange"""
    bl_label = "12473 Orange"
    bl_idname = 'color.ams_12473'
    def execute(self, context):
        set_base_color(0xDE6F3B, self.bl_label)
        return {'FINISHED'}

class AMS12648(bpy.types.Operator):
    """AMS12648 - Orange"""
    bl_label = "12648 Orange"
    bl_idname = 'color.ams_12648'
    def execute(self, context):
        set_base_color(0xE3BF9C, self.bl_label)
        return {'FINISHED'}

class AMS13275(bpy.types.Operator):
    """AMS13275 - Post Office Yellow"""
    bl_label = "13275 Post Office Yellow"
    bl_idname = 'color.ams_13275'
    def execute(self, context):
        set_base_color(0xB8833A, self.bl_label)
        return {'FINISHED'}

class AMS13415(bpy.types.Operator):
    """AMS13415 - School Bus Yellow"""
    bl_label = "13415 School Bus Yellow"
    bl_idname = 'color.ams_13415'
    def execute(self, context):
        set_base_color(0xE39632, self.bl_label)
        return {'FINISHED'}

class AMS13432(bpy.types.Operator):
    """AMS13432 - Yellow"""
    bl_label = "13432 Yellow"
    bl_idname = 'color.ams_13432'
    def execute(self, context):
        set_base_color(0xE79631, self.bl_label)
        return {'FINISHED'}

class AMS13507(bpy.types.Operator):
    """AMS13507 - DoT Highway Yellow"""
    bl_label = "13507 DoT Highway Yellow"
    bl_idname = 'color.ams_13507'
    def execute(self, context):
        set_base_color(0xF5A727, self.bl_label)
        return {'FINISHED'}

class AMS13522(bpy.types.Operator):
    """AMS13522 - Yellow"""
    bl_label = "13522 Yellow"
    bl_idname = 'color.ams_13522'
    def execute(self, context):
        set_base_color(0xC4B69C, self.bl_label)
        return {'FINISHED'}

class AMS13523(bpy.types.Operator):
    """AMS13523 - Yellow"""
    bl_label = "13523 Yellow"
    bl_idname = 'color.ams_13523'
    def execute(self, context):
        set_base_color(0xD3B886, self.bl_label)
        return {'FINISHED'}

class AMS13531(bpy.types.Operator):
    """AMS13531 - Beige"""
    bl_label = "13531 Beige"
    bl_idname = 'color.ams_13531'
    def execute(self, context):
        set_base_color(0xCBB8A0, self.bl_label)
        return {'FINISHED'}

class AMS13538(bpy.types.Operator):
    """AMS13538 - DoT Highway Yellow / ANA 506"""
    bl_label = "13538 DoT Highway Yellow / ANA 506"
    bl_idname = 'color.ams_13538'
    def execute(self, context):
        set_base_color(0xECA01D, self.bl_label)
        return {'FINISHED'}

class AMS13578(bpy.types.Operator):
    """AMS13578 - Warm Gray"""
    bl_label = "13578 Warm Gray"
    bl_idname = 'color.ams_13578'
    def execute(self, context):
        set_base_color(0xD4C2A0, self.bl_label)
        return {'FINISHED'}

class AMS13591(bpy.types.Operator):
    """AMS13591 - OSHA Safety Yellow"""
    bl_label = "13591 OSHA Safety Yellow"
    bl_idname = 'color.ams_13591'
    def execute(self, context):
        set_base_color(0xEBC235, self.bl_label)
        return {'FINISHED'}

class AMS13594(bpy.types.Operator):
    """AMS13594 - Aircraft Cream / ANA 507"""
    bl_label = "13594 Aircraft Cream / ANA 507"
    bl_idname = 'color.ams_13594'
    def execute(self, context):
        set_base_color(0xE7C183, self.bl_label)
        return {'FINISHED'}

class AMS13596(bpy.types.Operator):
    """AMS13596 - Yellow"""
    bl_label = "13596 Yellow"
    bl_idname = 'color.ams_13596'
    def execute(self, context):
        set_base_color(0xDDBB81, self.bl_label)
        return {'FINISHED'}

class AMS13613(bpy.types.Operator):
    """AMS13613 - Buff"""
    bl_label = "13613 Buff"
    bl_idname = 'color.ams_13613'
    def execute(self, context):
        set_base_color(0xE4C7A1, self.bl_label)
        return {'FINISHED'}

class AMS13618(bpy.types.Operator):
    """AMS13618 - Postal Service Cream"""
    bl_label = "13618 Postal Service Cream"
    bl_idname = 'color.ams_13618'
    def execute(self, context):
        set_base_color(0xE8C469, self.bl_label)
        return {'FINISHED'}

class AMS13637(bpy.types.Operator):
    """AMS13637 - Yellow"""
    bl_label = "13637 Yellow"
    bl_idname = 'color.ams_13637'
    def execute(self, context):
        set_base_color(0xD7A43C, self.bl_label)
        return {'FINISHED'}

class AMS13655(bpy.types.Operator):
    """AMS13655 - OSHA Safety Yellow / ANA 505"""
    bl_label = "13655 OSHA Safety Yellow / ANA 505"
    bl_idname = 'color.ams_13655'
    def execute(self, context):
        set_base_color(0xF5B417, self.bl_label)
        return {'FINISHED'}

class AMS13670(bpy.types.Operator):
    """AMS13670 - Yellow-Green"""
    bl_label = "13670 Yellow-Green"
    bl_idname = 'color.ams_13670'
    def execute(self, context):
        set_base_color(0xD2CD65, self.bl_label)
        return {'FINISHED'}

class AMS13690(bpy.types.Operator):
    """AMS13690 - Park Service Cream"""
    bl_label = "13690 Park Service Cream"
    bl_idname = 'color.ams_13690'
    def execute(self, context):
        set_base_color(0xE0CEAF, self.bl_label)
        return {'FINISHED'}

class AMS13695(bpy.types.Operator):
    """AMS13695 - Ivory / Forest Service"""
    bl_label = "13695 Ivory / Forest Service"
    bl_idname = 'color.ams_13695'
    def execute(self, context):
        set_base_color(0xEDC985, self.bl_label)
        return {'FINISHED'}

class AMS13711(bpy.types.Operator):
    """AMS13711 - Yellow"""
    bl_label = "13711 Yellow"
    bl_idname = 'color.ams_13711'
    def execute(self, context):
        set_base_color(0xE7CEAA, self.bl_label)
        return {'FINISHED'}

class AMS13740(bpy.types.Operator):
    """AMS13740 - DLA Orphean Sand"""
    bl_label = "13740 DLA Orphean Sand"
    bl_idname = 'color.ams_13740'
    def execute(self, context):
        set_base_color(0xE6D7C3, self.bl_label)
        return {'FINISHED'}

class AMS13814(bpy.types.Operator):
    """AMS13814 - Yellow"""
    bl_label = "13814 Yellow"
    bl_idname = 'color.ams_13814'
    def execute(self, context):
        set_base_color(0xDBDC9C, self.bl_label)
        return {'FINISHED'}

class AMS14036(bpy.types.Operator):
    """AMS14036 - Green"""
    bl_label = "14036 Green"
    bl_idname = 'color.ams_14036'
    def execute(self, context):
        set_base_color(0x3F4A47, self.bl_label)
        return {'FINISHED'}

class AMS14050(bpy.types.Operator):
    """AMS14050 - Army Green / NATO Green"""
    bl_label = "14050 Army Green / NATO Green"
    bl_idname = 'color.ams_14050'
    def execute(self, context):
        set_base_color(0x4D504B, self.bl_label)
        return {'FINISHED'}

class AMS14052(bpy.types.Operator):
    """AMS14052 - Marine Green #23"""
    bl_label = "14052 Marine Green #23"
    bl_idname = 'color.ams_14052'
    def execute(self, context):
        set_base_color(0x4D4E48, self.bl_label)
        return {'FINISHED'}

class AMS14056(bpy.types.Operator):
    """AMS14056 - Green"""
    bl_label = "14056 Green"
    bl_idname = 'color.ams_14056'
    def execute(self, context):
        set_base_color(0x474D4A, self.bl_label)
        return {'FINISHED'}

class AMS14062(bpy.types.Operator):
    """AMS14062 - Deep Green"""
    bl_label = "14062 Deep Green"
    bl_idname = 'color.ams_14062'
    def execute(self, context):
        set_base_color(0x3D5948, self.bl_label)
        return {'FINISHED'}

class AMS14064(bpy.types.Operator):
    """AMS14064 - Green"""
    bl_label = "14064 Green"
    bl_idname = 'color.ams_14064'
    def execute(self, context):
        set_base_color(0x52514A, self.bl_label)
        return {'FINISHED'}

class AMS14066(bpy.types.Operator):
    """AMS14066 - DoT Highway Green"""
    bl_label = "14066 DoT Highway Green"
    bl_idname = 'color.ams_14066'
    def execute(self, context):
        set_base_color(0x2C5B4B, self.bl_label)
        return {'FINISHED'}

class AMS14077(bpy.types.Operator):
    """AMS14077 - Green"""
    bl_label = "14077 Green"
    bl_idname = 'color.ams_14077'
    def execute(self, context):
        set_base_color(0x4E544F, self.bl_label)
        return {'FINISHED'}

class AMS14079(bpy.types.Operator):
    """AMS14079 - Green"""
    bl_label = "14079 Green"
    bl_idname = 'color.ams_14079'
    def execute(self, context):
        set_base_color(0x55574C, self.bl_label)
        return {'FINISHED'}

class AMS14081(bpy.types.Operator):
    """AMS14081 - Sikorsky Green"""
    bl_label = "14081 Sikorsky Green"
    bl_idname = 'color.ams_14081'
    def execute(self, context):
        set_base_color(0x525448, self.bl_label)
        return {'FINISHED'}

class AMS14084(bpy.types.Operator):
    """AMS14084 - Green"""
    bl_label = "14084 Green"
    bl_idname = 'color.ams_14084'
    def execute(self, context):
        set_base_color(0x484742, self.bl_label)
        return {'FINISHED'}

class AMS14090(bpy.types.Operator):
    """AMS14090 - Green"""
    bl_label = "14090 Green"
    bl_idname = 'color.ams_14090'
    def execute(self, context):
        set_base_color(0x2B6E4F, self.bl_label)
        return {'FINISHED'}

class AMS14097(bpy.types.Operator):
    """AMS14097 - Green"""
    bl_label = "14097 Green"
    bl_idname = 'color.ams_14097'
    def execute(self, context):
        set_base_color(0x616754, self.bl_label)
        return {'FINISHED'}

class AMS14109(bpy.types.Operator):
    """AMS14109 - DoT Highway Green"""
    bl_label = "14109 DoT Highway Green"
    bl_idname = 'color.ams_14109'
    def execute(self, context):
        set_base_color(0x30614E, self.bl_label)
        return {'FINISHED'}

class AMS14110(bpy.types.Operator):
    """AMS14110 - NASA Safety Medium Green"""
    bl_label = "14110 NASA Safety Medium Green"
    bl_idname = 'color.ams_14110'
    def execute(self, context):
        set_base_color(0x416C48, self.bl_label)
        return {'FINISHED'}

class AMS14115(bpy.types.Operator):
    """AMS14115 - Green"""
    bl_label = "14115 Green"
    bl_idname = 'color.ams_14115'
    def execute(self, context):
        set_base_color(0x33765B, self.bl_label)
        return {'FINISHED'}

class AMS14120(bpy.types.Operator):
    """AMS14120 - OSHA Safety Green"""
    bl_label = "14120 OSHA Safety Green"
    bl_idname = 'color.ams_14120'
    def execute(self, context):
        set_base_color(0x087D5F, self.bl_label)
        return {'FINISHED'}

class AMS14151(bpy.types.Operator):
    """AMS14151 - Green"""
    bl_label = "14151 Green"
    bl_idname = 'color.ams_14151'
    def execute(self, context):
        set_base_color(0x646342, self.bl_label)
        return {'FINISHED'}

class AMS14158(bpy.types.Operator):
    """AMS14158 - Green"""
    bl_label = "14158 Green"
    bl_idname = 'color.ams_14158'
    def execute(self, context):
        set_base_color(0x6A7774, self.bl_label)
        return {'FINISHED'}

class AMS14159(bpy.types.Operator):
    """AMS14159 - Green"""
    bl_label = "14159 Green"
    bl_idname = 'color.ams_14159'
    def execute(self, context):
        set_base_color(0x71796E, self.bl_label)
        return {'FINISHED'}

class AMS14187(bpy.types.Operator):
    """AMS14187 - Oxygen Tank Green / ANA 503"""
    bl_label = "14187 Oxygen Tank Green / ANA 503"
    bl_idname = 'color.ams_14187'
    def execute(self, context):
        set_base_color(0x567C43, self.bl_label)
        return {'FINISHED'}

class AMS14193(bpy.types.Operator):
    """AMS14193 - Coast Guard Green"""
    bl_label = "14193 Coast Guard Green"
    bl_idname = 'color.ams_14193'
    def execute(self, context):
        set_base_color(0x2E9155, self.bl_label)
        return {'FINISHED'}

class AMS14223(bpy.types.Operator):
    """AMS14223 - Green"""
    bl_label = "14223 Green"
    bl_idname = 'color.ams_14223'
    def execute(self, context):
        set_base_color(0x61876A, self.bl_label)
        return {'FINISHED'}

class AMS14241(bpy.types.Operator):
    """AMS14241 - Green"""
    bl_label = "14241 Green"
    bl_idname = 'color.ams_14241'
    def execute(self, context):
        set_base_color(0x829E93, self.bl_label)
        return {'FINISHED'}

class AMS14255(bpy.types.Operator):
    """AMS14255 - Green"""
    bl_label = "14255 Green"
    bl_idname = 'color.ams_14255'
    def execute(self, context):
        set_base_color(0x918764, self.bl_label)
        return {'FINISHED'}

class AMS14257(bpy.types.Operator):
    """AMS14257 - Green"""
    bl_label = "14257 Green"
    bl_idname = 'color.ams_14257'
    def execute(self, context):
        set_base_color(0x8E8B69, self.bl_label)
        return {'FINISHED'}

class AMS14260(bpy.types.Operator):
    """AMS14260 - OSHA Safety Green"""
    bl_label = "14260 OSHA Safety Green"
    bl_idname = 'color.ams_14260'
    def execute(self, context):
        set_base_color(0x679B7D, self.bl_label)
        return {'FINISHED'}

class AMS14272(bpy.types.Operator):
    """AMS14272 - Green"""
    bl_label = "14272 Green"
    bl_idname = 'color.ams_14272'
    def execute(self, context):
        set_base_color(0x76987D, self.bl_label)
        return {'FINISHED'}

class AMS14277(bpy.types.Operator):
    """AMS14277 - Green"""
    bl_label = "14277 Green"
    bl_idname = 'color.ams_14277'
    def execute(self, context):
        set_base_color(0x879992, self.bl_label)
        return {'FINISHED'}

class AMS14325(bpy.types.Operator):
    """AMS14325 - Green"""
    bl_label = "14325 Green"
    bl_idname = 'color.ams_14325'
    def execute(self, context):
        set_base_color(0x81A795, self.bl_label)
        return {'FINISHED'}

class AMS14449(bpy.types.Operator):
    """AMS14449 - Green"""
    bl_label = "14449 Green"
    bl_idname = 'color.ams_14449'
    def execute(self, context):
        set_base_color(0x81A795, self.bl_label)
        return {'FINISHED'}

class AMS14491(bpy.types.Operator):
    """AMS14491 - Green"""
    bl_label = "14491 Green"
    bl_idname = 'color.ams_14491'
    def execute(self, context):
        set_base_color(0xA6BBA7, self.bl_label)
        return {'FINISHED'}

class AMS14516(bpy.types.Operator):
    """AMS14516 - Green"""
    bl_label = "14516 Green"
    bl_idname = 'color.ams_14516'
    def execute(self, context):
        set_base_color(0xAEC0AF, self.bl_label)
        return {'FINISHED'}

class AMS14533(bpy.types.Operator):
    """AMS14533 - Green"""
    bl_label = "14533 Green"
    bl_idname = 'color.ams_14533'
    def execute(self, context):
        set_base_color(0xABB893, self.bl_label)
        return {'FINISHED'}

class AMS14664(bpy.types.Operator):
    """AMS14664 - Green"""
    bl_label = "14664 Green"
    bl_idname = 'color.ams_14664'
    def execute(self, context):
        set_base_color(0xBBD1B8, self.bl_label)
        return {'FINISHED'}

class AMS14672(bpy.types.Operator):
    """AMS14672 - Army Admin Vehicles"""
    bl_label = "14672 Army Admin Vehicles"
    bl_idname = 'color.ams_14672'
    def execute(self, context):
        set_base_color(0xCBD3B6, self.bl_label)
        return {'FINISHED'}

class AMS15042(bpy.types.Operator):
    """AMS15042 - Sea Blue / Teal Blue / ANA 623"""
    bl_label = "15042 Sea Blue / Teal Blue / ANA 623"
    bl_idname = 'color.ams_15042'
    def execute(self, context):
        set_base_color(0x40474B, self.bl_label)
        return {'FINISHED'}

class AMS15044(bpy.types.Operator):
    """AMS15044 - Dark Blue / Insignia Blue / ANA 502"""
    bl_label = "15044 Dark Blue / Insignia Blue / ANA 502"
    bl_idname = 'color.ams_15044'
    def execute(self, context):
        set_base_color(0x3F444D, self.bl_label)
        return {'FINISHED'}

class AMS15045(bpy.types.Operator):
    """AMS15045 - Strata Blue / Air Force Blue / ANA 516"""
    bl_label = "15045 Strata Blue / Air Force Blue / ANA 516"
    bl_idname = 'color.ams_15045'
    def execute(self, context):
        set_base_color(0x3D4952, self.bl_label)
        return {'FINISHED'}

class AMS15048(bpy.types.Operator):
    """AMS15048 - Post Office Dark Blue"""
    bl_label = "15048 Post Office Dark Blue"
    bl_idname = 'color.ams_15048'
    def execute(self, context):
        set_base_color(0x3D495C, self.bl_label)
        return {'FINISHED'}

class AMS15050(bpy.types.Operator):
    """AMS15050 - Post Office Box"""
    bl_label = "15050 Post Office Box"
    bl_idname = 'color.ams_15050'
    def execute(self, context):
        set_base_color(0x3E4D62, self.bl_label)
        return {'FINISHED'}

class AMS15051(bpy.types.Operator):
    """AMS15051 - RCAF Snowbird Blue I-6256"""
    bl_label = "15051 RCAF Snowbird Blue I-6256"
    bl_idname = 'color.ams_15051'
    def execute(self, context):
        set_base_color(0x3B5375, self.bl_label)
        return {'FINISHED'}

class AMS15052(bpy.types.Operator):
    """AMS15052 - Post Office Medium Blue"""
    bl_label = "15052 Post Office Medium Blue"
    bl_idname = 'color.ams_15052'
    def execute(self, context):
        set_base_color(0x3B5274, self.bl_label)
        return {'FINISHED'}

class AMS15055(bpy.types.Operator):
    """AMS15055 - Blue"""
    bl_label = "15055 Blue"
    bl_idname = 'color.ams_15055'
    def execute(self, context):
        set_base_color(0x3E486A, self.bl_label)
        return {'FINISHED'}

class AMS15056(bpy.types.Operator):
    """AMS15056 - Blue"""
    bl_label = "15056 Blue"
    bl_idname = 'color.ams_15056'
    def execute(self, context):
        set_base_color(0x3F4874, self.bl_label)
        return {'FINISHED'}

class AMS15065(bpy.types.Operator):
    """AMS15065 - DoT Highway Blue"""
    bl_label = "15065 DoT Highway Blue"
    bl_idname = 'color.ams_15065'
    def execute(self, context):
        set_base_color(0x2E5F82, self.bl_label)
        return {'FINISHED'}

class AMS15080(bpy.types.Operator):
    """AMS15080 - Handicap Blue"""
    bl_label = "15080 Handicap Blue"
    bl_idname = 'color.ams_15080'
    def execute(self, context):
        set_base_color(0x648292, self.bl_label)
        return {'FINISHED'}

class AMS15090(bpy.types.Operator):
    """AMS15090 - DoT Highway Blue"""
    bl_label = "15090 DoT Highway Blue"
    bl_idname = 'color.ams_15090'
    def execute(self, context):
        set_base_color(0x2E5D79, self.bl_label)
        return {'FINISHED'}

class AMS15092(bpy.types.Operator):
    """AMS15092 - OSHA Safety Blue"""
    bl_label = "15092 OSHA Safety Blue"
    bl_idname = 'color.ams_15092'
    def execute(self, context):
        set_base_color(0x2C79A2, self.bl_label)
        return {'FINISHED'}

class AMS15095(bpy.types.Operator):
    """AMS15095 - Post Office Light Blue"""
    bl_label = "15095 Post Office Light Blue"
    bl_idname = 'color.ams_15095'
    def execute(self, context):
        set_base_color(0x3C6BA6, self.bl_label)
        return {'FINISHED'}

class AMS15102(bpy.types.Operator):
    """AMS15102 - OSHA Safety Blue / ANA 501"""
    bl_label = "15102 OSHA Safety Blue / ANA 501"
    bl_idname = 'color.ams_15102'
    def execute(self, context):
        set_base_color(0x3B698F, self.bl_label)
        return {'FINISHED'}

class AMS15107(bpy.types.Operator):
    """AMS15107 - Blue"""
    bl_label = "15107 Blue"
    bl_idname = 'color.ams_15107'
    def execute(self, context):
        set_base_color(0x648392, self.bl_label)
        return {'FINISHED'}

class AMS15109(bpy.types.Operator):
    """AMS15109 - Blue"""
    bl_label = "15109 Blue"
    bl_idname = 'color.ams_15109'
    def execute(self, context):
        set_base_color(0x547181, self.bl_label)
        return {'FINISHED'}

class AMS15123(bpy.types.Operator):
    """AMS15123 - Bright Blue"""
    bl_label = "15123 Bright Blue"
    bl_idname = 'color.ams_15123'
    def execute(self, context):
        set_base_color(0x496FA2, self.bl_label)
        return {'FINISHED'}

class AMS15125(bpy.types.Operator):
    """AMS15125 - Blue"""
    bl_label = "15125 Blue"
    bl_idname = 'color.ams_15125'
    def execute(self, context):
        set_base_color(0x10748A, self.bl_label)
        return {'FINISHED'}

class AMS15177(bpy.types.Operator):
    """AMS15177 - Clear Blue"""
    bl_label = "15177 Clear Blue"
    bl_idname = 'color.ams_15177'
    def execute(self, context):
        set_base_color(0x608095, self.bl_label)
        return {'FINISHED'}

class AMS15180(bpy.types.Operator):
    """AMS15180 - Blue / 85285"""
    bl_label = "15180 Blue / 85285"
    bl_idname = 'color.ams_15180'
    def execute(self, context):
        set_base_color(0x3875A7, self.bl_label)
        return {'FINISHED'}

class AMS15182(bpy.types.Operator):
    """AMS15182 - Coast Guard Blue"""
    bl_label = "15182 Coast Guard Blue"
    bl_idname = 'color.ams_15182'
    def execute(self, context):
        set_base_color(0x3286AC, self.bl_label)
        return {'FINISHED'}

class AMS15187(bpy.types.Operator):
    """AMS15187 - Blue"""
    bl_label = "15187 Blue"
    bl_idname = 'color.ams_15187'
    def execute(self, context):
        set_base_color(0x2F9BBE, self.bl_label)
        return {'FINISHED'}

class AMS15193(bpy.types.Operator):
    """AMS15193 - Light Blue"""
    bl_label = "15193 Light Blue"
    bl_idname = 'color.ams_15193'
    def execute(self, context):
        set_base_color(0x5A898F, self.bl_label)
        return {'FINISHED'}

class AMS15200(bpy.types.Operator):
    """AMS15200 - Blue"""
    bl_label = "15200 Blue"
    bl_idname = 'color.ams_15200'
    def execute(self, context):
        set_base_color(0x5BB7CB, self.bl_label)
        return {'FINISHED'}

class AMS15450(bpy.types.Operator):
    """AMS15450 - Blue"""
    bl_label = "15450 Blue"
    bl_idname = 'color.ams_15450'
    def execute(self, context):
        set_base_color(0x90B8CC, self.bl_label)
        return {'FINISHED'}

class AMS15526(bpy.types.Operator):
    """AMS15526 - Blue"""
    bl_label = "15526 Blue"
    bl_idname = 'color.ams_15526'
    def execute(self, context):
        set_base_color(0xACC0C4, self.bl_label)
        return {'FINISHED'}

class AMS16076(bpy.types.Operator):
    """AMS16076 - Coast Guard Deck Gray"""
    bl_label = "16076 Coast Guard Deck Gray"
    bl_idname = 'color.ams_16076'
    def execute(self, context):
        set_base_color(0x5C6067, self.bl_label)
        return {'FINISHED'}

class AMS16081(bpy.types.Operator):
    """AMS16081 - Dark Gray / ANA 513"""
    bl_label = "16081 Dark Gray / ANA 513"
    bl_idname = 'color.ams_16081'
    def execute(self, context):
        set_base_color(0x575A5A, self.bl_label)
        return {'FINISHED'}

class AMS16099(bpy.types.Operator):
    """AMS16099 - Coast Guard Blue Gray"""
    bl_label = "16099 Coast Guard Blue Gray"
    bl_idname = 'color.ams_16099'
    def execute(self, context):
        set_base_color(0x5B6266, self.bl_label)
        return {'FINISHED'}

class AMS16160(bpy.types.Operator):
    """AMS16160 - Gray"""
    bl_label = "16160 Gray"
    bl_idname = 'color.ams_16160'
    def execute(self, context):
        set_base_color(0x837259, self.bl_label)
        return {'FINISHED'}

class AMS16165(bpy.types.Operator):
    """AMS16165 - Gray"""
    bl_label = "16165 Gray"
    bl_idname = 'color.ams_16165'
    def execute(self, context):
        set_base_color(0x777467, self.bl_label)
        return {'FINISHED'}

class AMS16187(bpy.types.Operator):
    """AMS16187 - Mechanic Gray Navy Standard"""
    bl_label = "16187 Mechanic Gray Navy Standard"
    bl_idname = 'color.ams_16187'
    def execute(self, context):
        set_base_color(0x767E7F, self.bl_label)
        return {'FINISHED'}

class AMS16250(bpy.types.Operator):
    """AMS16250 - Gray"""
    bl_label = "16250 Gray"
    bl_idname = 'color.ams_16250'
    def execute(self, context):
        set_base_color(0x848B8A, self.bl_label)
        return {'FINISHED'}

class AMS16251(bpy.types.Operator):
    """AMS16251 - Gray"""
    bl_label = "16251 Gray"
    bl_idname = 'color.ams_16251'
    def execute(self, context):
        set_base_color(0x86898A, self.bl_label)
        return {'FINISHED'}

class AMS16293(bpy.types.Operator):
    """AMS16293 - Gray"""
    bl_label = "16293 Gray"
    bl_idname = 'color.ams_16293'
    def execute(self, context):
        set_base_color(0x8F9596, self.bl_label)
        return {'FINISHED'}

class AMS16307(bpy.types.Operator):
    """AMS16307 - Machinery Gray"""
    bl_label = "16307 Machinery Gray"
    bl_idname = 'color.ams_16307'
    def execute(self, context):
        set_base_color(0x969890, self.bl_label)
        return {'FINISHED'}

class AMS16314(bpy.types.Operator):
    """AMS16314 - Gray"""
    bl_label = "16314 Gray"
    bl_idname = 'color.ams_16314'
    def execute(self, context):
        set_base_color(0x949995, self.bl_label)
        return {'FINISHED'}

class AMS16329(bpy.types.Operator):
    """AMS16329 - Gray"""
    bl_label = "16329 Gray"
    bl_idname = 'color.ams_16329'
    def execute(self, context):
        set_base_color(0x8F9F9F, self.bl_label)
        return {'FINISHED'}

class AMS16350(bpy.types.Operator):
    """AMS16350 - Gray"""
    bl_label = "16350 Gray"
    bl_idname = 'color.ams_16350'
    def execute(self, context):
        set_base_color(0x938C7A, self.bl_label)
        return {'FINISHED'}

class AMS16357(bpy.types.Operator):
    """AMS16357 - Gray"""
    bl_label = "16357 Gray"
    bl_idname = 'color.ams_16357'
    def execute(self, context):
        set_base_color(0xA3A094, self.bl_label)
        return {'FINISHED'}

class AMS16360(bpy.types.Operator):
    """AMS16360 - Gray"""
    bl_label = "16360 Gray"
    bl_idname = 'color.ams_16360'
    def execute(self, context):
        set_base_color(0xAEA895, self.bl_label)
        return {'FINISHED'}

class AMS16376(bpy.types.Operator):
    """AMS16376 - Blue"""
    bl_label = "16376 Blue"
    bl_idname = 'color.ams_16376'
    def execute(self, context):
        set_base_color(0xA0A298, self.bl_label)
        return {'FINISHED'}

class AMS16405(bpy.types.Operator):
    """AMS16405 - Parchment"""
    bl_label = "16405 Parchment"
    bl_idname = 'color.ams_16405'
    def execute(self, context):
        set_base_color(0xBEB7A2, self.bl_label)
        return {'FINISHED'}

class AMS16440(bpy.types.Operator):
    """AMS16440 - Light Gray 85285 / 81352"""
    bl_label = "16440 Light Gray 85285 / 81352"
    bl_idname = 'color.ams_16440'
    def execute(self, context):
        set_base_color(0xB4B5AC, self.bl_label)
        return {'FINISHED'}

class AMS16473(bpy.types.Operator):
    """AMS16473 - Aircraft Gray / NASA / ANA 512"""
    bl_label = "16473 Aircraft Gray / NASA / ANA 512"
    bl_idname = 'color.ams_16473'
    def execute(self, context):
        set_base_color(0xA2ACA8, self.bl_label)
        return {'FINISHED'}

class AMS16480(bpy.types.Operator):
    """AMS16480 - Canada 501-109 Gloss"""
    bl_label = "16480 Canada 501-109 Gloss"
    bl_idname = 'color.ams_16480'
    def execute(self, context):
        set_base_color(0xADBAB4, self.bl_label)
        return {'FINISHED'}

class AMS16492(bpy.types.Operator):
    """AMS16492 - Dawn Gray"""
    bl_label = "16492 Dawn Gray"
    bl_idname = 'color.ams_16492'
    def execute(self, context):
        set_base_color(0xBCBCB5, self.bl_label)
        return {'FINISHED'}

class AMS16515(bpy.types.Operator):
    """AMS16515 - Boeing Gray 707"""
    bl_label = "16515 Boeing Gray 707"
    bl_idname = 'color.ams_16515'
    def execute(self, context):
        set_base_color(0xBEC1BE, self.bl_label)
        return {'FINISHED'}

class AMS16555(bpy.types.Operator):
    """AMS16555 - Gray"""
    bl_label = "16555 Gray"
    bl_idname = 'color.ams_16555'
    def execute(self, context):
        set_base_color(0xC7BCA2, self.bl_label)
        return {'FINISHED'}

class AMS17038(bpy.types.Operator):
    """AMS17038 - OSHA Black / ANA 515 / 622"""
    bl_label = "17038 OSHA Black / ANA 515 / 622"
    bl_idname = 'color.ams_17038'
    def execute(self, context):
        set_base_color(0x3A3A3A, self.bl_label)
        return {'FINISHED'}

class AMS17043(bpy.types.Operator):
    """AMS17043 - Gold"""
    bl_label = "17043 Gold"
    bl_idname = 'color.ams_17043'
    def execute(self, context):
        set_base_color(0xB49A64, self.bl_label)
        return {'FINISHED'}

class AMS17100(bpy.types.Operator):
    """AMS17100 - Purple"""
    bl_label = "17100 Purple"
    bl_idname = 'color.ams_17100'
    def execute(self, context):
        set_base_color(0x6F5576, self.bl_label)
        return {'FINISHED'}

class AMS17142(bpy.types.Operator):
    """AMS17142 - OSHA Safety Purple"""
    bl_label = "17142 OSHA Safety Purple"
    bl_idname = 'color.ams_17142'
    def execute(self, context):
        set_base_color(0x945E83, self.bl_label)
        return {'FINISHED'}

class AMS17155(bpy.types.Operator):
    """AMS17155 - OSHA Safety Purple"""
    bl_label = "17155 OSHA Safety Purple"
    bl_idname = 'color.ams_17155'
    def execute(self, context):
        set_base_color(0x91648F, self.bl_label)
        return {'FINISHED'}

class AMS17178(bpy.types.Operator):
    """AMS17178 - Silver/Aluminum Intl"""
    bl_label = "17178 Silver/Aluminum Intl"
    bl_idname = 'color.ams_17178'
    def execute(self, context):
        set_base_color(0xC4C6C8, self.bl_label)
        return {'FINISHED'}

class AMS17773(bpy.types.Operator):
    """AMS17773 - Blue White"""
    bl_label = "17773 Blue White"
    bl_idname = 'color.ams_17773'
    def execute(self, context):
        set_base_color(0xDDE3D6, self.bl_label)
        return {'FINISHED'}

class AMS17778(bpy.types.Operator):
    """AMS17778 - """
    bl_label = "17778 "
    bl_idname = 'color.ams_17778'
    def execute(self, context):
        set_base_color(0xE7E1C9, self.bl_label)
        return {'FINISHED'}

class AMS17855(bpy.types.Operator):
    """AMS17855 - """
    bl_label = "17855 "
    bl_idname = 'color.ams_17855'
    def execute(self, context):
        set_base_color(0xE9DDBB, self.bl_label)
        return {'FINISHED'}

class AMS17860(bpy.types.Operator):
    """AMS17860 - Coast Guard White"""
    bl_label = "17860 Coast Guard White"
    bl_idname = 'color.ams_17860'
    def execute(self, context):
        set_base_color(0xE7E8DF, self.bl_label)
        return {'FINISHED'}

class AMS17865(bpy.types.Operator):
    """AMS17865 - Hawker Beechcraft White 17865"""
    bl_label = "17865 Hawker Beechcraft White 17865"
    bl_idname = 'color.ams_17865'
    def execute(self, context):
        set_base_color(0xE2E5E3, self.bl_label)
        return {'FINISHED'}

class AMS17875(bpy.types.Operator):
    """AMS17875 - Insignia White / ANA 511"""
    bl_label = "17875 Insignia White / ANA 511"
    bl_idname = 'color.ams_17875'
    def execute(self, context):
        set_base_color(0xE7E8DD, self.bl_label)
        return {'FINISHED'}

class AMS17877(bpy.types.Operator):
    """AMS17877 - Coast Guard White"""
    bl_label = "17877 Coast Guard White"
    bl_idname = 'color.ams_17877'
    def execute(self, context):
        set_base_color(0xE5EFE7, self.bl_label)
        return {'FINISHED'}

class AMS17886(bpy.types.Operator):
    """AMS17886 - Bone White"""
    bl_label = "17886 Bone White"
    bl_idname = 'color.ams_17886'
    def execute(self, context):
        set_base_color(0xEEEAD9, self.bl_label)
        return {'FINISHED'}

class AMS17925(bpy.types.Operator):
    """AMS17925 - Untinted White"""
    bl_label = "17925 Untinted White"
    bl_idname = 'color.ams_17925'
    def execute(self, context):
        set_base_color(0xF2F3EA, self.bl_label)
        return {'FINISHED'}

class AMS17930(bpy.types.Operator):
    """AMS17930 - RCAF Snowbird White I-1310"""
    bl_label = "17930 RCAF Snowbird White I-1310"
    bl_idname = 'color.ams_17930'
    def execute(self, context):
        set_base_color(0xF6F8F3, self.bl_label)
        return {'FINISHED'}

class AMS20040(bpy.types.Operator):
    """AMS20040 - Brown"""
    bl_label = "20040 Brown"
    bl_idname = 'color.ams_20040'
    def execute(self, context):
        set_base_color(0x534B46, self.bl_label)
        return {'FINISHED'}

class AMS20045(bpy.types.Operator):
    """AMS20045 - Brown"""
    bl_label = "20045 Brown"
    bl_idname = 'color.ams_20045'
    def execute(self, context):
        set_base_color(0x615554, self.bl_label)
        return {'FINISHED'}

class AMS20059(bpy.types.Operator):
    """AMS20059 - Forest Service Sign Standard"""
    bl_label = "20059 Forest Service Sign Standard"
    bl_idname = 'color.ams_20059'
    def execute(self, context):
        set_base_color(0x5E4E4A, self.bl_label)
        return {'FINISHED'}

class AMS20061(bpy.types.Operator):
    """AMS20061 - Brown"""
    bl_label = "20061 Brown"
    bl_idname = 'color.ams_20061'
    def execute(self, context):
        set_base_color(0x654949, self.bl_label)
        return {'FINISHED'}

class AMS20062(bpy.types.Operator):
    """AMS20062 - Brown"""
    bl_label = "20062 Brown"
    bl_idname = 'color.ams_20062'
    def execute(self, context):
        set_base_color(0x5A514F, self.bl_label)
        return {'FINISHED'}

class AMS20065(bpy.types.Operator):
    """AMS20065 - Brown 356"""
    bl_label = "20065 Brown 356"
    bl_idname = 'color.ams_20065'
    def execute(self, context):
        set_base_color(0x786F67, self.bl_label)
        return {'FINISHED'}

class AMS20068(bpy.types.Operator):
    """AMS20068 - Madeira 1957"""
    bl_label = "20068 Madeira 1957"
    bl_idname = 'color.ams_20068'
    def execute(self, context):
        set_base_color(0x61594C, self.bl_label)
        return {'FINISHED'}

class AMS20090(bpy.types.Operator):
    """AMS20090 - Highland 480"""
    bl_label = "20090 Highland 480"
    bl_idname = 'color.ams_20090'
    def execute(self, context):
        set_base_color(0x675446, self.bl_label)
        return {'FINISHED'}

class AMS20095(bpy.types.Operator):
    """AMS20095 - Brown"""
    bl_label = "20095 Brown"
    bl_idname = 'color.ams_20095'
    def execute(self, context):
        set_base_color(0x76685A, self.bl_label)
        return {'FINISHED'}

class AMS20100(bpy.types.Operator):
    """AMS20100 - Brown"""
    bl_label = "20100 Brown"
    bl_idname = 'color.ams_20100'
    def execute(self, context):
        set_base_color(0x855A49, self.bl_label)
        return {'FINISHED'}

class AMS20109(bpy.types.Operator):
    """AMS20109 - F. S. Seminal Brown"""
    bl_label = "20109 F. S. Seminal Brown"
    bl_idname = 'color.ams_20109'
    def execute(self, context):
        set_base_color(0x84534C, self.bl_label)
        return {'FINISHED'}

class AMS20117(bpy.types.Operator):
    """AMS20117 - Brown"""
    bl_label = "20117 Brown"
    bl_idname = 'color.ams_20117'
    def execute(self, context):
        set_base_color(0x7E5F50, self.bl_label)
        return {'FINISHED'}

class AMS20122(bpy.types.Operator):
    """AMS20122 - Brown"""
    bl_label = "20122 Brown"
    bl_idname = 'color.ams_20122'
    def execute(self, context):
        set_base_color(0x73594A, self.bl_label)
        return {'FINISHED'}

class AMS20140(bpy.types.Operator):
    """AMS20140 - Brown"""
    bl_label = "20140 Brown"
    bl_idname = 'color.ams_20140'
    def execute(self, context):
        set_base_color(0x816B5E, self.bl_label)
        return {'FINISHED'}

class AMS20150(bpy.types.Operator):
    """AMS20150 - Coyote 476 / 498"""
    bl_label = "20150 Coyote 476 / 498"
    bl_idname = 'color.ams_20150'
    def execute(self, context):
        set_base_color(0x7A6852, self.bl_label)
        return {'FINISHED'}

class AMS20152(bpy.types.Operator):
    """AMS20152 - Brown"""
    bl_label = "20152 Brown"
    bl_idname = 'color.ams_20152'
    def execute(self, context):
        set_base_color(0x8C5049, self.bl_label)
        return {'FINISHED'}

class AMS20155(bpy.types.Operator):
    """AMS20155 - Light Brown 493"""
    bl_label = "20155 Light Brown 493"
    bl_idname = 'color.ams_20155'
    def execute(self, context):
        set_base_color(0x7F604E, self.bl_label)
        return {'FINISHED'}

class AMS20170(bpy.types.Operator):
    """AMS20170 - Olive Mohave"""
    bl_label = "20170 Olive Mohave"
    bl_idname = 'color.ams_20170'
    def execute(self, context):
        set_base_color(0x83735F, self.bl_label)
        return {'FINISHED'}

class AMS20180(bpy.types.Operator):
    """AMS20180 - Tan 499"""
    bl_label = "20180 Tan 499"
    bl_idname = 'color.ams_20180'
    def execute(self, context):
        set_base_color(0x847A66, self.bl_label)
        return {'FINISHED'}

class AMS20206(bpy.types.Operator):
    """AMS20206 - Brown"""
    bl_label = "20206 Brown"
    bl_idname = 'color.ams_20206'
    def execute(self, context):
        set_base_color(0x987C78, self.bl_label)
        return {'FINISHED'}

class AMS20219(bpy.types.Operator):
    """AMS20219 - Brown"""
    bl_label = "20219 Brown"
    bl_idname = 'color.ams_20219'
    def execute(self, context):
        set_base_color(0x937968, self.bl_label)
        return {'FINISHED'}

class AMS20220(bpy.types.Operator):
    """AMS20220 - Light Coyote 481"""
    bl_label = "20220 Light Coyote 481"
    bl_idname = 'color.ams_20220'
    def execute(self, context):
        set_base_color(0x917F6B, self.bl_label)
        return {'FINISHED'}

class AMS20227(bpy.types.Operator):
    """AMS20227 - Brown"""
    bl_label = "20227 Brown"
    bl_idname = 'color.ams_20227'
    def execute(self, context):
        set_base_color(0x9A8576, self.bl_label)
        return {'FINISHED'}

class AMS20233(bpy.types.Operator):
    """AMS20233 - Brown"""
    bl_label = "20233 Brown"
    bl_idname = 'color.ams_20233'
    def execute(self, context):
        set_base_color(0xA1776C, self.bl_label)
        return {'FINISHED'}

class AMS20252(bpy.types.Operator):
    """AMS20252 - Rose"""
    bl_label = "20252 Rose"
    bl_idname = 'color.ams_20252'
    def execute(self, context):
        set_base_color(0xAE7969, self.bl_label)
        return {'FINISHED'}

class AMS20260(bpy.types.Operator):
    """AMS20260 - Brown"""
    bl_label = "20260 Brown"
    bl_idname = 'color.ams_20260'
    def execute(self, context):
        set_base_color(0xC6A571, self.bl_label)
        return {'FINISHED'}

class AMS20266(bpy.types.Operator):
    """AMS20266 - Brown"""
    bl_label = "20266 Brown"
    bl_idname = 'color.ams_20266'
    def execute(self, context):
        set_base_color(0xA7885E, self.bl_label)
        return {'FINISHED'}

class AMS20270(bpy.types.Operator):
    """AMS20270 - Urban Tan 478"""
    bl_label = "20270 Urban Tan 478"
    bl_idname = 'color.ams_20270'
    def execute(self, context):
        set_base_color(0xA19285, self.bl_label)
        return {'FINISHED'}

class AMS20313(bpy.types.Operator):
    """AMS20313 - Brown"""
    bl_label = "20313 Brown"
    bl_idname = 'color.ams_20313'
    def execute(self, context):
        set_base_color(0xB0978B, self.bl_label)
        return {'FINISHED'}

class AMS20318(bpy.types.Operator):
    """AMS20318 - Brown"""
    bl_label = "20318 Brown"
    bl_idname = 'color.ams_20318'
    def execute(self, context):
        set_base_color(0xA79982, self.bl_label)
        return {'FINISHED'}

class AMS20372(bpy.types.Operator):
    """AMS20372 - Tan"""
    bl_label = "20372 Tan"
    bl_idname = 'color.ams_20372'
    def execute(self, context):
        set_base_color(0xAE9F8C, self.bl_label)
        return {'FINISHED'}

class AMS20400(bpy.types.Operator):
    """AMS20400 - Brown"""
    bl_label = "20400 Brown"
    bl_idname = 'color.ams_20400'
    def execute(self, context):
        set_base_color(0xC79D77, self.bl_label)
        return {'FINISHED'}

class AMS20450(bpy.types.Operator):
    """AMS20450 - Brown"""
    bl_label = "20450 Brown"
    bl_idname = 'color.ams_20450'
    def execute(self, context):
        set_base_color(0xC1A794, self.bl_label)
        return {'FINISHED'}

class AMS20460(bpy.types.Operator):
    """AMS20460 - Mushroom"""
    bl_label = "20460 Mushroom"
    bl_idname = 'color.ams_20460'
    def execute(self, context):
        set_base_color(0xC1B6A3, self.bl_label)
        return {'FINISHED'}

class AMS20475(bpy.types.Operator):
    """AMS20475 - Saudi Color #11 (Sang)"""
    bl_label = "20475 Saudi Color #11 (Sang)"
    bl_idname = 'color.ams_20475'
    def execute(self, context):
        set_base_color(0xCDB090, self.bl_label)
        return {'FINISHED'}

class AMS21105(bpy.types.Operator):
    """AMS21105 - Red"""
    bl_label = "21105 Red"
    bl_idname = 'color.ams_21105'
    def execute(self, context):
        set_base_color(0x973F3F, self.bl_label)
        return {'FINISHED'}

class AMS21136(bpy.types.Operator):
    """AMS21136 - Red"""
    bl_label = "21136 Red"
    bl_idname = 'color.ams_21136'
    def execute(self, context):
        set_base_color(0x914344, self.bl_label)
        return {'FINISHED'}

class AMS21158(bpy.types.Operator):
    """AMS21158 - Red"""
    bl_label = "21158 Red"
    bl_idname = 'color.ams_21158'
    def execute(self, context):
        set_base_color(0xB65A65, self.bl_label)
        return {'FINISHED'}

class AMS21302(bpy.types.Operator):
    """AMS21302 - Red"""
    bl_label = "21302 Red"
    bl_idname = 'color.ams_21302'
    def execute(self, context):
        set_base_color(0xB74E4B, self.bl_label)
        return {'FINISHED'}

class AMS21310(bpy.types.Operator):
    """AMS21310 - Red"""
    bl_label = "21310 Red"
    bl_idname = 'color.ams_21310'
    def execute(self, context):
        set_base_color(0xB94843, self.bl_label)
        return {'FINISHED'}

class AMS21400(bpy.types.Operator):
    """AMS21400 - Red"""
    bl_label = "21400 Red"
    bl_idname = 'color.ams_21400'
    def execute(self, context):
        set_base_color(0xCA5348, self.bl_label)
        return {'FINISHED'}

class AMS21433(bpy.types.Operator):
    """AMS21433 - Red"""
    bl_label = "21433 Red"
    bl_idname = 'color.ams_21433'
    def execute(self, context):
        set_base_color(0xC89787, self.bl_label)
        return {'FINISHED'}

class AMS21575(bpy.types.Operator):
    """AMS21575 - Red"""
    bl_label = "21575 Red"
    bl_idname = 'color.ams_21575'
    def execute(self, context):
        set_base_color(0xDDB6A4, self.bl_label)
        return {'FINISHED'}

class AMS21643(bpy.types.Operator):
    """AMS21643 - Red"""
    bl_label = "21643 Red"
    bl_idname = 'color.ams_21643'
    def execute(self, context):
        set_base_color(0xE6CCB4, self.bl_label)
        return {'FINISHED'}

class AMS21667(bpy.types.Operator):
    """AMS21667 - Red"""
    bl_label = "21667 Red"
    bl_idname = 'color.ams_21667'
    def execute(self, context):
        set_base_color(0xE6CAAB, self.bl_label)
        return {'FINISHED'}

class AMS21668(bpy.types.Operator):
    """AMS21668 - Red"""
    bl_label = "21668 Red"
    bl_idname = 'color.ams_21668'
    def execute(self, context):
        set_base_color(0xE8CBC2, self.bl_label)
        return {'FINISHED'}

class AMS21670(bpy.types.Operator):
    """AMS21670 - Red"""
    bl_label = "21670 Red"
    bl_idname = 'color.ams_21670'
    def execute(self, context):
        set_base_color(0xEECAB3, self.bl_label)
        return {'FINISHED'}

class AMS22144(bpy.types.Operator):
    """AMS22144 - Orange"""
    bl_label = "22144 Orange"
    bl_idname = 'color.ams_22144'
    def execute(self, context):
        set_base_color(0xA55848, self.bl_label)
        return {'FINISHED'}

class AMS22190(bpy.types.Operator):
    """AMS22190 - Orange"""
    bl_label = "22190 Orange"
    bl_idname = 'color.ams_22190'
    def execute(self, context):
        set_base_color(0xCC4A3C, self.bl_label)
        return {'FINISHED'}

class AMS22203(bpy.types.Operator):
    """AMS22203 - Orange"""
    bl_label = "22203 Orange"
    bl_idname = 'color.ams_22203'
    def execute(self, context):
        set_base_color(0xB6614C, self.bl_label)
        return {'FINISHED'}

class AMS22246(bpy.types.Operator):
    """AMS22246 - Orange"""
    bl_label = "22246 Orange"
    bl_idname = 'color.ams_22246'
    def execute(self, context):
        set_base_color(0xD55E3D, self.bl_label)
        return {'FINISHED'}

class AMS22276(bpy.types.Operator):
    """AMS22276 - Orange"""
    bl_label = "22276 Orange"
    bl_idname = 'color.ams_22276'
    def execute(self, context):
        set_base_color(0xC17461, self.bl_label)
        return {'FINISHED'}

class AMS22356(bpy.types.Operator):
    """AMS22356 - Orange"""
    bl_label = "22356 Orange"
    bl_idname = 'color.ams_22356'
    def execute(self, context):
        set_base_color(0xD48070, self.bl_label)
        return {'FINISHED'}

class AMS22473(bpy.types.Operator):
    """AMS22473 - Orange"""
    bl_label = "22473 Orange"
    bl_idname = 'color.ams_22473'
    def execute(self, context):
        set_base_color(0xDC6D3A, self.bl_label)
        return {'FINISHED'}

class AMS22510(bpy.types.Operator):
    """AMS22510 - Orange"""
    bl_label = "22510 Orange"
    bl_idname = 'color.ams_22510'
    def execute(self, context):
        set_base_color(0xF16832, self.bl_label)
        return {'FINISHED'}

class AMS22516(bpy.types.Operator):
    """AMS22516 - Light Orange Brown"""
    bl_label = "22516 Light Orange Brown"
    bl_idname = 'color.ams_22516'
    def execute(self, context):
        set_base_color(0xD59776, self.bl_label)
        return {'FINISHED'}

class AMS22519(bpy.types.Operator):
    """AMS22519 - Rosewood"""
    bl_label = "22519 Rosewood"
    bl_idname = 'color.ams_22519'
    def execute(self, context):
        set_base_color(0xD3AF97, self.bl_label)
        return {'FINISHED'}

class AMS22544(bpy.types.Operator):
    """AMS22544 - Orange"""
    bl_label = "22544 Orange"
    bl_idname = 'color.ams_22544'
    def execute(self, context):
        set_base_color(0xEB9353, self.bl_label)
        return {'FINISHED'}

class AMS22563(bpy.types.Operator):
    """AMS22563 - Beachwood"""
    bl_label = "22563 Beachwood"
    bl_idname = 'color.ams_22563'
    def execute(self, context):
        set_base_color(0xD8B99C, self.bl_label)
        return {'FINISHED'}

class AMS22630(bpy.types.Operator):
    """AMS22630 - Buff"""
    bl_label = "22630 Buff"
    bl_idname = 'color.ams_22630'
    def execute(self, context):
        set_base_color(0xE0BEA2, self.bl_label)
        return {'FINISHED'}

class AMS22648(bpy.types.Operator):
    """AMS22648 - Buff"""
    bl_label = "22648 Buff"
    bl_idname = 'color.ams_22648'
    def execute(self, context):
        set_base_color(0xE3BE9A, self.bl_label)
        return {'FINISHED'}

class AMS23275(bpy.types.Operator):
    """AMS23275 - Yellow Orange"""
    bl_label = "23275 Orange"
    bl_idname = 'color.ams_23275'
    def execute(self, context):
        set_base_color(0xBA853E, self.bl_label)
        return {'FINISHED'}

class AMS23420(bpy.types.Operator):
    """AMS23420 - Khaki 475"""
    bl_label = "23420 Khaki 475"
    bl_idname = 'color.ams_23420'
    def execute(self, context):
        set_base_color(0x837E6E, self.bl_label)
        return {'FINISHED'}

class AMS23430(bpy.types.Operator):
    """AMS23430 - Khaki P1"""
    bl_label = "23430 Khaki P1"
    bl_idname = 'color.ams_23430'
    def execute(self, context):
        set_base_color(0x9D9279, self.bl_label)
        return {'FINISHED'}

class AMS23435(bpy.types.Operator):
    """AMS23435 - Ligh Khaki 494"""
    bl_label = "23435 Ligh Khaki 494"
    bl_idname = 'color.ams_23435'
    def execute(self, context):
        set_base_color(0x9C937B, self.bl_label)
        return {'FINISHED'}

class AMS23448(bpy.types.Operator):
    """AMS23448 - Yellow"""
    bl_label = "23448 Yellow"
    bl_idname = 'color.ams_23448'
    def execute(self, context):
        set_base_color(0xB7A17D, self.bl_label)
        return {'FINISHED'}

class AMS23522(bpy.types.Operator):
    """AMS23522 - Yellow"""
    bl_label = "23522 Yellow"
    bl_idname = 'color.ams_23522'
    def execute(self, context):
        set_base_color(0xC7B89E, self.bl_label)
        return {'FINISHED'}

class AMS23525(bpy.types.Operator):
    """AMS23525 - Desert Sand 500/503"""
    bl_label = "23525 Desert Sand 500/503"
    bl_idname = 'color.ams_23525'
    def execute(self, context):
        set_base_color(0xBFB4A5, self.bl_label)
        return {'FINISHED'}

class AMS23530(bpy.types.Operator):
    """AMS23530 - Light Tan 479"""
    bl_label = "23530 Light Tan 479"
    bl_idname = 'color.ams_23530'
    def execute(self, context):
        set_base_color(0xB3A798, self.bl_label)
        return {'FINISHED'}

class AMS23531(bpy.types.Operator):
    """AMS23531 - Light Mushroom"""
    bl_label = "23531 Light Mushroom"
    bl_idname = 'color.ams_23531'
    def execute(self, context):
        set_base_color(0xCEBBA4, self.bl_label)
        return {'FINISHED'}

class AMS23538(bpy.types.Operator):
    """AMS23538 - Yellow"""
    bl_label = "23538 Yellow"
    bl_idname = 'color.ams_23538'
    def execute(self, context):
        set_base_color(0xECA123, self.bl_label)
        return {'FINISHED'}

class AMS23540(bpy.types.Operator):
    """AMS23540 - Yellow"""
    bl_label = "23540 Yellow"
    bl_idname = 'color.ams_23540'
    def execute(self, context):
        set_base_color(0xDCA24B, self.bl_label)
        return {'FINISHED'}

class AMS23564(bpy.types.Operator):
    """AMS23564 - Yellow"""
    bl_label = "23564 Yellow"
    bl_idname = 'color.ams_23564'
    def execute(self, context):
        set_base_color(0xD5C59E, self.bl_label)
        return {'FINISHED'}

class AMS23578(bpy.types.Operator):
    """AMS23578 - Yellow"""
    bl_label = "23578 Yellow"
    bl_idname = 'color.ams_23578'
    def execute(self, context):
        set_base_color(0xD4C2A0, self.bl_label)
        return {'FINISHED'}

class AMS23594(bpy.types.Operator):
    """AMS23594 - Yellow"""
    bl_label = "23594 Yellow"
    bl_idname = 'color.ams_23594'
    def execute(self, context):
        set_base_color(0xE5C083, self.bl_label)
        return {'FINISHED'}

class AMS23613(bpy.types.Operator):
    """AMS23613 - Buff"""
    bl_label = "23613 Buff"
    bl_idname = 'color.ams_23613'
    def execute(self, context):
        set_base_color(0xE8C9A4, self.bl_label)
        return {'FINISHED'}

class AMS23617(bpy.types.Operator):
    """AMS23617 - Yellow"""
    bl_label = "23617 Yellow"
    bl_idname = 'color.ams_23617'
    def execute(self, context):
        set_base_color(0xD5C4AA, self.bl_label)
        return {'FINISHED'}

class AMS23619(bpy.types.Operator):
    """AMS23619 - Yellow"""
    bl_label = "23619 Yellow"
    bl_idname = 'color.ams_23619'
    def execute(self, context):
        set_base_color(0xDDC59E, self.bl_label)
        return {'FINISHED'}

class AMS23640(bpy.types.Operator):
    """AMS23640 - Yellow 13655"""
    bl_label = "23640 Yellow 13655"
    bl_idname = 'color.ams_23640'
    def execute(self, context):
        set_base_color(0xF6B524, self.bl_label)
        return {'FINISHED'}

class AMS23655(bpy.types.Operator):
    """AMS23655 - Yellow"""
    bl_label = "23655 Yellow"
    bl_idname = 'color.ams_23655'
    def execute(self, context):
        set_base_color(0xF7B51B, self.bl_label)
        return {'FINISHED'}

class AMS23685(bpy.types.Operator):
    """AMS23685 - Yellow"""
    bl_label = "23685 Yellow"
    bl_idname = 'color.ams_23685'
    def execute(self, context):
        set_base_color(0xDED7A1, self.bl_label)
        return {'FINISHED'}

class AMS23690(bpy.types.Operator):
    """AMS23690 - Yellow"""
    bl_label = "23690 Yellow"
    bl_idname = 'color.ams_23690'
    def execute(self, context):
        set_base_color(0xE0CEAD, self.bl_label)
        return {'FINISHED'}

class AMS23695(bpy.types.Operator):
    """AMS23695 - Forest Service Sign Standard"""
    bl_label = "23695 Forest Service Sign Standard"
    bl_idname = 'color.ams_23695'
    def execute(self, context):
        set_base_color(0xECC985, self.bl_label)
        return {'FINISHED'}

class AMS23697(bpy.types.Operator):
    """AMS23697 - Sunglow"""
    bl_label = "23697 Sunglow"
    bl_idname = 'color.ams_23697'
    def execute(self, context):
        set_base_color(0xE9CA85, self.bl_label)
        return {'FINISHED'}

class AMS23711(bpy.types.Operator):
    """AMS23711 - Yellow"""
    bl_label = "23711 Yellow"
    bl_idname = 'color.ams_23711'
    def execute(self, context):
        set_base_color(0xE7CEAA, self.bl_label)
        return {'FINISHED'}

class AMS23717(bpy.types.Operator):
    """AMS23717 - Yellow"""
    bl_label = "23717 Yellow"
    bl_idname = 'color.ams_23717'
    def execute(self, context):
        set_base_color(0xE5D2B0, self.bl_label)
        return {'FINISHED'}

class AMS23722(bpy.types.Operator):
    """AMS23722 - Yellow"""
    bl_label = "23722 Yellow"
    bl_idname = 'color.ams_23722'
    def execute(self, context):
        set_base_color(0xE3D0A6, self.bl_label)
        return {'FINISHED'}

class AMS23727(bpy.types.Operator):
    """AMS23727 - Yellow"""
    bl_label = "23727 Yellow"
    bl_idname = 'color.ams_23727'
    def execute(self, context):
        set_base_color(0xE7D5A4, self.bl_label)
        return {'FINISHED'}

class AMS23785(bpy.types.Operator):
    """AMS23785 - Yellow"""
    bl_label = "23785 Yellow"
    bl_idname = 'color.ams_23785'
    def execute(self, context):
        set_base_color(0xE7C753, self.bl_label)
        return {'FINISHED'}

class AMS23793(bpy.types.Operator):
    """AMS23793 - Yellow"""
    bl_label = "23793 Yellow"
    bl_idname = 'color.ams_23793'
    def execute(self, context):
        set_base_color(0xEDDD8C, self.bl_label)
        return {'FINISHED'}

class AMS23814(bpy.types.Operator):
    """AMS23814 - Yellow"""
    bl_label = "23814 Yellow"
    bl_idname = 'color.ams_23814'
    def execute(self, context):
        set_base_color(0xDCDD9D, self.bl_label)
        return {'FINISHED'}

class AMS24052(bpy.types.Operator):
    """AMS24052 - Marine Green #23"""
    bl_label = "24052 Marine Green #23"
    bl_idname = 'color.ams_24052'
    def execute(self, context):
        set_base_color(0x4D4E49, self.bl_label)
        return {'FINISHED'}

class AMS24064(bpy.types.Operator):
    """AMS24064 - Green"""
    bl_label = "24064 Green"
    bl_idname = 'color.ams_24064'
    def execute(self, context):
        set_base_color(0x53524A, self.bl_label)
        return {'FINISHED'}

class AMS24070(bpy.types.Operator):
    """AMS24070 - Army Green 491"""
    bl_label = "24070 Army Green 491"
    bl_idname = 'color.ams_24070'
    def execute(self, context):
        set_base_color(0x4C524F, self.bl_label)
        return {'FINISHED'}

class AMS24079(bpy.types.Operator):
    """AMS24079 - Green"""
    bl_label = "24079 Green"
    bl_idname = 'color.ams_24079'
    def execute(self, context):
        set_base_color(0x54574D, self.bl_label)
        return {'FINISHED'}

class AMS24084(bpy.types.Operator):
    """AMS24084 - Green"""
    bl_label = "24084 Green"
    bl_idname = 'color.ams_24084'
    def execute(self, context):
        set_base_color(0x4A4844, self.bl_label)
        return {'FINISHED'}

class AMS24091(bpy.types.Operator):
    """AMS24091 - Green"""
    bl_label = "24091 Green"
    bl_idname = 'color.ams_24091'
    def execute(self, context):
        set_base_color(0x63605E, self.bl_label)
        return {'FINISHED'}

class AMS24097(bpy.types.Operator):
    """AMS24097 - Green"""
    bl_label = "24097 Green"
    bl_idname = 'color.ams_24097'
    def execute(self, context):
        set_base_color(0x606652, self.bl_label)
        return {'FINISHED'}

class AMS24098(bpy.types.Operator):
    """AMS24098 - Green"""
    bl_label = "24098 Green"
    bl_idname = 'color.ams_24098'
    def execute(self, context):
        set_base_color(0x656249, self.bl_label)
        return {'FINISHED'}

class AMS24108(bpy.types.Operator):
    """AMS24108 - Green"""
    bl_label = "24108 Green"
    bl_idname = 'color.ams_24108'
    def execute(self, context):
        set_base_color(0x4D6959, self.bl_label)
        return {'FINISHED'}

class AMS24111(bpy.types.Operator):
    """AMS24111 - Dark Green 455"""
    bl_label = "24111 Dark Green 455"
    bl_idname = 'color.ams_24111'
    def execute(self, context):
        set_base_color(0x536151, self.bl_label)
        return {'FINISHED'}

class AMS24112(bpy.types.Operator):
    """AMS24112 - Green 474"""
    bl_label = "24112 Green 474"
    bl_idname = 'color.ams_24112'
    def execute(self, context):
        set_base_color(0x556258, self.bl_label)
        return {'FINISHED'}

class AMS24119(bpy.types.Operator):
    """AMS24119 - Marine OG Green"""
    bl_label = "24119 Marine OG Green"
    bl_idname = 'color.ams_24119'
    def execute(self, context):
        set_base_color(0x626555, self.bl_label)
        return {'FINISHED'}

class AMS24148(bpy.types.Operator):
    """AMS24148 - Green"""
    bl_label = "24148 Green"
    bl_idname = 'color.ams_24148'
    def execute(self, context):
        set_base_color(0x647776, self.bl_label)
        return {'FINISHED'}

class AMS24158(bpy.types.Operator):
    """AMS24158 - Green"""
    bl_label = "24158 Green"
    bl_idname = 'color.ams_24158'
    def execute(self, context):
        set_base_color(0x6B7875, self.bl_label)
        return {'FINISHED'}

class AMS24159(bpy.types.Operator):
    """AMS24159 - Green"""
    bl_label = "24159 Green"
    bl_idname = 'color.ams_24159'
    def execute(self, context):
        set_base_color(0x747B70, self.bl_label)
        return {'FINISHED'}

class AMS24165(bpy.types.Operator):
    """AMS24165 - Foliage Green 502/504"""
    bl_label = "24165 Foliage Green 502/504"
    bl_idname = 'color.ams_24165'
    def execute(self, context):
        set_base_color(0x6E716B, self.bl_label)
        return {'FINISHED'}

class AMS24172a(bpy.types.Operator):
    """AMS24172a - MIL-P-24441 Primer"""
    bl_label = "24172a MIL-P-24441 Primer"
    bl_idname = 'color.ams_24172a'
    def execute(self, context):
        set_base_color(0x76997C, self.bl_label)
        return {'FINISHED'}

class AMS24172b(bpy.types.Operator):
    """AMS24172b - Green"""
    bl_label = "24172b Green"
    bl_idname = 'color.ams_24172b'
    def execute(self, context):
        set_base_color(0x6C7B6A, self.bl_label)
        return {'FINISHED'}

class AMS24190(bpy.types.Operator):
    """AMS24190 - Green"""
    bl_label = "24190 Green"
    bl_idname = 'color.ams_24190'
    def execute(self, context):
        set_base_color(0x4A9D56, self.bl_label)
        return {'FINISHED'}

class AMS24201(bpy.types.Operator):
    """AMS24201 - Green"""
    bl_label = "24201 Green"
    bl_idname = 'color.ams_24201'
    def execute(self, context):
        set_base_color(0x88806C, self.bl_label)
        return {'FINISHED'}

class AMS24210(bpy.types.Operator):
    """AMS24210 - Light Green 354"""
    bl_label = "24210 Light Green 354"
    bl_idname = 'color.ams_24210'
    def execute(self, context):
        set_base_color(0x80765F, self.bl_label)
        return {'FINISHED'}

class AMS24226(bpy.types.Operator):
    """AMS24226 - Green"""
    bl_label = "24226 Green"
    bl_idname = 'color.ams_24226'
    def execute(self, context):
        set_base_color(0x7F8B7C, self.bl_label)
        return {'FINISHED'}

class AMS24227(bpy.types.Operator):
    """AMS24227 - Green"""
    bl_label = "24227 Green"
    bl_idname = 'color.ams_24227'
    def execute(self, context):
        set_base_color(0x7A8B70, self.bl_label)
        return {'FINISHED'}

class AMS24233(bpy.types.Operator):
    """AMS24233 - Green"""
    bl_label = "24233 Green"
    bl_idname = 'color.ams_24233'
    def execute(self, context):
        set_base_color(0x80928E, self.bl_label)
        return {'FINISHED'}

class AMS24241(bpy.types.Operator):
    """AMS24241 - Green"""
    bl_label = "24241 Green"
    bl_idname = 'color.ams_24241'
    def execute(self, context):
        set_base_color(0x829D92, self.bl_label)
        return {'FINISHED'}

class AMS24260(bpy.types.Operator):
    """AMS24260 - Green"""
    bl_label = "24260 Green"
    bl_idname = 'color.ams_24260'
    def execute(self, context):
        set_base_color(0x65987A, self.bl_label)
        return {'FINISHED'}

class AMS24277(bpy.types.Operator):
    """AMS24277 - Green"""
    bl_label = "24277 Green"
    bl_idname = 'color.ams_24277'
    def execute(self, context):
        set_base_color(0x879A93, self.bl_label)
        return {'FINISHED'}

class AMS24300(bpy.types.Operator):
    """AMS24300 - Green"""
    bl_label = "24300 Green"
    bl_idname = 'color.ams_24300'
    def execute(self, context):
        set_base_color(0x859C8E, self.bl_label)
        return {'FINISHED'}

class AMS24325(bpy.types.Operator):
    """AMS24325 - Green"""
    bl_label = "24325 Green"
    bl_idname = 'color.ams_24325'
    def execute(self, context):
        set_base_color(0x7FA695, self.bl_label)
        return {'FINISHED'}

class AMS24373(bpy.types.Operator):
    """AMS24373 - Green"""
    bl_label = "24373 Green"
    bl_idname = 'color.ams_24373'
    def execute(self, context):
        set_base_color(0x9AA991, self.bl_label)
        return {'FINISHED'}

class AMS24410(bpy.types.Operator):
    """AMS24410 - Green"""
    bl_label = "24410 Green"
    bl_idname = 'color.ams_24410'
    def execute(self, context):
        set_base_color(0xA0B0A1, self.bl_label)
        return {'FINISHED'}

class AMS24417(bpy.types.Operator):
    """AMS24417 - Green"""
    bl_label = "24417 Green"
    bl_idname = 'color.ams_24417'
    def execute(self, context):
        set_base_color(0xA9B29E, self.bl_label)
        return {'FINISHED'}

class AMS24424(bpy.types.Operator):
    """AMS24424 - Green"""
    bl_label = "24424 Green"
    bl_idname = 'color.ams_24424'
    def execute(self, context):
        set_base_color(0xAAAE97, self.bl_label)
        return {'FINISHED'}

class AMS24432(bpy.types.Operator):
    """AMS24432 - Green"""
    bl_label = "24432 Green"
    bl_idname = 'color.ams_24432'
    def execute(self, context):
        set_base_color(0xA7AF9E, self.bl_label)
        return {'FINISHED'}

class AMS24441(bpy.types.Operator):
    """AMS24441 - Green"""
    bl_label = "24441 Green"
    bl_idname = 'color.ams_24441'
    def execute(self, context):
        set_base_color(0xA7B39A, self.bl_label)
        return {'FINISHED'}

class AMS24449(bpy.types.Operator):
    """AMS24449 - Green"""
    bl_label = "24449 Green"
    bl_idname = 'color.ams_24449'
    def execute(self, context):
        set_base_color(0xA1B596, self.bl_label)
        return {'FINISHED'}

class AMS24466(bpy.types.Operator):
    """AMS24466 - Green"""
    bl_label = "24466 Green"
    bl_idname = 'color.ams_24466'
    def execute(self, context):
        set_base_color(0xA2B79F, self.bl_label)
        return {'FINISHED'}

class AMS24491(bpy.types.Operator):
    """AMS24491 - Green"""
    bl_label = "24491 Green"
    bl_idname = 'color.ams_24491'
    def execute(self, context):
        set_base_color(0xA6BCA7, self.bl_label)
        return {'FINISHED'}

class AMS24504(bpy.types.Operator):
    """AMS24504 - Green"""
    bl_label = "24504 Green"
    bl_idname = 'color.ams_24504'
    def execute(self, context):
        set_base_color(0xACBBA3, self.bl_label)
        return {'FINISHED'}

class AMS24516(bpy.types.Operator):
    """AMS24516 - Clipper Blue"""
    bl_label = "24516 Clipper Blue"
    bl_idname = 'color.ams_24516'
    def execute(self, context):
        set_base_color(0xB2C4B2, self.bl_label)
        return {'FINISHED'}

class AMS24518(bpy.types.Operator):
    """AMS24518 - Green"""
    bl_label = "24518 Green"
    bl_idname = 'color.ams_24518'
    def execute(self, context):
        set_base_color(0xAAB9A6, self.bl_label)
        return {'FINISHED'}

class AMS24525(bpy.types.Operator):
    """AMS24525 - Green"""
    bl_label = "24525 Green"
    bl_idname = 'color.ams_24525'
    def execute(self, context):
        set_base_color(0xB1BFA6, self.bl_label)
        return {'FINISHED'}

class AMS24533(bpy.types.Operator):
    """AMS24533 - Seafoam Green"""
    bl_label = "24533 Seafoam Green"
    bl_idname = 'color.ams_24533'
    def execute(self, context):
        set_base_color(0xADBA96, self.bl_label)
        return {'FINISHED'}

class AMS24552(bpy.types.Operator):
    """AMS24552 - Green"""
    bl_label = "24552 Green"
    bl_idname = 'color.ams_24552'
    def execute(self, context):
        set_base_color(0xC6C286, self.bl_label)
        return {'FINISHED'}

class AMS24554(bpy.types.Operator):
    """AMS24554 - Green"""
    bl_label = "24554 Green"
    bl_idname = 'color.ams_24554'
    def execute(self, context):
        set_base_color(0xCDCEB2, self.bl_label)
        return {'FINISHED'}

class AMS24558(bpy.types.Operator):
    """AMS24558 - Green"""
    bl_label = "24558 Green"
    bl_idname = 'color.ams_24558'
    def execute(self, context):
        set_base_color(0xB6C7A9, self.bl_label)
        return {'FINISHED'}

class AMS24583(bpy.types.Operator):
    """AMS24583 - Green"""
    bl_label = "24583 Green"
    bl_idname = 'color.ams_24583'
    def execute(self, context):
        set_base_color(0xB8BDA1, self.bl_label)
        return {'FINISHED'}

class AMS24585(bpy.types.Operator):
    """AMS24585 - Postal Green"""
    bl_label = "24585 Postal Green"
    bl_idname = 'color.ams_24585'
    def execute(self, context):
        set_base_color(0xC3DBBF, self.bl_label)
        return {'FINISHED'}

class AMS24664(bpy.types.Operator):
    """AMS24664 - Green"""
    bl_label = "24664 Green"
    bl_idname = 'color.ams_24664'
    def execute(self, context):
        set_base_color(0xBDD3BA, self.bl_label)
        return {'FINISHED'}

class AMS24670(bpy.types.Operator):
    """AMS24670 - Green"""
    bl_label = "24670 Green"
    bl_idname = 'color.ams_24670'
    def execute(self, context):
        set_base_color(0xC9D6C3, self.bl_label)
        return {'FINISHED'}

class AMS24672(bpy.types.Operator):
    """AMS24672 - Green"""
    bl_label = "24672 Green"
    bl_idname = 'color.ams_24672'
    def execute(self, context):
        set_base_color(0xCCD5B9, self.bl_label)
        return {'FINISHED'}

class AMS25042(bpy.types.Operator):
    """AMS25042 - Blue Sea / ANA 606"""
    bl_label = "25042 Blue Sea / ANA 606"
    bl_idname = 'color.ams_25042'
    def execute(self, context):
        set_base_color(0x43484D, self.bl_label)
        return {'FINISHED'}

class AMS25044(bpy.types.Operator):
    """AMS25044 - RCAF Blue 25044"""
    bl_label = "25044 RCAF Blue 25044"
    bl_idname = 'color.ams_25044'
    def execute(self, context):
        set_base_color(0x40444D, self.bl_label)
        return {'FINISHED'}

class AMS25045(bpy.types.Operator):
    """AMS25045 - Blue"""
    bl_label = "25045 Blue"
    bl_idname = 'color.ams_25045'
    def execute(self, context):
        set_base_color(0x3E4B53, self.bl_label)
        return {'FINISHED'}

class AMS25048(bpy.types.Operator):
    """AMS25048 - Blue"""
    bl_label = "25048 Blue"
    bl_idname = 'color.ams_25048'
    def execute(self, context):
        set_base_color(0x3D4A5E, self.bl_label)
        return {'FINISHED'}

class AMS25049(bpy.types.Operator):
    """AMS25049 - Army Blue 450"""
    bl_label = "25049 Army Blue 450"
    bl_idname = 'color.ams_25049'
    def execute(self, context):
        set_base_color(0x444649, self.bl_label)
        return {'FINISHED'}

class AMS25051(bpy.types.Operator):
    """AMS25051 - Blue"""
    bl_label = "25051 Blue"
    bl_idname = 'color.ams_25051'
    def execute(self, context):
        set_base_color(0x4F5666, self.bl_label)
        return {'FINISHED'}

class AMS25052(bpy.types.Operator):
    """AMS25052 - Blue"""
    bl_label = "25052 Blue"
    bl_idname = 'color.ams_25052'
    def execute(self, context):
        set_base_color(0x3C5270, self.bl_label)
        return {'FINISHED'}

class AMS25053(bpy.types.Operator):
    """AMS25053 - Royal Blue"""
    bl_label = "25053 Royal Blue"
    bl_idname = 'color.ams_25053'
    def execute(self, context):
        set_base_color(0x465469, self.bl_label)
        return {'FINISHED'}

class AMS25056(bpy.types.Operator):
    """AMS25056 - Blue"""
    bl_label = "25056 Blue"
    bl_idname = 'color.ams_25056'
    def execute(self, context):
        set_base_color(0x3D486D, self.bl_label)
        return {'FINISHED'}

class AMS25060(bpy.types.Operator):
    """AMS25060 - Army Blue 451"""
    bl_label = "25060 Army Blue 451"
    bl_idname = 'color.ams_25060'
    def execute(self, context):
        set_base_color(0x444E5F, self.bl_label)
        return {'FINISHED'}

class AMS25095(bpy.types.Operator):
    """AMS25095 - Blue"""
    bl_label = "25095 Blue"
    bl_idname = 'color.ams_25095'
    def execute(self, context):
        set_base_color(0x3D6CA6, self.bl_label)
        return {'FINISHED'}

class AMS25102(bpy.types.Operator):
    """AMS25102 - Blue"""
    bl_label = "25102 Blue"
    bl_idname = 'color.ams_25102'
    def execute(self, context):
        set_base_color(0x3C6990, self.bl_label)
        return {'FINISHED'}

class AMS25109(bpy.types.Operator):
    """AMS25109 - Blue"""
    bl_label = "25109 Blue"
    bl_idname = 'color.ams_25109'
    def execute(self, context):
        set_base_color(0x557183, self.bl_label)
        return {'FINISHED'}

class AMS25177(bpy.types.Operator):
    """AMS25177 - Blue"""
    bl_label = "25177 Blue"
    bl_idname = 'color.ams_25177'
    def execute(self, context):
        set_base_color(0x638194, self.bl_label)
        return {'FINISHED'}

class AMS25183(bpy.types.Operator):
    """AMS25183 - Blue"""
    bl_label = "25183 Blue"
    bl_idname = 'color.ams_25183'
    def execute(self, context):
        set_base_color(0x4083AE, self.bl_label)
        return {'FINISHED'}

class AMS25184(bpy.types.Operator):
    """AMS25184 - Blue"""
    bl_label = "25184 Blue"
    bl_idname = 'color.ams_25184'
    def execute(self, context):
        set_base_color(0x588496, self.bl_label)
        return {'FINISHED'}

class AMS25185(bpy.types.Operator):
    """AMS25185 - Blue"""
    bl_label = "25185 Blue"
    bl_idname = 'color.ams_25185'
    def execute(self, context):
        set_base_color(0x3D87A0, self.bl_label)
        return {'FINISHED'}

class AMS25189(bpy.types.Operator):
    """AMS25189 - Blue"""
    bl_label = "25189 Blue"
    bl_idname = 'color.ams_25189'
    def execute(self, context):
        set_base_color(0x70878E, self.bl_label)
        return {'FINISHED'}

class AMS25190(bpy.types.Operator):
    """AMS25190 - Blue"""
    bl_label = "25190 Blue"
    bl_idname = 'color.ams_25190'
    def execute(self, context):
        set_base_color(0x638DA0, self.bl_label)
        return {'FINISHED'}

class AMS25193(bpy.types.Operator):
    """AMS25193 - Blue"""
    bl_label = "25193 Blue"
    bl_idname = 'color.ams_25193'
    def execute(self, context):
        set_base_color(0x5B8A8F, self.bl_label)
        return {'FINISHED'}

class AMS25200(bpy.types.Operator):
    """AMS25200 - Blue"""
    bl_label = "25200 Blue"
    bl_idname = 'color.ams_25200'
    def execute(self, context):
        set_base_color(0x5BB7CC, self.bl_label)
        return {'FINISHED'}

class AMS25230(bpy.types.Operator):
    """AMS25230 - Electrical Blue"""
    bl_label = "25230 Electrical Blue"
    bl_idname = 'color.ams_25230'
    def execute(self, context):
        set_base_color(0x5490C5, self.bl_label)
        return {'FINISHED'}

class AMS25237(bpy.types.Operator):
    """AMS25237 - Blue"""
    bl_label = "25237 Blue"
    bl_idname = 'color.ams_25237'
    def execute(self, context):
        set_base_color(0x7E8A90, self.bl_label)
        return {'FINISHED'}

class AMS25240(bpy.types.Operator):
    """AMS25240 - Blue"""
    bl_label = "25240 Blue"
    bl_idname = 'color.ams_25240'
    def execute(self, context):
        set_base_color(0x7C96B4, self.bl_label)
        return {'FINISHED'}

class AMS25299(bpy.types.Operator):
    """AMS25299 - Blue"""
    bl_label = "25299 Blue"
    bl_idname = 'color.ams_25299'
    def execute(self, context):
        set_base_color(0x76A19B, self.bl_label)
        return {'FINISHED'}

class AMS25352(bpy.types.Operator):
    """AMS25352 - Blue"""
    bl_label = "25352 Blue"
    bl_idname = 'color.ams_25352'
    def execute(self, context):
        set_base_color(0x8AA19D, self.bl_label)
        return {'FINISHED'}

class AMS25414(bpy.types.Operator):
    """AMS25414 - Blue"""
    bl_label = "25414 Blue"
    bl_idname = 'color.ams_25414'
    def execute(self, context):
        set_base_color(0x90AAA8, self.bl_label)
        return {'FINISHED'}

class AMS25440(bpy.types.Operator):
    """AMS25440 - Admiral Blue"""
    bl_label = "25440 Admiral Blue"
    bl_idname = 'color.ams_25440'
    def execute(self, context):
        set_base_color(0x86AFC7, self.bl_label)
        return {'FINISHED'}

class AMS25488(bpy.types.Operator):
    """AMS25488 - Blue"""
    bl_label = "25488 Blue"
    bl_idname = 'color.ams_25488'
    def execute(self, context):
        set_base_color(0x9BBAD0, self.bl_label)
        return {'FINISHED'}

class AMS25526(bpy.types.Operator):
    """AMS25526 - Pastel Blue"""
    bl_label = "25526 Pastel Blue"
    bl_idname = 'color.ams_25526'
    def execute(self, context):
        set_base_color(0xC4C3B7, self.bl_label)
        return {'FINISHED'}

class AMS25530(bpy.types.Operator):
    """AMS25530 - Carl Vinson Blue"""
    bl_label = "25530 Carl Vinson Blue"
    bl_idname = 'color.ams_25530'
    def execute(self, context):
        set_base_color(0xB6C4C4, self.bl_label)
        return {'FINISHED'}

class AMS25550(bpy.types.Operator):
    """AMS25550 - Blue"""
    bl_label = "25550 Blue"
    bl_idname = 'color.ams_25550'
    def execute(self, context):
        set_base_color(0xC7D8DA, self.bl_label)
        return {'FINISHED'}

class AMS25622(bpy.types.Operator):
    """AMS25622 - Blue"""
    bl_label = "25622 Blue"
    bl_idname = 'color.ams_25622'
    def execute(self, context):
        set_base_color(0xC8D3C9, self.bl_label)
        return {'FINISHED'}

class AMS25630(bpy.types.Operator):
    """AMS25630 - Blue"""
    bl_label = "25630 Blue"
    bl_idname = 'color.ams_25630'
    def execute(self, context):
        set_base_color(0xD4D4CD, self.bl_label)
        return {'FINISHED'}

class AMS26008(bpy.types.Operator):
    """AMS26008 - Exterior Deck Gray"""
    bl_label = "26008 Exterior Deck Gray"
    bl_idname = 'color.ams_26008'
    def execute(self, context):
        set_base_color(0x575B5F, self.bl_label)
        return {'FINISHED'}

class AMS26044(bpy.types.Operator):
    """AMS26044 - Gray"""
    bl_label = "26044 Gray"
    bl_idname = 'color.ams_26044'
    def execute(self, context):
        set_base_color(0x494E53, self.bl_label)
        return {'FINISHED'}

class AMS26081(bpy.types.Operator):
    """AMS26081 - Sea Plane Gray / ANA 625"""
    bl_label = "26081 Sea Plane Gray / ANA 625"
    bl_idname = 'color.ams_26081'
    def execute(self, context):
        set_base_color(0x585B5B, self.bl_label)
        return {'FINISHED'}

class AMS26099(bpy.types.Operator):
    """AMS26099 - Gray"""
    bl_label = "26099 Gray"
    bl_idname = 'color.ams_26099'
    def execute(self, context):
        set_base_color(0x5B6267, self.bl_label)
        return {'FINISHED'}

class AMS26118(bpy.types.Operator):
    """AMS26118 - Gray"""
    bl_label = "26118 Gray"
    bl_idname = 'color.ams_26118'
    def execute(self, context):
        set_base_color(0x5E646B, self.bl_label)
        return {'FINISHED'}

class AMS26120(bpy.types.Operator):
    """AMS26120 - Gray"""
    bl_label = "26120 Gray"
    bl_idname = 'color.ams_26120'
    def execute(self, context):
        set_base_color(0x615853, self.bl_label)
        return {'FINISHED'}

class AMS26122(bpy.types.Operator):
    """AMS26122 - Gray"""
    bl_label = "26122 Gray"
    bl_idname = 'color.ams_26122'
    def execute(self, context):
        set_base_color(0x6B6968, self.bl_label)
        return {'FINISHED'}

class AMS26132(bpy.types.Operator):
    """AMS26132 - Slate Gray"""
    bl_label = "26132 Slate Gray"
    bl_idname = 'color.ams_26132'
    def execute(self, context):
        set_base_color(0x6D6F72, self.bl_label)
        return {'FINISHED'}

class AMS26134(bpy.types.Operator):
    """AMS26134 - Gray / Filing Cabinet"""
    bl_label = "26134 Gray / Filing Cabinet"
    bl_idname = 'color.ams_26134'
    def execute(self, context):
        set_base_color(0x70716E, self.bl_label)
        return {'FINISHED'}

class AMS26152(bpy.types.Operator):
    """AMS26152 - Gray"""
    bl_label = "26152 Gray"
    bl_idname = 'color.ams_26152'
    def execute(self, context):
        set_base_color(0x707577, self.bl_label)
        return {'FINISHED'}

class AMS26173(bpy.types.Operator):
    """AMS26173 - Ocean Gray / NAVSEA"""
    bl_label = "26173 Ocean Gray / NAVSEA"
    bl_idname = 'color.ams_26173'
    def execute(self, context):
        set_base_color(0x7B8187, self.bl_label)
        return {'FINISHED'}

class AMS26176(bpy.types.Operator):
    """AMS26176 - Ocean Gray"""
    bl_label = "26176 Ocean Gray"
    bl_idname = 'color.ams_26176'
    def execute(self, context):
        set_base_color(0x777F88, self.bl_label)
        return {'FINISHED'}

class AMS26187(bpy.types.Operator):
    """AMS26187 - Gray"""
    bl_label = "26187 Gray"
    bl_idname = 'color.ams_26187'
    def execute(self, context):
        set_base_color(0x767D7E, self.bl_label)
        return {'FINISHED'}

class AMS26231(bpy.types.Operator):
    """AMS26231 - Gray"""
    bl_label = "26231 Gray"
    bl_idname = 'color.ams_26231'
    def execute(self, context):
        set_base_color(0x848889, self.bl_label)
        return {'FINISHED'}

class AMS26250(bpy.types.Operator):
    """AMS26250 - Gray"""
    bl_label = "26250 Gray"
    bl_idname = 'color.ams_26250'
    def execute(self, context):
        set_base_color(0x858C8B, self.bl_label)
        return {'FINISHED'}

class AMS26251(bpy.types.Operator):
    """AMS26251 - Gray"""
    bl_label = "26251 Gray"
    bl_idname = 'color.ams_26251'
    def execute(self, context):
        set_base_color(0x888B8B, self.bl_label)
        return {'FINISHED'}

class AMS26255(bpy.types.Operator):
    """AMS26255 - Dark Gray 509"""
    bl_label = "26255 Dark Gray 509"
    bl_idname = 'color.ams_26255'
    def execute(self, context):
        set_base_color(0x818588, self.bl_label)
        return {'FINISHED'}

class AMS26260(bpy.types.Operator):
    """AMS26260 - Urban Gray 501/505"""
    bl_label = "26260 Urban Gray 501/505"
    bl_idname = 'color.ams_26260'
    def execute(self, context):
        set_base_color(0x8A8A81, self.bl_label)
        return {'FINISHED'}

class AMS26270(bpy.types.Operator):
    """AMS26270 - Interior Haze Gray"""
    bl_label = "26270 Interior Haze Gray"
    bl_idname = 'color.ams_26270'
    def execute(self, context):
        set_base_color(0x898F91, self.bl_label)
        return {'FINISHED'}

class AMS26280(bpy.types.Operator):
    """AMS26280 - Gray"""
    bl_label = "26280 Gray"
    bl_idname = 'color.ams_26280'
    def execute(self, context):
        set_base_color(0x8F938F, self.bl_label)
        return {'FINISHED'}

class AMS26290(bpy.types.Operator):
    """AMS26290 - Gray"""
    bl_label = "26290 Gray"
    bl_idname = 'color.ams_26290'
    def execute(self, context):
        set_base_color(0x8E9292, self.bl_label)
        return {'FINISHED'}

class AMS26293(bpy.types.Operator):
    """AMS26293 - Gray"""
    bl_label = "26293 Gray"
    bl_idname = 'color.ams_26293'
    def execute(self, context):
        set_base_color(0x8F9595, self.bl_label)
        return {'FINISHED'}

class AMS26295(bpy.types.Operator):
    """AMS26295 - Gray 510"""
    bl_label = "26295 Gray 510"
    bl_idname = 'color.ams_26295'
    def execute(self, context):
        set_base_color(0xA2A3A7, self.bl_label)
        return {'FINISHED'}

class AMS26306(bpy.types.Operator):
    """AMS26306 - Sand Gray"""
    bl_label = "26306 Sand Gray"
    bl_idname = 'color.ams_26306'
    def execute(self, context):
        set_base_color(0x9B938A, self.bl_label)
        return {'FINISHED'}

class AMS26307(bpy.types.Operator):
    """AMS26307 - Bulkhead Machinery Gray #30"""
    bl_label = "26307 Bulkhead Machinery Gray #30"
    bl_idname = 'color.ams_26307'
    def execute(self, context):
        set_base_color(0x94968D, self.bl_label)
        return {'FINISHED'}

class AMS26314(bpy.types.Operator):
    """AMS26314 - Gray"""
    bl_label = "26314 Gray"
    bl_idname = 'color.ams_26314'
    def execute(self, context):
        set_base_color(0x949996, self.bl_label)
        return {'FINISHED'}

class AMS26329(bpy.types.Operator):
    """AMS26329 - Gray"""
    bl_label = "26329 Gray"
    bl_idname = 'color.ams_26329'
    def execute(self, context):
        set_base_color(0x919F9F, self.bl_label)
        return {'FINISHED'}

class AMS26357(bpy.types.Operator):
    """AMS26357 - Gray"""
    bl_label = "26357 Gray"
    bl_idname = 'color.ams_26357'
    def execute(self, context):
        set_base_color(0xA4A295, self.bl_label)
        return {'FINISHED'}

class AMS26360(bpy.types.Operator):
    """AMS26360 - Gray"""
    bl_label = "26360 Gray"
    bl_idname = 'color.ams_26360'
    def execute(self, context):
        set_base_color(0xAEA996, self.bl_label)
        return {'FINISHED'}

class AMS26373(bpy.types.Operator):
    """AMS26373 - Light Gray #37"""
    bl_label = "26373 Light Gray #37"
    bl_idname = 'color.ams_26373'
    def execute(self, context):
        set_base_color(0xA4A9A8, self.bl_label)
        return {'FINISHED'}

class AMS26380(bpy.types.Operator):
    """AMS26380 - Medium Gray 508"""
    bl_label = "26380 Medium Gray 508"
    bl_idname = 'color.ams_26380'
    def execute(self, context):
        set_base_color(0xA3A9AC, self.bl_label)
        return {'FINISHED'}

class AMS26400(bpy.types.Operator):
    """AMS26400 - Yellow Gray"""
    bl_label = "26400 Yellow Gray"
    bl_idname = 'color.ams_26400'
    def execute(self, context):
        set_base_color(0xCBC2A9, self.bl_label)
        return {'FINISHED'}

class AMS26405(bpy.types.Operator):
    """AMS26405 - Gray"""
    bl_label = "26405 Gray"
    bl_idname = 'color.ams_26405'
    def execute(self, context):
        set_base_color(0xBFB7A2, self.bl_label)
        return {'FINISHED'}

class AMS26408(bpy.types.Operator):
    """AMS26408 - Gray"""
    bl_label = "26408 Gray"
    bl_idname = 'color.ams_26408'
    def execute(self, context):
        set_base_color(0xBCBBAD, self.bl_label)
        return {'FINISHED'}

class AMS26420(bpy.types.Operator):
    """AMS26420 - DLA Light Blue/Gray"""
    bl_label = "26420 DLA Light Blue/Gray"
    bl_idname = 'color.ams_26420'
    def execute(self, context):
        set_base_color(0xB4B1AE, self.bl_label)
        return {'FINISHED'}

class AMS26424(bpy.types.Operator):
    """AMS26424 - Gray"""
    bl_label = "26424 Gray"
    bl_idname = 'color.ams_26424'
    def execute(self, context):
        set_base_color(0xBEB6AC, self.bl_label)
        return {'FINISHED'}

class AMS26440(bpy.types.Operator):
    """AMS26440 - Gray"""
    bl_label = "26440 Gray"
    bl_idname = 'color.ams_26440'
    def execute(self, context):
        set_base_color(0xB4B4AB, self.bl_label)
        return {'FINISHED'}

class AMS26480(bpy.types.Operator):
    """AMS26480 - Canada 501-109"""
    bl_label = "26480 Canada 501-109"
    bl_idname = 'color.ams_26480'
    def execute(self, context):
        set_base_color(0xAFBBB5, self.bl_label)
        return {'FINISHED'}

class AMS26492(bpy.types.Operator):
    """AMS26492 - Gray"""
    bl_label = "26492 Gray"
    bl_idname = 'color.ams_26492'
    def execute(self, context):
        set_base_color(0xBCBCB6, self.bl_label)
        return {'FINISHED'}

class AMS26493(bpy.types.Operator):
    """AMS26493 - Pearl Gray"""
    bl_label = "26493 Pearl Gray"
    bl_idname = 'color.ams_26493'
    def execute(self, context):
        set_base_color(0xB9BCBA, self.bl_label)
        return {'FINISHED'}

class AMS26496(bpy.types.Operator):
    """AMS26496 - Green Gray"""
    bl_label = "26496 Green Gray"
    bl_idname = 'color.ams_26496'
    def execute(self, context):
        set_base_color(0xB1B2A7, self.bl_label)
        return {'FINISHED'}

class AMS26521(bpy.types.Operator):
    """AMS26521 - Gray"""
    bl_label = "26521 Gray"
    bl_idname = 'color.ams_26521'
    def execute(self, context):
        set_base_color(0xC4B9AC, self.bl_label)
        return {'FINISHED'}

class AMS26555(bpy.types.Operator):
    """AMS26555 - Gray"""
    bl_label = "26555 Gray"
    bl_idname = 'color.ams_26555'
    def execute(self, context):
        set_base_color(0xC8BEA2, self.bl_label)
        return {'FINISHED'}

class AMS26559(bpy.types.Operator):
    """AMS26559 - Parchment"""
    bl_label = "26559 Parchment"
    bl_idname = 'color.ams_26559'
    def execute(self, context):
        set_base_color(0xC1BFB0, self.bl_label)
        return {'FINISHED'}

class AMS26586(bpy.types.Operator):
    """AMS26586 - Gray"""
    bl_label = "26586 Gray"
    bl_idname = 'color.ams_26586'
    def execute(self, context):
        set_base_color(0xCBC3AA, self.bl_label)
        return {'FINISHED'}

class AMS26595(bpy.types.Operator):
    """AMS26595 - Gray"""
    bl_label = "26595 Gray"
    bl_idname = 'color.ams_26595'
    def execute(self, context):
        set_base_color(0xC2C2B3, self.bl_label)
        return {'FINISHED'}

class AMS26622(bpy.types.Operator):
    """AMS26622 - Gray"""
    bl_label = "26622 Gray"
    bl_idname = 'color.ams_26622'
    def execute(self, context):
        set_base_color(0xC5C3B8, self.bl_label)
        return {'FINISHED'}

class AMS26630(bpy.types.Operator):
    """AMS26630 - Light Gray 507"""
    bl_label = "26630 Light Gray 507"
    bl_idname = 'color.ams_26630'
    def execute(self, context):
        set_base_color(0xCED0CC, self.bl_label)
        return {'FINISHED'}

class AMS27038(bpy.types.Operator):
    """AMS27038 - ANA 514"""
    bl_label = "27038 ANA 514"
    bl_idname = 'color.ams_27038'
    def execute(self, context):
        set_base_color(0x3D3D3E, self.bl_label)
        return {'FINISHED'}

class AMS27040(bpy.types.Operator):
    """AMS27040 - Filing Cabinet Black"""
    bl_label = "27040 Filing Cabinet Black"
    bl_idname = 'color.ams_27040'
    def execute(self, context):
        set_base_color(0x424345, self.bl_label)
        return {'FINISHED'}

class AMS27041(bpy.types.Operator):
    """AMS27041 - Black"""
    bl_label = "27041 Black"
    bl_idname = 'color.ams_27041'
    def execute(self, context):
        set_base_color(0x424345, self.bl_label)
        return {'FINISHED'}

class AMS27043(bpy.types.Operator):
    """AMS27043 - Gold"""
    bl_label = "27043 Gold"
    bl_idname = 'color.ams_27043'
    def execute(self, context):
        set_base_color(0xB69E6A, self.bl_label)
        return {'FINISHED'}

class AMS27142(bpy.types.Operator):
    """AMS27142 - Misc Purple"""
    bl_label = "27142 Misc Purple"
    bl_idname = 'color.ams_27142'
    def execute(self, context):
        set_base_color(0x955F84, self.bl_label)
        return {'FINISHED'}

class AMS27144(bpy.types.Operator):
    """AMS27144 - Misc Purple"""
    bl_label = "27144 Misc Purple"
    bl_idname = 'color.ams_27144'
    def execute(self, context):
        set_base_color(0x836B8A, self.bl_label)
        return {'FINISHED'}

class AMS27160(bpy.types.Operator):
    """AMS27160 - Misc Purple"""
    bl_label = "27160 Misc Purple"
    bl_idname = 'color.ams_27160'
    def execute(self, context):
        set_base_color(0x9382B9, self.bl_label)
        return {'FINISHED'}

class AMS27722(bpy.types.Operator):
    """AMS27722 - Misc White"""
    bl_label = "27722 Misc White"
    bl_idname = 'color.ams_27722'
    def execute(self, context):
        set_base_color(0xDCD9CC, self.bl_label)
        return {'FINISHED'}

class AMS27769(bpy.types.Operator):
    """AMS27769 - Parchment"""
    bl_label = "27769 Parchment"
    bl_idname = 'color.ams_27769'
    def execute(self, context):
        set_base_color(0xDED3BB, self.bl_label)
        return {'FINISHED'}

class AMS27778(bpy.types.Operator):
    """AMS27778 - Candlelight"""
    bl_label = "27778 Candlelight"
    bl_idname = 'color.ams_27778'
    def execute(self, context):
        set_base_color(0xEAE3CA, self.bl_label)
        return {'FINISHED'}

class AMS27780(bpy.types.Operator):
    """AMS27780 - Misc White"""
    bl_label = "27780 Misc White"
    bl_idname = 'color.ams_27780'
    def execute(self, context):
        set_base_color(0xEAE4D2, self.bl_label)
        return {'FINISHED'}

class AMS27855(bpy.types.Operator):
    """AMS27855 - Misc Yellow White"""
    bl_label = "27855 Misc Yellow White"
    bl_idname = 'color.ams_27855'
    def execute(self, context):
        set_base_color(0xE9DDBB, self.bl_label)
        return {'FINISHED'}

class AMS27875(bpy.types.Operator):
    """AMS27875 - ANA 626"""
    bl_label = "27875 ANA 626"
    bl_idname = 'color.ams_27875'
    def execute(self, context):
        set_base_color(0xE8E9DE, self.bl_label)
        return {'FINISHED'}

class AMS27880(bpy.types.Operator):
    """AMS27880 - Misc White"""
    bl_label = "27880 Misc White"
    bl_idname = 'color.ams_27880'
    def execute(self, context):
        set_base_color(0xF4EEDC, self.bl_label)
        return {'FINISHED'}

class AMS27885(bpy.types.Operator):
    """AMS27885 - White 506"""
    bl_label = "27885 White 506"
    bl_idname = 'color.ams_27885'
    def execute(self, context):
        set_base_color(0xF3F1E7, self.bl_label)
        return {'FINISHED'}

class AMS27886(bpy.types.Operator):
    """AMS27886 - Misc White"""
    bl_label = "27886 Misc White"
    bl_idname = 'color.ams_27886'
    def execute(self, context):
        set_base_color(0xEFEAD9, self.bl_label)
        return {'FINISHED'}

class AMS27925(bpy.types.Operator):
    """AMS27925 - Misc White"""
    bl_label = "27925 Misc White"
    bl_idname = 'color.ams_27925'
    def execute(self, context):
        set_base_color(0xEFF1E7, self.bl_label)
        return {'FINISHED'}

class AMS28913(bpy.types.Operator):
    """AMS28913 - Fluorescent Red"""
    bl_label = "28913 Fluorescent Red"
    bl_idname = 'color.ams_28913'
    def execute(self, context):
        set_base_color(0xF64336, self.bl_label)
        return {'FINISHED'}

class AMS28915(bpy.types.Operator):
    """AMS28915 - Fluorescent Orange"""
    bl_label = "28915 Fluorescent Orange"
    bl_idname = 'color.ams_28915'
    def execute(self, context):
        set_base_color(0xFF5E2D, self.bl_label)
        return {'FINISHED'}

class AMS30037(bpy.types.Operator):
    """AMS30037 - U.S. Army #561 / Bark Brown"""
    bl_label = "30037 U.S. Army #561 / Bark Brown"
    bl_idname = 'color.ams_30037'
    def execute(self, context):
        set_base_color(0x584E4C, self.bl_label)
        return {'FINISHED'}

class AMS30040(bpy.types.Operator):
    """AMS30040 - Brown"""
    bl_label = "30040 Brown"
    bl_idname = 'color.ams_30040'
    def execute(self, context):
        set_base_color(0x514842, self.bl_label)
        return {'FINISHED'}

class AMS30045(bpy.types.Operator):
    """AMS30045 - Brown"""
    bl_label = "30045 Brown"
    bl_idname = 'color.ams_30045'
    def execute(self, context):
        set_base_color(0x5A4B47, self.bl_label)
        return {'FINISHED'}

class AMS30051(bpy.types.Operator):
    """AMS30051 - Brown 383 Camouflage"""
    bl_label = "30051 Brown 383 Camouflage"
    bl_idname = 'color.ams_30051'
    def execute(self, context):
        set_base_color(0x5A4E46, self.bl_label)
        return {'FINISHED'}

class AMS30059(bpy.types.Operator):
    """AMS30059 - Brown"""
    bl_label = "30059 Brown"
    bl_idname = 'color.ams_30059'
    def execute(self, context):
        set_base_color(0x523E37, self.bl_label)
        return {'FINISHED'}

class AMS30063(bpy.types.Operator):
    """AMS30063 - U.S. Army #530 Dark Brown"""
    bl_label = "30063 U.S. Army #530 Dark Brown"
    bl_idname = 'color.ams_30063'
    def execute(self, context):
        set_base_color(0x524844, self.bl_label)
        return {'FINISHED'}

class AMS30097(bpy.types.Operator):
    """AMS30097 - Earth Brown Camo"""
    bl_label = "30097 Earth Brown Camo"
    bl_idname = 'color.ams_30097'
    def execute(self, context):
        set_base_color(0x605143, self.bl_label)
        return {'FINISHED'}

class AMS30098(bpy.types.Operator):
    """AMS30098 - U.S. Army #529 Brown"""
    bl_label = "30098 U.S. Army #529 Brown"
    bl_idname = 'color.ams_30098'
    def execute(self, context):
        set_base_color(0x645241, self.bl_label)
        return {'FINISHED'}

class AMS30099(bpy.types.Operator):
    """AMS30099 - Earth Brown"""
    bl_label = "30099 Earth Brown"
    bl_idname = 'color.ams_30099'
    def execute(self, context):
        set_base_color(0x68584A, self.bl_label)
        return {'FINISHED'}

class AMS30108(bpy.types.Operator):
    """AMS30108 - Walnut Brown"""
    bl_label = "30108 Walnut Brown"
    bl_idname = 'color.ams_30108'
    def execute(self, context):
        set_base_color(0x5D463D, self.bl_label)
        return {'FINISHED'}

class AMS30109(bpy.types.Operator):
    """AMS30109 - Dull Red / ANA 618"""
    bl_label = "30109 Dull Red / ANA 618"
    bl_idname = 'color.ams_30109'
    def execute(self, context):
        set_base_color(0x824D44, self.bl_label)
        return {'FINISHED'}

class AMS30111(bpy.types.Operator):
    """AMS30111 - Maroon Olympic Russet / Park Service Brown"""
    bl_label = "30111 Maroon Olympic Russet / Park Service Brown"
    bl_idname = 'color.ams_30111'
    def execute(self, context):
        set_base_color(0x6F4E47, self.bl_label)
        return {'FINISHED'}

class AMS30117(bpy.types.Operator):
    """AMS30117 - Brown International"""
    bl_label = "30117 Brown International"
    bl_idname = 'color.ams_30117'
    def execute(self, context):
        set_base_color(0x7E5D4D, self.bl_label)
        return {'FINISHED'}

class AMS30118(bpy.types.Operator):
    """AMS30118 - Field Drab Camo / ANA 617"""
    bl_label = "30118 Field Drab Camo / ANA 617"
    bl_idname = 'color.ams_30118'
    def execute(self, context):
        set_base_color(0x6E5C42, self.bl_label)
        return {'FINISHED'}

class AMS30140(bpy.types.Operator):
    """AMS30140 - Brown International"""
    bl_label = "30140 Brown International"
    bl_idname = 'color.ams_30140'
    def execute(self, context):
        set_base_color(0x7A6150, self.bl_label)
        return {'FINISHED'}

class AMS30145(bpy.types.Operator):
    """AMS30145 - Butternut Stain"""
    bl_label = "30145 Butternut Stain"
    bl_idname = 'color.ams_30145'
    def execute(self, context):
        set_base_color(0x7D634B, self.bl_label)
        return {'FINISHED'}

class AMS30160(bpy.types.Operator):
    """AMS30160 - Brown"""
    bl_label = "30160 Brown"
    bl_idname = 'color.ams_30160'
    def execute(self, context):
        set_base_color(0x764650, self.bl_label)
        return {'FINISHED'}

class AMS30166(bpy.types.Operator):
    """AMS30166 - Brown"""
    bl_label = "30166 Brown"
    bl_idname = 'color.ams_30166'
    def execute(self, context):
        set_base_color(0x825047, self.bl_label)
        return {'FINISHED'}

class AMS30169(bpy.types.Operator):
    """AMS30169 - U.S. Army #450 / Tan"""
    bl_label = "30169 U.S. Army #450 / Tan"
    bl_idname = 'color.ams_30169'
    def execute(self, context):
        set_base_color(0x83715E, self.bl_label)
        return {'FINISHED'}

class AMS30206(bpy.types.Operator):
    """AMS30206 - Brown"""
    bl_label = "30206 Brown"
    bl_idname = 'color.ams_30206'
    def execute(self, context):
        set_base_color(0x906F6A, self.bl_label)
        return {'FINISHED'}

class AMS30215(bpy.types.Operator):
    """AMS30215 - Brown"""
    bl_label = "30215 Brown"
    bl_idname = 'color.ams_30215'
    def execute(self, context):
        set_base_color(0x8F674B, self.bl_label)
        return {'FINISHED'}

class AMS30219(bpy.types.Operator):
    """AMS30219 - Sierra Tan / ANA 628"""
    bl_label = "30219 Sierra Tan / ANA 628"
    bl_idname = 'color.ams_30219'
    def execute(self, context):
        set_base_color(0x917561, self.bl_label)
        return {'FINISHED'}

class AMS30227(bpy.types.Operator):
    """AMS30227 - Brown"""
    bl_label = "30227 Brown"
    bl_idname = 'color.ams_30227'
    def execute(self, context):
        set_base_color(0x998070, self.bl_label)
        return {'FINISHED'}

class AMS30233(bpy.types.Operator):
    """AMS30233 - Brown"""
    bl_label = "30233 Brown"
    bl_idname = 'color.ams_30233'
    def execute(self, context):
        set_base_color(0x9D7063, self.bl_label)
        return {'FINISHED'}

class AMS30252(bpy.types.Operator):
    """AMS30252 - Rust Red"""
    bl_label = "30252 Rust Red"
    bl_idname = 'color.ams_30252'
    def execute(self, context):
        set_base_color(0xAE755F, self.bl_label)
        return {'FINISHED'}

class AMS30257(bpy.types.Operator):
    """AMS30257 - Earth Yellow"""
    bl_label = "30257 Earth Yellow"
    bl_idname = 'color.ams_30257'
    def execute(self, context):
        set_base_color(0xB58B5D, self.bl_label)
        return {'FINISHED'}

class AMS30266(bpy.types.Operator):
    """AMS30266 - Tan / ANA 615"""
    bl_label = "30266 Tan / ANA 615"
    bl_idname = 'color.ams_30266'
    def execute(self, context):
        set_base_color(0xA38254, self.bl_label)
        return {'FINISHED'}

class AMS30267(bpy.types.Operator):
    """AMS30267 - U.S. Army #M-1 / Khaki"""
    bl_label = "30267 U.S. Army #M-1 / Khaki"
    bl_idname = 'color.ams_30267'
    def execute(self, context):
        set_base_color(0x988567, self.bl_label)
        return {'FINISHED'}

class AMS30277(bpy.types.Operator):
    """AMS30277 - Sand"""
    bl_label = "30277 Sand"
    bl_idname = 'color.ams_30277'
    def execute(self, context):
        set_base_color(0x9A8B72, self.bl_label)
        return {'FINISHED'}

class AMS30279(bpy.types.Operator):
    """AMS30279 - Desert Sand / ANA 616"""
    bl_label = "30279 Desert Sand / ANA 616"
    bl_idname = 'color.ams_30279'
    def execute(self, context):
        set_base_color(0xAD9281, self.bl_label)
        return {'FINISHED'}

class AMS30313(bpy.types.Operator):
    """AMS30313 - Desert Sand"""
    bl_label = "30313 Desert Sand"
    bl_idname = 'color.ams_30313'
    def execute(self, context):
        set_base_color(0xAA8F81, self.bl_label)
        return {'FINISHED'}

class AMS30315(bpy.types.Operator):
    """AMS30315 - Desert Sand Camo"""
    bl_label = "30315 Desert Sand Camo"
    bl_idname = 'color.ams_30315'
    def execute(self, context):
        set_base_color(0xAC9281, self.bl_label)
        return {'FINISHED'}

class AMS30318(bpy.types.Operator):
    """AMS30318 - Brown"""
    bl_label = "30318 Brown"
    bl_idname = 'color.ams_30318'
    def execute(self, context):
        set_base_color(0xA6967C, self.bl_label)
        return {'FINISHED'}

class AMS30324(bpy.types.Operator):
    """AMS30324 - Desert Sand"""
    bl_label = "30324 Desert Sand"
    bl_idname = 'color.ams_30324'
    def execute(self, context):
        set_base_color(0xA88D7D, self.bl_label)
        return {'FINISHED'}

class AMS30340(bpy.types.Operator):
    """AMS30340 - Tan 380"""
    bl_label = "30340 Tan 380"
    bl_idname = 'color.ams_30340'
    def execute(self, context):
        set_base_color(0xA6927F, self.bl_label)
        return {'FINISHED'}

class AMS30372(bpy.types.Operator):
    """AMS30372 - Brown"""
    bl_label = "30372 Brown"
    bl_idname = 'color.ams_30372'
    def execute(self, context):
        set_base_color(0xA89985, self.bl_label)
        return {'FINISHED'}

class AMS30373(bpy.types.Operator):
    """AMS30373 - U.S. Army #525 / Tan"""
    bl_label = "30373 U.S. Army #525 / Tan"
    bl_idname = 'color.ams_30373'
    def execute(self, context):
        set_base_color(0x9B836E, self.bl_label)
        return {'FINISHED'}

class AMS30450(bpy.types.Operator):
    """AMS30450 - Beige"""
    bl_label = "30450 Beige"
    bl_idname = 'color.ams_30450'
    def execute(self, context):
        set_base_color(0xC2A892, self.bl_label)
        return {'FINISHED'}

class AMS30475(bpy.types.Operator):
    """AMS30475 - Saudi Color #11 (Sang)"""
    bl_label = "30475 Saudi Color #11 (Sang)"
    bl_idname = 'color.ams_30475'
    def execute(self, context):
        set_base_color(0xC6A887, self.bl_label)
        return {'FINISHED'}

class AMS30480(bpy.types.Operator):
    """AMS30480 - Tan 459"""
    bl_label = "30480 Tan 459"
    bl_idname = 'color.ams_30480'
    def execute(self, context):
        set_base_color(0xCAAB8A, self.bl_label)
        return {'FINISHED'}

class AMS31090(bpy.types.Operator):
    """AMS31090 - Earth Red Camo"""
    bl_label = "31090 Earth Red Camo"
    bl_idname = 'color.ams_31090'
    def execute(self, context):
        set_base_color(0x76543C, self.bl_label)
        return {'FINISHED'}

class AMS31100(bpy.types.Operator):
    """AMS31100 - U.S. Army #453 / Maroon"""
    bl_label = "31100 U.S. Army #453 / Maroon"
    bl_idname = 'color.ams_31100'
    def execute(self, context):
        set_base_color(0x5B3C41, self.bl_label)
        return {'FINISHED'}

class AMS31136(bpy.types.Operator):
    """AMS31136 - Red International / CARC Aircraft Red / ANA 619"""
    bl_label = "31136 Red International / CARC Aircraft Red / ANA 619"
    bl_idname = 'color.ams_31136'
    def execute(self, context):
        set_base_color(0x8F403E, self.bl_label)
        return {'FINISHED'}

class AMS31158(bpy.types.Operator):
    """AMS31158 - Light Red International"""
    bl_label = "31158 Light Red International"
    bl_idname = 'color.ams_31158'
    def execute(self, context):
        set_base_color(0xB25761, self.bl_label)
        return {'FINISHED'}

class AMS31302(bpy.types.Operator):
    """AMS31302 - Red"""
    bl_label = "31302 Red"
    bl_idname = 'color.ams_31302'
    def execute(self, context):
        set_base_color(0xBA4740, self.bl_label)
        return {'FINISHED'}

class AMS31310(bpy.types.Operator):
    """AMS31310 - Red"""
    bl_label = "31310 Red"
    bl_idname = 'color.ams_31310'
    def execute(self, context):
        set_base_color(0xB94437, self.bl_label)
        return {'FINISHED'}

class AMS31348(bpy.types.Operator):
    """AMS31348 - U.S. Army #2501/2502/2510 / Scarlet"""
    bl_label = "31348 U.S. Army #2501/2502/2510 / Scarlet"
    bl_idname = 'color.ams_31348'
    def execute(self, context):
        set_base_color(0xA4393C, self.bl_label)
        return {'FINISHED'}

class AMS31400(bpy.types.Operator):
    """AMS31400 - Red"""
    bl_label = "31400 Red"
    bl_idname = 'color.ams_31400'
    def execute(self, context):
        set_base_color(0xC24A3C, self.bl_label)
        return {'FINISHED'}

class AMS31433(bpy.types.Operator):
    """AMS31433 - Red"""
    bl_label = "31433 Red"
    bl_idname = 'color.ams_31433'
    def execute(self, context):
        set_base_color(0xC39180, self.bl_label)
        return {'FINISHED'}

class AMS31575(bpy.types.Operator):
    """AMS31575 - Red"""
    bl_label = "31575 Red"
    bl_idname = 'color.ams_31575'
    def execute(self, context):
        set_base_color(0xD7B09C, self.bl_label)
        return {'FINISHED'}

class AMS31638(bpy.types.Operator):
    """AMS31638 - Red"""
    bl_label = "31638 Red"
    bl_idname = 'color.ams_31638'
    def execute(self, context):
        set_base_color(0xE2ABAD, self.bl_label)
        return {'FINISHED'}

class AMS31643(bpy.types.Operator):
    """AMS31643 - Red"""
    bl_label = "31643 Red"
    bl_idname = 'color.ams_31643'
    def execute(self, context):
        set_base_color(0xE3C8AF, self.bl_label)
        return {'FINISHED'}

class AMS31667(bpy.types.Operator):
    """AMS31667 - Tan"""
    bl_label = "31667 Tan"
    bl_idname = 'color.ams_31667'
    def execute(self, context):
        set_base_color(0xE5C6A8, self.bl_label)
        return {'FINISHED'}

class AMS31668(bpy.types.Operator):
    """AMS31668 - Red"""
    bl_label = "31668 Red"
    bl_idname = 'color.ams_31668'
    def execute(self, context):
        set_base_color(0xE7CAC0, self.bl_label)
        return {'FINISHED'}

class AMS31669(bpy.types.Operator):
    """AMS31669 - Red"""
    bl_label = "31669 Red"
    bl_idname = 'color.ams_31669'
    def execute(self, context):
        set_base_color(0xE8C7C3, self.bl_label)
        return {'FINISHED'}

class AMS31670(bpy.types.Operator):
    """AMS31670 - Red"""
    bl_label = "31670 Red"
    bl_idname = 'color.ams_31670'
    def execute(self, context):
        set_base_color(0xEECAB4, self.bl_label)
        return {'FINISHED'}

class AMS32169(bpy.types.Operator):
    """AMS32169 - Orange"""
    bl_label = "32169 Orange"
    bl_idname = 'color.ams_32169'
    def execute(self, context):
        set_base_color(0xAA5637, self.bl_label)
        return {'FINISHED'}

class AMS32246(bpy.types.Operator):
    """AMS32246 - Navy Torpedo"""
    bl_label = "32246 Navy Torpedo"
    bl_idname = 'color.ams_32246'
    def execute(self, context):
        set_base_color(0xD85B37, self.bl_label)
        return {'FINISHED'}

class AMS32276(bpy.types.Operator):
    """AMS32276 - Orange"""
    bl_label = "32276 Orange"
    bl_idname = 'color.ams_32276'
    def execute(self, context):
        set_base_color(0xBD6C56, self.bl_label)
        return {'FINISHED'}

class AMS32356(bpy.types.Operator):
    """AMS32356 - Orange"""
    bl_label = "32356 Orange"
    bl_idname = 'color.ams_32356'
    def execute(self, context):
        set_base_color(0xD47B69, self.bl_label)
        return {'FINISHED'}

class AMS32473(bpy.types.Operator):
    """AMS32473 - Orange"""
    bl_label = "32473 Orange"
    bl_idname = 'color.ams_32473'
    def execute(self, context):
        set_base_color(0xE16E34, self.bl_label)
        return {'FINISHED'}

class AMS32516(bpy.types.Operator):
    """AMS32516 - Orange"""
    bl_label = "32516 Orange"
    bl_idname = 'color.ams_32516'
    def execute(self, context):
        set_base_color(0xD4946F, self.bl_label)
        return {'FINISHED'}

class AMS32540(bpy.types.Operator):
    """AMS32540 - Naviar Flat Orange #1"""
    bl_label = "32540 Naviar Flat Orange #1"
    bl_idname = 'color.ams_32540'
    def execute(self, context):
        set_base_color(0xF68E44, self.bl_label)
        return {'FINISHED'}

class AMS32544(bpy.types.Operator):
    """AMS32544 - Orange"""
    bl_label = "32544 Orange"
    bl_idname = 'color.ams_32544'
    def execute(self, context):
        set_base_color(0xE9924D, self.bl_label)
        return {'FINISHED'}

class AMS32555(bpy.types.Operator):
    """AMS32555 - Orange"""
    bl_label = "32555 Orange"
    bl_idname = 'color.ams_32555'
    def execute(self, context):
        set_base_color(0xEBA059, self.bl_label)
        return {'FINISHED'}

class AMS32630(bpy.types.Operator):
    """AMS32630 - Orange"""
    bl_label = "32630 Orange"
    bl_idname = 'color.ams_32630'
    def execute(self, context):
        set_base_color(0xDFBB9D, self.bl_label)
        return {'FINISHED'}

class AMS32648(bpy.types.Operator):
    """AMS32648 - Orange"""
    bl_label = "32648 Orange"
    bl_idname = 'color.ams_32648'
    def execute(self, context):
        set_base_color(0xE1BB96, self.bl_label)
        return {'FINISHED'}

class AMS33070(bpy.types.Operator):
    """AMS33070 - Olive Drab Camo"""
    bl_label = "33070 Olive Drab Camo"
    bl_idname = 'color.ams_33070'
    def execute(self, context):
        set_base_color(0x544F3E, self.bl_label)
        return {'FINISHED'}

class AMS33105(bpy.types.Operator):
    """AMS33105 - Field Drab Camouflage"""
    bl_label = "33105 Field Drab Camouflage"
    bl_idname = 'color.ams_33105'
    def execute(self, context):
        set_base_color(0x6F5C42, self.bl_label)
        return {'FINISHED'}

class AMS33245(bpy.types.Operator):
    """AMS33245 - Earth Yellow Camouflage"""
    bl_label = "33245 Earth Yellow Camouflage"
    bl_idname = 'color.ams_33245'
    def execute(self, context):
        set_base_color(0xA27C53, self.bl_label)
        return {'FINISHED'}

class AMS33275(bpy.types.Operator):
    """AMS33275 - Yellow"""
    bl_label = "33275 Yellow"
    bl_idname = 'color.ams_33275'
    def execute(self, context):
        set_base_color(0xB48030, self.bl_label)
        return {'FINISHED'}

class AMS33303(bpy.types.Operator):
    """AMS33303 - Sand Camouflage"""
    bl_label = "33303 Sand Camouflage"
    bl_idname = 'color.ams_33303'
    def execute(self, context):
        set_base_color(0x9F9074, self.bl_label)
        return {'FINISHED'}

class AMS33434(bpy.types.Operator):
    """AMS33434 - Yellow"""
    bl_label = "33434 Yellow"
    bl_idname = 'color.ams_33434'
    def execute(self, context):
        set_base_color(0xCD994E, self.bl_label)
        return {'FINISHED'}

class AMS33440(bpy.types.Operator):
    """AMS33440 - Green Gold Stain"""
    bl_label = "33440 Green Gold Stain"
    bl_idname = 'color.ams_33440'
    def execute(self, context):
        set_base_color(0x9A8159, self.bl_label)
        return {'FINISHED'}

class AMS33446(bpy.types.Operator):
    """AMS33446 - Tan 686A Camouflage"""
    bl_label = "33446 Tan 686A Camouflage"
    bl_idname = 'color.ams_33446'
    def execute(self, context):
        set_base_color(0xB49D80, self.bl_label)
        return {'FINISHED'}

class AMS33448(bpy.types.Operator):
    """AMS33448 - Yellow"""
    bl_label = "33448 Yellow"
    bl_idname = 'color.ams_33448'
    def execute(self, context):
        set_base_color(0xB89F7A, self.bl_label)
        return {'FINISHED'}

class AMS33481(bpy.types.Operator):
    """AMS33481 - Yellow"""
    bl_label = "33481 Yellow"
    bl_idname = 'color.ams_33481'
    def execute(self, context):
        set_base_color(0xC3A749, self.bl_label)
        return {'FINISHED'}

class AMS33510(bpy.types.Operator):
    """AMS33510 - Dark Sandstone Camouflage"""
    bl_label = "33510 Dark Sandstone Camouflage"
    bl_idname = 'color.ams_33510'
    def execute(self, context):
        set_base_color(0xBDAB90, self.bl_label)
        return {'FINISHED'}

class AMS33522(bpy.types.Operator):
    """AMS33522 - Tan"""
    bl_label = "33522 Tan"
    bl_idname = 'color.ams_33522'
    def execute(self, context):
        set_base_color(0xC3B296, self.bl_label)
        return {'FINISHED'}

class AMS33531(bpy.types.Operator):
    """AMS33531 - Sand"""
    bl_label = "33531 Sand"
    bl_idname = 'color.ams_33531'
    def execute(self, context):
        set_base_color(0xC7B49E, self.bl_label)
        return {'FINISHED'}

class AMS33538(bpy.types.Operator):
    """AMS33538 - Yellow International / Traffic Yellow / ANA 614"""
    bl_label = "33538 Yellow International / Traffic Yellow / ANA 614"
    bl_idname = 'color.ams_33538'
    def execute(self, context):
        set_base_color(0xEFA11B, self.bl_label)
        return {'FINISHED'}

class AMS33564(bpy.types.Operator):
    """AMS33564 - Yellow"""
    bl_label = "33564 Yellow"
    bl_idname = 'color.ams_33564'
    def execute(self, context):
        set_base_color(0xD5C49C, self.bl_label)
        return {'FINISHED'}

class AMS33578(bpy.types.Operator):
    """AMS33578 - Yellow"""
    bl_label = "33578 Yellow"
    bl_idname = 'color.ams_33578'
    def execute(self, context):
        set_base_color(0xD4C39F, self.bl_label)
        return {'FINISHED'}

class AMS33613(bpy.types.Operator):
    """AMS33613 - Yellow"""
    bl_label = "33613 Yellow"
    bl_idname = 'color.ams_33613'
    def execute(self, context):
        set_base_color(0xE7C7A1, self.bl_label)
        return {'FINISHED'}

class AMS33617(bpy.types.Operator):
    """AMS33617 - Sand / Tt-P-47"""
    bl_label = "33617 Sand / Tt-P-47"
    bl_idname = 'color.ams_33617'
    def execute(self, context):
        set_base_color(0xD1BFA3, self.bl_label)
        return {'FINISHED'}

class AMS33637(bpy.types.Operator):
    """AMS33637 - Yellow"""
    bl_label = "33637 Yellow"
    bl_idname = 'color.ams_33637'
    def execute(self, context):
        set_base_color(0xDAA222, self.bl_label)
        return {'FINISHED'}

class AMS33654(bpy.types.Operator):
    """AMS33654 - U.S. Army #558 / Gold"""
    bl_label = "33654 U.S. Army #558 / Gold"
    bl_idname = 'color.ams_33654'
    def execute(self, context):
        set_base_color(0xEDB31B, self.bl_label)
        return {'FINISHED'}

class AMS33655(bpy.types.Operator):
    """AMS33655 - Yellow"""
    bl_label = "33655 Yellow"
    bl_idname = 'color.ams_33655'
    def execute(self, context):
        set_base_color(0xF3B100, self.bl_label)
        return {'FINISHED'}

class AMS33685(bpy.types.Operator):
    """AMS33685 - Yellow"""
    bl_label = "33685 Yellow"
    bl_idname = 'color.ams_33685'
    def execute(self, context):
        set_base_color(0xDDD5A0, self.bl_label)
        return {'FINISHED'}

class AMS33690(bpy.types.Operator):
    """AMS33690 - Very Light Sand"""
    bl_label = "33690 Very Light Sand"
    bl_idname = 'color.ams_33690'
    def execute(self, context):
        set_base_color(0xDDCBAB, self.bl_label)
        return {'FINISHED'}

class AMS33695(bpy.types.Operator):
    """AMS33695 - Yellow"""
    bl_label = "33695 Yellow"
    bl_idname = 'color.ams_33695'
    def execute(self, context):
        set_base_color(0xEAC67D, self.bl_label)
        return {'FINISHED'}

class AMS33696(bpy.types.Operator):
    """AMS33696 - Yellow"""
    bl_label = "33696 Yellow"
    bl_idname = 'color.ams_33696'
    def execute(self, context):
        set_base_color(0xF9C767, self.bl_label)
        return {'FINISHED'}

class AMS33711(bpy.types.Operator):
    """AMS33711 - Tan"""
    bl_label = "33711 Tan"
    bl_idname = 'color.ams_33711'
    def execute(self, context):
        set_base_color(0xE3CAA6, self.bl_label)
        return {'FINISHED'}

class AMS33717(bpy.types.Operator):
    """AMS33717 - Yellow"""
    bl_label = "33717 Yellow"
    bl_idname = 'color.ams_33717'
    def execute(self, context):
        set_base_color(0xE4D1AF, self.bl_label)
        return {'FINISHED'}

class AMS33722(bpy.types.Operator):
    """AMS33722 - Yellow"""
    bl_label = "33722 Yellow"
    bl_idname = 'color.ams_33722'
    def execute(self, context):
        set_base_color(0xE3CFA4, self.bl_label)
        return {'FINISHED'}

class AMS33727(bpy.types.Operator):
    """AMS33727 - Yellow"""
    bl_label = "33727 Yellow"
    bl_idname = 'color.ams_33727'
    def execute(self, context):
        set_base_color(0xE7D5A4, self.bl_label)
        return {'FINISHED'}

class AMS33793(bpy.types.Operator):
    """AMS33793 - Yellow"""
    bl_label = "33793 Yellow"
    bl_idname = 'color.ams_33793'
    def execute(self, context):
        set_base_color(0xEFDC8D, self.bl_label)
        return {'FINISHED'}

class AMS33798(bpy.types.Operator):
    """AMS33798 - Yellow"""
    bl_label = "33798 Yellow"
    bl_idname = 'color.ams_33798'
    def execute(self, context):
        set_base_color(0xF0D89A, self.bl_label)
        return {'FINISHED'}

class AMS33814(bpy.types.Operator):
    """AMS33814 - Yellow"""
    bl_label = "33814 Yellow"
    bl_idname = 'color.ams_33814'
    def execute(self, context):
        set_base_color(0xD5D799, self.bl_label)
        return {'FINISHED'}

class AMS34031(bpy.types.Operator):
    """AMS34031 - Aircraft Green Camouflage"""
    bl_label = "34031 Aircraft Green Camouflage"
    bl_idname = 'color.ams_34031'
    def execute(self, context):
        set_base_color(0x484743, self.bl_label)
        return {'FINISHED'}

class AMS34052(bpy.types.Operator):
    """AMS34052 - Marine Green #23"""
    bl_label = "34052 Marine Green #23"
    bl_idname = 'color.ams_34052'
    def execute(self, context):
        set_base_color(0x4B4E48, self.bl_label)
        return {'FINISHED'}

class AMS34057(bpy.types.Operator):
    """AMS34057 - U.S. Army #297 / Rifle Green"""
    bl_label = "34057 U.S. Army #297 / Rifle Green"
    bl_idname = 'color.ams_34057'
    def execute(self, context):
        set_base_color(0x3B4140, self.bl_label)
        return {'FINISHED'}

class AMS34058(bpy.types.Operator):
    """AMS34058 - Dark Blue Green"""
    bl_label = "34058 Dark Blue Green"
    bl_idname = 'color.ams_34058'
    def execute(self, context):
        set_base_color(0x325251, self.bl_label)
        return {'FINISHED'}

class AMS34064(bpy.types.Operator):
    """AMS34064 - Olive Drab 85285"""
    bl_label = "34064 Olive Drab 85285"
    bl_idname = 'color.ams_34064'
    def execute(self, context):
        set_base_color(0x4C4C42, self.bl_label)
        return {'FINISHED'}

class AMS34065(bpy.types.Operator):
    """AMS34065 - U.S. Army #2209 / Green"""
    bl_label = "34065 U.S. Army #2209 / Green"
    bl_idname = 'color.ams_34065'
    def execute(self, context):
        set_base_color(0x57514A, self.bl_label)
        return {'FINISHED'}

class AMS34076(bpy.types.Operator):
    """AMS34076 - U.S. Army / Ranger Green"""
    bl_label = "34076 U.S. Army / Ranger Green"
    bl_idname = 'color.ams_34076'
    def execute(self, context):
        set_base_color(0x605B50, self.bl_label)
        return {'FINISHED'}

class AMS34078(bpy.types.Operator):
    """AMS34078 - U.S. Army #2247/2248 / OD Green"""
    bl_label = "34078 U.S. Army #2247/2248 / OD Green"
    bl_idname = 'color.ams_34078'
    def execute(self, context):
        set_base_color(0x4E5040, self.bl_label)
        return {'FINISHED'}

class AMS34079(bpy.types.Operator):
    """AMS34079 - Army Forest Green / ANA 631"""
    bl_label = "34079 Army Forest Green / ANA 631"
    bl_idname = 'color.ams_34079'
    def execute(self, context):
        set_base_color(0x545648, self.bl_label)
        return {'FINISHED'}

class AMS34080(bpy.types.Operator):
    """AMS34080 - U.S. Army #2212 / Green"""
    bl_label = "34080 U.S. Army #2212 / Green"
    bl_idname = 'color.ams_34080'
    def execute(self, context):
        set_base_color(0x535046, self.bl_label)
        return {'FINISHED'}

class AMS34082(bpy.types.Operator):
    """AMS34082 - Dark Green Camouflage"""
    bl_label = "34082 Dark Green Camouflage"
    bl_idname = 'color.ams_34082'
    def execute(self, context):
        set_base_color(0x565C44, self.bl_label)
        return {'FINISHED'}

class AMS34083(bpy.types.Operator):
    """AMS34083 - Air Force Forest Green"""
    bl_label = "34083 Air Force Forest Green"
    bl_idname = 'color.ams_34083'
    def execute(self, context):
        set_base_color(0x494B3D, self.bl_label)
        return {'FINISHED'}

class AMS34084(bpy.types.Operator):
    """AMS34084 - Dark Green Camo"""
    bl_label = "34084 Dark Green Camo"
    bl_idname = 'color.ams_34084'
    def execute(self, context):
        set_base_color(0x46443E, self.bl_label)
        return {'FINISHED'}

class AMS34085(bpy.types.Operator):
    """AMS34085 - U.S. Army Green #2243 / Green"""
    bl_label = "34085 U.S. Army Green #2243 / Green"
    bl_idname = 'color.ams_34085'
    def execute(self, context):
        set_base_color(0x515044, self.bl_label)
        return {'FINISHED'}

class AMS34086(bpy.types.Operator):
    """AMS34086 - Army Forest Green Camo"""
    bl_label = "34086 Army Forest Green Camo"
    bl_idname = 'color.ams_34086'
    def execute(self, context):
        set_base_color(0x57554C, self.bl_label)
        return {'FINISHED'}

class AMS34087(bpy.types.Operator):
    """AMS34087 - U.S. Army #523 / Belleau Wood Green"""
    bl_label = "34087 U.S. Army #523 / Belleau Wood Green"
    bl_idname = 'color.ams_34087'
    def execute(self, context):
        set_base_color(0x534E42, self.bl_label)
        return {'FINISHED'}

class AMS34088(bpy.types.Operator):
    """AMS34088 - Olive Drab CARC"""
    bl_label = "34088 Olive Drab CARC"
    bl_idname = 'color.ams_34088'
    def execute(self, context):
        set_base_color(0x665F4C, self.bl_label)
        return {'FINISHED'}

class AMS34089(bpy.types.Operator):
    """AMS34089 - Light Green Camo"""
    bl_label = "34089 Light Green Camo"
    bl_idname = 'color.ams_34089'
    def execute(self, context):
        set_base_color(0x5F5F3A, self.bl_label)
        return {'FINISHED'}

class AMS34090(bpy.types.Operator):
    """AMS34090 - Green"""
    bl_label = "34090 Green"
    bl_idname = 'color.ams_34090'
    def execute(self, context):
        set_base_color(0x1B6B48, self.bl_label)
        return {'FINISHED'}

class AMS34092(bpy.types.Operator):
    """AMS34092 - Gunship Green / ANA 612"""
    bl_label = "34092 Gunship Green / ANA 612"
    bl_idname = 'color.ams_34092'
    def execute(self, context):
        set_base_color(0x4A5A52, self.bl_label)
        return {'FINISHED'}

class AMS34094(bpy.types.Operator):
    """AMS34094 - Green 383 Camouflage"""
    bl_label = "34094 Green 383 Camouflage"
    bl_idname = 'color.ams_34094'
    def execute(self, context):
        set_base_color(0x4F5545, self.bl_label)
        return {'FINISHED'}

class AMS34095(bpy.types.Operator):
    """AMS34095 - Field Green"""
    bl_label = "34095 Field Green"
    bl_idname = 'color.ams_34095'
    def execute(self, context):
        set_base_color(0x50553F, self.bl_label)
        return {'FINISHED'}

class AMS34096(bpy.types.Operator):
    """AMS34096 - Green"""
    bl_label = "34096 Green"
    bl_idname = 'color.ams_34096'
    def execute(self, context):
        set_base_color(0x545647, self.bl_label)
        return {'FINISHED'}

class AMS34097(bpy.types.Operator):
    """AMS34097 - Field Green / ANA 627"""
    bl_label = "34097 Field Green / ANA 627"
    bl_idname = 'color.ams_34097'
    def execute(self, context):
        set_base_color(0x5B634A, self.bl_label)
        return {'FINISHED'}

class AMS34098(bpy.types.Operator):
    """AMS34098 - Green"""
    bl_label = "34098 Green"
    bl_idname = 'color.ams_34098'
    def execute(self, context):
        set_base_color(0x636143, self.bl_label)
        return {'FINISHED'}

class AMS34101(bpy.types.Operator):
    """AMS34101 - U.S. Army #528 / Dark Green"""
    bl_label = "34101 U.S. Army #528 / Dark Green"
    bl_idname = 'color.ams_34101'
    def execute(self, context):
        set_base_color(0x5D644A, self.bl_label)
        return {'FINISHED'}

class AMS34102(bpy.types.Operator):
    """AMS34102 - Dark Green"""
    bl_label = "34102 Dark Green"
    bl_idname = 'color.ams_34102'
    def execute(self, context):
        set_base_color(0x585C46, self.bl_label)
        return {'FINISHED'}

class AMS34108(bpy.types.Operator):
    """AMS34108 - Dark Green International / Navy Torpedo"""
    bl_label = "34108 Dark Green International / Navy Torpedo"
    bl_idname = 'color.ams_34108'
    def execute(self, context):
        set_base_color(0x466653, self.bl_label)
        return {'FINISHED'}

class AMS34127(bpy.types.Operator):
    """AMS34127 - Light Green Camo"""
    bl_label = "34127 Light Green Camo"
    bl_idname = 'color.ams_34127'
    def execute(self, context):
        set_base_color(0x605F41, self.bl_label)
        return {'FINISHED'}

class AMS34128(bpy.types.Operator):
    """AMS34128 - Green"""
    bl_label = "34128 Green"
    bl_idname = 'color.ams_34128'
    def execute(self, context):
        set_base_color(0x586753, self.bl_label)
        return {'FINISHED'}

class AMS34129(bpy.types.Operator):
    """AMS34129 - Navair Flat Green #2"""
    bl_label = "34129 Navair Flat Green #2"
    bl_idname = 'color.ams_34129'
    def execute(self, context):
        set_base_color(0x5C5C4B, self.bl_label)
        return {'FINISHED'}

class AMS34130(bpy.types.Operator):
    """AMS34130 - Munsell Color 10y3/3"""
    bl_label = "34130 Munsell Color 10y3/3"
    bl_idname = 'color.ams_34130'
    def execute(self, context):
        set_base_color(0x5D5B3C, self.bl_label)
        return {'FINISHED'}

class AMS34138(bpy.types.Operator):
    """AMS34138 - Green"""
    bl_label = "34138 Green"
    bl_idname = 'color.ams_34138'
    def execute(self, context):
        set_base_color(0x547648, self.bl_label)
        return {'FINISHED'}

class AMS34148(bpy.types.Operator):
    """AMS34148 - Green"""
    bl_label = "34148 Green"
    bl_idname = 'color.ams_34148'
    def execute(self, context):
        set_base_color(0x5A716F, self.bl_label)
        return {'FINISHED'}

class AMS34150(bpy.types.Operator):
    """AMS34150 - U.S. Army #562 / Moss Green"""
    bl_label = "34150 U.S. Army #562 / Moss Green"
    bl_idname = 'color.ams_34150'
    def execute(self, context):
        set_base_color(0x746C49, self.bl_label)
        return {'FINISHED'}

class AMS34151(bpy.types.Operator):
    """AMS34151 - Interior Green TT-P-1757 / ANA 611"""
    bl_label = "34151 Interior Green TT-P-1757 / ANA 611"
    bl_idname = 'color.ams_34151'
    def execute(self, context):
        set_base_color(0x65643C, self.bl_label)
        return {'FINISHED'}

class AMS34158(bpy.types.Operator):
    """AMS34158 - Blue Drab"""
    bl_label = "34158 Blue Drab"
    bl_idname = 'color.ams_34158'
    def execute(self, context):
        set_base_color(0x62706E, self.bl_label)
        return {'FINISHED'}

class AMS34159(bpy.types.Operator):
    """AMS34159 - Green"""
    bl_label = "34159 Green"
    bl_idname = 'color.ams_34159'
    def execute(self, context):
        set_base_color(0x6A7367, self.bl_label)
        return {'FINISHED'}

class AMS34160(bpy.types.Operator):
    """AMS34160 - Foliage Green"""
    bl_label = "34160 Foliage Green"
    bl_idname = 'color.ams_34160'
    def execute(self, context):
        set_base_color(0x676962, self.bl_label)
        return {'FINISHED'}

class AMS34170(bpy.types.Operator):
    """AMS34170 - Navair Flat Green #1"""
    bl_label = "34170 Navair Flat Green #1"
    bl_idname = 'color.ams_34170'
    def execute(self, context):
        set_base_color(0x606154, self.bl_label)
        return {'FINISHED'}

class AMS34201(bpy.types.Operator):
    """AMS34201 - Green"""
    bl_label = "34201 Green"
    bl_idname = 'color.ams_34201'
    def execute(self, context):
        set_base_color(0x827963, self.bl_label)
        return {'FINISHED'}

class AMS34202(bpy.types.Operator):
    """AMS34202 - U.S. Army #526 / Pale Green"""
    bl_label = "34202 U.S. Army #526 / Pale Green"
    bl_idname = 'color.ams_34202'
    def execute(self, context):
        set_base_color(0x887E65, self.bl_label)
        return {'FINISHED'}

class AMS34203(bpy.types.Operator):
    """AMS34203 - U.S. Army #560 / Light Sage"""
    bl_label = "34203 U.S. Army #560 / Light Sage"
    bl_idname = 'color.ams_34203'
    def execute(self, context):
        set_base_color(0x898067, self.bl_label)
        return {'FINISHED'}

class AMS34226(bpy.types.Operator):
    """AMS34226 - NASA Primer"""
    bl_label = "34226 NASA Primer"
    bl_idname = 'color.ams_34226'
    def execute(self, context):
        set_base_color(0x7A8676, self.bl_label)
        return {'FINISHED'}

class AMS34227(bpy.types.Operator):
    """AMS34227 - Green"""
    bl_label = "34227 Green"
    bl_idname = 'color.ams_34227'
    def execute(self, context):
        set_base_color(0x788A6D, self.bl_label)
        return {'FINISHED'}

class AMS34230(bpy.types.Operator):
    """AMS34230 - Green"""
    bl_label = "34230 Green"
    bl_idname = 'color.ams_34230'
    def execute(self, context):
        set_base_color(0x518F4E, self.bl_label)
        return {'FINISHED'}

class AMS34233(bpy.types.Operator):
    """AMS34233 - Green"""
    bl_label = "34233 Green"
    bl_idname = 'color.ams_34233'
    def execute(self, context):
        set_base_color(0x7D908C, self.bl_label)
        return {'FINISHED'}

class AMS34241(bpy.types.Operator):
    """AMS34241 - Green"""
    bl_label = "34241 Green"
    bl_idname = 'color.ams_34241'
    def execute(self, context):
        set_base_color(0x7E9B8D, self.bl_label)
        return {'FINISHED'}

class AMS34256(bpy.types.Operator):
    """AMS34256 - U.S. Army #527 / Olive"""
    bl_label = "34256 U.S. Army #527 / Olive"
    bl_idname = 'color.ams_34256'
    def execute(self, context):
        set_base_color(0x877C5B, self.bl_label)
        return {'FINISHED'}

class AMS34258(bpy.types.Operator):
    """AMS34258 - Green"""
    bl_label = "34258 Green"
    bl_idname = 'color.ams_34258'
    def execute(self, context):
        set_base_color(0x7F8259, self.bl_label)
        return {'FINISHED'}

class AMS34259(bpy.types.Operator):
    """AMS34259 - Green"""
    bl_label = "34259 Green"
    bl_idname = 'color.ams_34259'
    def execute(self, context):
        set_base_color(0x807235, self.bl_label)
        return {'FINISHED'}

class AMS34272(bpy.types.Operator):
    """AMS34272 - Green"""
    bl_label = "34272 Green"
    bl_idname = 'color.ams_34272'
    def execute(self, context):
        set_base_color(0x6F9575, self.bl_label)
        return {'FINISHED'}

class AMS34277(bpy.types.Operator):
    """AMS34277 - Sea Mist Green"""
    bl_label = "34277 Sea Mist Green"
    bl_idname = 'color.ams_34277'
    def execute(self, context):
        set_base_color(0x788A6D, self.bl_label)
        return {'FINISHED'}

class AMS34300(bpy.types.Operator):
    """AMS34300 - Green"""
    bl_label = "34300 Green"
    bl_idname = 'color.ams_34300'
    def execute(self, context):
        set_base_color(0x839B8C, self.bl_label)
        return {'FINISHED'}

class AMS34325(bpy.types.Operator):
    """AMS34325 - Green"""
    bl_label = "34325 Green"
    bl_idname = 'color.ams_34325'
    def execute(self, context):
        set_base_color(0x80A695, self.bl_label)
        return {'FINISHED'}

class AMS34350(bpy.types.Operator):
    """AMS34350 - Forest Service Green"""
    bl_label = "34350 Forest Service Green"
    bl_idname = 'color.ams_34350'
    def execute(self, context):
        set_base_color(0x6DC8AF, self.bl_label)
        return {'FINISHED'}

class AMS34373(bpy.types.Operator):
    """AMS34373 - Sagebrush"""
    bl_label = "34373 Sagebrush"
    bl_idname = 'color.ams_34373'
    def execute(self, context):
        set_base_color(0x97A78F, self.bl_label)
        return {'FINISHED'}

class AMS34410(bpy.types.Operator):
    """AMS34410 - Green"""
    bl_label = "34410 Green"
    bl_idname = 'color.ams_34410'
    def execute(self, context):
        set_base_color(0x9DAE9E, self.bl_label)
        return {'FINISHED'}

class AMS34414(bpy.types.Operator):
    """AMS34414 - Green"""
    bl_label = "34414 Green"
    bl_idname = 'color.ams_34414'
    def execute(self, context):
        set_base_color(0xABB8A3, self.bl_label)
        return {'FINISHED'}

class AMS34424(bpy.types.Operator):
    """AMS34424 - ANA 610"""
    bl_label = "34424 ANA 610"
    bl_idname = 'color.ams_34424'
    def execute(self, context):
        set_base_color(0xA9AC95, self.bl_label)
        return {'FINISHED'}

class AMS34432(bpy.types.Operator):
    """AMS34432 - Green"""
    bl_label = "34432 Green"
    bl_idname = 'color.ams_34432'
    def execute(self, context):
        set_base_color(0xA4AD9B, self.bl_label)
        return {'FINISHED'}

class AMS34441(bpy.types.Operator):
    """AMS34441 - Green"""
    bl_label = "34441 Green"
    bl_idname = 'color.ams_34441'
    def execute(self, context):
        set_base_color(0xA4B095, self.bl_label)
        return {'FINISHED'}

class AMS34449(bpy.types.Operator):
    """AMS34449 - Light Green International"""
    bl_label = "34449 Light Green International"
    bl_idname = 'color.ams_34449'
    def execute(self, context):
        set_base_color(0xA2B597, self.bl_label)
        return {'FINISHED'}

class AMS34491(bpy.types.Operator):
    """AMS34491 - Green"""
    bl_label = "34491 Green"
    bl_idname = 'color.ams_34491'
    def execute(self, context):
        set_base_color(0xA3B9A3, self.bl_label)
        return {'FINISHED'}

class AMS34504(bpy.types.Operator):
    """AMS34504 - Green"""
    bl_label = "34504 Green"
    bl_idname = 'color.ams_34504'
    def execute(self, context):
        set_base_color(0xA6B59C, self.bl_label)
        return {'FINISHED'}

class AMS34516(bpy.types.Operator):
    """AMS34516 - Green"""
    bl_label = "34516 Green"
    bl_idname = 'color.ams_34516'
    def execute(self, context):
        set_base_color(0xAFBFAD, self.bl_label)
        return {'FINISHED'}

class AMS34518(bpy.types.Operator):
    """AMS34518 - Green"""
    bl_label = "34518 Green"
    bl_idname = 'color.ams_34518'
    def execute(self, context):
        set_base_color(0xA6B6A4, self.bl_label)
        return {'FINISHED'}

class AMS34524(bpy.types.Operator):
    """AMS34524 - Green"""
    bl_label = "34524 Green"
    bl_idname = 'color.ams_34524'
    def execute(self, context):
        set_base_color(0xAFBA91, self.bl_label)
        return {'FINISHED'}

class AMS34533(bpy.types.Operator):
    """AMS34533 - Green"""
    bl_label = "34533 Green"
    bl_idname = 'color.ams_34533'
    def execute(self, context):
        set_base_color(0xA8B690, self.bl_label)
        return {'FINISHED'}

class AMS34540(bpy.types.Operator):
    """AMS34540 - Green"""
    bl_label = "34540 Green"
    bl_idname = 'color.ams_34540'
    def execute(self, context):
        set_base_color(0x95C57F, self.bl_label)
        return {'FINISHED'}

class AMS34552(bpy.types.Operator):
    """AMS34552 - Green"""
    bl_label = "34552 Green"
    bl_idname = 'color.ams_34552'
    def execute(self, context):
        set_base_color(0xC4BF82, self.bl_label)
        return {'FINISHED'}

class AMS34554(bpy.types.Operator):
    """AMS34554 - Public Building Standard"""
    bl_label = "34554 Public Building Standard"
    bl_idname = 'color.ams_34554'
    def execute(self, context):
        set_base_color(0xCACBAE, self.bl_label)
        return {'FINISHED'}

class AMS34558(bpy.types.Operator):
    """AMS34558 - Light Green International"""
    bl_label = "34558 Light Green International"
    bl_idname = 'color.ams_34558'
    def execute(self, context):
        set_base_color(0xB7C8AA, self.bl_label)
        return {'FINISHED'}

class AMS34583(bpy.types.Operator):
    """AMS34583 - Green"""
    bl_label = "34583 Green"
    bl_idname = 'color.ams_34583'
    def execute(self, context):
        set_base_color(0xB1B697, self.bl_label)
        return {'FINISHED'}

class AMS34666(bpy.types.Operator):
    """AMS34666 - Green"""
    bl_label = "34666 Green"
    bl_idname = 'color.ams_34666'
    def execute(self, context):
        set_base_color(0xCDDA9F, self.bl_label)
        return {'FINISHED'}

class AMS34670(bpy.types.Operator):
    """AMS34670 - Green"""
    bl_label = "34670 Green"
    bl_idname = 'color.ams_34670'
    def execute(self, context):
        set_base_color(0xC7D3C1, self.bl_label)
        return {'FINISHED'}

class AMS34672(bpy.types.Operator):
    """AMS34672 - Pastel Blue"""
    bl_label = "34672 Pastel Blue"
    bl_idname = 'color.ams_34672'
    def execute(self, context):
        set_base_color(0xC7D0B3, self.bl_label)
        return {'FINISHED'}

class AMS35039(bpy.types.Operator):
    """AMS35039 - U.S. Army #2307 / Marine Dark Blue"""
    bl_label = "35039 U.S. Army #2307 / Marine Dark Blue"
    bl_idname = 'color.ams_35039'
    def execute(self, context):
        set_base_color(0x3C3D3F, self.bl_label)
        return {'FINISHED'}

class AMS35040(bpy.types.Operator):
    """AMS35040 - U.S. Army #2312 / Marine Dark Blue"""
    bl_label = "35040 U.S. Army #2312 / Marine Dark Blue"
    bl_idname = 'color.ams_35040'
    def execute(self, context):
        set_base_color(0x3B3B3D, self.bl_label)
        return {'FINISHED'}

class AMS35041(bpy.types.Operator):
    """AMS35041 - U.S. Army #450 / Blue"""
    bl_label = "35041 U.S. Army #450 / Blue"
    bl_idname = 'color.ams_35041'
    def execute(self, context):
        set_base_color(0x3B3C3F, self.bl_label)
        return {'FINISHED'}

class AMS35042(bpy.types.Operator):
    """AMS35042 - Sea Blue / ANA 607"""
    bl_label = "35042 Sea Blue / ANA 607"
    bl_idname = 'color.ams_35042'
    def execute(self, context):
        set_base_color(0x3F464A, self.bl_label)
        return {'FINISHED'}

class AMS35043(bpy.types.Operator):
    """AMS35043 - U.S. Army #3378 / Blue"""
    bl_label = "35043 U.S. Army #3378 / Blue"
    bl_idname = 'color.ams_35043'
    def execute(self, context):
        set_base_color(0x393A42, self.bl_label)
        return {'FINISHED'}

class AMS35044(bpy.types.Operator):
    """AMS35044 - Aircraft Insignia Blue / ANA 605"""
    bl_label = "35044 Aircraft Insignia Blue / ANA 605"
    bl_idname = 'color.ams_35044'
    def execute(self, context):
        set_base_color(0x3B3B49, self.bl_label)
        return {'FINISHED'}

class AMS35045(bpy.types.Operator):
    """AMS35045 - Blue"""
    bl_label = "35045 Blue"
    bl_idname = 'color.ams_35045'
    def execute(self, context):
        set_base_color(0x39454E, self.bl_label)
        return {'FINISHED'}

class AMS35046(bpy.types.Operator):
    """AMS35046 - U.S. Army #2319 / Sky Blue"""
    bl_label = "35046 U.S. Army #2319 / Sky Blue"
    bl_idname = 'color.ams_35046'
    def execute(self, context):
        set_base_color(0x36425B, self.bl_label)
        return {'FINISHED'}

class AMS35047(bpy.types.Operator):
    """AMS35047 - U.S. Army #451 / Blue"""
    bl_label = "35047 U.S. Army #451 / Blue"
    bl_idname = 'color.ams_35047'
    def execute(self, context):
        set_base_color(0x374258, self.bl_label)
        return {'FINISHED'}

class AMS35048(bpy.types.Operator):
    """AMS35048 - Blue"""
    bl_label = "35048 Blue"
    bl_idname = 'color.ams_35048'
    def execute(self, context):
        set_base_color(0x38455C, self.bl_label)
        return {'FINISHED'}

class AMS35052(bpy.types.Operator):
    """AMS35052 - Blue"""
    bl_label = "35052 Blue"
    bl_idname = 'color.ams_35052'
    def execute(self, context):
        set_base_color(0x3A4F6B, self.bl_label)
        return {'FINISHED'}

class AMS35056(bpy.types.Operator):
    """AMS35056 - Blue"""
    bl_label = "35056 Blue"
    bl_idname = 'color.ams_35056'
    def execute(self, context):
        set_base_color(0x3D456C, self.bl_label)
        return {'FINISHED'}

class AMS35095(bpy.types.Operator):
    """AMS35095 - Blue"""
    bl_label = "35095 Blue"
    bl_idname = 'color.ams_35095'
    def execute(self, context):
        set_base_color(0x38639C, self.bl_label)
        return {'FINISHED'}

class AMS35109(bpy.types.Operator):
    """AMS35109 - Light Blue International"""
    bl_label = "35109 Light Blue International"
    bl_idname = 'color.ams_35109'
    def execute(self, context):
        set_base_color(0x4B6B7E, self.bl_label)
        return {'FINISHED'}

class AMS35164(bpy.types.Operator):
    """AMS35164 - Navy Blue 212 / ANA 608"""
    bl_label = "35164 Navy Blue 212 / ANA 608"
    bl_idname = 'color.ams_35164'
    def execute(self, context):
        set_base_color(0x63727E, self.bl_label)
        return {'FINISHED'}

class AMS35177(bpy.types.Operator):
    """AMS35177 - Blue"""
    bl_label = "35177 Blue"
    bl_idname = 'color.ams_35177'
    def execute(self, context):
        set_base_color(0x5A7A90, self.bl_label)
        return {'FINISHED'}

class AMS35180(bpy.types.Operator):
    """AMS35180 - Blue"""
    bl_label = "35180 Blue"
    bl_idname = 'color.ams_35180'
    def execute(self, context):
        set_base_color(0x316FA2, self.bl_label)
        return {'FINISHED'}

class AMS35183(bpy.types.Operator):
    """AMS35183 - Blue"""
    bl_label = "35183 Blue"
    bl_idname = 'color.ams_35183'
    def execute(self, context):
        set_base_color(0x347CA7, self.bl_label)
        return {'FINISHED'}

class AMS35189(bpy.types.Operator):
    """AMS35189 - Blue"""
    bl_label = "35189 Blue"
    bl_idname = 'color.ams_35189'
    def execute(self, context):
        set_base_color(0x71868C, self.bl_label)
        return {'FINISHED'}

class AMS35190(bpy.types.Operator):
    """AMS35190 - Blue"""
    bl_label = "35190 Blue"
    bl_idname = 'color.ams_35190'
    def execute(self, context):
        set_base_color(0x618C9F, self.bl_label)
        return {'FINISHED'}

class AMS35193(bpy.types.Operator):
    """AMS35193 - Blue"""
    bl_label = "35193 Blue"
    bl_idname = 'color.ams_35193'
    def execute(self, context):
        set_base_color(0x55868C, self.bl_label)
        return {'FINISHED'}

class AMS35231(bpy.types.Operator):
    """AMS35231 - ANA 609"""
    bl_label = "35231 ANA 609"
    bl_idname = 'color.ams_35231'
    def execute(self, context):
        set_base_color(0x708AAD, self.bl_label)
        return {'FINISHED'}

class AMS35237(bpy.types.Operator):
    """AMS35237 - Blue Gray"""
    bl_label = "35237 Blue Gray"
    bl_idname = 'color.ams_35237'
    def execute(self, context):
        set_base_color(0x7C898E, self.bl_label)
        return {'FINISHED'}

class AMS35240(bpy.types.Operator):
    """AMS35240 - Blue"""
    bl_label = "35240 Blue"
    bl_idname = 'color.ams_35240'
    def execute(self, context):
        set_base_color(0x7591B1, self.bl_label)
        return {'FINISHED'}

class AMS35250(bpy.types.Operator):
    """AMS35250 - UN Flag Blue"""
    bl_label = "35250 UN Flag Blue"
    bl_idname = 'color.ams_35250'
    def execute(self, context):
        set_base_color(0x54A2CB, self.bl_label)
        return {'FINISHED'}

class AMS35260(bpy.types.Operator):
    """AMS35260 - Forest Service Blue"""
    bl_label = "35260 Forest Service Blue"
    bl_idname = 'color.ams_35260'
    def execute(self, context):
        set_base_color(0x44ABC9, self.bl_label)
        return {'FINISHED'}

class AMS35275(bpy.types.Operator):
    """AMS35275 - Blue"""
    bl_label = "35275 Blue"
    bl_idname = 'color.ams_35275'
    def execute(self, context):
        set_base_color(0x329FA2, self.bl_label)
        return {'FINISHED'}

class AMS35299(bpy.types.Operator):
    """AMS35299 - Blue"""
    bl_label = "35299 Blue"
    bl_idname = 'color.ams_35299'
    def execute(self, context):
        set_base_color(0x70A099, self.bl_label)
        return {'FINISHED'}

class AMS35352(bpy.types.Operator):
    """AMS35352 - Blue"""
    bl_label = "35352 Blue"
    bl_idname = 'color.ams_35352'
    def execute(self, context):
        set_base_color(0x839C98, self.bl_label)
        return {'FINISHED'}

class AMS35414(bpy.types.Operator):
    """AMS35414 - Blue Green"""
    bl_label = "35414 Blue Green"
    bl_idname = 'color.ams_35414'
    def execute(self, context):
        set_base_color(0x88A4A1, self.bl_label)
        return {'FINISHED'}

class AMS35450(bpy.types.Operator):
    """AMS35450 - Blue"""
    bl_label = "35450 Blue"
    bl_idname = 'color.ams_35450'
    def execute(self, context):
        set_base_color(0x89B2C5, self.bl_label)
        return {'FINISHED'}

class AMS35466(bpy.types.Operator):
    """AMS35466 - Blue"""
    bl_label = "35466 Blue"
    bl_idname = 'color.ams_35466'
    def execute(self, context):
        set_base_color(0x7DC6D8, self.bl_label)
        return {'FINISHED'}

class AMS35488(bpy.types.Operator):
    """AMS35488 - Blue"""
    bl_label = "35488 Blue"
    bl_idname = 'color.ams_35488'
    def execute(self, context):
        set_base_color(0x98B9CE, self.bl_label)
        return {'FINISHED'}

class AMS35526(bpy.types.Operator):
    """AMS35526 - Blue"""
    bl_label = "35526 Blue"
    bl_idname = 'color.ams_35526'
    def execute(self, context):
        set_base_color(0xA5BBBE, self.bl_label)
        return {'FINISHED'}

class AMS35550(bpy.types.Operator):
    """AMS35550 - Blue"""
    bl_label = "35550 Blue"
    bl_idname = 'color.ams_35550'
    def execute(self, context):
        set_base_color(0xC6D8D9, self.bl_label)
        return {'FINISHED'}

class AMS35622(bpy.types.Operator):
    """AMS35622 - Blue"""
    bl_label = "35622 Blue"
    bl_idname = 'color.ams_35622'
    def execute(self, context):
        set_base_color(0xC6D1C7, self.bl_label)
        return {'FINISHED'}

class AMS35630(bpy.types.Operator):
    """AMS35630 - Blue"""
    bl_label = "35630 Blue"
    bl_idname = 'color.ams_35630'
    def execute(self, context):
        set_base_color(0xD2D2CA, self.bl_label)
        return {'FINISHED'}

class AMS36007(bpy.types.Operator):
    """AMS36007 - U.S. Army #548 / Slate Gray"""
    bl_label = "36007 U.S. Army #548 / Slate Gray"
    bl_idname = 'color.ams_36007'
    def execute(self, context):
        set_base_color(0x474A49, self.bl_label)
        return {'FINISHED'}

class AMS36076(bpy.types.Operator):
    """AMS36076 - Navy Gray #2 / Dark Gray"""
    bl_label = "36076 Navy Gray #2 / Dark Gray"
    bl_idname = 'color.ams_36076'
    def execute(self, context):
        set_base_color(0x4E5259, self.bl_label)
        return {'FINISHED'}

class AMS36081(bpy.types.Operator):
    """AMS36081 - Deep Gray / F-4 Aircraft"""
    bl_label = "36081 Deep Gray / F-4 Aircraft"
    bl_idname = 'color.ams_36081'
    def execute(self, context):
        set_base_color(0x585A5A, self.bl_label)
        return {'FINISHED'}

class AMS36099(bpy.types.Operator):
    """AMS36099 - Dark Blue Gray"""
    bl_label = "36099 Dark Blue Gray"
    bl_idname = 'color.ams_36099'
    def execute(self, context):
        set_base_color(0x525B61, self.bl_label)
        return {'FINISHED'}

class AMS36118(bpy.types.Operator):
    """AMS36118 - Gunship Gray / ANA 603"""
    bl_label = "36118 Gunship Gray / ANA 603"
    bl_idname = 'color.ams_36118'
    def execute(self, context):
        set_base_color(0x5C626A, self.bl_label)
        return {'FINISHED'}

class AMS36134(bpy.types.Operator):
    """AMS36134 - Gray"""
    bl_label = "36134 Gray"
    bl_idname = 'color.ams_36134'
    def execute(self, context):
        set_base_color(0x676966, self.bl_label)
        return {'FINISHED'}

class AMS36152(bpy.types.Operator):
    """AMS36152 - Gray"""
    bl_label = "36152 Gray"
    bl_idname = 'color.ams_36152'
    def execute(self, context):
        set_base_color(0x686E71, self.bl_label)
        return {'FINISHED'}

class AMS36170(bpy.types.Operator):
    """AMS36170 - Camouflage Gray"""
    bl_label = "36170 Camouflage Gray"
    bl_idname = 'color.ams_36170'
    def execute(self, context):
        set_base_color(0x6C6C6B, self.bl_label)
        return {'FINISHED'}

class AMS36173(bpy.types.Operator):
    """AMS36173 - Ocean Gray / NAVSEA"""
    bl_label = "36173 Ocean Gray / NAVSEA"
    bl_idname = 'color.ams_36173'
    def execute(self, context):
        set_base_color(0x71787E, self.bl_label)
        return {'FINISHED'}

class AMS36176(bpy.types.Operator):
    """AMS36176 - Ocean Gray"""
    bl_label = "36176 Ocean Gray"
    bl_idname = 'color.ams_36176'
    def execute(self, context):
        set_base_color(0x6D7881, self.bl_label)
        return {'FINISHED'}

class AMS36231(bpy.types.Operator):
    """AMS36231 - Gray International / Aircraft Gray / ANA 621"""
    bl_label = "36231 Gray International / Aircraft Gray / ANA 621"
    bl_idname = 'color.ams_36231'
    def execute(self, context):
        set_base_color(0x7E8385, self.bl_label)
        return {'FINISHED'}

class AMS36251(bpy.types.Operator):
    """AMS36251 - Gray"""
    bl_label = "36251 Gray"
    bl_idname = 'color.ams_36251'
    def execute(self, context):
        set_base_color(0x828585, self.bl_label)
        return {'FINISHED'}

class AMS36270(bpy.types.Operator):
    """AMS36270 - Haze Gray"""
    bl_label = "36270 Haze Gray"
    bl_idname = 'color.ams_36270'
    def execute(self, context):
        set_base_color(0x84898C, self.bl_label)
        return {'FINISHED'}

class AMS36280(bpy.types.Operator):
    """AMS36280 - Gray"""
    bl_label = "36280 Gray"
    bl_idname = 'color.ams_36280'
    def execute(self, context):
        set_base_color(0x898D8B, self.bl_label)
        return {'FINISHED'}

class AMS36293(bpy.types.Operator):
    """AMS36293 - Gray"""
    bl_label = "36293 Gray"
    bl_idname = 'color.ams_36293'
    def execute(self, context):
        set_base_color(0x898F90, self.bl_label)
        return {'FINISHED'}

class AMS36300(bpy.types.Operator):
    """AMS36300 - Aircraft Gray Camouflage"""
    bl_label = "36300 Aircraft Gray Camouflage"
    bl_idname = 'color.ams_36300'
    def execute(self, context):
        set_base_color(0x91979F, self.bl_label)
        return {'FINISHED'}

class AMS36306(bpy.types.Operator):
    """AMS36306 - Gray"""
    bl_label = "36306 Gray"
    bl_idname = 'color.ams_36306'
    def execute(self, context):
        set_base_color(0x978F85, self.bl_label)
        return {'FINISHED'}

class AMS36307(bpy.types.Operator):
    """AMS36307 - Bulkhead Gray"""
    bl_label = "36307 Bulkhead Gray"
    bl_idname = 'color.ams_36307'
    def execute(self, context):
        set_base_color(0x95978F, self.bl_label)
        return {'FINISHED'}

class AMS36314(bpy.types.Operator):
    """AMS36314 - Gray"""
    bl_label = "36314 Gray"
    bl_idname = 'color.ams_36314'
    def execute(self, context):
        set_base_color(0x8F9591, self.bl_label)
        return {'FINISHED'}

class AMS36320(bpy.types.Operator):
    """AMS36320 - Gray"""
    bl_label = "36320 Gray"
    bl_idname = 'color.ams_36320'
    def execute(self, context):
        set_base_color(0x8C969E, self.bl_label)
        return {'FINISHED'}

class AMS36356(bpy.types.Operator):
    """AMS36356 - U.S. Army #2246 / Pewter"""
    bl_label = "36356 U.S. Army #2246 / Pewter"
    bl_idname = 'color.ams_36356'
    def execute(self, context):
        set_base_color(0x7D786B, self.bl_label)
        return {'FINISHED'}

class AMS36357(bpy.types.Operator):
    """AMS36357 - Gray"""
    bl_label = "36357 Gray"
    bl_idname = 'color.ams_36357'
    def execute(self, context):
        set_base_color(0x9E9C8F, self.bl_label)
        return {'FINISHED'}

class AMS36373(bpy.types.Operator):
    """AMS36373 - Gray"""
    bl_label = "36373 Gray"
    bl_idname = 'color.ams_36373'
    def execute(self, context):
        set_base_color(0x9CA2A2, self.bl_label)
        return {'FINISHED'}

class AMS36375(bpy.types.Operator):
    """AMS36375 - Medium Gray"""
    bl_label = "36375 Medium Gray"
    bl_idname = 'color.ams_36375'
    def execute(self, context):
        set_base_color(0x9BA4AA, self.bl_label)
        return {'FINISHED'}

class AMS36405(bpy.types.Operator):
    """AMS36405 - Gray"""
    bl_label = "36405 Gray"
    bl_idname = 'color.ams_36405'
    def execute(self, context):
        set_base_color(0xBBB49D, self.bl_label)
        return {'FINISHED'}

class AMS36415(bpy.types.Operator):
    """AMS36415 - Beige Gray Stain"""
    bl_label = "36415 Beige Gray Stain"
    bl_idname = 'color.ams_36415'
    def execute(self, context):
        set_base_color(0xBAAA92, self.bl_label)
        return {'FINISHED'}

class AMS36424(bpy.types.Operator):
    """AMS36424 - Gray"""
    bl_label = "36424 Gray"
    bl_idname = 'color.ams_36424'
    def execute(self, context):
        set_base_color(0xBBB3A7, self.bl_label)
        return {'FINISHED'}

class AMS36440(bpy.types.Operator):
    """AMS36440 - Light Gray 81352 / ANA 602 / 620"""
    bl_label = "36440 Light Gray 81352 / ANA 602 / 620"
    bl_idname = 'color.ams_36440'
    def execute(self, context):
        set_base_color(0xADADA3, self.bl_label)
        return {'FINISHED'}

class AMS36463(bpy.types.Operator):
    """AMS36463 - Gray"""
    bl_label = "36463 Gray"
    bl_idname = 'color.ams_36463'
    def execute(self, context):
        set_base_color(0xA5A9A8, self.bl_label)
        return {'FINISHED'}

class AMS36473(bpy.types.Operator):
    """AMS36473 - Gray"""
    bl_label = "36473 Gray"
    bl_idname = 'color.ams_36473'
    def execute(self, context):
        set_base_color(0x9DA8A6, self.bl_label)
        return {'FINISHED'}

class AMS36480(bpy.types.Operator):
    """AMS36480 - Canada 501-109"""
    bl_label = "36480 Canada 501-109"
    bl_idname = 'color.ams_36480'
    def execute(self, context):
        set_base_color(0xAAB7B1, self.bl_label)
        return {'FINISHED'}

class AMS36492(bpy.types.Operator):
    """AMS36492 - Gray"""
    bl_label = "36492 Gray"
    bl_idname = 'color.ams_36492'
    def execute(self, context):
        set_base_color(0xBABAB4, self.bl_label)
        return {'FINISHED'}

class AMS36495(bpy.types.Operator):
    """AMS36495 - Gray"""
    bl_label = "36495 Gray"
    bl_idname = 'color.ams_36495'
    def execute(self, context):
        set_base_color(0xC2C7C4, self.bl_label)
        return {'FINISHED'}

class AMS36521(bpy.types.Operator):
    """AMS36521 - Gray"""
    bl_label = "36521 Gray"
    bl_idname = 'color.ams_36521'
    def execute(self, context):
        set_base_color(0xC2B6A8, self.bl_label)
        return {'FINISHED'}

class AMS36555(bpy.types.Operator):
    """AMS36555 - Beige"""
    bl_label = "36555 Beige"
    bl_idname = 'color.ams_36555'
    def execute(self, context):
        set_base_color(0xC8BDA1, self.bl_label)
        return {'FINISHED'}

class AMS36559(bpy.types.Operator):
    """AMS36559 - Gray"""
    bl_label = "36559 Gray"
    bl_idname = 'color.ams_36559'
    def execute(self, context):
        set_base_color(0xC0BFAE, self.bl_label)
        return {'FINISHED'}

class AMS36586(bpy.types.Operator):
    """AMS36586 - Gray"""
    bl_label = "36586 Gray"
    bl_idname = 'color.ams_36586'
    def execute(self, context):
        set_base_color(0xC8C0A7, self.bl_label)
        return {'FINISHED'}

class AMS36595(bpy.types.Operator):
    """AMS36595 - Gray"""
    bl_label = "36595 Gray"
    bl_idname = 'color.ams_36595'
    def execute(self, context):
        set_base_color(0xC1C3B3, self.bl_label)
        return {'FINISHED'}

class AMS36622(bpy.types.Operator):
    """AMS36622 - Gray"""
    bl_label = "36622 Gray"
    bl_idname = 'color.ams_36622'
    def execute(self, context):
        set_base_color(0xC1C1B4, self.bl_label)
        return {'FINISHED'}

class AMS36628(bpy.types.Operator):
    """AMS36628 - Gray"""
    bl_label = "36628 Gray"
    bl_idname = 'color.ams_36628'
    def execute(self, context):
        set_base_color(0xCBCEC7, self.bl_label)
        return {'FINISHED'}

class AMS36642(bpy.types.Operator):
    """AMS36642 - Gray"""
    bl_label = "36642 Gray"
    bl_idname = 'color.ams_36642'
    def execute(self, context):
        set_base_color(0xE0CCB7, self.bl_label)
        return {'FINISHED'}

class AMS36650(bpy.types.Operator):
    """AMS36650 - DLA Light Blue / Gray"""
    bl_label = "36650 DLA Light Blue / Gray"
    bl_idname = 'color.ams_36650'
    def execute(self, context):
        set_base_color(0xE2DFD8, self.bl_label)
        return {'FINISHED'}

class AMS37029(bpy.types.Operator):
    """AMS37029 - U.S. Army #477 / Black"""
    bl_label = "37029 U.S. Army #477 / Black"
    bl_idname = 'color.ams_37029'
    def execute(self, context):
        set_base_color(0x3B3C3D, self.bl_label)
        return {'FINISHED'}

class AMS37030(bpy.types.Operator):
    """AMS37030 - Black Camouflage"""
    bl_label = "37030 Black Camouflage"
    bl_idname = 'color.ams_37030'
    def execute(self, context):
        set_base_color(0x393A3A, self.bl_label)
        return {'FINISHED'}

class AMS37031(bpy.types.Operator):
    """AMS37031 - Interior Aircraft Black / Camouflage"""
    bl_label = "37031 Interior Aircraft Black / Camouflage"
    bl_idname = 'color.ams_37031'
    def execute(self, context):
        set_base_color(0x383939, self.bl_label)
        return {'FINISHED'}

class AMS37032(bpy.types.Operator):
    """AMS37032 - U.S. Army #557 / Black"""
    bl_label = "37032 U.S. Army #557 / Black"
    bl_idname = 'color.ams_37032'
    def execute(self, context):
        set_base_color(0x3C3C3C, self.bl_label)
        return {'FINISHED'}

class AMS37033(bpy.types.Operator):
    """AMS37033 - U.S. Army #458 / Black"""
    bl_label = "37033 U.S. Army #458 / Black"
    bl_idname = 'color.ams_37033'
    def execute(self, context):
        set_base_color(0x3C3C3E, self.bl_label)
        return {'FINISHED'}

class AMS37034(bpy.types.Operator):
    """AMS37034 - U.S. Army #3202 / Black"""
    bl_label = "37034 U.S. Army #3202 / Black"
    bl_idname = 'color.ams_37034'
    def execute(self, context):
        set_base_color(0x3C3D3E, self.bl_label)
        return {'FINISHED'}

class AMS37038(bpy.types.Operator):
    """AMS37038 - Black International / Navy #3 Black / ANA 604"""
    bl_label = "37038 Black International / Navy #3 Black / ANA 604"
    bl_idname = 'color.ams_37038'
    def execute(self, context):
        set_base_color(0x393A3A, self.bl_label)
        return {'FINISHED'}

class AMS37039(bpy.types.Operator):
    """AMS37039 - U.S. Army #2607 / Black"""
    bl_label = "37039 U.S. Army #2607 / Black"
    bl_idname = 'color.ams_37039'
    def execute(self, context):
        set_base_color(0x3E3F41, self.bl_label)
        return {'FINISHED'}

class AMS37056(bpy.types.Operator):
    """AMS37056 - Misc"""
    bl_label = "37056 Misc"
    bl_idname = 'color.ams_37056'
    def execute(self, context):
        set_base_color(0x4C4643, self.bl_label)
        return {'FINISHED'}

class AMS37100(bpy.types.Operator):
    """AMS37100 - Violet"""
    bl_label = "37100 Violet"
    bl_idname = 'color.ams_37100'
    def execute(self, context):
        set_base_color(0x684972, self.bl_label)
        return {'FINISHED'}

class AMS37142(bpy.types.Operator):
    """AMS37142 - Misc"""
    bl_label = "37142 Misc"
    bl_idname = 'color.ams_37142'
    def execute(self, context):
        set_base_color(0x92557F, self.bl_label)
        return {'FINISHED'}

class AMS37144(bpy.types.Operator):
    """AMS37144 - Misc"""
    bl_label = "37144 Misc"
    bl_idname = 'color.ams_37144'
    def execute(self, context):
        set_base_color(0x806687, self.bl_label)
        return {'FINISHED'}

class AMS37150(bpy.types.Operator):
    """AMS37150 - Misc"""
    bl_label = "37150 Misc"
    bl_idname = 'color.ams_37150'
    def execute(self, context):
        set_base_color(0xD0C8BA, self.bl_label)
        return {'FINISHED'}

class AMS37200(bpy.types.Operator):
    """AMS37200 - Misc"""
    bl_label = "37200 Misc"
    bl_idname = 'color.ams_37200'
    def execute(self, context):
        set_base_color(0x9C9D9D, self.bl_label)
        return {'FINISHED'}

class AMS37490(bpy.types.Operator):
    """AMS37490 - U.S. Army #559 / Dark Cream"""
    bl_label = "37490 U.S. Army #559 / Dark Cream"
    bl_idname = 'color.ams_37490'
    def execute(self, context):
        set_base_color(0x9D9482, self.bl_label)
        return {'FINISHED'}

class AMS37500(bpy.types.Operator):
    """AMS37500 - U.S. Army #524 / Cream"""
    bl_label = "37500 U.S. Army #524 / Cream"
    bl_idname = 'color.ams_37500'
    def execute(self, context):
        set_base_color(0xA79B85, self.bl_label)
        return {'FINISHED'}

class AMS37722(bpy.types.Operator):
    """AMS37722 - Misc"""
    bl_label = "37722 Misc"
    bl_idname = 'color.ams_37722'
    def execute(self, context):
        set_base_color(0xD9D4C4, self.bl_label)
        return {'FINISHED'}

class AMS37769(bpy.types.Operator):
    """AMS37769 - Misc"""
    bl_label = "37769 Misc"
    bl_idname = 'color.ams_37769'
    def execute(self, context):
        set_base_color(0xDFD3BC, self.bl_label)
        return {'FINISHED'}

class AMS37778(bpy.types.Operator):
    """AMS37778 - Misc"""
    bl_label = "37778 Misc"
    bl_idname = 'color.ams_37778'
    def execute(self, context):
        set_base_color(0xE7DFC7, self.bl_label)
        return {'FINISHED'}

class AMS37855(bpy.types.Operator):
    """AMS37855 - Eggshell / Ivory"""
    bl_label = "37855 Eggshell / Ivory"
    bl_idname = 'color.ams_37855'
    def execute(self, context):
        set_base_color(0xE9DCB9, self.bl_label)
        return {'FINISHED'}

class AMS37875(bpy.types.Operator):
    """AMS37875 - White Intl / ACFT Insignia White / ANA 601"""
    bl_label = "37875 White Intl / ACFT Insignia White / ANA 601"
    bl_idname = 'color.ams_37875'
    def execute(self, context):
        set_base_color(0xE4E6D8, self.bl_label)
        return {'FINISHED'}

class AMS37886(bpy.types.Operator):
    """AMS37886 - Misc"""
    bl_label = "37886 Misc"
    bl_idname = 'color.ams_37886'
    def execute(self, context):
        set_base_color(0xEDE8D5, self.bl_label)
        return {'FINISHED'}

class AMS37925(bpy.types.Operator):
    """AMS37925 - Misc"""
    bl_label = "37925 Misc"
    bl_idname = 'color.ams_37925'
    def execute(self, context):
        set_base_color(0xF0F0E3, self.bl_label)
        return {'FINISHED'}

class AMS37970(bpy.types.Operator):
    """AMS37970 - U.S. Army #521 / White"""
    bl_label = "37970 U.S. Army #521 / White"
    bl_idname = 'color.ams_37970'
    def execute(self, context):
        set_base_color(0xE3E7ED, self.bl_label)
        return {'FINISHED'}

class AMS37971(bpy.types.Operator):
    """AMS37971 - U.S. Army #2414 / White"""
    bl_label = "37971 U.S. Army #2414 / White"
    bl_idname = 'color.ams_37971'
    def execute(self, context):
        set_base_color(0xEAEDF2, self.bl_label)
        return {'FINISHED'}

class AMS38901(bpy.types.Operator):
    """AMS38901 - Fluorescent Green"""
    bl_label = "38901 Fluorescent Green"
    bl_idname = 'color.ams_38901'
    def execute(self, context):
        set_base_color(0x00A240, self.bl_label)
        return {'FINISHED'}

class AMS38903(bpy.types.Operator):
    """AMS38903 - Fluorescent Orange"""
    bl_label = "38903 Fluorescent Orange"
    bl_idname = 'color.ams_38903'
    def execute(self, context):
        set_base_color(0xFF4B19, self.bl_label)
        return {'FINISHED'}

class AMS38905(bpy.types.Operator):
    """AMS38905 - Fluorescent Red"""
    bl_label = "38905 Fluorescent Red"
    bl_idname = 'color.ams_38905'
    def execute(self, context):
        set_base_color(0xF33932, self.bl_label)
        return {'FINISHED'}

class AMS38907(bpy.types.Operator):
    """AMS38907 - Fluorescent Yellow"""
    bl_label = "38907 Fluorescent Yellow"
    bl_idname = 'color.ams_38907'
    def execute(self, context):
        set_base_color(0xFFAC00, self.bl_label)
        return {'FINISHED'}


# AMS PANEL

class AMSPanel(bpy.types.Panel):
    bl_idname = "AMS_PT_Panel"
    bl_label = "AMS"
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
        scol.label(text="", icon_value=g.c_icons["ams_10045"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10049"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10055"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10059"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10070"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10075"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10076"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10080"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10091"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10115"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10219"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10233"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10260"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10266"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10324"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_10371"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11086"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11105"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11120"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11136"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11140"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11302"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11310"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11328"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11330"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11350"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11400"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11630"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_11670"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12197"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12199"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12215"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12243"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12246"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12250"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12300"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12473"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_12648"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13275"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13415"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13432"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13507"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13522"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13523"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13531"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13538"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13578"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13591"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13594"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13596"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13613"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13618"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13637"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13655"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13670"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13690"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13695"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13711"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13740"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_13814"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14036"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14050"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14052"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14056"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14062"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14064"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14066"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14077"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14079"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14081"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14084"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14090"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14097"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14109"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14110"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14115"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14120"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14151"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14158"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14159"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14187"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14193"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14223"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14241"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14255"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14257"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14260"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14272"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14277"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14325"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14449"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14491"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14516"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14533"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14664"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_14672"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15042"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15044"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15045"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15048"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15050"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15051"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15052"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15055"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15056"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15065"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15080"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15090"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15092"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15095"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15102"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15107"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15109"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15123"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15125"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15177"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15180"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15182"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15187"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15193"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15200"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15450"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_15526"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16076"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16081"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16099"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16165"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16187"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16250"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16251"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16293"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16307"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16314"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16329"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16350"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16357"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16360"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16376"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16405"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16440"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16473"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16480"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16492"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16515"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_16555"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17038"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17043"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17100"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17142"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17155"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17178"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17773"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17778"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17855"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17860"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17865"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17875"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17877"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17886"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17925"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_17930"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20040"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20045"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20059"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20061"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20062"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20065"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20068"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20090"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20095"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20100"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20109"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20117"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20122"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20140"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20150"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20152"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20155"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20170"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20180"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20206"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20219"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20220"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20227"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20233"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20252"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20260"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20266"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20270"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20313"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20318"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20372"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20400"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20450"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20460"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_20475"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21105"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21136"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21158"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21302"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21310"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21400"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21433"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21575"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21643"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21667"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21668"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_21670"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22144"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22190"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22203"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22246"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22276"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22356"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22473"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22510"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22516"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22519"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22544"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22563"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22630"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_22648"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23275"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23420"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23430"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23435"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23448"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23522"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23525"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23530"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23531"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23538"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23540"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23564"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23578"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23594"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23613"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23617"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23619"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23640"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23655"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23685"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23690"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23695"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23697"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23711"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23717"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23722"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23727"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23785"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23793"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_23814"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24052"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24064"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24070"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24079"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24084"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24091"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24097"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24098"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24108"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24111"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24112"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24119"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24148"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24158"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24159"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24165"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24172a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24172b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24190"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24201"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24210"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24226"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24227"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24233"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24241"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24260"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24277"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24300"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24325"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24373"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24410"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24417"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24424"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24432"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24441"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24449"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24466"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24491"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24504"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24516"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24518"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24525"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24533"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24552"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24554"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24558"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24583"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24585"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24664"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24670"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_24672"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25042"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25044"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25045"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25048"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25049"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25051"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25052"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25053"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25056"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25060"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25095"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25102"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25109"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25177"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25183"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25184"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25185"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25189"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25190"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25193"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25200"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25230"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25237"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25240"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25299"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25352"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25414"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25440"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25488"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25526"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25530"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25550"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25622"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_25630"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26008"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26044"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26081"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26099"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26118"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26120"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26122"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26132"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26134"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26152"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26173"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26176"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26187"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26231"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26250"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26251"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26255"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26260"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26270"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26280"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26290"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26293"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26295"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26306"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26307"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26314"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26329"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26357"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26360"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26373"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26380"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26400"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26405"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26408"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26420"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26424"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26440"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26480"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26492"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26493"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26496"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26521"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26555"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26559"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26586"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26595"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26622"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_26630"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27038"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27040"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27041"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27043"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27142"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27144"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27722"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27769"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27778"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27780"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27855"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27875"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27880"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27885"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27886"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_27925"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_28913"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_28915"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30037"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30040"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30045"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30051"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30059"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30063"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30097"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30098"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30099"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30108"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30109"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30111"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30117"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30118"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30140"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30145"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30166"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30169"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30206"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30215"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30219"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30227"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30233"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30252"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30257"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30266"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30267"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30277"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30279"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30313"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30315"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30318"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30324"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30340"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30372"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30373"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30450"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30475"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_30480"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31090"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31100"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31136"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31158"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31302"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31310"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31348"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31400"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31433"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31575"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31638"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31643"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31667"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31668"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31669"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_31670"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32169"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32246"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32276"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32356"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32473"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32516"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32540"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32544"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32555"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32630"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_32648"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33070"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33105"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33245"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33275"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33303"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33434"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33440"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33446"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33448"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33481"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33510"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33522"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33531"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33538"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33564"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33578"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33613"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33617"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33637"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33654"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33655"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33685"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33690"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33695"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33696"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33711"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33717"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33722"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33727"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33793"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33798"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_33814"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34031"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34052"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34057"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34058"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34064"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34065"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34076"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34078"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34079"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34080"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34082"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34083"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34084"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34085"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34086"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34087"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34088"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34089"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34090"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34092"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34094"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34095"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34096"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34097"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34098"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34101"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34102"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34108"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34127"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34128"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34129"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34130"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34138"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34148"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34150"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34151"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34158"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34159"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34170"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34201"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34202"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34203"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34226"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34227"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34230"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34233"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34241"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34256"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34258"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34259"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34272"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34277"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34300"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34325"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34350"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34373"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34410"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34414"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34424"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34432"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34441"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34449"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34491"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34504"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34516"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34518"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34524"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34533"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34540"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34552"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34554"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34558"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34583"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34666"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34670"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_34672"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35039"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35040"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35041"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35042"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35043"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35044"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35045"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35046"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35047"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35048"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35052"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35056"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35095"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35109"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35164"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35177"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35180"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35183"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35189"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35190"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35193"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35231"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35237"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35240"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35250"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35260"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35275"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35299"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35352"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35414"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35450"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35466"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35488"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35526"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35550"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35622"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_35630"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36007"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36076"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36081"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36099"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36118"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36134"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36152"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36170"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36173"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36176"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36231"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36251"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36270"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36280"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36293"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36300"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36306"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36307"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36314"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36320"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36356"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36357"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36373"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36375"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36405"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36415"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36424"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36440"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36463"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36473"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36480"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36492"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36495"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36521"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36555"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36559"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36586"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36595"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36622"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36628"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36642"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_36650"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37029"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37030"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37031"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37032"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37033"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37034"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37038"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37039"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37056"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37100"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37142"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37144"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37150"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37200"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37490"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37500"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37722"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37769"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37778"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37855"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37875"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37886"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37925"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37970"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_37971"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_38901"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_38903"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_38905"].icon_id)
        scol.label(text="", icon_value=g.c_icons["ams_38907"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.ams_10045", text="10045 Brown")
        scol.operator("color.ams_10049", text="10049 Maroon 81352 / ANA 510")
        scol.operator("color.ams_10055", text="10055 DoT Highway Brown")
        scol.operator("color.ams_10059", text="10059 Brown")
        scol.operator("color.ams_10070", text="10070 Brown")
        scol.operator("color.ams_10075", text="10075 Brown")
        scol.operator("color.ams_10076", text="10076 Coast Guard Deck Red / Metallic Red-Brown")
        scol.operator("color.ams_10080", text="10080 Seal Brown / NASA Safety Brown")
        scol.operator("color.ams_10091", text="10091 Dark Oak")
        scol.operator("color.ams_10115", text="10115 Brown")
        scol.operator("color.ams_10219", text="10219 Brown")
        scol.operator("color.ams_10233", text="10233 Cocoa Brown / National Parks Service")
        scol.operator("color.ams_10260", text="10260 Brown")
        scol.operator("color.ams_10266", text="10266 Middlestone")
        scol.operator("color.ams_10324", text="10324 Brown")
        scol.operator("color.ams_10371", text="10371 Buff / TT-E-489")
        scol.operator("color.ams_11086", text="11086 DoT Highway Red")
        scol.operator("color.ams_11105", text="11105 OSHA Safety Red / DoT Highway Red")
        scol.operator("color.ams_11120", text="11120 OSHA Safety Red")
        scol.operator("color.ams_11136", text="11136 Insignia Red / Carmine Red")
        scol.operator("color.ams_11140", text="11140 OSHA Safety Red")
        scol.operator("color.ams_11302", text="11302 Red")
        scol.operator("color.ams_11310", text="11310 Post Office Red")
        scol.operator("color.ams_11328", text="11328 Red")
        scol.operator("color.ams_11330", text="11330 RCAF Snowbird Red I-4147")
        scol.operator("color.ams_11350", text="11350 Coast Guard Buoy Red")
        scol.operator("color.ams_11400", text="11400 Red")
        scol.operator("color.ams_11630", text="11630 Red")
        scol.operator("color.ams_11670", text="11670 Peach")
        scol.operator("color.ams_12160", text="12160 Orange-Brown")
        scol.operator("color.ams_12197", text="12197 International Orange / ANA 508")
        scol.operator("color.ams_12199", text="12199 Coast Guard Red #40")
        scol.operator("color.ams_12215", text="12215 Orange")
        scol.operator("color.ams_12243", text="12243 DoT Highway Orange")
        scol.operator("color.ams_12246", text="12246 OSHA Safety Orange")
        scol.operator("color.ams_12250", text="12250 Coast Guard Orange")
        scol.operator("color.ams_12300", text="12300 OSHA Safety Orange")
        scol.operator("color.ams_12473", text="12473 Orange")
        scol.operator("color.ams_12648", text="12648 Orange")
        scol.operator("color.ams_13275", text="13275 Post Office Yellow")
        scol.operator("color.ams_13415", text="13415 School Bus Yellow")
        scol.operator("color.ams_13432", text="13432 Yellow")
        scol.operator("color.ams_13507", text="13507 DoT Highway Yellow")
        scol.operator("color.ams_13522", text="13522 Yellow")
        scol.operator("color.ams_13523", text="13523 Yellow")
        scol.operator("color.ams_13531", text="13531 Beige")
        scol.operator("color.ams_13538", text="13538 DoT Highway Yellow / ANA 506")
        scol.operator("color.ams_13578", text="13578 Warm Gray")
        scol.operator("color.ams_13591", text="13591 OSHA Safety Yellow")
        scol.operator("color.ams_13594", text="13594 Aircraft Cream / ANA 507")
        scol.operator("color.ams_13596", text="13596 Yellow")
        scol.operator("color.ams_13613", text="13613 Buff")
        scol.operator("color.ams_13618", text="13618 Postal Service Cream")
        scol.operator("color.ams_13637", text="13637 Yellow")
        scol.operator("color.ams_13655", text="13655 OSHA Safety Yellow / ANA 505")
        scol.operator("color.ams_13670", text="13670 Yellow-Green")
        scol.operator("color.ams_13690", text="13690 Park Service Cream")
        scol.operator("color.ams_13695", text="13695 Ivory / Forest Service")
        scol.operator("color.ams_13711", text="13711 Yellow")
        scol.operator("color.ams_13740", text="13740 DLA Orphean Sand")
        scol.operator("color.ams_13814", text="13814 Yellow")
        scol.operator("color.ams_14036", text="14036 Green")
        scol.operator("color.ams_14050", text="14050 Army Green / NATO Green")
        scol.operator("color.ams_14052", text="14052 Marine Green #23")
        scol.operator("color.ams_14056", text="14056 Green")
        scol.operator("color.ams_14062", text="14062 Deep Green")
        scol.operator("color.ams_14064", text="14064 Green")
        scol.operator("color.ams_14066", text="14066 DoT Highway Green")
        scol.operator("color.ams_14077", text="14077 Green")
        scol.operator("color.ams_14079", text="14079 Green")
        scol.operator("color.ams_14081", text="14081 Sikorsky Green")
        scol.operator("color.ams_14084", text="14084 Green")
        scol.operator("color.ams_14090", text="14090 Green")
        scol.operator("color.ams_14097", text="14097 Green")
        scol.operator("color.ams_14109", text="14109 DoT Highway Green")
        scol.operator("color.ams_14110", text="14110 NASA Safety Medium Green")
        scol.operator("color.ams_14115", text="14115 Green")
        scol.operator("color.ams_14120", text="14120 OSHA Safety Green")
        scol.operator("color.ams_14151", text="14151 Green")
        scol.operator("color.ams_14158", text="14158 Green")
        scol.operator("color.ams_14159", text="14159 Green")
        scol.operator("color.ams_14187", text="14187 Oxygen Tank Green / ANA 503")
        scol.operator("color.ams_14193", text="14193 Coast Guard Green")
        scol.operator("color.ams_14223", text="14223 Green")
        scol.operator("color.ams_14241", text="14241 Green")
        scol.operator("color.ams_14255", text="14255 Green")
        scol.operator("color.ams_14257", text="14257 Green")
        scol.operator("color.ams_14260", text="14260 OSHA Safety Green")
        scol.operator("color.ams_14272", text="14272 Green")
        scol.operator("color.ams_14277", text="14277 Green")
        scol.operator("color.ams_14325", text="14325 Green")
        scol.operator("color.ams_14449", text="14449 Green")
        scol.operator("color.ams_14491", text="14491 Green")
        scol.operator("color.ams_14516", text="14516 Green")
        scol.operator("color.ams_14533", text="14533 Green")
        scol.operator("color.ams_14664", text="14664 Green")
        scol.operator("color.ams_14672", text="14672 Army Admin Vehicles")
        scol.operator("color.ams_15042", text="15042 Sea Blue / Teal Blue / ANA 623")
        scol.operator("color.ams_15044", text="15044 Dark Blue / Insignia Blue / ANA 502")
        scol.operator("color.ams_15045", text="15045 Strata Blue / Air Force Blue / ANA 516")
        scol.operator("color.ams_15048", text="15048 Post Office Dark Blue")
        scol.operator("color.ams_15050", text="15050 Post Office Box")
        scol.operator("color.ams_15051", text="15051 RCAF Snowbird Blue I-6256")
        scol.operator("color.ams_15052", text="15052 Post Office Medium Blue")
        scol.operator("color.ams_15055", text="15055 Blue")
        scol.operator("color.ams_15056", text="15056 Blue")
        scol.operator("color.ams_15065", text="15065 DoT Highway Blue")
        scol.operator("color.ams_15080", text="15080 Handicap Blue")
        scol.operator("color.ams_15090", text="15090 DoT Highway Blue")
        scol.operator("color.ams_15092", text="15092 OSHA Safety Blue")
        scol.operator("color.ams_15095", text="15095 Post Office Light Blue")
        scol.operator("color.ams_15102", text="15102 OSHA Safety Blue / ANA 501")
        scol.operator("color.ams_15107", text="15107 Blue")
        scol.operator("color.ams_15109", text="15109 Blue")
        scol.operator("color.ams_15123", text="15123 Bright Blue")
        scol.operator("color.ams_15125", text="15125 Blue")
        scol.operator("color.ams_15177", text="15177 Clear Blue")
        scol.operator("color.ams_15180", text="15180 Blue / 85285")
        scol.operator("color.ams_15182", text="15182 Coast Guard Blue")
        scol.operator("color.ams_15187", text="15187 Blue")
        scol.operator("color.ams_15193", text="15193 Light Blue")
        scol.operator("color.ams_15200", text="15200 Blue")
        scol.operator("color.ams_15450", text="15450 Blue")
        scol.operator("color.ams_15526", text="15526 Blue")
        scol.operator("color.ams_16076", text="16076 Coast Guard Deck Gray")
        scol.operator("color.ams_16081", text="16081 Dark Gray / ANA 513")
        scol.operator("color.ams_16099", text="16099 Coast Guard Blue Gray")
        scol.operator("color.ams_16160", text="16160 Gray")
        scol.operator("color.ams_16165", text="16165 Gray")
        scol.operator("color.ams_16187", text="16187 Mechanic Gray Navy Standard")
        scol.operator("color.ams_16250", text="16250 Gray")
        scol.operator("color.ams_16251", text="16251 Gray")
        scol.operator("color.ams_16293", text="16293 Gray")
        scol.operator("color.ams_16307", text="16307 Machinery Gray")
        scol.operator("color.ams_16314", text="16314 Gray")
        scol.operator("color.ams_16329", text="16329 Gray")
        scol.operator("color.ams_16350", text="16350 Gray")
        scol.operator("color.ams_16357", text="16357 Gray")
        scol.operator("color.ams_16360", text="16360 Gray")
        scol.operator("color.ams_16376", text="16376 Blue")
        scol.operator("color.ams_16405", text="16405 Parchment")
        scol.operator("color.ams_16440", text="16440 Light Gray 85285 / 81352")
        scol.operator("color.ams_16473", text="16473 Aircraft Gray / NASA / ANA 512")
        scol.operator("color.ams_16480", text="16480 Canada 501-109 Gloss")
        scol.operator("color.ams_16492", text="16492 Dawn Gray")
        scol.operator("color.ams_16515", text="16515 Boeing Gray 707")
        scol.operator("color.ams_16555", text="16555 Gray")
        scol.operator("color.ams_17038", text="17038 OSHA Black / ANA 515 / 622")
        scol.operator("color.ams_17043", text="17043 Gold")
        scol.operator("color.ams_17100", text="17100 Purple")
        scol.operator("color.ams_17142", text="17142 OSHA Safety Purple")
        scol.operator("color.ams_17155", text="17155 OSHA Safety Purple")
        scol.operator("color.ams_17178", text="17178 Silver/Aluminum Intl")
        scol.operator("color.ams_17773", text="17773 Blue White")
        scol.operator("color.ams_17778", text="17778 ")
        scol.operator("color.ams_17855", text="17855 ")
        scol.operator("color.ams_17860", text="17860 Coast Guard White")
        scol.operator("color.ams_17865", text="17865 Hawker Beechcraft White 17865")
        scol.operator("color.ams_17875", text="17875 Insignia White / ANA 511")
        scol.operator("color.ams_17877", text="17877 Coast Guard White")
        scol.operator("color.ams_17886", text="17886 Bone White")
        scol.operator("color.ams_17925", text="17925 Untinted White")
        scol.operator("color.ams_17930", text="17930 RCAF Snowbird White I-1310")
        scol.operator("color.ams_20040", text="20040 Brown")
        scol.operator("color.ams_20045", text="20045 Brown")
        scol.operator("color.ams_20059", text="20059 Forest Service Sign Standard")
        scol.operator("color.ams_20061", text="20061 Brown")
        scol.operator("color.ams_20062", text="20062 Brown")
        scol.operator("color.ams_20065", text="20065 Brown 356")
        scol.operator("color.ams_20068", text="20068 Madeira 1957")
        scol.operator("color.ams_20090", text="20090 Highland 480")
        scol.operator("color.ams_20095", text="20095 Brown")
        scol.operator("color.ams_20100", text="20100 Brown")
        scol.operator("color.ams_20109", text="20109 F. S. Seminal Brown")
        scol.operator("color.ams_20117", text="20117 Brown")
        scol.operator("color.ams_20122", text="20122 Brown")
        scol.operator("color.ams_20140", text="20140 Brown")
        scol.operator("color.ams_20150", text="20150 Coyote 476 / 498")
        scol.operator("color.ams_20152", text="20152 Brown")
        scol.operator("color.ams_20155", text="20155 Light Brown 493")
        scol.operator("color.ams_20170", text="20170 Olive Mohave")
        scol.operator("color.ams_20180", text="20180 Tan 499")
        scol.operator("color.ams_20206", text="20206 Brown")
        scol.operator("color.ams_20219", text="20219 Brown")
        scol.operator("color.ams_20220", text="20220 Light Coyote 481")
        scol.operator("color.ams_20227", text="20227 Brown")
        scol.operator("color.ams_20233", text="20233 Brown")
        scol.operator("color.ams_20252", text="20252 Rose")
        scol.operator("color.ams_20260", text="20260 Brown")
        scol.operator("color.ams_20266", text="20266 Brown")
        scol.operator("color.ams_20270", text="20270 Urban Tan 478")
        scol.operator("color.ams_20313", text="20313 Brown")
        scol.operator("color.ams_20318", text="20318 Brown")
        scol.operator("color.ams_20372", text="20372 Tan")
        scol.operator("color.ams_20400", text="20400 Brown")
        scol.operator("color.ams_20450", text="20450 Brown")
        scol.operator("color.ams_20460", text="20460 Mushroom")
        scol.operator("color.ams_20475", text="20475 Saudi Color #11 (Sang)")
        scol.operator("color.ams_21105", text="21105 Red")
        scol.operator("color.ams_21136", text="21136 Red")
        scol.operator("color.ams_21158", text="21158 Red")
        scol.operator("color.ams_21302", text="21302 Red")
        scol.operator("color.ams_21310", text="21310 Red")
        scol.operator("color.ams_21400", text="21400 Red")
        scol.operator("color.ams_21433", text="21433 Red")
        scol.operator("color.ams_21575", text="21575 Red")
        scol.operator("color.ams_21643", text="21643 Red")
        scol.operator("color.ams_21667", text="21667 Red")
        scol.operator("color.ams_21668", text="21668 Red")
        scol.operator("color.ams_21670", text="21670 Red")
        scol.operator("color.ams_22144", text="22144 Orange")
        scol.operator("color.ams_22190", text="22190 Orange")
        scol.operator("color.ams_22203", text="22203 Orange")
        scol.operator("color.ams_22246", text="22246 Orange")
        scol.operator("color.ams_22276", text="22276 Orange")
        scol.operator("color.ams_22356", text="22356 Orange")
        scol.operator("color.ams_22473", text="22473 Orange")
        scol.operator("color.ams_22510", text="22510 Orange")
        scol.operator("color.ams_22516", text="22516 Light Orange Brown")
        scol.operator("color.ams_22519", text="22519 Rosewood")
        scol.operator("color.ams_22544", text="22544 Orange")
        scol.operator("color.ams_22563", text="22563 Beachwood")
        scol.operator("color.ams_22630", text="22630 Buff")
        scol.operator("color.ams_22648", text="22648 Buff")
        scol.operator("color.ams_23275", text="23275 Orange")
        scol.operator("color.ams_23420", text="23420 Khaki 475")
        scol.operator("color.ams_23430", text="23430 Khaki P1")
        scol.operator("color.ams_23435", text="23435 Ligh Khaki 494")
        scol.operator("color.ams_23448", text="23448 Yellow")
        scol.operator("color.ams_23522", text="23522 Yellow")
        scol.operator("color.ams_23525", text="23525 Desert Sand 500/503")
        scol.operator("color.ams_23530", text="23530 Light Tan 479")
        scol.operator("color.ams_23531", text="23531 Light Mushroom")
        scol.operator("color.ams_23538", text="23538 Yellow")
        scol.operator("color.ams_23540", text="23540 Yellow")
        scol.operator("color.ams_23564", text="23564 Yellow")
        scol.operator("color.ams_23578", text="23578 Yellow")
        scol.operator("color.ams_23594", text="23594 Yellow")
        scol.operator("color.ams_23613", text="23613 Buff")
        scol.operator("color.ams_23617", text="23617 Yellow")
        scol.operator("color.ams_23619", text="23619 Yellow")
        scol.operator("color.ams_23640", text="23640 Yellow 13655")
        scol.operator("color.ams_23655", text="23655 Yellow")
        scol.operator("color.ams_23685", text="23685 Yellow")
        scol.operator("color.ams_23690", text="23690 Yellow")
        scol.operator("color.ams_23695", text="23695 Forest Service Sign Standard")
        scol.operator("color.ams_23697", text="23697 Sunglow")
        scol.operator("color.ams_23711", text="23711 Yellow")
        scol.operator("color.ams_23717", text="23717 Yellow")
        scol.operator("color.ams_23722", text="23722 Yellow")
        scol.operator("color.ams_23727", text="23727 Yellow")
        scol.operator("color.ams_23785", text="23785 Yellow")
        scol.operator("color.ams_23793", text="23793 Yellow")
        scol.operator("color.ams_23814", text="23814 Yellow")
        scol.operator("color.ams_24052", text="24052 Marine Green #23")
        scol.operator("color.ams_24064", text="24064 Green")
        scol.operator("color.ams_24070", text="24070 Army Green 491")
        scol.operator("color.ams_24079", text="24079 Green")
        scol.operator("color.ams_24084", text="24084 Green")
        scol.operator("color.ams_24091", text="24091 Green")
        scol.operator("color.ams_24097", text="24097 Green")
        scol.operator("color.ams_24098", text="24098 Green")
        scol.operator("color.ams_24108", text="24108 Green")
        scol.operator("color.ams_24111", text="24111 Dark Green 455")
        scol.operator("color.ams_24112", text="24112 Green 474")
        scol.operator("color.ams_24119", text="24119 Marine OG Green")
        scol.operator("color.ams_24148", text="24148 Green")
        scol.operator("color.ams_24158", text="24158 Green")
        scol.operator("color.ams_24159", text="24159 Green")
        scol.operator("color.ams_24165", text="24165 Foliage Green 502/504")
        scol.operator("color.ams_24172a", text="24172a MIL-P-24441 Primer")
        scol.operator("color.ams_24172b", text="24172b Green")
        scol.operator("color.ams_24190", text="24190 Green")
        scol.operator("color.ams_24201", text="24201 Green")
        scol.operator("color.ams_24210", text="24210 Light Green 354")
        scol.operator("color.ams_24226", text="24226 Green")
        scol.operator("color.ams_24227", text="24227 Green")
        scol.operator("color.ams_24233", text="24233 Green")
        scol.operator("color.ams_24241", text="24241 Green")
        scol.operator("color.ams_24260", text="24260 Green")
        scol.operator("color.ams_24277", text="24277 Green")
        scol.operator("color.ams_24300", text="24300 Green")
        scol.operator("color.ams_24325", text="24325 Green")
        scol.operator("color.ams_24373", text="24373 Green")
        scol.operator("color.ams_24410", text="24410 Green")
        scol.operator("color.ams_24417", text="24417 Green")
        scol.operator("color.ams_24424", text="24424 Green")
        scol.operator("color.ams_24432", text="24432 Green")
        scol.operator("color.ams_24441", text="24441 Green")
        scol.operator("color.ams_24449", text="24449 Green")
        scol.operator("color.ams_24466", text="24466 Green")
        scol.operator("color.ams_24491", text="24491 Green")
        scol.operator("color.ams_24504", text="24504 Green")
        scol.operator("color.ams_24516", text="24516 Clipper Blue")
        scol.operator("color.ams_24518", text="24518 Green")
        scol.operator("color.ams_24525", text="24525 Green")
        scol.operator("color.ams_24533", text="24533 Seafoam Green")
        scol.operator("color.ams_24552", text="24552 Green")
        scol.operator("color.ams_24554", text="24554 Green")
        scol.operator("color.ams_24558", text="24558 Green")
        scol.operator("color.ams_24583", text="24583 Green")
        scol.operator("color.ams_24585", text="24585 Postal Green")
        scol.operator("color.ams_24664", text="24664 Green")
        scol.operator("color.ams_24670", text="24670 Green")
        scol.operator("color.ams_24672", text="24672 Green")
        scol.operator("color.ams_25042", text="25042 Blue Sea / ANA 606")
        scol.operator("color.ams_25044", text="25044 RCAF Blue 25044")
        scol.operator("color.ams_25045", text="25045 Blue")
        scol.operator("color.ams_25048", text="25048 Blue")
        scol.operator("color.ams_25049", text="25049 Army Blue 450")
        scol.operator("color.ams_25051", text="25051 Blue")
        scol.operator("color.ams_25052", text="25052 Blue")
        scol.operator("color.ams_25053", text="25053 Royal Blue")
        scol.operator("color.ams_25056", text="25056 Blue")
        scol.operator("color.ams_25060", text="25060 Army Blue 451")
        scol.operator("color.ams_25095", text="25095 Blue")
        scol.operator("color.ams_25102", text="25102 Blue")
        scol.operator("color.ams_25109", text="25109 Blue")
        scol.operator("color.ams_25177", text="25177 Blue")
        scol.operator("color.ams_25183", text="25183 Blue")
        scol.operator("color.ams_25184", text="25184 Blue")
        scol.operator("color.ams_25185", text="25185 Blue")
        scol.operator("color.ams_25189", text="25189 Blue")
        scol.operator("color.ams_25190", text="25190 Blue")
        scol.operator("color.ams_25193", text="25193 Blue")
        scol.operator("color.ams_25200", text="25200 Blue")
        scol.operator("color.ams_25230", text="25230 Electrical Blue")
        scol.operator("color.ams_25237", text="25237 Blue")
        scol.operator("color.ams_25240", text="25240 Blue")
        scol.operator("color.ams_25299", text="25299 Blue")
        scol.operator("color.ams_25352", text="25352 Blue")
        scol.operator("color.ams_25414", text="25414 Blue")
        scol.operator("color.ams_25440", text="25440 Admiral Blue")
        scol.operator("color.ams_25488", text="25488 Blue")
        scol.operator("color.ams_25526", text="25526 Pastel Blue")
        scol.operator("color.ams_25530", text="25530 Carl Vinson Blue")
        scol.operator("color.ams_25550", text="25550 Blue")
        scol.operator("color.ams_25622", text="25622 Blue")
        scol.operator("color.ams_25630", text="25630 Blue")
        scol.operator("color.ams_26008", text="26008 Exterior Deck Gray")
        scol.operator("color.ams_26044", text="26044 Gray")
        scol.operator("color.ams_26081", text="26081 Sea Plane Gray / ANA 625")
        scol.operator("color.ams_26099", text="26099 Gray")
        scol.operator("color.ams_26118", text="26118 Gray")
        scol.operator("color.ams_26120", text="26120 Gray")
        scol.operator("color.ams_26122", text="26122 Gray")
        scol.operator("color.ams_26132", text="26132 Slate Gray")
        scol.operator("color.ams_26134", text="26134 Gray / Filing Cabinet")
        scol.operator("color.ams_26152", text="26152 Gray")
        scol.operator("color.ams_26173", text="26173 Ocean Gray / NAVSEA")
        scol.operator("color.ams_26176", text="26176 Ocean Gray")
        scol.operator("color.ams_26187", text="26187 Gray")
        scol.operator("color.ams_26231", text="26231 Gray")
        scol.operator("color.ams_26250", text="26250 Gray")
        scol.operator("color.ams_26251", text="26251 Gray")
        scol.operator("color.ams_26255", text="26255 Dark Gray 509")
        scol.operator("color.ams_26260", text="26260 Urban Gray 501/505")
        scol.operator("color.ams_26270", text="26270 Interior Haze Gray")
        scol.operator("color.ams_26280", text="26280 Gray")
        scol.operator("color.ams_26290", text="26290 Gray")
        scol.operator("color.ams_26293", text="26293 Gray")
        scol.operator("color.ams_26295", text="26295 Gray 510")
        scol.operator("color.ams_26306", text="26306 Sand Gray")
        scol.operator("color.ams_26307", text="26307 Bulkhead Machinery Gray #30")
        scol.operator("color.ams_26314", text="26314 Gray")
        scol.operator("color.ams_26329", text="26329 Gray")
        scol.operator("color.ams_26357", text="26357 Gray")
        scol.operator("color.ams_26360", text="26360 Gray")
        scol.operator("color.ams_26373", text="26373 Light Gray #37")
        scol.operator("color.ams_26380", text="26380 Medium Gray 508")
        scol.operator("color.ams_26400", text="26400 Yellow Gray")
        scol.operator("color.ams_26405", text="26405 Gray")
        scol.operator("color.ams_26408", text="26408 Gray")
        scol.operator("color.ams_26420", text="26420 DLA Light Blue/Gray")
        scol.operator("color.ams_26424", text="26424 Gray")
        scol.operator("color.ams_26440", text="26440 Gray")
        scol.operator("color.ams_26480", text="26480 Canada 501-109")
        scol.operator("color.ams_26492", text="26492 Gray")
        scol.operator("color.ams_26493", text="26493 Pearl Gray")
        scol.operator("color.ams_26496", text="26496 Green Gray")
        scol.operator("color.ams_26521", text="26521 Gray")
        scol.operator("color.ams_26555", text="26555 Gray")
        scol.operator("color.ams_26559", text="26559 Parchment")
        scol.operator("color.ams_26586", text="26586 Gray")
        scol.operator("color.ams_26595", text="26595 Gray")
        scol.operator("color.ams_26622", text="26622 Gray")
        scol.operator("color.ams_26630", text="26630 Light Gray 507")
        scol.operator("color.ams_27038", text="27038 ANA 514")
        scol.operator("color.ams_27040", text="27040 Filing Cabinet Black")
        scol.operator("color.ams_27041", text="27041 Black")
        scol.operator("color.ams_27043", text="27043 Gold")
        scol.operator("color.ams_27142", text="27142 Misc Purple")
        scol.operator("color.ams_27144", text="27144 Misc Purple")
        scol.operator("color.ams_27160", text="27160 Misc Purple")
        scol.operator("color.ams_27722", text="27722 Misc White")
        scol.operator("color.ams_27769", text="27769 Parchment")
        scol.operator("color.ams_27778", text="27778 Candlelight")
        scol.operator("color.ams_27780", text="27780 Misc White")
        scol.operator("color.ams_27855", text="27855 Misc Yellow White")
        scol.operator("color.ams_27875", text="27875 ANA 626")
        scol.operator("color.ams_27880", text="27880 Misc White")
        scol.operator("color.ams_27885", text="27885 White 506")
        scol.operator("color.ams_27886", text="27886 Misc White")
        scol.operator("color.ams_27925", text="27925 Misc White")
        scol.operator("color.ams_28913", text="28913 Fluorescent Red")
        scol.operator("color.ams_28915", text="28915 Fluorescent Orange")
        scol.operator("color.ams_30037", text="30037 U.S. Army #561 / Bark Brown")
        scol.operator("color.ams_30040", text="30040 Brown")
        scol.operator("color.ams_30045", text="30045 Brown")
        scol.operator("color.ams_30051", text="30051 Brown 383 Camouflage")
        scol.operator("color.ams_30059", text="30059 Brown")
        scol.operator("color.ams_30063", text="30063 U.S. Army #530 Dark Brown")
        scol.operator("color.ams_30097", text="30097 Earth Brown Camo")
        scol.operator("color.ams_30098", text="30098 U.S. Army #529 Brown")
        scol.operator("color.ams_30099", text="30099 Earth Brown")
        scol.operator("color.ams_30108", text="30108 Walnut Brown")
        scol.operator("color.ams_30109", text="30109 Dull Red / ANA 618")
        scol.operator("color.ams_30111", text="30111 Maroon Olympic Russet / Park Service Brown")
        scol.operator("color.ams_30117", text="30117 Brown International")
        scol.operator("color.ams_30118", text="30118 Field Drab Camo / ANA 617")
        scol.operator("color.ams_30140", text="30140 Brown International")
        scol.operator("color.ams_30145", text="30145 Butternut Stain")
        scol.operator("color.ams_30160", text="30160 Brown")
        scol.operator("color.ams_30166", text="30166 Brown")
        scol.operator("color.ams_30169", text="30169 U.S. Army #450 / Tan")
        scol.operator("color.ams_30206", text="30206 Brown")
        scol.operator("color.ams_30215", text="30215 Brown")
        scol.operator("color.ams_30219", text="30219 Sierra Tan / ANA 628")
        scol.operator("color.ams_30227", text="30227 Brown")
        scol.operator("color.ams_30233", text="30233 Brown")
        scol.operator("color.ams_30252", text="30252 Rust Red")
        scol.operator("color.ams_30257", text="30257 Earth Yellow")
        scol.operator("color.ams_30266", text="30266 Tan / ANA 615")
        scol.operator("color.ams_30267", text="30267 U.S. Army #M-1 / Khaki")
        scol.operator("color.ams_30277", text="30277 Sand")
        scol.operator("color.ams_30279", text="30279 Desert Sand / ANA 616")
        scol.operator("color.ams_30313", text="30313 Desert Sand")
        scol.operator("color.ams_30315", text="30315 Desert Sand Camo")
        scol.operator("color.ams_30318", text="30318 Brown")
        scol.operator("color.ams_30324", text="30324 Desert Sand")
        scol.operator("color.ams_30340", text="30340 Tan 380")
        scol.operator("color.ams_30372", text="30372 Brown")
        scol.operator("color.ams_30373", text="30373 U.S. Army #525 / Tan")
        scol.operator("color.ams_30450", text="30450 Beige")
        scol.operator("color.ams_30475", text="30475 Saudi Color #11 (Sang)")
        scol.operator("color.ams_30480", text="30480 Tan 459")
        scol.operator("color.ams_31090", text="31090 Earth Red Camo")
        scol.operator("color.ams_31100", text="31100 U.S. Army #453 / Maroon")
        scol.operator("color.ams_31136", text="31136 Red International / CARC Aircraft Red / ANA 619")
        scol.operator("color.ams_31158", text="31158 Light Red International")
        scol.operator("color.ams_31302", text="31302 Red")
        scol.operator("color.ams_31310", text="31310 Red")
        scol.operator("color.ams_31348", text="31348 U.S. Army #2501/2502/2510 / Scarlet")
        scol.operator("color.ams_31400", text="31400 Red")
        scol.operator("color.ams_31433", text="31433 Red")
        scol.operator("color.ams_31575", text="31575 Red")
        scol.operator("color.ams_31638", text="31638 Red")
        scol.operator("color.ams_31643", text="31643 Red")
        scol.operator("color.ams_31667", text="31667 Tan")
        scol.operator("color.ams_31668", text="31668 Red")
        scol.operator("color.ams_31669", text="31669 Red")
        scol.operator("color.ams_31670", text="31670 Red")
        scol.operator("color.ams_32169", text="32169 Orange")
        scol.operator("color.ams_32246", text="32246 Navy Torpedo")
        scol.operator("color.ams_32276", text="32276 Orange")
        scol.operator("color.ams_32356", text="32356 Orange")
        scol.operator("color.ams_32473", text="32473 Orange")
        scol.operator("color.ams_32516", text="32516 Orange")
        scol.operator("color.ams_32540", text="32540 Naviar Flat Orange #1")
        scol.operator("color.ams_32544", text="32544 Orange")
        scol.operator("color.ams_32555", text="32555 Orange")
        scol.operator("color.ams_32630", text="32630 Orange")
        scol.operator("color.ams_32648", text="32648 Orange")
        scol.operator("color.ams_33070", text="33070 Olive Drab Camo")
        scol.operator("color.ams_33105", text="33105 Field Drab Camouflage")
        scol.operator("color.ams_33245", text="33245 Earth Yellow Camouflage")
        scol.operator("color.ams_33275", text="33275 Yellow")
        scol.operator("color.ams_33303", text="33303 Sand Camouflage")
        scol.operator("color.ams_33434", text="33434 Yellow")
        scol.operator("color.ams_33440", text="33440 Green Gold Stain")
        scol.operator("color.ams_33446", text="33446 Tan 686A Camouflage")
        scol.operator("color.ams_33448", text="33448 Yellow")
        scol.operator("color.ams_33481", text="33481 Yellow")
        scol.operator("color.ams_33510", text="33510 Dark Sandstone Camouflage")
        scol.operator("color.ams_33522", text="33522 Tan")
        scol.operator("color.ams_33531", text="33531 Sand")
        scol.operator("color.ams_33538", text="33538 Yellow International / Traffic Yellow / ANA 614")
        scol.operator("color.ams_33564", text="33564 Yellow")
        scol.operator("color.ams_33578", text="33578 Yellow")
        scol.operator("color.ams_33613", text="33613 Yellow")
        scol.operator("color.ams_33617", text="33617 Sand / Tt-P-47")
        scol.operator("color.ams_33637", text="33637 Yellow")
        scol.operator("color.ams_33654", text="33654 U.S. Army #558 / Gold")
        scol.operator("color.ams_33655", text="33655 Yellow")
        scol.operator("color.ams_33685", text="33685 Yellow")
        scol.operator("color.ams_33690", text="33690 Very Light Sand")
        scol.operator("color.ams_33695", text="33695 Yellow")
        scol.operator("color.ams_33696", text="33696 Yellow")
        scol.operator("color.ams_33711", text="33711 Tan")
        scol.operator("color.ams_33717", text="33717 Yellow")
        scol.operator("color.ams_33722", text="33722 Yellow")
        scol.operator("color.ams_33727", text="33727 Yellow")
        scol.operator("color.ams_33793", text="33793 Yellow")
        scol.operator("color.ams_33798", text="33798 Yellow")
        scol.operator("color.ams_33814", text="33814 Yellow")
        scol.operator("color.ams_34031", text="34031 Aircraft Green Camouflage")
        scol.operator("color.ams_34052", text="34052 Marine Green #23")
        scol.operator("color.ams_34057", text="34057 U.S. Army #297 / Rifle Green")
        scol.operator("color.ams_34058", text="34058 Dark Blue Green")
        scol.operator("color.ams_34064", text="34064 Olive Drab 85285")
        scol.operator("color.ams_34065", text="34065 U.S. Army #2209 / Green")
        scol.operator("color.ams_34076", text="34076 U.S. Army / Ranger Green")
        scol.operator("color.ams_34078", text="34078 U.S. Army #2247/2248 / OD Green")
        scol.operator("color.ams_34079", text="34079 Army Forest Green / ANA 631")
        scol.operator("color.ams_34080", text="34080 U.S. Army #2212 / Green")
        scol.operator("color.ams_34082", text="34082 Dark Green Camouflage")
        scol.operator("color.ams_34083", text="34083 Air Force Forest Green")
        scol.operator("color.ams_34084", text="34084 Dark Green Camo")
        scol.operator("color.ams_34085", text="34085 U.S. Army Green #2243 / Green")
        scol.operator("color.ams_34086", text="34086 Army Forest Green Camo")
        scol.operator("color.ams_34087", text="34087 U.S. Army #523 / Belleau Wood Green")
        scol.operator("color.ams_34088", text="34088 Olive Drab CARC")
        scol.operator("color.ams_34089", text="34089 Light Green Camo")
        scol.operator("color.ams_34090", text="34090 Green")
        scol.operator("color.ams_34092", text="34092 Gunship Green / ANA 612")
        scol.operator("color.ams_34094", text="34094 Green 383 Camouflage")
        scol.operator("color.ams_34095", text="34095 Field Green")
        scol.operator("color.ams_34096", text="34096 Green")
        scol.operator("color.ams_34097", text="34097 Field Green / ANA 627")
        scol.operator("color.ams_34098", text="34098 Green")
        scol.operator("color.ams_34101", text="34101 U.S. Army #528 / Dark Green")
        scol.operator("color.ams_34102", text="34102 Dark Green")
        scol.operator("color.ams_34108", text="34108 Dark Green International / Navy Torpedo")
        scol.operator("color.ams_34127", text="34127 Light Green Camo")
        scol.operator("color.ams_34128", text="34128 Green")
        scol.operator("color.ams_34129", text="34129 Navair Flat Green #2")
        scol.operator("color.ams_34130", text="34130 Munsell Color 10y3/3")
        scol.operator("color.ams_34138", text="34138 Green")
        scol.operator("color.ams_34148", text="34148 Green")
        scol.operator("color.ams_34150", text="34150 U.S. Army #562 / Moss Green")
        scol.operator("color.ams_34151", text="34151 Interior Green TT-P-1757 / ANA 611")
        scol.operator("color.ams_34158", text="34158 Blue Drab")
        scol.operator("color.ams_34159", text="34159 Green")
        scol.operator("color.ams_34160", text="34160 Foliage Green")
        scol.operator("color.ams_34170", text="34170 Navair Flat Green #1")
        scol.operator("color.ams_34201", text="34201 Green")
        scol.operator("color.ams_34202", text="34202 U.S. Army #526 / Pale Green")
        scol.operator("color.ams_34203", text="34203 U.S. Army #560 / Light Sage")
        scol.operator("color.ams_34226", text="34226 NASA Primer")
        scol.operator("color.ams_34227", text="34227 Green")
        scol.operator("color.ams_34230", text="34230 Green")
        scol.operator("color.ams_34233", text="34233 Green")
        scol.operator("color.ams_34241", text="34241 Green")
        scol.operator("color.ams_34256", text="34256 U.S. Army #527 / Olive")
        scol.operator("color.ams_34258", text="34258 Green")
        scol.operator("color.ams_34259", text="34259 Green")
        scol.operator("color.ams_34272", text="34272 Green")
        scol.operator("color.ams_34277", text="34277 Sea Mist Green")
        scol.operator("color.ams_34300", text="34300 Green")
        scol.operator("color.ams_34325", text="34325 Green")
        scol.operator("color.ams_34350", text="34350 Forest Service Green")
        scol.operator("color.ams_34373", text="34373 Sagebrush")
        scol.operator("color.ams_34410", text="34410 Green")
        scol.operator("color.ams_34414", text="34414 Green")
        scol.operator("color.ams_34424", text="34424 ANA 610")
        scol.operator("color.ams_34432", text="34432 Green")
        scol.operator("color.ams_34441", text="34441 Green")
        scol.operator("color.ams_34449", text="34449 Light Green International")
        scol.operator("color.ams_34491", text="34491 Green")
        scol.operator("color.ams_34504", text="34504 Green")
        scol.operator("color.ams_34516", text="34516 Green")
        scol.operator("color.ams_34518", text="34518 Green")
        scol.operator("color.ams_34524", text="34524 Green")
        scol.operator("color.ams_34533", text="34533 Green")
        scol.operator("color.ams_34540", text="34540 Green")
        scol.operator("color.ams_34552", text="34552 Green")
        scol.operator("color.ams_34554", text="34554 Public Building Standard")
        scol.operator("color.ams_34558", text="34558 Light Green International")
        scol.operator("color.ams_34583", text="34583 Green")
        scol.operator("color.ams_34666", text="34666 Green")
        scol.operator("color.ams_34670", text="34670 Green")
        scol.operator("color.ams_34672", text="34672 Pastel Blue")
        scol.operator("color.ams_35039", text="35039 U.S. Army #2307 / Marine Dark Blue")
        scol.operator("color.ams_35040", text="35040 U.S. Army #2312 / Marine Dark Blue")
        scol.operator("color.ams_35041", text="35041 U.S. Army #450 / Blue")
        scol.operator("color.ams_35042", text="35042 Sea Blue / ANA 607")
        scol.operator("color.ams_35043", text="35043 U.S. Army #3378 / Blue")
        scol.operator("color.ams_35044", text="35044 Aircraft Insignia Blue / ANA 605")
        scol.operator("color.ams_35045", text="35045 Blue")
        scol.operator("color.ams_35046", text="35046 U.S. Army #2319 / Sky Blue")
        scol.operator("color.ams_35047", text="35047 U.S. Army #451 / Blue")
        scol.operator("color.ams_35048", text="35048 Blue")
        scol.operator("color.ams_35052", text="35052 Blue")
        scol.operator("color.ams_35056", text="35056 Blue")
        scol.operator("color.ams_35095", text="35095 Blue")
        scol.operator("color.ams_35109", text="35109 Light Blue International")
        scol.operator("color.ams_35164", text="35164 Navy Blue 212 / ANA 608")
        scol.operator("color.ams_35177", text="35177 Blue")
        scol.operator("color.ams_35180", text="35180 Blue")
        scol.operator("color.ams_35183", text="35183 Blue")
        scol.operator("color.ams_35189", text="35189 Blue")
        scol.operator("color.ams_35190", text="35190 Blue")
        scol.operator("color.ams_35193", text="35193 Blue")
        scol.operator("color.ams_35231", text="35231 ANA 609")
        scol.operator("color.ams_35237", text="35237 Blue Gray")
        scol.operator("color.ams_35240", text="35240 Blue")
        scol.operator("color.ams_35250", text="35250 UN Flag Blue")
        scol.operator("color.ams_35260", text="35260 Forest Service Blue")
        scol.operator("color.ams_35275", text="35275 Blue")
        scol.operator("color.ams_35299", text="35299 Blue")
        scol.operator("color.ams_35352", text="35352 Blue")
        scol.operator("color.ams_35414", text="35414 Blue Green")
        scol.operator("color.ams_35450", text="35450 Blue")
        scol.operator("color.ams_35466", text="35466 Blue")
        scol.operator("color.ams_35488", text="35488 Blue")
        scol.operator("color.ams_35526", text="35526 Blue")
        scol.operator("color.ams_35550", text="35550 Blue")
        scol.operator("color.ams_35622", text="35622 Blue")
        scol.operator("color.ams_35630", text="35630 Blue")
        scol.operator("color.ams_36007", text="36007 U.S. Army #548 / Slate Gray")
        scol.operator("color.ams_36076", text="36076 Navy Gray #2 / Dark Gray")
        scol.operator("color.ams_36081", text="36081 Deep Gray / F-4 Aircraft")
        scol.operator("color.ams_36099", text="36099 Dark Blue Gray")
        scol.operator("color.ams_36118", text="36118 Gunship Gray / ANA 603")
        scol.operator("color.ams_36134", text="36134 Gray")
        scol.operator("color.ams_36152", text="36152 Gray")
        scol.operator("color.ams_36170", text="36170 Camouflage Gray")
        scol.operator("color.ams_36173", text="36173 Ocean Gray / NAVSEA")
        scol.operator("color.ams_36176", text="36176 Ocean Gray")
        scol.operator("color.ams_36231", text="36231 Gray International / Aircraft Gray / ANA 621")
        scol.operator("color.ams_36251", text="36251 Gray")
        scol.operator("color.ams_36270", text="36270 Haze Gray")
        scol.operator("color.ams_36280", text="36280 Gray")
        scol.operator("color.ams_36293", text="36293 Gray")
        scol.operator("color.ams_36300", text="36300 Aircraft Gray Camouflage")
        scol.operator("color.ams_36306", text="36306 Gray")
        scol.operator("color.ams_36307", text="36307 Bulkhead Gray")
        scol.operator("color.ams_36314", text="36314 Gray")
        scol.operator("color.ams_36320", text="36320 Gray")
        scol.operator("color.ams_36356", text="36356 U.S. Army #2246 / Pewter")
        scol.operator("color.ams_36357", text="36357 Gray")
        scol.operator("color.ams_36373", text="36373 Gray")
        scol.operator("color.ams_36375", text="36375 Medium Gray")
        scol.operator("color.ams_36405", text="36405 Gray")
        scol.operator("color.ams_36415", text="36415 Beige Gray Stain")
        scol.operator("color.ams_36424", text="36424 Gray")
        scol.operator("color.ams_36440", text="36440 Light Gray 81352 / ANA 602 / 620")
        scol.operator("color.ams_36463", text="36463 Gray")
        scol.operator("color.ams_36473", text="36473 Gray")
        scol.operator("color.ams_36480", text="36480 Canada 501-109")
        scol.operator("color.ams_36492", text="36492 Gray")
        scol.operator("color.ams_36495", text="36495 Gray")
        scol.operator("color.ams_36521", text="36521 Gray")
        scol.operator("color.ams_36555", text="36555 Beige")
        scol.operator("color.ams_36559", text="36559 Gray")
        scol.operator("color.ams_36586", text="36586 Gray")
        scol.operator("color.ams_36595", text="36595 Gray")
        scol.operator("color.ams_36622", text="36622 Gray")
        scol.operator("color.ams_36628", text="36628 Gray")
        scol.operator("color.ams_36642", text="36642 Gray")
        scol.operator("color.ams_36650", text="36650 DLA Light Blue / Gray")
        scol.operator("color.ams_37029", text="37029 U.S. Army #477 / Black")
        scol.operator("color.ams_37030", text="37030 Black Camouflage")
        scol.operator("color.ams_37031", text="37031 Interior Aircraft Black / Camouflage")
        scol.operator("color.ams_37032", text="37032 U.S. Army #557 / Black")
        scol.operator("color.ams_37033", text="37033 U.S. Army #458 / Black")
        scol.operator("color.ams_37034", text="37034 U.S. Army #3202 / Black")
        scol.operator("color.ams_37038", text="37038 Black International / Navy #3 Black / ANA 604")
        scol.operator("color.ams_37039", text="37039 U.S. Army #2607 / Black")
        scol.operator("color.ams_37056", text="37056 Misc")
        scol.operator("color.ams_37100", text="37100 Violet")
        scol.operator("color.ams_37142", text="37142 Misc")
        scol.operator("color.ams_37144", text="37144 Misc")
        scol.operator("color.ams_37150", text="37150 Misc")
        scol.operator("color.ams_37200", text="37200 Misc")
        scol.operator("color.ams_37490", text="37490 U.S. Army #559 / Dark Cream")
        scol.operator("color.ams_37500", text="37500 U.S. Army #524 / Cream")
        scol.operator("color.ams_37722", text="37722 Misc")
        scol.operator("color.ams_37769", text="37769 Misc")
        scol.operator("color.ams_37778", text="37778 Misc")
        scol.operator("color.ams_37855", text="37855 Eggshell / Ivory")
        scol.operator("color.ams_37875", text="37875 White Intl / ACFT Insignia White / ANA 601")
        scol.operator("color.ams_37886", text="37886 Misc")
        scol.operator("color.ams_37925", text="37925 Misc")
        scol.operator("color.ams_37970", text="37970 U.S. Army #521 / White")
        scol.operator("color.ams_37971", text="37971 U.S. Army #2414 / White")
        scol.operator("color.ams_38901", text="38901 Fluorescent Green")
        scol.operator("color.ams_38903", text="38903 Fluorescent Orange")
        scol.operator("color.ams_38905", text="38905 Fluorescent Red")
        scol.operator("color.ams_38907", text="38907 Fluorescent Yellow")


# AMS CLASSES
array_ams = [
    AMSPanel,
    AMS10045,
    AMS10049,
    AMS10055,
    AMS10059,
    AMS10070,
    AMS10075,
    AMS10076,
    AMS10080,
    AMS10091,
    AMS10115,
    AMS10219,
    AMS10233,
    AMS10260,
    AMS10266,
    AMS10324,
    AMS10371,
    AMS11086,
    AMS11105,
    AMS11120,
    AMS11136,
    AMS11140,
    AMS11302,
    AMS11310,
    AMS11328,
    AMS11330,
    AMS11350,
    AMS11400,
    AMS11630,
    AMS11670,
    AMS12160,
    AMS12197,
    AMS12199,
    AMS12215,
    AMS12243,
    AMS12246,
    AMS12250,
    AMS12300,
    AMS12473,
    AMS12648,
    AMS13275,
    AMS13415,
    AMS13432,
    AMS13507,
    AMS13522,
    AMS13523,
    AMS13531,
    AMS13538,
    AMS13578,
    AMS13591,
    AMS13594,
    AMS13596,
    AMS13613,
    AMS13618,
    AMS13637,
    AMS13655,
    AMS13670,
    AMS13690,
    AMS13695,
    AMS13711,
    AMS13740,
    AMS13814,
    AMS14036,
    AMS14050,
    AMS14052,
    AMS14056,
    AMS14062,
    AMS14064,
    AMS14066,
    AMS14077,
    AMS14079,
    AMS14081,
    AMS14084,
    AMS14090,
    AMS14097,
    AMS14109,
    AMS14110,
    AMS14115,
    AMS14120,
    AMS14151,
    AMS14158,
    AMS14159,
    AMS14187,
    AMS14193,
    AMS14223,
    AMS14241,
    AMS14255,
    AMS14257,
    AMS14260,
    AMS14272,
    AMS14277,
    AMS14325,
    AMS14449,
    AMS14491,
    AMS14516,
    AMS14533,
    AMS14664,
    AMS14672,
    AMS15042,
    AMS15044,
    AMS15045,
    AMS15048,
    AMS15050,
    AMS15051,
    AMS15052,
    AMS15055,
    AMS15056,
    AMS15065,
    AMS15080,
    AMS15090,
    AMS15092,
    AMS15095,
    AMS15102,
    AMS15107,
    AMS15109,
    AMS15123,
    AMS15125,
    AMS15177,
    AMS15180,
    AMS15182,
    AMS15187,
    AMS15193,
    AMS15200,
    AMS15450,
    AMS15526,
    AMS16076,
    AMS16081,
    AMS16099,
    AMS16160,
    AMS16165,
    AMS16187,
    AMS16250,
    AMS16251,
    AMS16293,
    AMS16307,
    AMS16314,
    AMS16329,
    AMS16350,
    AMS16357,
    AMS16360,
    AMS16376,
    AMS16405,
    AMS16440,
    AMS16473,
    AMS16480,
    AMS16492,
    AMS16515,
    AMS16555,
    AMS17038,
    AMS17043,
    AMS17100,
    AMS17142,
    AMS17155,
    AMS17178,
    AMS17773,
    AMS17778,
    AMS17855,
    AMS17860,
    AMS17865,
    AMS17875,
    AMS17877,
    AMS17886,
    AMS17925,
    AMS17930,
    AMS20040,
    AMS20045,
    AMS20059,
    AMS20061,
    AMS20062,
    AMS20065,
    AMS20068,
    AMS20090,
    AMS20095,
    AMS20100,
    AMS20109,
    AMS20117,
    AMS20122,
    AMS20140,
    AMS20150,
    AMS20152,
    AMS20155,
    AMS20170,
    AMS20180,
    AMS20206,
    AMS20219,
    AMS20220,
    AMS20227,
    AMS20233,
    AMS20252,
    AMS20260,
    AMS20266,
    AMS20270,
    AMS20313,
    AMS20318,
    AMS20372,
    AMS20400,
    AMS20450,
    AMS20460,
    AMS20475,
    AMS21105,
    AMS21136,
    AMS21158,
    AMS21302,
    AMS21310,
    AMS21400,
    AMS21433,
    AMS21575,
    AMS21643,
    AMS21667,
    AMS21668,
    AMS21670,
    AMS22144,
    AMS22190,
    AMS22203,
    AMS22246,
    AMS22276,
    AMS22356,
    AMS22473,
    AMS22510,
    AMS22516,
    AMS22519,
    AMS22544,
    AMS22563,
    AMS22630,
    AMS22648,
    AMS23275,
    AMS23420,
    AMS23430,
    AMS23435,
    AMS23448,
    AMS23522,
    AMS23525,
    AMS23530,
    AMS23531,
    AMS23538,
    AMS23540,
    AMS23564,
    AMS23578,
    AMS23594,
    AMS23613,
    AMS23617,
    AMS23619,
    AMS23640,
    AMS23655,
    AMS23685,
    AMS23690,
    AMS23695,
    AMS23697,
    AMS23711,
    AMS23717,
    AMS23722,
    AMS23727,
    AMS23785,
    AMS23793,
    AMS23814,
    AMS24052,
    AMS24064,
    AMS24070,
    AMS24079,
    AMS24084,
    AMS24091,
    AMS24097,
    AMS24098,
    AMS24108,
    AMS24111,
    AMS24112,
    AMS24119,
    AMS24148,
    AMS24158,
    AMS24159,
    AMS24165,
    AMS24172a,
    AMS24172b,
    AMS24190,
    AMS24201,
    AMS24210,
    AMS24226,
    AMS24227,
    AMS24233,
    AMS24241,
    AMS24260,
    AMS24277,
    AMS24300,
    AMS24325,
    AMS24373,
    AMS24410,
    AMS24417,
    AMS24424,
    AMS24432,
    AMS24441,
    AMS24449,
    AMS24466,
    AMS24491,
    AMS24504,
    AMS24516,
    AMS24518,
    AMS24525,
    AMS24533,
    AMS24552,
    AMS24554,
    AMS24558,
    AMS24583,
    AMS24585,
    AMS24664,
    AMS24670,
    AMS24672,
    AMS25042,
    AMS25044,
    AMS25045,
    AMS25048,
    AMS25049,
    AMS25051,
    AMS25052,
    AMS25053,
    AMS25056,
    AMS25060,
    AMS25095,
    AMS25102,
    AMS25109,
    AMS25177,
    AMS25183,
    AMS25184,
    AMS25185,
    AMS25189,
    AMS25190,
    AMS25193,
    AMS25200,
    AMS25230,
    AMS25237,
    AMS25240,
    AMS25299,
    AMS25352,
    AMS25414,
    AMS25440,
    AMS25488,
    AMS25526,
    AMS25530,
    AMS25550,
    AMS25622,
    AMS25630,
    AMS26008,
    AMS26044,
    AMS26081,
    AMS26099,
    AMS26118,
    AMS26120,
    AMS26122,
    AMS26132,
    AMS26134,
    AMS26152,
    AMS26173,
    AMS26176,
    AMS26187,
    AMS26231,
    AMS26250,
    AMS26251,
    AMS26255,
    AMS26260,
    AMS26270,
    AMS26280,
    AMS26290,
    AMS26293,
    AMS26295,
    AMS26306,
    AMS26307,
    AMS26314,
    AMS26329,
    AMS26357,
    AMS26360,
    AMS26373,
    AMS26380,
    AMS26400,
    AMS26405,
    AMS26408,
    AMS26420,
    AMS26424,
    AMS26440,
    AMS26480,
    AMS26492,
    AMS26493,
    AMS26496,
    AMS26521,
    AMS26555,
    AMS26559,
    AMS26586,
    AMS26595,
    AMS26622,
    AMS26630,
    AMS27038,
    AMS27040,
    AMS27041,
    AMS27043,
    AMS27142,
    AMS27144,
    AMS27160,
    AMS27722,
    AMS27769,
    AMS27778,
    AMS27780,
    AMS27855,
    AMS27875,
    AMS27880,
    AMS27885,
    AMS27886,
    AMS27925,
    AMS28913,
    AMS28915,
    AMS30037,
    AMS30040,
    AMS30045,
    AMS30051,
    AMS30059,
    AMS30063,
    AMS30097,
    AMS30098,
    AMS30099,
    AMS30108,
    AMS30109,
    AMS30111,
    AMS30117,
    AMS30118,
    AMS30140,
    AMS30145,
    AMS30160,
    AMS30166,
    AMS30169,
    AMS30206,
    AMS30215,
    AMS30219,
    AMS30227,
    AMS30233,
    AMS30252,
    AMS30257,
    AMS30266,
    AMS30267,
    AMS30277,
    AMS30279,
    AMS30313,
    AMS30315,
    AMS30318,
    AMS30324,
    AMS30340,
    AMS30372,
    AMS30373,
    AMS30450,
    AMS30475,
    AMS30480,
    AMS31090,
    AMS31100,
    AMS31136,
    AMS31158,
    AMS31302,
    AMS31310,
    AMS31348,
    AMS31400,
    AMS31433,
    AMS31575,
    AMS31638,
    AMS31643,
    AMS31667,
    AMS31668,
    AMS31669,
    AMS31670,
    AMS32169,
    AMS32246,
    AMS32276,
    AMS32356,
    AMS32473,
    AMS32516,
    AMS32540,
    AMS32544,
    AMS32555,
    AMS32630,
    AMS32648,
    AMS33070,
    AMS33105,
    AMS33245,
    AMS33275,
    AMS33303,
    AMS33434,
    AMS33440,
    AMS33446,
    AMS33448,
    AMS33481,
    AMS33510,
    AMS33522,
    AMS33531,
    AMS33538,
    AMS33564,
    AMS33578,
    AMS33613,
    AMS33617,
    AMS33637,
    AMS33654,
    AMS33655,
    AMS33685,
    AMS33690,
    AMS33695,
    AMS33696,
    AMS33711,
    AMS33717,
    AMS33722,
    AMS33727,
    AMS33793,
    AMS33798,
    AMS33814,
    AMS34031,
    AMS34052,
    AMS34057,
    AMS34058,
    AMS34064,
    AMS34065,
    AMS34076,
    AMS34078,
    AMS34079,
    AMS34080,
    AMS34082,
    AMS34083,
    AMS34084,
    AMS34085,
    AMS34086,
    AMS34087,
    AMS34088,
    AMS34089,
    AMS34090,
    AMS34092,
    AMS34094,
    AMS34095,
    AMS34096,
    AMS34097,
    AMS34098,
    AMS34101,
    AMS34102,
    AMS34108,
    AMS34127,
    AMS34128,
    AMS34129,
    AMS34130,
    AMS34138,
    AMS34148,
    AMS34150,
    AMS34151,
    AMS34158,
    AMS34159,
    AMS34160,
    AMS34170,
    AMS34201,
    AMS34202,
    AMS34203,
    AMS34226,
    AMS34227,
    AMS34230,
    AMS34233,
    AMS34241,
    AMS34256,
    AMS34258,
    AMS34259,
    AMS34272,
    AMS34277,
    AMS34300,
    AMS34325,
    AMS34350,
    AMS34373,
    AMS34410,
    AMS34414,
    AMS34424,
    AMS34432,
    AMS34441,
    AMS34449,
    AMS34491,
    AMS34504,
    AMS34516,
    AMS34518,
    AMS34524,
    AMS34533,
    AMS34540,
    AMS34552,
    AMS34554,
    AMS34558,
    AMS34583,
    AMS34666,
    AMS34670,
    AMS34672,
    AMS35039,
    AMS35040,
    AMS35041,
    AMS35042,
    AMS35043,
    AMS35044,
    AMS35045,
    AMS35046,
    AMS35047,
    AMS35048,
    AMS35052,
    AMS35056,
    AMS35095,
    AMS35109,
    AMS35164,
    AMS35177,
    AMS35180,
    AMS35183,
    AMS35189,
    AMS35190,
    AMS35193,
    AMS35231,
    AMS35237,
    AMS35240,
    AMS35250,
    AMS35260,
    AMS35275,
    AMS35299,
    AMS35352,
    AMS35414,
    AMS35450,
    AMS35466,
    AMS35488,
    AMS35526,
    AMS35550,
    AMS35622,
    AMS35630,
    AMS36007,
    AMS36076,
    AMS36081,
    AMS36099,
    AMS36118,
    AMS36134,
    AMS36152,
    AMS36170,
    AMS36173,
    AMS36176,
    AMS36231,
    AMS36251,
    AMS36270,
    AMS36280,
    AMS36293,
    AMS36300,
    AMS36306,
    AMS36307,
    AMS36314,
    AMS36320,
    AMS36356,
    AMS36357,
    AMS36373,
    AMS36375,
    AMS36405,
    AMS36415,
    AMS36424,
    AMS36440,
    AMS36463,
    AMS36473,
    AMS36480,
    AMS36492,
    AMS36495,
    AMS36521,
    AMS36555,
    AMS36559,
    AMS36586,
    AMS36595,
    AMS36622,
    AMS36628,
    AMS36642,
    AMS36650,
    AMS37029,
    AMS37030,
    AMS37031,
    AMS37032,
    AMS37033,
    AMS37034,
    AMS37038,
    AMS37039,
    AMS37056,
    AMS37100,
    AMS37142,
    AMS37144,
    AMS37150,
    AMS37200,
    AMS37490,
    AMS37500,
    AMS37722,
    AMS37769,
    AMS37778,
    AMS37855,
    AMS37875,
    AMS37886,
    AMS37925,
    AMS37970,
    AMS37971,
    AMS38901,
    AMS38903,
    AMS38905,
    AMS38907,
]
