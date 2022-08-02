import bpy

from .panel_classes import *

# PCOY PANEL
class PMSPanel(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel"
    bl_label = "Pantone Color of the Year"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout


# 2000-09 PANEL
class PMSPanel2000(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2000"
    bl_label = "2000-09"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2000")
        scol.label(text="2001")
        scol.label(text="2002")
        scol.label(text="2003")
        scol.label(text="2004")
        scol.label(text="2005")
        scol.label(text="2006")
        scol.label(text="2007")
        scol.label(text="2008")
        scol.label(text="2009")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2000"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2001"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2002"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2003"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2004"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2005"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2006"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2007"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2008"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2009"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2000", text="Cerulean Blue")
        scol.operator("color.pms_2001", text="Fuschia Rose")
        scol.operator("color.pms_2002", text="True Red")
        scol.operator("color.pms_2003", text="Aqua Sky")
        scol.operator("color.pms_2004", text="Tigerlily")
        scol.operator("color.pms_2005", text="Blue Turquoise")
        scol.operator("color.pms_2006", text="Sand Dollar")
        scol.operator("color.pms_2007", text="Chili Pepper")
        scol.operator("color.pms_2008", text="Blue Iris")
        scol.operator("color.pms_2009", text="Mimosa")


# 2010-19 PANEL
class PMSPanel2010(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2010"
    bl_label = "2010-19"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2010")
        scol.label(text="2011")
        scol.label(text="2012")
        scol.label(text="2013")
        scol.label(text="2014")
        scol.label(text="2015")
        scol.label(text="2016")
        scol.label(text="2016")
        scol.label(text="2017")
        scol.label(text="2018")
        scol.label(text="2019")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2010"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2011"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2012"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2013"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2014"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2015"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2016a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2016b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2017"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2018"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2019"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2010", text="Turquoise")
        scol.operator("color.pms_2011", text="Honeysuckle")
        scol.operator("color.pms_2012", text="Tangerine")
        scol.operator("color.pms_2013", text="Emerald")
        scol.operator("color.pms_2014", text="Radiant Orchid")
        scol.operator("color.pms_2015", text="Marsala")
        scol.operator("color.pms_2016_a", text="Rose Quartz")
        scol.operator("color.pms_2016_b", text="Serenity")
        scol.operator("color.pms_2017", text="Greenery")
        scol.operator("color.pms_2018", text="Ultra Violet")
        scol.operator("color.pms_2019", text="Living Coral")


# 2020+ PANEL
class PMSPanel2020(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_2020"
    bl_label = "2020-29"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 0.5
        scol.label(text="2020")
        scol.label(text="2021")
        scol.label(text="2021")
        scol.label(text="2022")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2020"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2021a"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2021b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2022"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 2.0
        scol.operator("color.pms_2020", text="Classic Blue")
        scol.operator("color.pms_2021_a", text="Ultimate Gray")
        scol.operator("color.pms_2021_b", text="Illuminating")
        scol.operator("color.pms_2022", text="Very Peri")


# SS2022 LONDON PANEL
class PMSPanelSS2022London(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_SS2022London"
    bl_label = "SS2022 London"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pms_12_4401"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_13_1513"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_2042"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_19_4151"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_14_0850"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_16_4118"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_4728"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1019"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_3324"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1564"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_12_4401", text="Spun Sugar")
        scol.operator("color.pms_13_1513", text="Gossamer Pink")
        scol.operator("color.pms_18_2042", text="Innuendo")
        scol.operator("color.pms_19_4151", text="Skydiver")
        scol.operator("color.pms_14_0850", text="Daffodil")
        scol.operator("color.pms_16_4118", text="Glacier Lake")
        scol.operator("color.pms_18_4728", text="Harbor Blue")
        scol.operator("color.pms_18_1019", text="Coca Mocha")
        scol.operator("color.pms_18_3324", text="Dahlia")
        scol.operator("color.pms_18_1564", text="Poinciana")


# SS2022 NY PANEL
class PMSPanelSS2022NY(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_SS2022NY"
    bl_label = "SS2022 New York"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pms_14_5713"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_16_1349"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_4143"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_12_0825"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_13_2004"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_17_1928"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1160"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_15_0549"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_14_3612"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_18_1307"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_14_5713", text="Cascade")
        scol.operator("color.pms_16_1349", text="Coral Rose")
        scol.operator("color.pms_18_4143", text="Super Sonic")
        scol.operator("color.pms_12_0825", text="Popcorn")
        scol.operator("color.pms_13_2004", text="Potpourri")
        scol.operator("color.pms_17_1928", text="Bubblegum")
        scol.operator("color.pms_18_1160", text="Sudan Brown")
        scol.operator("color.pms_15_0549", text="Fragile Sprou")
        scol.operator("color.pms_14_3612", text="Orchid Bloo")
        scol.operator("color.pms_18_1307", text="Coffee Quartz")


# Extras & Apocrypha PANEL
class PMSPanelExtras(bpy.types.Panel):
    bl_idname = "PMS_PT_Panel_Extras"
    bl_label = "Extras & Apocrypha"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'PMS_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["pcoy_2020b"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pcoy_2043"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_prince"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_conan"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_uw"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_383"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_448"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_freedom_blue"].icon_id)
        scol.label(text="", icon_value=g.c_icons["pms_energizing_yellow"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.pms_bcoral", text="2020 Bleached Coral")
        scol.operator("color.pms_dcoral", text="2043 Dead Coral")
        scol.operator("color.pms_prince", text="Prince")
        scol.operator("color.pms_conan", text="Team Coco Orange")
        scol.operator("color.pms_uwign", text="United Way Unignorable")
        scol.operator("color.pms_383", text="A Nice Green")
        scol.operator("color.pms_448c", text="Ugliest Color in the World (Official)")
        scol.operator("color.pms_freedom_blue", text="Freedom Blue")
        scol.operator("color.pms_energizing_yellow", text="Energizing Yellow")
