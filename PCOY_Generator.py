# PCOY GENERATOR

# WRITE THIS SCRIPT TO FILE WITH:
# python PCOY_Generator.py > output.txt


from PIL import Image, ImageDraw, ImageColor
import os



panel_name = "HG71"
panel_label = "House & Garden 1971"
dir = './icons/'

if not os.path.isdir(dir):
    os.mkdir(dir)



array = [
# ["Class Name","Tool Tip","Label Name","ID Name","Hex Color"],
["HG71Pineapple","House & Garden 1971 Pineapple","Pineapple","hg71_pineapple","faf076"],
["HG71SunYellow","House & Garden 1971 Sun Yellow","Sun Yellow","hg71_sun_yellow","fce612"],
["HG71Kumquat","House & Garden 1971 Kumquat","Kumquat","hg71_kumquat","f2ac18"],
["HG71Bittersweet","House & Garden 1971 Bittersweet","Bittersweet","hg71_bittersweet","fd4f1c"],
["HG71Tangerine","House & Garden 1971 Tangerine","Tangerine","hg71_tangerine","ec4c53"],
["HG71PompeiianRed","House & Garden 1971 Pompeiian Red","Pompeiian Red","hg71_pompeiian_red","b34848"],
["HG71Zinnia","House & Garden 1971 Zinnia","Zinnia","hg71_zinnia","db7543"],
["HG71Mushroom","House & Garden 1971 Mushroom","Mushroom","hg71_mushroom","8b8484"],
["HG71VelvetBrown","House & Garden 1971 Velvet Brown","Velvet Brown","hg71_velvet_brown","4a3439"],
["HG71LacquerGreen","House & Garden 1971 Lacquer Green","Lacquer Green","hg71_lacquer_green","26572e"],
["HG71MossGreen","House & Garden 1971 Moss Green","Moss Green","hg71_moss_green","687d37"],
["HG71GreenMint","House & Garden 1971 Green Mint","Green Mint","hg71_green_mint","42ab52"],
["HG71ParrotGreen","House & Garden 1971 Parrot Green","Parrot Green","hg71_parrot_green","a9ca5a"],
["HG71Lettuce","House & Garden 1971 Lettuce","Lettuce","hg71_lettuce","dceb71"],
["HG71Celery","House & Garden 1971 Celery","Celery","hg71_celery","e8e9ce"],
["HG71MapleSugar","House & Garden 1971 Maple Sugar","Maple Sugar","hg71_maple_sugar","b3a67f"],
["HG71Goldenrod","House & Garden 1971 Goldenrod","Goldenrod","hg71_goldenrod","d1ab4e"],
["HG71AntiqueGold","House & Garden 1971 Antique Gold","Antique Gold","hg71_antique_gold","b39859"],
["HG71Pongee","House & Garden 1971 Pongee","Pongee","hg71_pongee","d3c995"],
["HG71CreamyApricot","House & Garden 1971 Creamy Apricot","Creamy Apricot","hg71_creamy_apricot","f5caab"],
["HG71PinkCoral","House & Garden 1971 Pink Coral","Pink Coral","hg71_pink_coral","ec939f"],
["HG71FlagRed","House & Garden 1971 Flag Red","Flag Red","hg71_flag_red","d21b5c"],
["HG71BeachPlum","House & Garden 1971 Beach Plum","Beach Plum","hg71_beach_plum","49134c"],
["HG71PinkPink","House & Garden 1971 Pink Pink","Pink Pink","hg71_pink_pink","e9c7e9"],
["HG71Azalea","House & Garden 1971 Azalea","Azalea","hg71_azalea","e586b9"],
["HG71AfricanViolet","House & Garden 1971 African Violet","African Violet","hg71_african_violet","ce90cf"],
["HG71Lavender","House & Garden 1971 Lavender","Lavender","hg71_lavender","d1bce0"],
["HG71OysterWhite","House & Garden 1971 Oyster White","Oyster White","hg71_oyster_white","e2dddb"],
["HG71Mercury","House & Garden 1971 Mercury","Mercury","hg71_mercury","b2b0b5"],
["HG71BlackPearl","House & Garden 1971 Black Pearl","Black Pearl","hg71_black_pearl","0a0a13"],
["HG71MidnightBlue","House & Garden 1971 Midnight Blue","Midnight Blue","hg71_midnight_blue","17195c"],
["HG71UltramarineBlue","House & Garden 1971 Ultramarine Blue","Ultramarine Blue","hg71_ultramarine_blue","1648a6"],
["HG71SpaceBlue","House & Garden 1971 Space Blue","Space Blue","hg71_space_blue","1973cf"],
["HG71BlueSky","House & Garden 1971 Blue Sky","Blue Sky","hg71_blue_sky","9ec4ef"],
["HG71BlueOpaline","House & Garden 1971 Blue Opaline","Blue Opaline","hg71_blue_opaline","3a66a2"],
["HG71AquamarineBlue","House & Garden 1971 Aquamarine Blue","Aquamarine Blue","hg71_aquamarine_blue","cad1d3"],
]



# WRITE OPERATORS
print("\n# OPERATORS")
for i in array:
  print("\nclass",i[0]+"(bpy.types.Operator):")
  print("    \"\"\""+i[1]+"\"\"\"")
  print("    bl_label = \""+i[2]+"\"")
  print("    bl_idname = 'color."+i[3]+"'")
  print("    def execute(self, context):")
  print("        set_base_color(0x"+i[4]+", self.bl_label)")
  print("        return {'FINISHED'}")



# WRITE PANEL
print("\n")
print("# "+panel_label.upper()+" PANEL")
print("")
print("class "+panel_name+"Panel(bpy.types.Panel):")
print("    bl_idname = \""+panel_name+"_PT_Panel\"")
print("    bl_label = \""+panel_label+"\"")
print("    bl_space_type = \"VIEW_3D\"")
print("    bl_region_type = \"UI\"")
print("    bl_category = \"MAT\"")
print("    bl_parent_id = 'PMS_PT_Panel'")
print("    bl_options = {'DEFAULT_CLOSED'}")
print("")
print("    def draw(self, context):")
print("        global c_icons")
print("        layout = self.layout")
print("")
print("        srow = layout.row()")
print("        scol = srow.column(align=True)")
print("        scol.scale_y = 1.25")
for i in array:
  print("        scol.label(text=\"\", icon_value=c_icons[\""+i[3]+"\"].icon_id)")
print("")
print("        scol = srow.column(align=True)")
print("        scol.scale_y = 1.25")
print("        scol.scale_x = 3.0")
for i in array:
  print("        scol.operator(\"color."+i[3]+"\", text=\""+i[2]+"\")")



# WRITE CLASSES
print("\n")
print("# CLASSES")
print("")
for i in array:
  print("    "+i[0]+",")
print("    "+panel_name+"Panel,")



# CREATE PNG ICONS
for i in array:
  # name of the file to save
  filename = i[3]+".png"
  file_path = os.path.join(dir, filename)
  # create new image
  col = ImageColor.getcolor("#"+i[4], "RGB")
  image = Image.new(mode = "RGB", size = (32,32), color = col)
  # save the file
  image.save(file_path)
  # !!! remember to run ImageOptim on folder !!!
