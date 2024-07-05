# COCO COLORS SET

import bpy

from .globals import *
from .color_functions import *

# COCO OPERATORS
def set_roughness(roughness_value):
    bpy.context.object.active_material.roughness = roughness_value


class COCO_Undefined(bpy.types.Operator):
    """0 Undefined"""
    bl_label = "Undefined"
    bl_idname = 'color.coco_undefined'
    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Person(bpy.types.Operator):
    """1 Person"""
    bl_label = "Person"
    bl_idname = 'color.coco_person'
    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Backpack(bpy.types.Operator):
    """27 Backpack"""
    bl_label = "Backpack"
    bl_idname = 'color.coco_backpack'
    def execute(self, context):
        set_base_color(0xC0C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Eye_Glasses(bpy.types.Operator):
    """30 Eye Glasses"""
    bl_label = "Eye Glasses"
    bl_idname = 'color.coco_eye_glasses'
    def execute(self, context):
        set_base_color(0x40C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Handbag(bpy.types.Operator):
    """31 Handbag"""
    bl_label = "Handbag"
    bl_idname = 'color.coco_handbag'
    def execute(self, context):
        set_base_color(0xC0C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Hat(bpy.types.Operator):
    """26 Hat"""
    bl_label = "Hat"
    bl_idname = 'color.coco_hat'
    def execute(self, context):
        set_base_color(0x40C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Shoe(bpy.types.Operator):
    """29 Shoe"""
    bl_label = "Shoe"
    bl_idname = 'color.coco_shoe'
    def execute(self, context):
        set_base_color(0xC04080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Suitcase(bpy.types.Operator):
    """33 Suitcase"""
    bl_label = "Suitcase"
    bl_idname = 'color.coco_suitcase'
    def execute(self, context):
        set_base_color(0x800040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Tie(bpy.types.Operator):
    """32 Tie"""
    bl_label = "Tie"
    bl_idname = 'color.coco_tie'
    def execute(self, context):
        set_base_color(0x000040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Umbrella(bpy.types.Operator):
    """28 Umbrella"""
    bl_label = "Umbrella"
    bl_idname = 'color.coco_umbrella'
    def execute(self, context):
        set_base_color(0x404080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bear(bpy.types.Operator):
    """23 Bear"""
    bl_label = "Bear"
    bl_idname = 'color.coco_bear'
    def execute(self, context):
        set_base_color(0x80C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bird(bpy.types.Operator):
    """16 Bird"""
    bl_label = "Bird"
    bl_idname = 'color.coco_bird'
    def execute(self, context):
        set_base_color(0x004000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cat(bpy.types.Operator):
    """17 Cat"""
    bl_label = "Cat"
    bl_idname = 'color.coco_cat'
    def execute(self, context):
        set_base_color(0x804000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cow(bpy.types.Operator):
    """21 Cow"""
    bl_label = "Cow"
    bl_idname = 'color.coco_cow'
    def execute(self, context):
        set_base_color(0x804080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Dog(bpy.types.Operator):
    """18 Dog"""
    bl_label = "Dog"
    bl_idname = 'color.coco_dog'
    def execute(self, context):
        set_base_color(0x00C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Elephant(bpy.types.Operator):
    """22 Elephant"""
    bl_label = "Elephant"
    bl_idname = 'color.coco_elephant'
    def execute(self, context):
        set_base_color(0x00C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Giraffe(bpy.types.Operator):
    """25 Giraffe"""
    bl_label = "Giraffe"
    bl_idname = 'color.coco_giraffe'
    def execute(self, context):
        set_base_color(0xC04000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Horse(bpy.types.Operator):
    """19 Horse"""
    bl_label = "Horse"
    bl_idname = 'color.coco_horse'
    def execute(self, context):
        set_base_color(0x80C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sheep(bpy.types.Operator):
    """20 Sheep"""
    bl_label = "Sheep"
    bl_idname = 'color.coco_sheep'
    def execute(self, context):
        set_base_color(0x004080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Zebra(bpy.types.Operator):
    """24 Zebra"""
    bl_label = "Zebra"
    bl_idname = 'color.coco_zebra'
    def execute(self, context):
        set_base_color(0x404000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bench(bpy.types.Operator):
    """15 Bench"""
    bl_label = "Bench"
    bl_idname = 'color.coco_bench'
    def execute(self, context):
        set_base_color(0xC08080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Fire_Hydrant(bpy.types.Operator):
    """11 Fire Hydrant"""
    bl_label = "Fire Hydrant"
    bl_idname = 'color.coco_fire_hydrant'
    def execute(self, context):
        set_base_color(0xC08000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Parking_Meter(bpy.types.Operator):
    """14 Parking Meter"""
    bl_label = "Parking Meter"
    bl_idname = 'color.coco_parking_meter'
    def execute(self, context):
        set_base_color(0x408080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Stop_Sign(bpy.types.Operator):
    """13 Stop Sign"""
    bl_label = "Stop Sign"
    bl_idname = 'color.coco_stop_sign'
    def execute(self, context):
        set_base_color(0xC00080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Street_Sign(bpy.types.Operator):
    """12 Street Sign"""
    bl_label = "Street Sign"
    bl_idname = 'color.coco_street_sign'
    def execute(self, context):
        set_base_color(0x400080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Traffic_Light(bpy.types.Operator):
    """10 Traffic Light"""
    bl_label = "Traffic Light"
    bl_idname = 'color.coco_traffic_light'
    def execute(self, context):
        set_base_color(0x408000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Baseball_Bat(bpy.types.Operator):
    """39 Baseball Bat"""
    bl_label = "Baseball Bat"
    bl_idname = 'color.coco_baseball_bat'
    def execute(self, context):
        set_base_color(0x8080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Baseball_Glove(bpy.types.Operator):
    """40 Baseball Glove"""
    bl_label = "Baseball Glove"
    bl_idname = 'color.coco_baseball_glove'
    def execute(self, context):
        set_base_color(0x400040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Frisbee(bpy.types.Operator):
    """34 Frisbee"""
    bl_label = "Frisbee"
    bl_idname = 'color.coco_frisbee'
    def execute(self, context):
        set_base_color(0x008040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Kite(bpy.types.Operator):
    """38 Kite"""
    bl_label = "Kite"
    bl_idname = 'color.coco_kite'
    def execute(self, context):
        set_base_color(0x0080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Skateboard(bpy.types.Operator):
    """41 Skateboard"""
    bl_label = "Skateboard"
    bl_idname = 'color.coco_skateboard'
    def execute(self, context):
        set_base_color(0xC00040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Skis(bpy.types.Operator):
    """35 Skis"""
    bl_label = "Skis"
    bl_idname = 'color.coco_skis'
    def execute(self, context):
        set_base_color(0x808040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Snowboard(bpy.types.Operator):
    """36 Snowboard"""
    bl_label = "Snowboard"
    bl_idname = 'color.coco_snowboard'
    def execute(self, context):
        set_base_color(0x0000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sports_Ball(bpy.types.Operator):
    """37 Sports Ball"""
    bl_label = "Sports Ball"
    bl_idname = 'color.coco_sports_ball'
    def execute(self, context):
        set_base_color(0x8000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Surfboard(bpy.types.Operator):
    """42 Surfboard"""
    bl_label = "Surfboard"
    bl_idname = 'color.coco_surfboard'
    def execute(self, context):
        set_base_color(0x408040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Tennis_Racket(bpy.types.Operator):
    """43 Tennis Racket"""
    bl_label = "Tennis Racket"
    bl_idname = 'color.coco_tennis_racket'
    def execute(self, context):
        set_base_color(0xC08040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Airplane(bpy.types.Operator):
    """5 Airplane"""
    bl_label = "Airplane"
    bl_idname = 'color.coco_airplane'
    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bicycle(bpy.types.Operator):
    """2 Bicycle"""
    bl_label = "Bicycle"
    bl_idname = 'color.coco_bicycle'
    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Boat(bpy.types.Operator):
    """9 Boat"""
    bl_label = "Boat"
    bl_idname = 'color.coco_boat'
    def execute(self, context):
        set_base_color(0xC00000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bus(bpy.types.Operator):
    """6 Bus"""
    bl_label = "Bus"
    bl_idname = 'color.coco_bus'
    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Car(bpy.types.Operator):
    """3 Car"""
    bl_label = "Car"
    bl_idname = 'color.coco_car'
    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Motorcycle(bpy.types.Operator):
    """4 Motorcycle"""
    bl_label = "Motorcycle"
    bl_idname = 'color.coco_motorcycle'
    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Train(bpy.types.Operator):
    """7 Train"""
    bl_label = "Train"
    bl_idname = 'color.coco_train'
    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Truck(bpy.types.Operator):
    """8 Truck"""
    bl_label = "Truck"
    bl_idname = 'color.coco_truck'
    def execute(self, context):
        set_base_color(0x400000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Blender(bpy.types.Operator):
    """83 Blender"""
    bl_label = "Blender"
    bl_idname = 'color.coco_blender'
    def execute(self, context):
        set_base_color(0xA0C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Microwave(bpy.types.Operator):
    """78 Microwave"""
    bl_label = "Microwave"
    bl_idname = 'color.coco_microwave'
    def execute(self, context):
        set_base_color(0x608080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Oven(bpy.types.Operator):
    """79 Oven"""
    bl_label = "Oven"
    bl_idname = 'color.coco_oven'
    def execute(self, context):
        set_base_color(0xE08080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Refrigerator(bpy.types.Operator):
    """82 Refrigerator"""
    bl_label = "Refrigerator"
    bl_idname = 'color.coco_refrigerator'
    def execute(self, context):
        set_base_color(0x20C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sink(bpy.types.Operator):
    """81 Sink"""
    bl_label = "Sink"
    bl_idname = 'color.coco_sink'
    def execute(self, context):
        set_base_color(0xA04000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Toaster(bpy.types.Operator):
    """80 Toaster"""
    bl_label = "Toaster"
    bl_idname = 'color.coco_toaster'
    def execute(self, context):
        set_base_color(0x204000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cell_Phone(bpy.types.Operator):
    """77 Cell Phone"""
    bl_label = "Cell Phone"
    bl_idname = 'color.coco_cell_phone'
    def execute(self, context):
        set_base_color(0xE00080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Keyboard(bpy.types.Operator):
    """76 Keyboard"""
    bl_label = "Keyboard"
    bl_idname = 'color.coco_keyboard'
    def execute(self, context):
        set_base_color(0x600080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Laptop(bpy.types.Operator):
    """73 Laptop"""
    bl_label = "Laptop"
    bl_idname = 'color.coco_laptop'
    def execute(self, context):
        set_base_color(0xE00000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Mouse(bpy.types.Operator):
    """74 Mouse"""
    bl_label = "Mouse"
    bl_idname = 'color.coco_mouse'
    def execute(self, context):
        set_base_color(0x608000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Remote(bpy.types.Operator):
    """75 Remote"""
    bl_label = "Remote"
    bl_idname = 'color.coco_remote'
    def execute(self, context):
        set_base_color(0xE08000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_TV(bpy.types.Operator):
    """72 TV"""
    bl_label = "TV"
    bl_idname = 'color.coco_tv'
    def execute(self, context):
        set_base_color(0x600000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Apple(bpy.types.Operator):
    """53 Apple"""
    bl_label = "Apple"
    bl_idname = 'color.coco_apple'
    def execute(self, context):
        set_base_color(0x8040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Banana(bpy.types.Operator):
    """52 Banana"""
    bl_label = "Banana"
    bl_idname = 'color.coco_banana'
    def execute(self, context):
        set_base_color(0x0040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Broccoli(bpy.types.Operator):
    """56 Broccoli"""
    bl_label = "Broccoli"
    bl_idname = 'color.coco_broccoli'
    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cake(bpy.types.Operator):
    """61 Cake"""
    bl_label = "Cake"
    bl_idname = 'color.coco_cake'
    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Carrot(bpy.types.Operator):
    """57 Carrot"""
    bl_label = "Carrot"
    bl_idname = 'color.coco_carrot'
    def execute(self, context):
        set_base_color(0xC04040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Donut(bpy.types.Operator):
    """60 Donut"""
    bl_label = "Donut"
    bl_idname = 'color.coco_donut'
    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Hot_Dog(bpy.types.Operator):
    """58 Hot Dog"""
    bl_label = "Hot Dog"
    bl_idname = 'color.coco_hot_dog'
    def execute(self, context):
        set_base_color(0x40C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Orange(bpy.types.Operator):
    """55 Orange"""
    bl_label = "Orange"
    bl_idname = 'color.coco_orange'
    def execute(self, context):
        set_base_color(0x80C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Pizza(bpy.types.Operator):
    """59 Pizza"""
    bl_label = "Pizza"
    bl_idname = 'color.coco_pizza'
    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sandwich(bpy.types.Operator):
    """54 Sandwich"""
    bl_label = "Sandwich"
    bl_idname = 'color.coco_sandwich'
    def execute(self, context):
        set_base_color(0x00C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bed(bpy.types.Operator):
    """65 Bed"""
    bl_label = "Bed"
    bl_idname = 'color.coco_bed'
    def execute(self, context):
        set_base_color(0xA00000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Chair(bpy.types.Operator):
    """62 Chair"""
    bl_label = "Chair"
    bl_idname = 'color.coco_chair'
    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Couch(bpy.types.Operator):
    """63 Couch"""
    bl_label = "Couch"
    bl_idname = 'color.coco_couch'
    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Desk(bpy.types.Operator):
    """69 Desk"""
    bl_label = "Desk"
    bl_idname = 'color.coco_desk'
    def execute(self, context):
        set_base_color(0xA00080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Dining_Table(bpy.types.Operator):
    """67 Dining Table"""
    bl_label = "Dining Table"
    bl_idname = 'color.coco_dining_table'
    def execute(self, context):
        set_base_color(0xA08000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Door(bpy.types.Operator):
    """71 Door"""
    bl_label = "Door"
    bl_idname = 'color.coco_door'
    def execute(self, context):
        set_base_color(0xA08080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Mirror(bpy.types.Operator):
    """66 Mirror"""
    bl_label = "Mirror"
    bl_idname = 'color.coco_mirror'
    def execute(self, context):
        set_base_color(0x208000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Potted_Plant(bpy.types.Operator):
    """64 Potted Plant"""
    bl_label = "Potted Plant"
    bl_idname = 'color.coco_potted_plant'
    def execute(self, context):
        set_base_color(0x200000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Toilet(bpy.types.Operator):
    """70 Toilet"""
    bl_label = "Toilet"
    bl_idname = 'color.coco_toilet'
    def execute(self, context):
        set_base_color(0x208080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Window(bpy.types.Operator):
    """68 Window"""
    bl_label = "Window"
    bl_idname = 'color.coco_window'
    def execute(self, context):
        set_base_color(0x200080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Book(bpy.types.Operator):
    """84 Book"""
    bl_label = "Book"
    bl_idname = 'color.coco_book'
    def execute(self, context):
        set_base_color(0x204080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Clock(bpy.types.Operator):
    """85 Clock"""
    bl_label = "Clock"
    bl_idname = 'color.coco_clock'
    def execute(self, context):
        set_base_color(0xA04080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Hair_Brush(bpy.types.Operator):
    """91 Hair Brush"""
    bl_label = "Hair Brush"
    bl_idname = 'color.coco_hair_brush'
    def execute(self, context):
        set_base_color(0xE0C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Hair_Drier(bpy.types.Operator):
    """89 Hair Drier"""
    bl_label = "Hair Drier"
    bl_idname = 'color.coco_hair_drier'
    def execute(self, context):
        set_base_color(0xE04000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Scissors(bpy.types.Operator):
    """87 Scissors"""
    bl_label = "Scissors"
    bl_idname = 'color.coco_scissors'
    def execute(self, context):
        set_base_color(0xA0C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Teddy_Bear(bpy.types.Operator):
    """88 Teddy Bear"""
    bl_label = "Teddy Bear"
    bl_idname = 'color.coco_teddy_bear'
    def execute(self, context):
        set_base_color(0x604000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Toothbrush(bpy.types.Operator):
    """90 Toothbrush"""
    bl_label = "Toothbrush"
    bl_idname = 'color.coco_toothbrush'
    def execute(self, context):
        set_base_color(0x60C000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Vase(bpy.types.Operator):
    """86 Vase"""
    bl_label = "Vase"
    bl_idname = 'color.coco_vase'
    def execute(self, context):
        set_base_color(0x20C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bottle(bpy.types.Operator):
    """44 Bottle"""
    bl_label = "Bottle"
    bl_idname = 'color.coco_bottle'
    def execute(self, context):
        set_base_color(0x4000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bowl(bpy.types.Operator):
    """51 Bowl"""
    bl_label = "Bowl"
    bl_idname = 'color.coco_bowl'
    def execute(self, context):
        set_base_color(0x80C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cup(bpy.types.Operator):
    """47 Cup"""
    bl_label = "Cup"
    bl_idname = 'color.coco_cup'
    def execute(self, context):
        set_base_color(0xC080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Fork(bpy.types.Operator):
    """48 Fork"""
    bl_label = "Fork"
    bl_idname = 'color.coco_fork'
    def execute(self, context):
        set_base_color(0x004040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Knife(bpy.types.Operator):
    """49 Knife"""
    bl_label = "Knife"
    bl_idname = 'color.coco_knife'
    def execute(self, context):
        set_base_color(0x804040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Plate(bpy.types.Operator):
    """45 Plate"""
    bl_label = "Plate"
    bl_idname = 'color.coco_plate'
    def execute(self, context):
        set_base_color(0xC000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Spoon(bpy.types.Operator):
    """50 Spoon"""
    bl_label = "Spoon"
    bl_idname = 'color.coco_spoon'
    def execute(self, context):
        set_base_color(0x00C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wine_Glass(bpy.types.Operator):
    """46 Wine Glass"""
    bl_label = "Wine Glass"
    bl_idname = 'color.coco_wine_glass'
    def execute(self, context):
        set_base_color(0x4080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bridge(bpy.types.Operator):
    """95 Bridge"""
    bl_label = "Bridge"
    bl_idname = 'color.coco_bridge'
    def execute(self, context):
        set_base_color(0xE0C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Building_Other(bpy.types.Operator):
    """96 Building Other"""
    bl_label = "Building Other"
    bl_idname = 'color.coco_building_other'
    def execute(self, context):
        set_base_color(0x200040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_House(bpy.types.Operator):
    """128 House"""
    bl_label = "House"
    bl_idname = 'color.coco_house'
    def execute(self, context):
        set_base_color(0x002000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Roof(bpy.types.Operator):
    """151 Roof"""
    bl_label = "Roof"
    bl_idname = 'color.coco_roof'
    def execute(self, context):
        set_base_color(0x80E080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Skyscraper(bpy.types.Operator):
    """158 Skyscraper"""
    bl_label = "Skyscraper"
    bl_idname = 'color.coco_skyscraper'
    def execute(self, context):
        set_base_color(0x40E080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Tent(bpy.types.Operator):
    """166 Tent"""
    bl_label = "Tent"
    bl_idname = 'color.coco_tent'
    def execute(self, context):
        set_base_color(0x00A0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Dirt(bpy.types.Operator):
    """111 Dirt"""
    bl_label = "Dirt"
    bl_idname = 'color.coco_dirt'
    def execute(self, context):
        set_base_color(0xE080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Gravel(bpy.types.Operator):
    """125 Gravel"""
    bl_label = "Gravel"
    bl_idname = 'color.coco_gravel'
    def execute(self, context):
        set_base_color(0xE040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Ground_Other(bpy.types.Operator):
    """126 Ground Other"""
    bl_label = "Ground Other"
    bl_idname = 'color.coco_ground_other'
    def execute(self, context):
        set_base_color(0x60C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Mud(bpy.types.Operator):
    """136 Mud"""
    bl_label = "Mud"
    bl_idname = 'color.coco_mud'
    def execute(self, context):
        set_base_color(0x402000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Pavement(bpy.types.Operator):
    """140 Pavement"""
    bl_label = "Pavement"
    bl_idname = 'color.coco_pavement'
    def execute(self, context):
        set_base_color(0x402080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Platform(bpy.types.Operator):
    """144 Platform"""
    bl_label = "Platform"
    bl_idname = 'color.coco_platform'
    def execute(self, context):
        set_base_color(0x006000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Playing_Field(bpy.types.Operator):
    """145 Playing Field"""
    bl_label = "Playing Field"
    bl_idname = 'color.coco_playing_field'
    def execute(self, context):
        set_base_color(0x806000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Railroad(bpy.types.Operator):
    """147 Railroad"""
    bl_label = "Railroad"
    bl_idname = 'color.coco_railroad'
    def execute(self, context):
        set_base_color(0x80E000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Road(bpy.types.Operator):
    """149 Road"""
    bl_label = "Road"
    bl_idname = 'color.coco_road'
    def execute(self, context):
        set_base_color(0x806080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sand(bpy.types.Operator):
    """154 Sand"""
    bl_label = "Sand"
    bl_idname = 'color.coco_sand'
    def execute(self, context):
        set_base_color(0x40E000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Snow(bpy.types.Operator):
    """159 Snow"""
    bl_label = "Snow"
    bl_idname = 'color.coco_snow'
    def execute(self, context):
        set_base_color(0xC0E080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Branch(bpy.types.Operator):
    """94 Branch"""
    bl_label = "Branch"
    bl_idname = 'color.coco_branch'
    def execute(self, context):
        set_base_color(0x60C080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Bush(bpy.types.Operator):
    """97 Bush"""
    bl_label = "Bush"
    bl_idname = 'color.coco_bush'
    def execute(self, context):
        set_base_color(0xA00040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Flower(bpy.types.Operator):
    """119 Flower"""
    bl_label = "Flower"
    bl_idname = 'color.coco_flower'
    def execute(self, context):
        set_base_color(0xA0C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Grass(bpy.types.Operator):
    """124 Grass"""
    bl_label = "Grass"
    bl_idname = 'color.coco_grass'
    def execute(self, context):
        set_base_color(0x1DC331, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Leaves(bpy.types.Operator):
    """129 Leaves"""
    bl_label = "Leaves"
    bl_idname = 'color.coco_leaves'
    def execute(self, context):
        set_base_color(0x802000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Moss(bpy.types.Operator):
    """134 Moss"""
    bl_label = "Moss"
    bl_idname = 'color.coco_moss'
    def execute(self, context):
        set_base_color(0x00A080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Plant_Other(bpy.types.Operator):
    """142 Plant Other"""
    bl_label = "Plant Other"
    bl_idname = 'color.coco_plant_other'
    def execute(self, context):
        set_base_color(0x40A080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Straw(bpy.types.Operator):
    """163 Straw"""
    bl_label = "Straw"
    bl_idname = 'color.coco_straw'
    def execute(self, context):
        set_base_color(0x80A040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Tree(bpy.types.Operator):
    """169 Tree"""
    bl_label = "Tree"
    bl_idname = 'color.coco_tree'
    def execute(self, context):
        set_base_color(0x8C682F, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Clouds(bpy.types.Operator):
    """106 Clouds"""
    bl_label = "Clouds"
    bl_idname = 'color.coco_clouds'
    def execute(self, context):
        set_base_color(0xAAAAAA, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sky_Other(bpy.types.Operator):
    """157 Sky Other"""
    bl_label = "Sky Other"
    bl_idname = 'color.coco_sky_other'
    def execute(self, context):
        set_base_color(0x5FDBFF, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Hill(bpy.types.Operator):
    """127 Hill"""
    bl_label = "Hill"
    bl_idname = 'color.coco_hill'
    def execute(self, context):
        set_base_color(0xE0C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Mountain(bpy.types.Operator):
    """135 Mountain"""
    bl_label = "Mountain"
    bl_idname = 'color.coco_mountain'
    def execute(self, context):
        set_base_color(0x80A080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Rock(bpy.types.Operator):
    """150 Rock"""
    bl_label = "Rock"
    bl_idname = 'color.coco_rock'
    def execute(self, context):
        set_base_color(0x00E080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Solid_Other(bpy.types.Operator):
    """160 Solid Other"""
    bl_label = "Solid Other"
    bl_idname = 'color.coco_solid_other'
    def execute(self, context):
        set_base_color(0x002040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Stone(bpy.types.Operator):
    """162 Stone"""
    bl_label = "Stone"
    bl_idname = 'color.coco_stone'
    def execute(self, context):
        set_base_color(0x00A040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wood(bpy.types.Operator):
    """182 Wood"""
    bl_label = "Wood"
    bl_idname = 'color.coco_wood'
    def execute(self, context):
        set_base_color(0x00E0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cage(bpy.types.Operator):
    """99 Cage"""
    bl_label = "Cage"
    bl_idname = 'color.coco_cage'
    def execute(self, context):
        set_base_color(0xA08040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Fence(bpy.types.Operator):
    """113 Fence"""
    bl_label = "Fence"
    bl_idname = 'color.coco_fence'
    def execute(self, context):
        set_base_color(0xA04040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Net(bpy.types.Operator):
    """138 Net"""
    bl_label = "Net"
    bl_idname = 'color.coco_net'
    def execute(self, context):
        set_base_color(0x40A000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Railing(bpy.types.Operator):
    """146 Railing"""
    bl_label = "Railing"
    bl_idname = 'color.coco_railing'
    def execute(self, context):
        set_base_color(0x00E000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Structural_Other(bpy.types.Operator):
    """164 Structural Other"""
    bl_label = "Structural Other"
    bl_idname = 'color.coco_structural_other'
    def execute(self, context):
        set_base_color(0x0020C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Fog(bpy.types.Operator):
    """120 Fog"""
    bl_label = "Fog"
    bl_idname = 'color.coco_fog'
    def execute(self, context):
        set_base_color(0x604040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_River(bpy.types.Operator):
    """148 River"""
    bl_label = "River"
    bl_idname = 'color.coco_river'
    def execute(self, context):
        set_base_color(0x006080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Sea(bpy.types.Operator):
    """155 Sea"""
    bl_label = "Sea"
    bl_idname = 'color.coco_sea'
    def execute(self, context):
        set_base_color(0x363EA7, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Water_Other(bpy.types.Operator):
    """178 Water Other"""
    bl_label = "Water Other"
    bl_idname = 'color.coco_water_other'
    def execute(self, context):
        set_base_color(0x00E040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Waterdrops(bpy.types.Operator):
    """179 Waterdrops"""
    bl_label = "Waterdrops"
    bl_idname = 'color.coco_waterdrops'
    def execute(self, context):
        set_base_color(0x80E040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Ceiling_Other(bpy.types.Operator):
    """102 Ceiling Other"""
    bl_label = "Ceiling Other"
    bl_idname = 'color.coco_ceiling_other'
    def execute(self, context):
        set_base_color(0x2080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Ceiling_Tile(bpy.types.Operator):
    """103 Ceiling Tile"""
    bl_label = "Ceiling Tile"
    bl_idname = 'color.coco_ceiling_tile'
    def execute(self, context):
        set_base_color(0xA080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Carpet(bpy.types.Operator):
    """101 Carpet"""
    bl_label = "Carpet"
    bl_idname = 'color.coco_carpet'
    def execute(self, context):
        set_base_color(0xA000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Floor_Marble(bpy.types.Operator):
    """114 Floor Marble"""
    bl_label = "Floor Marble"
    bl_idname = 'color.coco_floor_marble'
    def execute(self, context):
        set_base_color(0x20C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Floor_Other(bpy.types.Operator):
    """115 Floor Other"""
    bl_label = "Floor Other"
    bl_idname = 'color.coco_floor_other'
    def execute(self, context):
        set_base_color(0xA0C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Floor_Stone(bpy.types.Operator):
    """116 Floor Stone"""
    bl_label = "Floor Stone"
    bl_idname = 'color.coco_floor_stone'
    def execute(self, context):
        set_base_color(0x2040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Floor_Tile(bpy.types.Operator):
    """117 Floor Tile"""
    bl_label = "Floor Tile"
    bl_idname = 'color.coco_floor_tile'
    def execute(self, context):
        set_base_color(0xA040C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Floor_Wood(bpy.types.Operator):
    """118 Floor Wood"""
    bl_label = "Floor Wood"
    bl_idname = 'color.coco_floor_wood'
    def execute(self, context):
        set_base_color(0x20C0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Food_Other(bpy.types.Operator):
    """121 Food Other"""
    bl_label = "Food Other"
    bl_idname = 'color.coco_food_other'
    def execute(self, context):
        set_base_color(0xE04040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Fruit(bpy.types.Operator):
    """122 Fruit"""
    bl_label = "Fruit"
    bl_idname = 'color.coco_fruit'
    def execute(self, context):
        set_base_color(0x60C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Salad(bpy.types.Operator):
    """153 Salad"""
    bl_label = "Salad"
    bl_idname = 'color.coco_salad'
    def execute(self, context):
        set_base_color(0xC06000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Vegetable(bpy.types.Operator):
    """170 Vegetable"""
    bl_label = "Vegetable"
    bl_idname = 'color.coco_vegetable'
    def execute(self, context):
        set_base_color(0x40A040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cabinet(bpy.types.Operator):
    """98 Cabinet"""
    bl_label = "Cabinet"
    bl_idname = 'color.coco_cabinet'
    def execute(self, context):
        set_base_color(0x208040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Counter(bpy.types.Operator):
    """107 Counter"""
    bl_label = "Counter"
    bl_idname = 'color.coco_counter'
    def execute(self, context):
        set_base_color(0xE08040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cupboard(bpy.types.Operator):
    """108 Cupboard"""
    bl_label = "Cupboard"
    bl_idname = 'color.coco_cupboard'
    def execute(self, context):
        set_base_color(0x6000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Desk_Stuff(bpy.types.Operator):
    """110 Desk Stuff"""
    bl_label = "Desk Stuff"
    bl_idname = 'color.coco_desk_stuff'
    def execute(self, context):
        set_base_color(0x6080C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Door_Stuff(bpy.types.Operator):
    """112 Door Stuff"""
    bl_label = "Door Stuff"
    bl_idname = 'color.coco_door_stuff'
    def execute(self, context):
        set_base_color(0x204040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Furniture_Other(bpy.types.Operator):
    """123 Furniture Other"""
    bl_label = "Furniture Other"
    bl_idname = 'color.coco_furniture_other'
    def execute(self, context):
        set_base_color(0xE0C040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Light(bpy.types.Operator):
    """130 Light"""
    bl_label = "Light"
    bl_idname = 'color.coco_light'
    def execute(self, context):
        set_base_color(0x00A000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Mirror_Stuff(bpy.types.Operator):
    """133 Mirror Stuff"""
    bl_label = "Mirror Stuff"
    bl_idname = 'color.coco_mirror_stuff'
    def execute(self, context):
        set_base_color(0x802080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Shelf(bpy.types.Operator):
    """156 Shelf"""
    bl_label = "Shelf"
    bl_idname = 'color.coco_shelf'
    def execute(self, context):
        set_base_color(0x406080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Stairs(bpy.types.Operator):
    """161 Stairs"""
    bl_label = "Stairs"
    bl_idname = 'color.coco_stairs'
    def execute(self, context):
        set_base_color(0x802040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Table(bpy.types.Operator):
    """165 Table"""
    bl_label = "Table"
    bl_idname = 'color.coco_table'
    def execute(self, context):
        set_base_color(0x8020C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cardboard(bpy.types.Operator):
    """100 Cardboard"""
    bl_label = "Cardboard"
    bl_idname = 'color.coco_cardboard'
    def execute(self, context):
        set_base_color(0x2000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Metal(bpy.types.Operator):
    """132 Metal"""
    bl_label = "Metal"
    bl_idname = 'color.coco_metal'
    def execute(self, context):
        set_base_color(0x002080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Paper(bpy.types.Operator):
    """139 Paper"""
    bl_label = "Paper"
    bl_idname = 'color.coco_paper'
    def execute(self, context):
        set_base_color(0xC0A000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Plastic(bpy.types.Operator):
    """143 Plastic"""
    bl_label = "Plastic"
    bl_idname = 'color.coco_plastic'
    def execute(self, context):
        set_base_color(0xC0A080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Banner(bpy.types.Operator):
    """92 Banner"""
    bl_label = "Banner"
    bl_idname = 'color.coco_banner'
    def execute(self, context):
        set_base_color(0x604080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Blanket(bpy.types.Operator):
    """93 Blanket"""
    bl_label = "Blanket"
    bl_idname = 'color.coco_blanket'
    def execute(self, context):
        set_base_color(0xE04080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Cloth(bpy.types.Operator):
    """104 Cloth"""
    bl_label = "Cloth"
    bl_idname = 'color.coco_cloth'
    def execute(self, context):
        set_base_color(0x600040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Clothes(bpy.types.Operator):
    """105 Clothes"""
    bl_label = "Clothes"
    bl_idname = 'color.coco_clothes'
    def execute(self, context):
        set_base_color(0xE00040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Curtain(bpy.types.Operator):
    """109 Curtain"""
    bl_label = "Curtain"
    bl_idname = 'color.coco_curtain'
    def execute(self, context):
        set_base_color(0xE000C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Mat(bpy.types.Operator):
    """131 Mat"""
    bl_label = "Mat"
    bl_idname = 'color.coco_mat'
    def execute(self, context):
        set_base_color(0x80A000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Napkin(bpy.types.Operator):
    """137 Napkin"""
    bl_label = "Napkin"
    bl_idname = 'color.coco_napkin'
    def execute(self, context):
        set_base_color(0xC02000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Pillow(bpy.types.Operator):
    """141 Pillow"""
    bl_label = "Pillow"
    bl_idname = 'color.coco_pillow'
    def execute(self, context):
        set_base_color(0xC02080, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Rug(bpy.types.Operator):
    """152 Rug"""
    bl_label = "Rug"
    bl_idname = 'color.coco_rug'
    def execute(self, context):
        set_base_color(0x406000, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Textile_Other(bpy.types.Operator):
    """167 Textile Other"""
    bl_label = "Textile Other"
    bl_idname = 'color.coco_textile_other'
    def execute(self, context):
        set_base_color(0x80A0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Towel(bpy.types.Operator):
    """168 Towel"""
    bl_label = "Towel"
    bl_idname = 'color.coco_towel'
    def execute(self, context):
        set_base_color(0x402040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Brick(bpy.types.Operator):
    """171 Wall Brick"""
    bl_label = "Wall Brick"
    bl_idname = 'color.coco_wall_brick'
    def execute(self, context):
        set_base_color(0xC0A040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Concrete(bpy.types.Operator):
    """172 Wall Concrete"""
    bl_label = "Wall Concrete"
    bl_idname = 'color.coco_wall_concrete'
    def execute(self, context):
        set_base_color(0x4020C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Other(bpy.types.Operator):
    """173 Wall Other"""
    bl_label = "Wall Other"
    bl_idname = 'color.coco_wall_other'
    def execute(self, context):
        set_base_color(0xC020C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Panel(bpy.types.Operator):
    """174 Wall Panel"""
    bl_label = "Wall Panel"
    bl_idname = 'color.coco_wall_panel'
    def execute(self, context):
        set_base_color(0x40A0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Stone(bpy.types.Operator):
    """175 Wall Stone"""
    bl_label = "Wall Stone"
    bl_idname = 'color.coco_wall_stone'
    def execute(self, context):
        set_base_color(0xC0A0C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Tile(bpy.types.Operator):
    """176 Wall Tile"""
    bl_label = "Wall Tile"
    bl_idname = 'color.coco_wall_tile'
    def execute(self, context):
        set_base_color(0x006040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Wall_Wood(bpy.types.Operator):
    """177 Wall Wood"""
    bl_label = "Wall Wood"
    bl_idname = 'color.coco_wall_wood'
    def execute(self, context):
        set_base_color(0x806040, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Window_Blind(bpy.types.Operator):
    """180 Window Blind"""
    bl_label = "Window Blind"
    bl_idname = 'color.coco_window_blind'
    def execute(self, context):
        set_base_color(0x0060C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}

class COCO_Window_Other(bpy.types.Operator):
    """181 Window Other"""
    bl_label = "Window Other"
    bl_idname = 'color.coco_window_other'
    def execute(self, context):
        set_base_color(0x8060C0, self.bl_label)
        set_roughness(1)
        return {'FINISHED'}


# COCO PANEL
class COCOPanel(bpy.types.Panel):
    bl_idname = "COCO_PT_Panel"
    bl_label = "COCO Segmentation"
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
        scol.label(text="", icon_value=g.c_icons["coco_undefined"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_person"].icon_id)


        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_undefined", text="Undefined")
        scol.operator("color.coco_person", text="Person")


# COCO THINGS OUTDOOR PANEL
class COCOThingsOutPanel(bpy.types.Panel):
    bl_idname = "COCO_THINGS_OUT_PT_Panel"
    bl_label = "    Things Outdoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# COCO THINGS INDOOR PANEL
class COCOThingsInPanel(bpy.types.Panel):
    bl_idname = "COCO_THINGS_IN_PT_Panel"
    bl_label = "    Things Indoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# COCO STUFF OUTDOOR PANEL
class COCOStuffOutPanel(bpy.types.Panel):
    bl_idname = "COCO_STUFF_OUT_PT_Panel"
    bl_label = "    Stuff Outdoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# COCO STUFF INDOOR PANEL
class COCOStuffInPanel(bpy.types.Panel):
    bl_idname = "COCO_STUFF_IN_PT_Panel"
    bl_label = "    Stuff Indoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# COCO THINGS OUTDOOR ACCESSORY PANEL
class COCOTOAccessoryPanel(bpy.types.Panel):
    bl_idname = "COCO_ACCESSORY_PT_PANEL"
    bl_label = "        Accessory"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_backpack"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_eye_glasses"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_handbag"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_hat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_shoe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_suitcase"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_tie"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_umbrella"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_backpack", text="Backpack")
        scol.operator("color.coco_eye_glasses", text="Eye Glasses")
        scol.operator("color.coco_handbag", text="Handbag")
        scol.operator("color.coco_hat", text="Hat")
        scol.operator("color.coco_shoe", text="Shoe")
        scol.operator("color.coco_suitcase", text="Suitcase")
        scol.operator("color.coco_tie", text="Tie")
        scol.operator("color.coco_umbrella", text="Umbrella")


# COCO THINGS OUTDOOR ANIMAL PANEL
class COCOTOAnimalPanel(bpy.types.Panel):
    bl_idname = "COCO_ANIMAL_PT_PANEL"
    bl_label = "        Animal"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_bear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_bird"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_cat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_cow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_dog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_elephant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_giraffe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_horse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sheep"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_zebra"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_bear", text="Bear")
        scol.operator("color.coco_bird", text="Bird")
        scol.operator("color.coco_cat", text="Cat")
        scol.operator("color.coco_cow", text="Cow")
        scol.operator("color.coco_dog", text="Dog")
        scol.operator("color.coco_elephant", text="Elephant")
        scol.operator("color.coco_giraffe", text="Giraffe")
        scol.operator("color.coco_horse", text="Horse")
        scol.operator("color.coco_sheep", text="Sheep")
        scol.operator("color.coco_zebra", text="Zebra")


# COCO THINGS OUTDOOR OUTDOOR PANEL
class COCOTOOutdoorPanel(bpy.types.Panel):
    bl_idname = "COCO_OUTDOOR_PT_PANEL"
    bl_label = "        Outdoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_bench"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_fire_hydrant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_parking_meter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_stop_sign"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_street_sign"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_traffic_light"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_bench", text="Bench")
        scol.operator("color.coco_fire_hydrant", text="Fire Hydrant")
        scol.operator("color.coco_parking_meter", text="Parking Meter")
        scol.operator("color.coco_stop_sign", text="Stop Sign")
        scol.operator("color.coco_street_sign", text="Street Sign")
        scol.operator("color.coco_traffic_light", text="Traffic Light")


# COCO THINGS OUTDOOR SPORTS PANEL
class COCOTOSportsPanel(bpy.types.Panel):
    bl_idname = "COCO_SPORTS_PT_PANEL"
    bl_label = "        Sports"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_baseball_bat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_baseball_glove"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_frisbee"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_kite"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_skateboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_skis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_snowboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sports_ball"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_surfboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_tennis_racket"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_baseball_bat", text="Baseball Bat")
        scol.operator("color.coco_baseball_glove", text="Baseball Glove")
        scol.operator("color.coco_frisbee", text="Frisbee")
        scol.operator("color.coco_kite", text="Kite")
        scol.operator("color.coco_skateboard", text="Skateboard")
        scol.operator("color.coco_skis", text="Skis")
        scol.operator("color.coco_snowboard", text="Snowboard")
        scol.operator("color.coco_sports_ball", text="Sports Ball")
        scol.operator("color.coco_surfboard", text="Surfboard")
        scol.operator("color.coco_tennis_racket", text="Tennis Racket")


# COCO THINGS OUTDOOR VEHICLE PANEL
class COCOTOVehiclePanel(bpy.types.Panel):
    bl_idname = "COCO_VEHICLE_PT_PANEL"
    bl_label = "        Vehicle"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_airplane"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_bicycle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_boat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_bus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_car"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_motorcycle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_train"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_truck"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_airplane", text="Airplane")
        scol.operator("color.coco_bicycle", text="Bicycle")
        scol.operator("color.coco_boat", text="Boat")
        scol.operator("color.coco_bus", text="Bus")
        scol.operator("color.coco_car", text="Car")
        scol.operator("color.coco_motorcycle", text="Motorcycle")
        scol.operator("color.coco_train", text="Train")
        scol.operator("color.coco_truck", text="Truck")


# COCO THINGS INDOOR APPLIANCE PANEL
class COCOTIAppliancePanel(bpy.types.Panel):
    bl_idname = "COCO_APPLIANCE_PT_PANEL"
    bl_label = "        Appliance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_blender"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_microwave"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_oven"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_refrigerator"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_toaster"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_blender", text="Blender")
        scol.operator("color.coco_microwave", text="Microwave")
        scol.operator("color.coco_oven", text="Oven")
        scol.operator("color.coco_refrigerator", text="Refrigerator")
        scol.operator("color.coco_sink", text="Sink")
        scol.operator("color.coco_toaster", text="Toaster")


# COCO THINGS INDOOR ELECTRONIC PANEL
class COCOTIElectronicPanel(bpy.types.Panel):
    bl_idname = "COCO_ELECTRONIC_PT_PANEL"
    bl_label = "        Electronic"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_cell_phone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_keyboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_laptop"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_mouse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_remote"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_tv"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_cell_phone", text="Cell Phone")
        scol.operator("color.coco_keyboard", text="Keyboard")
        scol.operator("color.coco_laptop", text="Laptop")
        scol.operator("color.coco_mouse", text="Mouse")
        scol.operator("color.coco_remote", text="Remote")
        scol.operator("color.coco_tv", text="TV")


# COCO THINGS INDOOR FOOD PANEL
class COCOTIFoodPanel(bpy.types.Panel):
    bl_idname = "COCO_FOOD_PT_PANEL"
    bl_label = "        Food"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_apple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_banana"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_broccoli"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_cake"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_carrot"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_donut"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_hot_dog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_pizza"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sandwich"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_apple", text="Apple")
        scol.operator("color.coco_banana", text="Banana")
        scol.operator("color.coco_broccoli", text="Broccoli")
        scol.operator("color.coco_cake", text="Cake")
        scol.operator("color.coco_carrot", text="Carrot")
        scol.operator("color.coco_donut", text="Donut")
        scol.operator("color.coco_hot_dog", text="Hot Dog")
        scol.operator("color.coco_orange", text="Orange")
        scol.operator("color.coco_pizza", text="Pizza")
        scol.operator("color.coco_sandwich", text="Sandwich")


# COCO THINGS INDOOR FURNITURE PANEL
class COCOTIFurniturePanel(bpy.types.Panel):
    bl_idname = "COCO_FURNITURE_PT_PANEL"
    bl_label = "        Furniture"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_bed"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_chair"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_couch"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_desk"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_dining_table"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_door"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_mirror"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_potted_plant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_toilet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_window"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_bed", text="Bed")
        scol.operator("color.coco_chair", text="Chair")
        scol.operator("color.coco_couch", text="Couch")
        scol.operator("color.coco_desk", text="Desk")
        scol.operator("color.coco_dining_table", text="Dining Table")
        scol.operator("color.coco_door", text="Door")
        scol.operator("color.coco_mirror", text="Mirror")
        scol.operator("color.coco_potted_plant", text="Potted Plant")
        scol.operator("color.coco_toilet", text="Toilet")
        scol.operator("color.coco_window", text="Window")


# COCO THINGS INDOOR INDOOR PANEL
class COCOTIIndoorPanel(bpy.types.Panel):
    bl_idname = "COCO_INDOOR_PT_PANEL"
    bl_label = "        Indoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_book"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_clock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_hair_brush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_hair_drier"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_scissors"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_teddy_bear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_toothbrush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_vase"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_book", text="Book")
        scol.operator("color.coco_clock", text="Clock")
        scol.operator("color.coco_hair_brush", text="Hair Brush")
        scol.operator("color.coco_hair_drier", text="Hair Drier")
        scol.operator("color.coco_scissors", text="Scissors")
        scol.operator("color.coco_teddy_bear", text="Teddy Bear")
        scol.operator("color.coco_toothbrush", text="Toothbrush")
        scol.operator("color.coco_vase", text="Vase")


# COCO THINGS INDOOR KITCHEN PANEL
class COCOTIKitchenPanel(bpy.types.Panel):
    bl_idname = "COCO_KITCHEN_PT_PANEL"
    bl_label = "        Kitchen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_bottle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_bowl"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_cup"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_fork"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_knife"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_plate"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_spoon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wine_glass"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_bottle", text="Bottle")
        scol.operator("color.coco_bowl", text="Bowl")
        scol.operator("color.coco_cup", text="Cup")
        scol.operator("color.coco_fork", text="Fork")
        scol.operator("color.coco_knife", text="Knife")
        scol.operator("color.coco_plate", text="Plate")
        scol.operator("color.coco_spoon", text="Spoon")
        scol.operator("color.coco_wine_glass", text="Wine Glass")


# COCO STUFF OUTDOOR BUILDING PANEL
class COCOSOBuildingPanel(bpy.types.Panel):
    bl_idname = "COCO_BUILDING_PT_PANEL"
    bl_label = "        Building"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_bridge"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_building_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_house"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_roof"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_skyscraper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_tent"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_bridge", text="Bridge")
        scol.operator("color.coco_building_other", text="Building Other")
        scol.operator("color.coco_house", text="House")
        scol.operator("color.coco_roof", text="Roof")
        scol.operator("color.coco_skyscraper", text="Skyscraper")
        scol.operator("color.coco_tent", text="Tent")


# COCO STUFF OUTDOOR GROUND PANEL
class COCOSOGroundPanel(bpy.types.Panel):
    bl_idname = "COCO_GROUND_PT_PANEL"
    bl_label = "        Ground"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_dirt"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_gravel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_ground_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_mud"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_pavement"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_platform"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_playing_field"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_railroad"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_road"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sand"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_snow"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_dirt", text="Dirt")
        scol.operator("color.coco_gravel", text="Gravel")
        scol.operator("color.coco_ground_other", text="Ground Other")
        scol.operator("color.coco_mud", text="Mud")
        scol.operator("color.coco_pavement", text="Pavement")
        scol.operator("color.coco_platform", text="Platform")
        scol.operator("color.coco_playing_field", text="Playing Field")
        scol.operator("color.coco_railroad", text="Railroad")
        scol.operator("color.coco_road", text="Road")
        scol.operator("color.coco_sand", text="Sand")
        scol.operator("color.coco_snow", text="Snow")


# COCO STUFF OUTDOOR PLANT PANEL
class COCOSOPlantPanel(bpy.types.Panel):
    bl_idname = "COCO_PLANT_PT_PANEL"
    bl_label = "        Plant"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_branch"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_bush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_flower"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_grass"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_leaves"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_moss"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_plant_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_straw"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_tree"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_branch", text="Branch")
        scol.operator("color.coco_bush", text="Bush")
        scol.operator("color.coco_flower", text="Flower")
        scol.operator("color.coco_grass", text="Grass")
        scol.operator("color.coco_leaves", text="Leaves")
        scol.operator("color.coco_moss", text="Moss")
        scol.operator("color.coco_plant_other", text="Plant Other")
        scol.operator("color.coco_straw", text="Straw")
        scol.operator("color.coco_tree", text="Tree")


# COCO STUFF OUTDOOR SKY PANEL
class COCOSOSkyPanel(bpy.types.Panel):
    bl_idname = "COCO_SKY_PT_PANEL"
    bl_label = "        Sky"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_clouds"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sky_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_clouds", text="Clouds")
        scol.operator("color.coco_sky_other", text="Sky Other")


# COCO STUFF OUTDOOR SOLID PANEL
class COCOSOSolidPanel(bpy.types.Panel):
    bl_idname = "COCO_SOLID_PT_PANEL"
    bl_label = "        Solid"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_hill"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_mountain"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_rock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_solid_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wood"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_hill", text="Hill")
        scol.operator("color.coco_mountain", text="Mountain")
        scol.operator("color.coco_rock", text="Rock")
        scol.operator("color.coco_solid_other", text="Solid Other")
        scol.operator("color.coco_stone", text="Stone")
        scol.operator("color.coco_wood", text="Wood")


# COCO STUFF OUTDOOR STRUCTURAL PANEL
class COCOSOStructuralPanel(bpy.types.Panel):
    bl_idname = "COCO_STRUCTURAL_PT_PANEL"
    bl_label = "        Structural"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_cage"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_fence"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_net"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_railing"].icon_id)
        scol.label(
            text="", icon_value=g.c_icons["coco_structural_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_cage", text="Cage")
        scol.operator("color.coco_fence", text="Fence")
        scol.operator("color.coco_net", text="Net")
        scol.operator("color.coco_railing", text="Railing")
        scol.operator("color.coco_structural_other", text="Structural Other")


# COCO STUFF OUTDOOR WATER PANEL
class COCOSOWaterPanel(bpy.types.Panel):
    bl_idname = "COCO_WATER_PT_PANEL"
    bl_label = "        Water"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_fog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_river"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_sea"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_water_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_waterdrops"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_fog", text="Fog")
        scol.operator("color.coco_river", text="River")
        scol.operator("color.coco_sea", text="Sea")
        scol.operator("color.coco_water_other", text="Water Other")
        scol.operator("color.coco_waterdrops", text="Waterdrops")


# COCO STUFF INDOOR CEILING PANEL
class COCOSICeilingPanel(bpy.types.Panel):
    bl_idname = "COCO_CEILING_PT_PANEL"
    bl_label = "        Ceiling"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_ceiling_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_ceiling_tile"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_ceiling_other", text="Ceiling Other")
        scol.operator("color.coco_ceiling_tile", text="Ceiling Tile")


# COCO STUFF INDOOR FLOOR PANEL
class COCOSIFloorPanel(bpy.types.Panel):
    bl_idname = "COCO_FLOOR_PT_PANEL"
    bl_label = "        Floor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_carpet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_floor_marble"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_floor_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_floor_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_floor_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_floor_wood"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_carpet", text="Carpet")
        scol.operator("color.coco_floor_marble", text="Floor Marble")
        scol.operator("color.coco_floor_other", text="Floor Other")
        scol.operator("color.coco_floor_stone", text="Floor Stone")
        scol.operator("color.coco_floor_tile", text="Floor Tile")
        scol.operator("color.coco_floor_wood", text="Floor Wood")


# COCO STUFF INDOOR FOOD PANEL
class COCOSIFoodPanel(bpy.types.Panel):
    bl_idname = "COCO_SI_FOOD_PT_PANEL"
    bl_label = "        Food"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_food_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_fruit"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_salad"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_vegetable"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_food_other", text="Food Other")
        scol.operator("color.coco_fruit", text="Fruit")
        scol.operator("color.coco_salad", text="Salad")
        scol.operator("color.coco_vegetable", text="Vegetable")


# COCO STUFF INDOOR FURNITURE PANEL
class COCOSIFurniturePanel(bpy.types.Panel):
    bl_idname = "COCO_SI_FURNITURE_PT_PANEL"
    bl_label = "        Furniture"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_cabinet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_counter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_cupboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_desk_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_door_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_furniture_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_mirror_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_shelf"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_stairs"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_table"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_cabinet", text="Cabinet")
        scol.operator("color.coco_counter", text="Counter")
        scol.operator("color.coco_cupboard", text="Cupboard")
        scol.operator("color.coco_desk_stuff", text="Desk (Stuff)")
        scol.operator("color.coco_door_stuff", text="Door (Stuff)")
        scol.operator("color.coco_furniture_other", text="Furniture Other")
        scol.operator("color.coco_light", text="Light")
        scol.operator("color.coco_mirror_stuff", text="Mirror (Stuff)")
        scol.operator("color.coco_shelf", text="Shelf")
        scol.operator("color.coco_stairs", text="Stairs")
        scol.operator("color.coco_table", text="Table")


# COCO STUFF INDOOR RAW MATERIAL PANEL
class COCOSIRawMaterialPanel(bpy.types.Panel):
    bl_idname = "COCO_RAW_MATERIAL_PT_PANEL"
    bl_label = "        Raw Material"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_cardboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_metal"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_paper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_plastic"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_cardboard", text="Cardboard")
        scol.operator("color.coco_metal", text="Metal")
        scol.operator("color.coco_paper", text="Paper")
        scol.operator("color.coco_plastic", text="Plastic")


# COCO STUFF INDOOR TEXTILE PANEL
class COCOSITextilePanel(bpy.types.Panel):
    bl_idname = "COCO_TEXTILE_PT_PANEL"
    bl_label = "        Textile"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_banner"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_blanket"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_cloth"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_clothes"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_curtain"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_mat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_napkin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_pillow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_rug"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_textile_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_towel"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_banner", text="Banner")
        scol.operator("color.coco_blanket", text="Blanket")
        scol.operator("color.coco_cloth", text="Cloth")
        scol.operator("color.coco_clothes", text="Clothes")
        scol.operator("color.coco_curtain", text="Curtain")
        scol.operator("color.coco_mat", text="Mat")
        scol.operator("color.coco_napkin", text="Napkin")
        scol.operator("color.coco_pillow", text="Pillow")
        scol.operator("color.coco_rug", text="Rug")
        scol.operator("color.coco_textile_other", text="Textile Other")
        scol.operator("color.coco_towel", text="Towel")


# COCO STUFF INDOOR WALL PANEL
class COCOSIWallPanel(bpy.types.Panel):
    bl_idname = "COCO_WALL_PT_PANEL"
    bl_label = "        Wall"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_wall_brick"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wall_concrete"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wall_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wall_panel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wall_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wall_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_wall_wood"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_wall_brick", text="Wall Brick")
        scol.operator("color.coco_wall_concrete", text="Wall Concrete")
        scol.operator("color.coco_wall_other", text="Wall Other")
        scol.operator("color.coco_wall_panel", text="Wall Panel")
        scol.operator("color.coco_wall_stone", text="Wall Stone")
        scol.operator("color.coco_wall_tile", text="Wall Tile")
        scol.operator("color.coco_wall_wood", text="Wall Wood")


# COCO STUFF INDOOR WINDOW PANEL
class COCOSIWindowPanel(bpy.types.Panel):
    bl_idname = "COCO_WINDOW_PT_PANEL"
    bl_label = "        Window"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'COCO_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout
        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["coco_window_blind"].icon_id)
        scol.label(text="", icon_value=g.c_icons["coco_window_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.coco_window_blind", text="Window Blind")
        scol.operator("color.coco_window_other", text="Window Other")


# COCO CLASSES
array_coco = [
    COCOPanel,
    COCOThingsOutPanel,
    COCOThingsInPanel,
    COCOStuffOutPanel,
    COCOStuffInPanel,
    COCOTOAccessoryPanel,
    COCOTOAnimalPanel,
    COCOTOOutdoorPanel,
    COCOTOSportsPanel,
    COCOTOVehiclePanel,
    COCOTIAppliancePanel,
    COCOTIElectronicPanel,
    COCOTIFoodPanel,
    COCOTIFurniturePanel,
    COCOTIIndoorPanel,
    COCOTIKitchenPanel,
    COCOSOBuildingPanel,
    COCOSOGroundPanel,
    COCOSOPlantPanel,
    COCOSOSkyPanel,
    COCOSOSolidPanel,
    COCOSOStructuralPanel,
    COCOSOWaterPanel,
    COCOSICeilingPanel,
    COCOSIFloorPanel,
    COCOSIFoodPanel,
    COCOSIFurniturePanel,
    COCOSIRawMaterialPanel,
    COCOSITextilePanel,
    COCOSIWallPanel,
    COCOSIWindowPanel,
    COCO_Undefined,
    COCO_Person,
    COCO_Backpack,
    COCO_Eye_Glasses,
    COCO_Handbag,
    COCO_Hat,
    COCO_Shoe,
    COCO_Suitcase,
    COCO_Tie,
    COCO_Umbrella,
    COCO_Bear,
    COCO_Bird,
    COCO_Cat,
    COCO_Cow,
    COCO_Dog,
    COCO_Elephant,
    COCO_Giraffe,
    COCO_Horse,
    COCO_Sheep,
    COCO_Zebra,
    COCO_Bench,
    COCO_Fire_Hydrant,
    COCO_Parking_Meter,
    COCO_Stop_Sign,
    COCO_Street_Sign,
    COCO_Traffic_Light,
    COCO_Baseball_Bat,
    COCO_Baseball_Glove,
    COCO_Frisbee,
    COCO_Kite,
    COCO_Skateboard,
    COCO_Skis,
    COCO_Snowboard,
    COCO_Sports_Ball,
    COCO_Surfboard,
    COCO_Tennis_Racket,
    COCO_Airplane,
    COCO_Bicycle,
    COCO_Boat,
    COCO_Bus,
    COCO_Car,
    COCO_Motorcycle,
    COCO_Train,
    COCO_Truck,
    COCO_Blender,
    COCO_Microwave,
    COCO_Oven,
    COCO_Refrigerator,
    COCO_Sink,
    COCO_Toaster,
    COCO_Cell_Phone,
    COCO_Keyboard,
    COCO_Laptop,
    COCO_Mouse,
    COCO_Remote,
    COCO_TV,
    COCO_Apple,
    COCO_Banana,
    COCO_Broccoli,
    COCO_Cake,
    COCO_Carrot,
    COCO_Donut,
    COCO_Hot_Dog,
    COCO_Orange,
    COCO_Pizza,
    COCO_Sandwich,
    COCO_Bed,
    COCO_Chair,
    COCO_Couch,
    COCO_Desk,
    COCO_Dining_Table,
    COCO_Door,
    COCO_Mirror,
    COCO_Potted_Plant,
    COCO_Toilet,
    COCO_Window,
    COCO_Book,
    COCO_Clock,
    COCO_Hair_Brush,
    COCO_Hair_Drier,
    COCO_Scissors,
    COCO_Teddy_Bear,
    COCO_Toothbrush,
    COCO_Vase,
    COCO_Bottle,
    COCO_Bowl,
    COCO_Cup,
    COCO_Fork,
    COCO_Knife,
    COCO_Plate,
    COCO_Spoon,
    COCO_Wine_Glass,
    COCO_Bridge,
    COCO_Building_Other,
    COCO_House,
    COCO_Roof,
    COCO_Skyscraper,
    COCO_Tent,
    COCO_Dirt,
    COCO_Gravel,
    COCO_Ground_Other,
    COCO_Mud,
    COCO_Pavement,
    COCO_Platform,
    COCO_Playing_Field,
    COCO_Railroad,
    COCO_Road,
    COCO_Sand,
    COCO_Snow,
    COCO_Branch,
    COCO_Bush,
    COCO_Flower,
    COCO_Grass,
    COCO_Leaves,
    COCO_Moss,
    COCO_Plant_Other,
    COCO_Straw,
    COCO_Tree,
    COCO_Clouds,
    COCO_Sky_Other,
    COCO_Hill,
    COCO_Mountain,
    COCO_Rock,
    COCO_Solid_Other,
    COCO_Stone,
    COCO_Wood,
    COCO_Cage,
    COCO_Fence,
    COCO_Net,
    COCO_Railing,
    COCO_Structural_Other,
    COCO_Fog,
    COCO_River,
    COCO_Sea,
    COCO_Water_Other,
    COCO_Waterdrops,
    COCO_Ceiling_Other,
    COCO_Ceiling_Tile,
    COCO_Carpet,
    COCO_Floor_Marble,
    COCO_Floor_Other,
    COCO_Floor_Stone,
    COCO_Floor_Tile,
    COCO_Floor_Wood,
    COCO_Food_Other,
    COCO_Fruit,
    COCO_Salad,
    COCO_Vegetable,
    COCO_Cabinet,
    COCO_Counter,
    COCO_Cupboard,
    COCO_Desk_Stuff,
    COCO_Door_Stuff,
    COCO_Furniture_Other,
    COCO_Light,
    COCO_Mirror_Stuff,
    COCO_Shelf,
    COCO_Stairs,
    COCO_Table,
    COCO_Cardboard,
    COCO_Metal,
    COCO_Paper,
    COCO_Plastic,
    COCO_Banner,
    COCO_Blanket,
    COCO_Cloth,
    COCO_Clothes,
    COCO_Curtain,
    COCO_Mat,
    COCO_Napkin,
    COCO_Pillow,
    COCO_Rug,
    COCO_Textile_Other,
    COCO_Towel,
    COCO_Wall_Brick,
    COCO_Wall_Concrete,
    COCO_Wall_Other,
    COCO_Wall_Panel,
    COCO_Wall_Stone,
    COCO_Wall_Tile,
    COCO_Wall_Wood,
    COCO_Window_Blind,
    COCO_Window_Other,
]
