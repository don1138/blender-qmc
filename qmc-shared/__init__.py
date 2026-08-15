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
    "description": "Sets the Base Color of a Material Shader",
    "author"     : "Don Schnitzius",
    "version"    : (1, 16, 2),
    "blender"    : (4, 5, 0),
    "location"   : "3D Viewport > Sidebar > MAT > Quick Material Colors",
    "warning"    : "",
    "doc_url"    : "https://github.com/don1138/blender-qmc",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}


import os
import bpy
import bpy.utils.previews


# IMPORT GLOBALS
from .color_sets.globals import *
from .color_sets.color_functions import set_base_color
from .color_index import COLOR_INDEX as QMC_COLOR_INDEX
from .color_search import ALL_HUES, find_colors

try:
    from .color_index_plus import COLOR_INDEX as QMC_PLUS_COLOR_INDEX
except ModuleNotFoundError:
    QMC_PLUS_COLOR_INDEX = ()


COLOR_RECORDS = QMC_COLOR_INDEX + QMC_PLUS_COLOR_INDEX
INITIAL_RESULT_LIMIT = 50
RESULT_LIMIT_STEP = 50


def reset_finder_limit(self, context):
    if context is not None and getattr(context, "window_manager", None) is not None:
        context.window_manager.qmc_finder.visible_limit = INITIAL_RESULT_LIMIT


def update_finder_query(self, context):
    query_active = bool(self.query.strip())
    if query_active and not self.query_active:
        self.sort_mode = 'RELEVANCE'
    elif not query_active and self.sort_mode == 'RELEVANCE':
        self.sort_mode = 'ALPHABETICAL'
    self.query_active = query_active
    reset_finder_limit(self, context)


def update_finder_sort(self, context):
    if self.sort_mode == 'RELEVANCE' and not self.query.strip():
        self.sort_mode = 'ALPHABETICAL'
    reset_finder_limit(self, context)


def version_label():
    return ".".join(str(part) for part in bl_info["version"])


def collection_options():
    options = {
        (record["collection_key"], record["collection_name"])
        for record in COLOR_RECORDS
    }
    return sorted(options, key=lambda item: (item[1].casefold(), item[0]))


def initialize_collection_filters(window_manager):
    finder = window_manager.qmc_finder
    expected = collection_options()
    current = {item.collection_key: item.selected for item in finder.collections}
    if [item.collection_key for item in finder.collections] == [key for key, _ in expected]:
        return
    finder.collections.clear()
    for key, label in expected:
        item = finder.collections.add()
        item.collection_key = key
        item.label = label
        item.selected = current.get(key, True)


def selected_collection_keys(finder):
    selected = {item.collection_key for item in finder.collections if item.selected}
    if len(selected) == len(finder.collections):
        return None
    return selected


def finder_page(finder):
    return find_colors(
        COLOR_RECORDS,
        query=finder.query,
        hue=finder.hue,
        collections=selected_collection_keys(finder),
        sort=finder.sort_mode,
        descending=finder.descending,
        limit=finder.visible_limit,
    )


class QMC_COLLECTION_FILTER_ITEM(bpy.types.PropertyGroup):
    collection_key: bpy.props.StringProperty(options={'HIDDEN'})
    label: bpy.props.StringProperty(options={'HIDDEN'})
    selected: bpy.props.BoolProperty(name="", default=True, update=reset_finder_limit)


