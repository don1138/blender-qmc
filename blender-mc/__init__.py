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
    "version"    : (0, 10, 0),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > More Colors",
    "warning"    : "",
    "doc_url"    : "https://github.com/don1138/blender-pcoy",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}



import os
import bpy
import bpy.utils.previews



# BOOLEAN FOR PANEL
class MORE_SETTINGS(bpy.types.PropertyGroup):
    rename_material_more: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )
    world_color_more: bpy.props.BoolProperty(
        name='World Background',
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
        world_bool = context.scene.world_bool

        col = layout.column(align=True)
        col.prop(more_bool, "rename_material_more")

        col = layout.column(align=True)
        col.prop(world_bool, "world_color_more")

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


from .color_sets.colors_f58 import *
from .color_sets.colors_ge import *
from .color_sets.colors_moods import *
# from .color_sets.colors_sw_ext import *
from .color_sets.colors_sw_int import *
from .color_sets.colors_sw_ja import *


classes = [
    MORE_SETTINGS,
    MOREWPanel,
    F1958Panel,
    GEPanel,
    SMIPanel,
    # SMEPanel,
    JAPanel,
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
        bpy.types.Scene.world_bool = bpy.props.PointerProperty(type=MORE_SETTINGS)


def unregister():
    # Addon updater unregister.
#    addon_updater_ops.unregister()
#   UNREGISTER ICONS
    global c_icons
    bpy.utils.previews.remove(c_icons)

    del bpy.types.Scene.more_bool
    del bpy.types.Scene.world_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
