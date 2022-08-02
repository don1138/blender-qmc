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
    "name"       : "QMC (Quick Material Colors)",
    "description": "Sets the Base Color of a Principled BSDF",
    "author"     : "Don Schnitzius",
    "version"    : (1, 0, 1),
    "blender"    : (2, 80, 0),
    "location"   : "3D Viewport > Sidebar > MAT > Quick Material Colors",
    "warning"    : "",
    "doc_url"    : "https://github.com/don1138/blender-qmc",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}


import os
import bpy
import bpy.utils.previews


# IMPORT COLOR CLASSES
from .color_sets.colors_f58 import *
from .color_sets.colors_ge import *
from .color_sets.colors_hg71 import *
from .color_sets.colors_moods import *
from .color_sets.colors_mcmc import *
from .color_sets.colors_pcoy import *
from .color_sets.colors_ss import *
from .color_sets.colors_sw_ext import *
from .color_sets.colors_sw_int import *
from .color_sets.colors_sw_ja import *


# IMPORT GLOBALS
from .panels.panel_classes import *


# BOOLEAN FOR PANEL
class QMC_SETTINGS(bpy.types.PropertyGroup):
    rename_material_more: bpy.props.BoolProperty(
        name='Rename Material',
        default=False
    )
    world_color_more: bpy.props.BoolProperty(
        name='World Background',
        default=False
    )


# PARENT PANEL
class QMCPanel(bpy.types.Panel):
    bl_idname = "QMC_PT_Panel"
    bl_label = "Quick Material Colors"
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

# IMPORT PANELS
from .panels.panel_f58 import *
from .panels.panel_ge import *
from .panels.panel_hg71 import *
from .panels.panel_moods import *
from .panels.panel_mcmc import *
from .panels.panel_pcoy import *
from .panels.panel_ss import *
from .panels.panel_sw_ext import *
from .panels.panel_sw_int import *
from .panels.panel_sw_ja import *