class QMC_FINDER_SETTINGS(bpy.types.PropertyGroup):
    query: bpy.props.StringProperty(
        name="Search",
        description="Search color names, codes, and collection names",
        default="",
        update=update_finder_query,
    )
    query_active: bpy.props.BoolProperty(default=False, options={'HIDDEN', 'SKIP_SAVE'})
    hue: bpy.props.EnumProperty(
        name="Hue",
        items=(
            ('ALL', "All", "Do not filter by hue"),
            ('NEUTRAL', "Neutral", "Show colors at or below 5% HSV saturation"),
            ('RED', "Red", "Show red colors"),
            ('YELLOW', "Yellow", "Show yellow colors"),
            ('GREEN', "Green", "Show green colors"),
            ('CYAN', "Cyan", "Show cyan colors"),
            ('BLUE', "Blue", "Show blue colors"),
            ('MAGENTA', "Magenta", "Show magenta colors"),
        ),
        default='ALL',
        update=reset_finder_limit,
    )
    sort_mode: bpy.props.EnumProperty(
        name="Sort",
        items=(
            ('RELEVANCE', "Relevance", "Rank text matches by relevance"),
            ('ALPHABETICAL', "Alphabetical", "Sort by color name"),
            ('COLLECTION', "Collection", "Group by collection, then color name"),
        ),
        default='ALPHABETICAL',
        update=update_finder_sort,
    )
    descending: bpy.props.BoolProperty(
        name="Descending",
        description="Reverse alphabetical or collection order",
        default=False,
        update=reset_finder_limit,
    )
    visible_limit: bpy.props.IntProperty(
        name="Visible Results",
        default=INITIAL_RESULT_LIMIT,
        min=INITIAL_RESULT_LIMIT,
        options={'HIDDEN', 'SKIP_SAVE'},
    )
    collections: bpy.props.CollectionProperty(type=QMC_COLLECTION_FILTER_ITEM)


# BOOLEAN FOR PANEL
class QMC_SETTINGS(bpy.types.PropertyGroup):
    active_node_more: bpy.props.BoolProperty(name="",default=False)
    rename_material_more: bpy.props.BoolProperty(name="",default=False)
    diffuse_more: bpy.props.BoolProperty(name="",default=False)
    world_color_more: bpy.props.BoolProperty(name="",default=False)


# PARENT PANEL
class QMCPanel(bpy.types.Panel):
    bl_idname = "QMC_PT_Panel"
    bl_label = f"Quick Material Colors — {version_label()}"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Quick Tools"
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        active_bool = context.scene.active_bool
        more_bool = context.scene.more_bool
        diffuse_bool = context.scene.diffuse_bool
        world_bool = context.scene.world_bool

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.prop(active_bool, "active_node_more")
        scol.prop(more_bool, "rename_material_more")
        scol.prop(diffuse_bool, "diffuse_more")
        scol.prop(world_bool, "world_color_more")

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.label(text="Selected Nodes Only")
        scol.label(text="Rename Material")
        scol.label(text="Set Viewport Color")
        scol.label(text="Set World Background")


class QMC_OT_CLEAR_SEARCH(bpy.types.Operator):
    bl_idname = "qmc.clear_color_search"
    bl_label = "Clear Search"
    bl_description = "Clear the Color Finder text search"

    def execute(self, context):
        context.window_manager.qmc_finder.query = ""
        return {'FINISHED'}


class QMC_OT_TOGGLE_SORT_DIRECTION(bpy.types.Operator):
    bl_idname = "qmc.toggle_color_sort_direction"
    bl_label = "Toggle Sort Direction"

    @classmethod
    def description(cls, context, properties):
        finder = context.window_manager.qmc_finder
        return "Switch to ascending order" if finder.descending else "Switch to descending order"

    def execute(self, context):
        finder = context.window_manager.qmc_finder
        finder.descending = not finder.descending
        return {'FINISHED'}


class QMC_OT_SET_COLLECTION_FILTERS(bpy.types.Operator):
    bl_idname = "qmc.set_collection_filters"
    bl_label = "Set Collection Filters"

    selected: bpy.props.BoolProperty(options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, properties):
        return "Select all collections" if properties.selected else "Clear all collections"

    def execute(self, context):
        finder = context.window_manager.qmc_finder
        for item in finder.collections:
            item.selected = self.selected
        finder.visible_limit = INITIAL_RESULT_LIMIT
        return {'FINISHED'}


class QMC_OT_SHOW_MORE_COLORS(bpy.types.Operator):
    bl_idname = "qmc.show_more_colors"
    bl_label = "Show More"
    bl_description = "Show the next 50 matching colors"

    def execute(self, context):
        context.window_manager.qmc_finder.visible_limit += RESULT_LIMIT_STEP
        return {'FINISHED'}


