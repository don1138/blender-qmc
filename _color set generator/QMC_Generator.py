# BMC GENERATOR

# WRITE THIS SCRIPT TO FILE WITH:
# python BMC_Generator.py > pcoy-2023.py


from PIL import Image, ImageDraw, ImageColor
import os


# IMPORT VARS
from _arrays.pcoy_vars import *


icons_dir = './icons/'
if not os.path.isdir(icons_dir):
    os.mkdir(icons_dir)


# WRITE HEADER
print("#",panel_name,"COLORS SET")
print("\nimport bpy")
print("\nfrom .globals import *")
print("from .color_functions import *")


# WRITE OPERATORS
print("\n#",panel_name,"OPERATORS")
for i in array:
    print("\nclass", f"{i[0]}(bpy.types.Operator):")
    print("    \"\"\""+i[1]+"\"\"\"")
    print("    bl_label = \""+i[2]+"\"")
    print("    bl_idname = 'color."+i[3]+"'")
    print("    def execute(self, context):")
    print(f"        set_base_color(0x{i[4]}, self.bl_label)")
    print("        return {'FINISHED'}")


# WRITE PANEL
print("\n")
print("#",panel_name,"PANEL")
print("")
print(f"class {panel_label}Panel(bpy.types.Panel):")
print("    bl_idname = \""+panel_name+"_PT_Panel\"")
print("    bl_label = \""+panel_label+"\"")
print("    bl_space_type = \"VIEW_3D\"")
print("    bl_region_type = \"UI\"")
print("    bl_category = \"MAT\"")
print("    bl_parent_id = 'QMC_PT_Panel'")
print("    bl_options = {'DEFAULT_CLOSED'}")
print("")
print("    def draw(self, context):")
print("        g.c_icons")
print("        layout = self.layout")
print("")
print("        srow = layout.row()")
print("        scol = srow.column(align=True)")
print("        scol.scale_y = 1.25")
for i in array:
  print("        scol.label(text=\"\", icon_value=g.c_icons[\""+i[3]+"\"].icon_id)")
print("")
print("        scol = srow.column(align=True)")
print("        scol.scale_y = 1.25")
print("        scol.scale_x = 3.0")
for i in array:
  print("        scol.operator(\"color."+i[3]+"\", text=\""+i[2]+"\")")


# WRITE CLASSES
print("\n")
print("#",panel_name,"CLASSES")
print(f"{array_name} = [")
print(f"    {panel_label}Panel,")
for i in array:
    print(f"    {i[0]},")
print("]")


# CREATE PNG ICONS
# !!! REMEMBER TO RUN ImageOptim ON FOLDER !!!
for i in array:
    # name of the file to save
    filename = f"{i[3]}.png"
    # file_path = os.path.join(dir, filename)
    file_path = f"./icons/{i[3]}.png"
    # create new image
    col = ImageColor.getcolor(f"#{i[4]}", "RGB")
    image = Image.new(mode = "RGB", size = (32,32), color = col)
    # save the file
    image.save(file_path)