classes = [
    QMC_SETTINGS,
    QMCPanel,
    F1958Panel,
    HG71Panel,
    HG71_YELLOW_Panel,
    HG71_GREEN_Panel,
    HG71_BLUE_Panel,
    HG71_ORANGE_Panel,
    HG71_RED_Panel,
    HG71_PURPLE_Panel,
    HG71_GRAY_Panel,
    GEPanel,
    MCMCPanel,
    PMSPanel,
    PMSPanel2000,
    PMSPanel2010,
    PMSPanel2020,
    PMSPanelSS2022London,
    PMSPanelSS2022NY,
    PMSPanelExtras,
    PMSPanelSchnitzius,
    SMEPanel,
    SME_APanel,
    SME_BPanel,
    SME_CPanel,
    SME_DPanel,
    SME_EPanel,
    SME_FPanel,
    SME_GPanel,
    SME_HPanel,
    SME_JPanel,
    SMIPanel,
    JAPanel,
    MOODSPanel,
    MOODRELAXPanel,
    MOODENERGYPanel,
    MOODCOZYPanel,
    MOODFOCUSPanel,
    MOODMOODYPanel,
    # MOODWHITESPanel,
# F58 COLORS
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
# HG71 COLORS
    HG71Pineapple,
    HG71SunYellow,
    HG71Kumquat,
    HG71Goldenrod,
    HG71AntiqueGold,
    HG71MapleSugar,
    HG71Pongee,
    HG71MossGreen,
    HG71LacquerGreen,
    HG71GreenMint,
    HG71ParrotGreen,
    HG71Lettuce,
    HG71Celery,
    HG71MidnightBlue,
    HG71UltramarineBlue,
    HG71SpaceBlue,
    HG71BlueOpaline,
    HG71BlueSky,
    HG71AquamarineBlue,
    HG71Bittersweet,
    HG71Tangerine,
    HG71PompeiianRed,
    HG71Zinnia,
    HG71CreamyApricot,
    HG71VelvetBrown,
    HG71FlagRed,
    HG71PinkCoral,
    HG71PinkPink,
    HG71Azalea,
    HG71BeachPlum,
    HG71AfricanViolet,
    HG71Lavender,
    HG71OysterWhite,
    HG71Mercury,
    HG71Mushroom,
    HG71BlackPearl,
#MCMC COLORS
    MCMCGINGER_ALE,
    MCMCPABLO_HONEY,
    MCMCMIAMI_PARASOL,
    MCMCTANLINES,
    MCMCBLUE_SEAFOAM,
    MCMCSATURDAY_ON_SUNDAY,
    MCMCSICILY_OR_CYPRUS,
    MCMCNOVELTY_WAVE,
    MCMCRELENTLESS_OLIVE,
    MCMCGREEN_ROOT,
    MCMCSAGED,
    MCMCDRIVE_THRU_SAFARI,
    MCMCNATURAL_HABITAT,
    MCMCCHEROKEE_RED,
    MCMCLIPSTICK_ON_THE_MIRROR,
    MCMCSELF_PORTRAIT,
    MCMCNEGRONI,
    MCMCAUTUMN_GLIMMER,
    MCMCORANGE_FRUIT,
    MCMCAPERITIVO_HOUR,
    MCMCBRIGHT_MARIGOLD,
    MCMCWRIGHT_SOFT_GRAY,
    MCMCAFTER_HOURS,
    MCMCMOTOR_GRAY,
    MCMCNO_CURFEW,
    MCMCCOCOA_SHELL,
    MCMCFAWN_DOE,
    MCMCSENTIMENTAL_REASONS,
    MCMCCOBBLESTONE_STREETS,
    MCMCYELLOWS,
    MCMCBLUES,
    MCMCGREENS,
    MCMCREDS,
    MCMCORANGES,
    MCMCGRAYS,
    MCMCBROWNS,
#PCOY COLORS
    PMS2000,
    PMS2001,
    PMS2002,
    PMS2003,
    PMS2004,
    PMS2005,
    PMS2006,
    PMS2007,
    PMS2008,
    PMS2009,
    PMS2010,
    PMS2011,
    PMS2012,
    PMS2013,
    PMS2014,
    PMS2015,
    PMS2016A,
    PMS2016B,
    PMS2017,
    PMS2018,
    PMS2019,
    PMS2020,
    PMS2021A,
    PMS2021B,
    PMS2022,
    PMSPrince,
    PMSConan,
    PMSBCoral,
    PMSSDCoral,
    PMSUnignorable,
    PMS383,
    PMS448C,
    PMSFreedomBlue,
    PMSEnergizingYellow,
# SCHNITZIUS SELECTS COLORS
    SCHNITZIUS_GREEN,
    PMS_381U,
    SCHNITZIUS_RED,
    PMS_172_C,
    SCHNITZIUS_BLUE,
    PMS_2685U,
    SCHNITZIUS_YELLOW,
    PMS_396U,
    SCHNITZIUS_BRONZE_PALE,
    PMS_729U,
    SCHNITZIUS_BRONZE_RICH,
    PMS_7518U,
    SCHNITZIUS_WHITE,
    PMS_7499U,
    PMS12_4401,
    PMS13_1513,
    PMS18_2042,
    PMS19_4151,
    PMS14_0850,
    PMS16_4118,
    PMS18_4728,
    PMS18_1019,
    PMS18_3324,
    PMS18_1564,
    PMS14_5713,
    PMS16_1349,
    PMS18_4143,
    PMS12_0825,
    PMS13_2004,
    PMS17_1928,
    PMS18_1160,
    PMS15_0549,
    PMS14_3612,
    PMS18_1307,
#SW INTERIOR COLORS
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
# SW EXTERIOR COLORS
    SMBirdseyeMaple,
    SMCocoon,
    SMOldeWorldGold,
    SMWoolSkein,
    SMArtisanTan,
    SMStatusBronze,
    SMTatamiTan,
    SMColonyBuff,
    SMHomburgGray,
    SMMuslin,
    SMStrawHarvest,
    SMRuralGreen,
    SMExtraWhite,
    SMRushingRiver,
    SMSpicedCider,
    SMRetreat,
    SMNetsuke,
    SMEdgyGold,
    SMJoggingPath,
    SMIntellectualGray,
    SMThunderGray,
    SMAnjouPear,
    SMJerseyCream,
    SMWarmStone,
    SMCorkWedge,
    SMSmokehouse,
    SMRusticRed,
# JAZZ AGE COLORS
    JAChineseRed,
    JAJazzAgeCoral,
    JAFrostwork,
    JAAlexandrite,
    JASalonRose,
    JAStudioMauve,
    JABlueSky,
    JABluePeacock,
# GE COLORS
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
# MOODS COLORS
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
    # MoodsWhite04,
    # MoodsWhite03,
    # MoodsWhite02,
    # MoodsWhite01,
]


def register():
    # LOAD CUSTOM ICONS
    addon_path =  os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")
    for entry in os.listdir(icons_dir):
        g.c_icons.load(os.path.splitext(entry)[0], os.path.join(icons_dir, entry), "IMAGE")
    # Register the example panel, to show updater buttons.
    for cls in classes:
        bpy.utils.register_class(cls)
        bpy.types.Scene.more_bool = bpy.props.PointerProperty(type=QMC_SETTINGS)
        bpy.types.Scene.world_bool = bpy.props.PointerProperty(type=QMC_SETTINGS)


def unregister():
#   UNREGISTER ICONS
    bpy.utils.previews.remove(g.c_icons)
    del bpy.types.Scene.more_bool
    del bpy.types.Scene.world_bool
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