class QMC_OT_APPLY_INDEXED_COLOR(bpy.types.Operator):
    bl_idname = "qmc.apply_indexed_color"
    bl_label = "Apply Indexed Color"

    hex_value: bpy.props.IntProperty(min=0, max=0xFFFFFF, options={'HIDDEN', 'SKIP_SAVE'})
    color_label: bpy.props.StringProperty(options={'HIDDEN', 'SKIP_SAVE'})
    tooltip: bpy.props.StringProperty(options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, properties):
        return properties.tooltip

    def execute(self, context):
        set_base_color(self.hex_value, self.color_label)
        return {'FINISHED'}


class QMCColorFinderPanel(bpy.types.Panel):
    bl_idname = "QMC_COLOR_FINDER_PT_Panel"
    bl_label = "Color Finder"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Quick Tools"
    bl_parent_id = 'QMC_PT_Panel'

    def draw(self, context):
        layout = self.layout
        finder = context.window_manager.qmc_finder
        initialize_collection_filters(context.window_manager)

        search_row = layout.row(align=True)
        search_row.prop(finder, "query", text="", icon='VIEWZOOM')
        search_row.operator("qmc.clear_color_search", text="", icon='X')

        sort_row = layout.row(align=True)
        sort_row.prop(finder, "sort_mode", text="")
        direction = sort_row.row(align=True)
        direction.enabled = finder.sort_mode != 'RELEVANCE'
        direction.operator(
            "qmc.toggle_color_sort_direction",
            text="",
            icon='TRIA_DOWN' if finder.descending else 'TRIA_UP',
        )

        hue_row = layout.row(align=True)
        hue_row.prop_enum(finder, "hue", 'ALL', text="All")
        hue_row.prop_enum(finder, "hue", 'NEUTRAL', text="Neutral")

        hue_row = layout.row(align=True)
        hue_row.prop_enum(finder, "hue", 'RED', text="Red")
        hue_row.prop_enum(finder, "hue", 'YELLOW', text="Yellow")
        hue_row.prop_enum(finder, "hue", 'GREEN', text="Green")

        hue_row = layout.row(align=True)
        hue_row.prop_enum(finder, "hue", 'CYAN', text="Cyan")
        hue_row.prop_enum(finder, "hue", 'BLUE', text="Blue")
        hue_row.prop_enum(finder, "hue", 'MAGENTA', text="Magenta")

        collection_header, collection_body = layout.panel(
            "qmc_color_finder_collections",
            default_closed=True,
        )
        collection_header.label(text="Filter by Collection")
        if collection_body is not None:
            controls = collection_body.row(align=True)
            select_all = controls.operator("qmc.set_collection_filters", text="All")
            select_all.selected = True
            clear_all = controls.operator("qmc.set_collection_filters", text="Clear")
            clear_all.selected = False
            for item in finder.collections:
                collection_body.prop(item, "selected", text=item.label)

        page = finder_page(finder)
        if page.total == 0:
            collections = selected_collection_keys(finder)
            is_idle = not finder.query.strip() and finder.hue == ALL_HUES and collections is None
            layout.label(
                text="Enter a search or choose a filter" if is_idle else "No matching colors",
                icon='INFO',
            )
            return

        match_label = "match" if page.total == 1 else "matches"
        layout.label(text=f"{page.total:,} {match_label}")
        for record in page.items:
            label = f'{record["label"]} · {record["collection_name"]}'
            tooltip = (
                f'{record["label"]}\n'
                f'Collection: {record["collection_name"]}\n'
                f'HEX: #{record["hex"]:06X}\n'
                f'HSV: {record["hue"]:.1f}°, {record["saturation"]:.1f}%, {record["value"]:.1f}%'
            )
            operator = layout.operator(
                "qmc.apply_indexed_color",
                text=label,
                icon_value=g.c_icons[record["icon"]].icon_id,
            )
            operator.hex_value = record["hex"]
            operator.color_label = record["label"]
            operator.tooltip = tooltip

        if len(page.items) < page.total:
            layout.operator("qmc.show_more_colors", text="Show More")


class QMCBrowseCollectionsPanel(bpy.types.Panel):
    bl_idname = "QMC_BROWSE_COLLECTIONS_PT_Panel"
    bl_label = "Browse Collections"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Quick Tools"
    bl_parent_id = 'QMC_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        pass


# IMPORT PANELS
from .color_sets.ams_595a import *
from .color_sets.bclr import *
from .color_sets.bsc import *
from .color_sets.coco import *
from .color_sets.ecc import *
from .color_sets.f58 import *
from .color_sets.ge import *
from .color_sets.hg71 import *
from .color_sets.mcm import *
from .color_sets.moods import *
from .color_sets.pcoy import *
from .color_sets.ral import *
from .color_sets.sw_ext import *
from .color_sets.sw_int import *
from .color_sets.sw_ja import *
from .color_sets.wgsn import *


# INTERNAL CLASSES
array_int = [
    QMC_COLLECTION_FILTER_ITEM,
    QMC_FINDER_SETTINGS,
    QMC_SETTINGS,
    QMCPanel,
    QMC_OT_CLEAR_SEARCH,
    QMC_OT_TOGGLE_SORT_DIRECTION,
    QMC_OT_SET_COLLECTION_FILTERS,
    QMC_OT_SHOW_MORE_COLORS,
    QMC_OT_APPLY_INDEXED_COLOR,
    QMCColorFinderPanel,
    QMCBrowseCollectionsPanel,
]


# IMPORT & CONCATENATE CLASSES
classes = [
   *array_int,
   *array_ams,
   *array_bclr,
   *array_bsc,
   *array_coco,
   *array_ecc,
   *array_f58,
   *array_ge,
   *array_hg71,
   *array_mcm,
   *array_moods,
   *array_pcoy,
   *array_ral,
   *array_sw_ext,
   *array_sw_int,
   *array_sw_ja,
   *array_wgsn,
]


def register():
    # LOAD CUSTOM ICONS
    if g.c_icons is None:
        g.c_icons = bpy.utils.previews.new()

    addon_path = os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")
    
    if not os.path.exists(icons_dir):
        print(f"Warning: Icons directory {icons_dir} not found.")
    else:
        for entry in os.listdir(icons_dir):
            icon_path = os.path.join(icons_dir, entry)
            if os.path.isfile(icon_path):
                try:
                    icon_name = os.path.splitext(entry)[0]
                    g.c_icons.load(icon_name, icon_path, "IMAGE")
                except Exception as e:
                    print(f"Error loading icon {entry}: {e}")
            else:
                print(f"Warning: {entry} is not a file and will be skipped.")

    # Reparent the existing top-level collection panels under one browser.
    for cls in classes:
        if (
            isinstance(cls, type)
            and issubclass(cls, bpy.types.Panel)
            and getattr(cls, "bl_parent_id", None) == 'QMC_PT_Panel'
            and cls not in {QMCColorFinderPanel, QMCBrowseCollectionsPanel}
        ):
            cls.bl_parent_id = QMCBrowseCollectionsPanel.bl_idname

    # Register classes
    bpy_types_scene_properties = ["active_bool", "more_bool", "diffuse_bool", "world_bool"]

    for cls in classes:
        bpy.utils.register_class(cls)
    
    for prop in bpy_types_scene_properties:
        setattr(bpy.types.Scene, prop, bpy.props.PointerProperty(type=QMC_SETTINGS))

    bpy.types.WindowManager.qmc_finder = bpy.props.PointerProperty(type=QMC_FINDER_SETTINGS)
    initialize_collection_filters(bpy.context.window_manager)


def unregister():
    if g.c_icons is not None:
        try:
            bpy.utils.previews.remove(g.c_icons)
        except KeyError:
            # Blender can close previews before add-on cleanup during reloads.
            pass
        finally:
            g.c_icons = None

    bpy_types_scene_properties = ["active_bool", "more_bool", "diffuse_bool", "world_bool"]

    if hasattr(bpy.types.WindowManager, "qmc_finder"):
        del bpy.types.WindowManager.qmc_finder
    
    for prop in bpy_types_scene_properties:
        if hasattr(bpy.types.Scene, prop):
            delattr(bpy.types.Scene, prop)
        
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
