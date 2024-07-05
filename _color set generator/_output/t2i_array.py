# T2I COLORS SET

import bpy

from .globals import *
from .color_functions import *

# T2I OPERATORS


class T2I_Undefined(bpy.types.Operator):
    """T2I Undefined"""
    bl_label = "Undefined"
    bl_idname = 'color.t2i_undefined'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Person(bpy.types.Operator):
    """T2I Person"""
    bl_label = "Person"
    bl_idname = 'color.t2i_person'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Backpack(bpy.types.Operator):
    """T2I Backpack"""
    bl_label = "Backpack"
    bl_idname = 'color.t2i_backpack'

    def execute(self, context):
        set_base_color(0xA020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Eye_Glasses(bpy.types.Operator):
    """T2I Eye Glasses"""
    bl_label = "Eye Glasses"
    bl_idname = 'color.t2i_eye_glasses'

    def execute(self, context):
        set_base_color(0x60E060, self.bl_label)
        return {'FINISHED'}


class T2I_Handbag(bpy.types.Operator):
    """T2I Handbag"""
    bl_label = "Handbag"
    bl_idname = 'color.t2i_handbag'

    def execute(self, context):
        set_base_color(0xE060E0, self.bl_label)
        return {'FINISHED'}


class T2I_Hat(bpy.types.Operator):
    """T2I Hat"""
    bl_label = "Hat"
    bl_idname = 'color.t2i_hat'

    def execute(self, context):
        set_base_color(0x60E020, self.bl_label)
        return {'FINISHED'}


class T2I_Shoe(bpy.types.Operator):
    """T2I Shoe"""
    bl_label = "Shoe"
    bl_idname = 'color.t2i_shoe'

    def execute(self, context):
        set_base_color(0xA060E0, self.bl_label)
        return {'FINISHED'}


class T2I_Suitcase(bpy.types.Operator):
    """T2I Suitcase"""
    bl_label = "Suitcase"
    bl_idname = 'color.t2i_suitcase'

    def execute(self, context):
        set_base_color(0xA020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Tie(bpy.types.Operator):
    """T2I Tie"""
    bl_label = "Tie"
    bl_idname = 'color.t2i_tie'

    def execute(self, context):
        set_base_color(0x20A020, self.bl_label)
        return {'FINISHED'}


class T2I_Umbrella(bpy.types.Operator):
    """T2I Umbrella"""
    bl_label = "Umbrella"
    bl_idname = 'color.t2i_umbrella'

    def execute(self, context):
        set_base_color(0x20A020, self.bl_label)
        return {'FINISHED'}


class T2I_Bear(bpy.types.Operator):
    """T2I Bear"""
    bl_label = "Bear"
    bl_idname = 'color.t2i_bear'

    def execute(self, context):
        set_base_color(0xA020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Bird(bpy.types.Operator):
    """T2I Bird"""
    bl_label = "Bird"
    bl_idname = 'color.t2i_bird'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Cat(bpy.types.Operator):
    """T2I Cat"""
    bl_label = "Cat"
    bl_idname = 'color.t2i_cat'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Cow(bpy.types.Operator):
    """T2I Cow"""
    bl_label = "Cow"
    bl_idname = 'color.t2i_cow'

    def execute(self, context):
        set_base_color(0xC020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Dog(bpy.types.Operator):
    """T2I Dog"""
    bl_label = "Dog"
    bl_idname = 'color.t2i_dog'

    def execute(self, context):
        set_base_color(0x008040, self.bl_label)
        return {'FINISHED'}


class T2I_Elephant(bpy.types.Operator):
    """T2I Elephant"""
    bl_label = "Elephant"
    bl_idname = 'color.t2i_elephant'

    def execute(self, context):
        set_base_color(0x20A020, self.bl_label)
        return {'FINISHED'}


class T2I_Giraffe(bpy.types.Operator):
    """T2I Giraffe"""
    bl_label = "Giraffe"
    bl_idname = 'color.t2i_giraffe'

    def execute(self, context):
        set_base_color(0xE060E0, self.bl_label)
        return {'FINISHED'}


class T2I_Horse(bpy.types.Operator):
    """T2I Horse"""
    bl_label = "Horse"
    bl_idname = 'color.t2i_horse'

    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Sheep(bpy.types.Operator):
    """T2I Sheep"""
    bl_label = "Sheep"
    bl_idname = 'color.t2i_sheep'

    def execute(self, context):
        set_base_color(0x40C040, self.bl_label)
        return {'FINISHED'}


class T2I_Zebra(bpy.types.Operator):
    """T2I Zebra"""
    bl_label = "Zebra"
    bl_idname = 'color.t2i_zebra'

    def execute(self, context):
        set_base_color(0x60E060, self.bl_label)
        return {'FINISHED'}


class T2I_Bench(bpy.types.Operator):
    """T2I Bench"""
    bl_label = "Bench"
    bl_idname = 'color.t2i_bench'

    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Fire_Hydrant(bpy.types.Operator):
    """T2I Fire Hydrant"""
    bl_label = "Fire Hydrant"
    bl_idname = 'color.t2i_fire_hydrant'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Parking_Meter(bpy.types.Operator):
    """T2I Parking Meter"""
    bl_label = "Parking Meter"
    bl_idname = 'color.t2i_parking_meter'

    def execute(self, context):
        set_base_color(0x40C040, self.bl_label)
        return {'FINISHED'}


class T2I_Stop_Sign(bpy.types.Operator):
    """T2I Stop Sign"""
    bl_label = "Stop Sign"
    bl_idname = 'color.t2i_stop_sign'

    def execute(self, context):
        set_base_color(0x8040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Street_Sign(bpy.types.Operator):
    """T2I Street Sign"""
    bl_label = "Street Sign"
    bl_idname = 'color.t2i_street_sign'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Traffic_Light(bpy.types.Operator):
    """T2I Traffic Light"""
    bl_label = "Traffic Light"
    bl_idname = 'color.t2i_traffic_light'

    def execute(self, context):
        set_base_color(0x40C000, self.bl_label)
        return {'FINISHED'}


class T2I_Baseball_Bat(bpy.types.Operator):
    """T2I Baseball Bat"""
    bl_label = "Baseball Bat"
    bl_idname = 'color.t2i_baseball_bat'

    def execute(self, context):
        set_base_color(0xA020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Baseball_Glove(bpy.types.Operator):
    """T2I Baseball Glove"""
    bl_label = "Baseball Glove"
    bl_idname = 'color.t2i_baseball_glove'

    def execute(self, context):
        set_base_color(0x60E060, self.bl_label)
        return {'FINISHED'}


class T2I_Frisbee(bpy.types.Operator):
    """T2I Frisbee"""
    bl_label = "Frisbee"
    bl_idname = 'color.t2i_frisbee'

    def execute(self, context):
        set_base_color(0x20A060, self.bl_label)
        return {'FINISHED'}


class T2I_Kite(bpy.types.Operator):
    """T2I Kite"""
    bl_label = "Kite"
    bl_idname = 'color.t2i_kite'

    def execute(self, context):
        set_base_color(0x20A020, self.bl_label)
        return {'FINISHED'}


class T2I_Skateboard(bpy.types.Operator):
    """T2I Skateboard"""
    bl_label = "Skateboard"
    bl_idname = 'color.t2i_skateboard'

    def execute(self, context):
        set_base_color(0xE01DE0, self.bl_label)
        return {'FINISHED'}


class T2I_Skis(bpy.types.Operator):
    """T2I Skis"""
    bl_label = "Skis"
    bl_idname = 'color.t2i_skis'

    def execute(self, context):
        set_base_color(0xE0AAE0, self.bl_label)
        return {'FINISHED'}


class T2I_Snowboard(bpy.types.Operator):
    """T2I Snowboard"""
    bl_label = "Snowboard"
    bl_idname = 'color.t2i_snowboard'

    def execute(self, context):
        set_base_color(0x60E060, self.bl_label)
        return {'FINISHED'}


class T2I_Sports_Ball(bpy.types.Operator):
    """T2I Sports Ball"""
    bl_label = "Sports Ball"
    bl_idname = 'color.t2i_sports_ball'

    def execute(self, context):
        set_base_color(0xE020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Surfboard(bpy.types.Operator):
    """T2I Surfboard"""
    bl_label = "Surfboard"
    bl_idname = 'color.t2i_surfboard'

    def execute(self, context):
        set_base_color(0x60E000, self.bl_label)
        return {'FINISHED'}


class T2I_Tennis_Racket(bpy.types.Operator):
    """T2I Tennis Racket"""
    bl_label = "Tennis Racket"
    bl_idname = 'color.t2i_tennis_racket'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Airplane(bpy.types.Operator):
    """T2I Airplane"""
    bl_label = "Airplane"
    bl_idname = 'color.t2i_airplane'

    def execute(self, context):
        set_base_color(0xC00080, self.bl_label)
        return {'FINISHED'}


class T2I_Bicycle(bpy.types.Operator):
    """T2I Bicycle"""
    bl_label = "Bicycle"
    bl_idname = 'color.t2i_bicycle'

    def execute(self, context):
        set_base_color(0x008040, self.bl_label)
        return {'FINISHED'}


class T2I_Boat(bpy.types.Operator):
    """T2I Boat"""
    bl_label = "Boat"
    bl_idname = 'color.t2i_boat'

    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Bus(bpy.types.Operator):
    """T2I Bus"""
    bl_label = "Bus"
    bl_idname = 'color.t2i_bus'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Car(bpy.types.Operator):
    """T2I Car"""
    bl_label = "Car"
    bl_idname = 'color.t2i_car'

    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Motorcycle(bpy.types.Operator):
    """T2I Motorcycle"""
    bl_label = "Motorcycle"
    bl_idname = 'color.t2i_motorcycle'

    def execute(self, context):
        set_base_color(0x40C040, self.bl_label)
        return {'FINISHED'}


class T2I_Train(bpy.types.Operator):
    """T2I Train"""
    bl_label = "Train"
    bl_idname = 'color.t2i_train'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Truck(bpy.types.Operator):
    """T2I Truck"""
    bl_label = "Truck"
    bl_idname = 'color.t2i_truck'

    def execute(self, context):
        set_base_color(0x40C040, self.bl_label)
        return {'FINISHED'}


class T2I_Blender(bpy.types.Operator):
    """T2I Blender"""
    bl_label = "Blender"
    bl_idname = 'color.t2i_blender'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_Microwave(bpy.types.Operator):
    """T2I Microwave"""
    bl_label = "Microwave"
    bl_idname = 'color.t2i_microwave'

    def execute(self, context):
        set_base_color(0xC04040, self.bl_label)
        return {'FINISHED'}


class T2I_Oven(bpy.types.Operator):
    """T2I Oven"""
    bl_label = "Oven"
    bl_idname = 'color.t2i_oven'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Refrigerator(bpy.types.Operator):
    """T2I Refrigerator"""
    bl_label = "Refrigerator"
    bl_idname = 'color.t2i_refrigerator'

    def execute(self, context):
        set_base_color(0xC00000, self.bl_label)
        return {'FINISHED'}


class T2I_Sink(bpy.types.Operator):
    """T2I Sink"""
    bl_label = "Sink"
    bl_idname = 'color.t2i_sink'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Toaster(bpy.types.Operator):
    """T2I Toaster"""
    bl_label = "Toaster"
    bl_idname = 'color.t2i_toaster'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Cell_Phone(bpy.types.Operator):
    """T2I Cell Phone"""
    bl_label = "Cell Phone"
    bl_idname = 'color.t2i_cell_phone'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Keyboard(bpy.types.Operator):
    """T2I Keyboard"""
    bl_label = "Keyboard"
    bl_idname = 'color.t2i_keyboard'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Laptop(bpy.types.Operator):
    """T2I Laptop"""
    bl_label = "Laptop"
    bl_idname = 'color.t2i_laptop'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Mouse(bpy.types.Operator):
    """T2I Mouse"""
    bl_label = "Mouse"
    bl_idname = 'color.t2i_mouse'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Remote(bpy.types.Operator):
    """T2I Remote"""
    bl_label = "Remote"
    bl_idname = 'color.t2i_remote'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_TV(bpy.types.Operator):
    """T2I TV"""
    bl_label = "TV"
    bl_idname = 'color.t2i_tv'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Apple(bpy.types.Operator):
    """T2I Apple"""
    bl_label = "Apple"
    bl_idname = 'color.t2i_apple'

    def execute(self, context):
        set_base_color(0xC00080, self.bl_label)
        return {'FINISHED'}


class T2I_Banana(bpy.types.Operator):
    """T2I Banana"""
    bl_label = "Banana"
    bl_idname = 'color.t2i_banana'

    def execute(self, context):
        set_base_color(0x405F40, self.bl_label)
        return {'FINISHED'}


class T2I_Broccoli(bpy.types.Operator):
    """T2I Broccoli"""
    bl_label = "Broccoli"
    bl_idname = 'color.t2i_broccoli'

    def execute(self, context):
        set_base_color(0x408C40, self.bl_label)
        return {'FINISHED'}


class T2I_Cake(bpy.types.Operator):
    """T2I Cake"""
    bl_label = "Cake"
    bl_idname = 'color.t2i_cake'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Carrot(bpy.types.Operator):
    """T2I Carrot"""
    bl_label = "Carrot"
    bl_idname = 'color.t2i_carrot'

    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Donut(bpy.types.Operator):
    """T2I Donut"""
    bl_label = "Donut"
    bl_idname = 'color.t2i_donut'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Hot_Dog(bpy.types.Operator):
    """T2I Hot Dog"""
    bl_label = "Hot Dog"
    bl_idname = 'color.t2i_hot_dog'

    def execute(self, context):
        set_base_color(0x40C000, self.bl_label)
        return {'FINISHED'}


class T2I_Orange(bpy.types.Operator):
    """T2I Orange"""
    bl_label = "Orange"
    bl_idname = 'color.t2i_orange'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Pizza(bpy.types.Operator):
    """T2I Pizza"""
    bl_label = "Pizza"
    bl_idname = 'color.t2i_pizza'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Sandwich(bpy.types.Operator):
    """T2I Sandwich"""
    bl_label = "Sandwich"
    bl_idname = 'color.t2i_sandwich'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Bed(bpy.types.Operator):
    """T2I Bed"""
    bl_label = "Bed"
    bl_idname = 'color.t2i_bed'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Chair(bpy.types.Operator):
    """T2I Chair"""
    bl_label = "Chair"
    bl_idname = 'color.t2i_chair'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Couch(bpy.types.Operator):
    """T2I Couch"""
    bl_label = "Couch"
    bl_idname = 'color.t2i_couch'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_Desk(bpy.types.Operator):
    """T2I Desk"""
    bl_label = "Desk"
    bl_idname = 'color.t2i_desk'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Dining_Table(bpy.types.Operator):
    """T2I Dining Table"""
    bl_label = "Dining Table"
    bl_idname = 'color.t2i_dining_table'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Door(bpy.types.Operator):
    """T2I Door"""
    bl_label = "Door"
    bl_idname = 'color.t2i_door'

    def execute(self, context):
        set_base_color(0xC0C000, self.bl_label)
        return {'FINISHED'}


class T2I_Mirror(bpy.types.Operator):
    """T2I Mirror"""
    bl_label = "Mirror"
    bl_idname = 'color.t2i_mirror'

    def execute(self, context):
        set_base_color(0x804040, self.bl_label)
        return {'FINISHED'}


class T2I_Potted_Plant(bpy.types.Operator):
    """T2I Potted Plant"""
    bl_label = "Potted Plant"
    bl_idname = 'color.t2i_potted_plant'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Toilet(bpy.types.Operator):
    """T2I Toilet"""
    bl_label = "Toilet"
    bl_idname = 'color.t2i_toilet'

    def execute(self, context):
        set_base_color(0xC04040, self.bl_label)
        return {'FINISHED'}


class T2I_Window(bpy.types.Operator):
    """T2I Window"""
    bl_label = "Window"
    bl_idname = 'color.t2i_window'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Book(bpy.types.Operator):
    """T2I Book"""
    bl_label = "Book"
    bl_idname = 'color.t2i_book'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Clock(bpy.types.Operator):
    """T2I Clock"""
    bl_label = "Clock"
    bl_idname = 'color.t2i_clock'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Hair_Brush(bpy.types.Operator):
    """T2I Hair Brush"""
    bl_label = "Hair Brush"
    bl_idname = 'color.t2i_hair_brush'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Hair_Drier(bpy.types.Operator):
    """T2I Hair Drier"""
    bl_label = "Hair Drier"
    bl_idname = 'color.t2i_hair_drier'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Scissors(bpy.types.Operator):
    """T2I Scissors"""
    bl_label = "Scissors"
    bl_idname = 'color.t2i_scissors'

    def execute(self, context):
        set_base_color(0x808040, self.bl_label)
        return {'FINISHED'}


class T2I_Teddy_Bear(bpy.types.Operator):
    """T2I Teddy Bear"""
    bl_label = "Teddy Bear"
    bl_idname = 'color.t2i_teddy_bear'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Toothbrush(bpy.types.Operator):
    """T2I Toothbrush"""
    bl_label = "Toothbrush"
    bl_idname = 'color.t2i_toothbrush'

    def execute(self, context):
        set_base_color(0xC04040, self.bl_label)
        return {'FINISHED'}


class T2I_Vase(bpy.types.Operator):
    """T2I Vase"""
    bl_label = "Vase"
    bl_idname = 'color.t2i_vase'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Bottle(bpy.types.Operator):
    """T2I Bottle"""
    bl_label = "Bottle"
    bl_idname = 'color.t2i_bottle'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Bowl(bpy.types.Operator):
    """T2I Bowl"""
    bl_label = "Bowl"
    bl_idname = 'color.t2i_bowl'

    def execute(self, context):
        set_base_color(0xC04036, self.bl_label)
        return {'FINISHED'}


class T2I_Cup(bpy.types.Operator):
    """T2I Cup"""
    bl_label = "Cup"
    bl_idname = 'color.t2i_cup'

    def execute(self, context):
        set_base_color(0xC040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Fork(bpy.types.Operator):
    """T2I Fork"""
    bl_label = "Fork"
    bl_idname = 'color.t2i_fork'

    def execute(self, context):
        set_base_color(0x008000, self.bl_label)
        return {'FINISHED'}


class T2I_Knife(bpy.types.Operator):
    """T2I Knife"""
    bl_label = "Knife"
    bl_idname = 'color.t2i_knife'

    def execute(self, context):
        set_base_color(0x800080, self.bl_label)
        return {'FINISHED'}


class T2I_Plate(bpy.types.Operator):
    """T2I Plate"""
    bl_label = "Plate"
    bl_idname = 'color.t2i_plate'

    def execute(self, context):
        set_base_color(0x8040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Spoon(bpy.types.Operator):
    """T2I Spoon"""
    bl_label = "Spoon"
    bl_idname = 'color.t2i_spoon'

    def execute(self, context):
        set_base_color(0x008040, self.bl_label)
        return {'FINISHED'}


class T2I_Wine_Glass(bpy.types.Operator):
    """T2I Wine Glass"""
    bl_label = "Wine Glass"
    bl_idname = 'color.t2i_wine_glass'

    def execute(self, context):
        set_base_color(0x40C040, self.bl_label)
        return {'FINISHED'}


class T2I_Bridge(bpy.types.Operator):
    """T2I Bridge"""
    bl_label = "Bridge"
    bl_idname = 'color.t2i_bridge'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_Building_Other(bpy.types.Operator):
    """T2I Building Other"""
    bl_label = "Building Other"
    bl_idname = 'color.t2i_building_other'

    def execute(self, context):
        set_base_color(0x00AA80, self.bl_label)
        return {'FINISHED'}


class T2I_House(bpy.types.Operator):
    """T2I House"""
    bl_label = "House"
    bl_idname = 'color.t2i_house'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Roof(bpy.types.Operator):
    """T2I Roof"""
    bl_label = "Roof"
    bl_idname = 'color.t2i_roof'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Skyscraper(bpy.types.Operator):
    """T2I Skyscraper"""
    bl_label = "Skyscraper"
    bl_idname = 'color.t2i_skyscraper'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Tent(bpy.types.Operator):
    """T2I Tent"""
    bl_label = "Tent"
    bl_idname = 'color.t2i_tent'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Dirt(bpy.types.Operator):
    """T2I Dirt"""
    bl_label = "Dirt"
    bl_idname = 'color.t2i_dirt'

    def execute(self, context):
        set_base_color(0xE0E060, self.bl_label)
        return {'FINISHED'}


class T2I_Gravel(bpy.types.Operator):
    """T2I Gravel"""
    bl_label = "Gravel"
    bl_idname = 'color.t2i_gravel'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Ground_Other(bpy.types.Operator):
    """T2I Ground Other"""
    bl_label = "Ground Other"
    bl_idname = 'color.t2i_ground_other'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Mud(bpy.types.Operator):
    """T2I Mud"""
    bl_label = "Mud"
    bl_idname = 'color.t2i_mud'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Pavement(bpy.types.Operator):
    """T2I Pavement"""
    bl_label = "Pavement"
    bl_idname = 'color.t2i_pavement'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Platform(bpy.types.Operator):
    """T2I Platform"""
    bl_label = "Platform"
    bl_idname = 'color.t2i_platform'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Playing_Field(bpy.types.Operator):
    """T2I Playing Field"""
    bl_label = "Playing Field"
    bl_idname = 'color.t2i_playing_field'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Railroad(bpy.types.Operator):
    """T2I Railroad"""
    bl_label = "Railroad"
    bl_idname = 'color.t2i_railroad'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Road(bpy.types.Operator):
    """T2I Road"""
    bl_label = "Road"
    bl_idname = 'color.t2i_road'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Sand(bpy.types.Operator):
    """T2I Sand"""
    bl_label = "Sand"
    bl_idname = 'color.t2i_sand'

    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        return {'FINISHED'}


class T2I_Snow(bpy.types.Operator):
    """T2I Snow"""
    bl_label = "Snow"
    bl_idname = 'color.t2i_snow'

    def execute(self, context):
        set_base_color(0xC04040, self.bl_label)
        return {'FINISHED'}


class T2I_Branch(bpy.types.Operator):
    """T2I Branch"""
    bl_label = "Branch"
    bl_idname = 'color.t2i_branch'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Bush(bpy.types.Operator):
    """T2I Bush"""
    bl_label = "Bush"
    bl_idname = 'color.t2i_bush'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Flower(bpy.types.Operator):
    """T2I Flower"""
    bl_label = "Flower"
    bl_idname = 'color.t2i_flower'

    def execute(self, context):
        set_base_color(0xA0A060, self.bl_label)
        return {'FINISHED'}


class T2I_Grass(bpy.types.Operator):
    """T2I Grass"""
    bl_label = "Grass"
    bl_idname = 'color.t2i_grass'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_Leaves(bpy.types.Operator):
    """T2I Leaves"""
    bl_label = "Leaves"
    bl_idname = 'color.t2i_leaves'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Moss(bpy.types.Operator):
    """T2I Moss"""
    bl_label = "Moss"
    bl_idname = 'color.t2i_moss'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Plant_Other(bpy.types.Operator):
    """T2I Plant Other"""
    bl_label = "Plant Other"
    bl_idname = 'color.t2i_plant_other'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Straw(bpy.types.Operator):
    """T2I Straw"""
    bl_label = "Straw"
    bl_idname = 'color.t2i_straw'

    def execute(self, context):
        set_base_color(0x4031C0, self.bl_label)
        return {'FINISHED'}


class T2I_Tree(bpy.types.Operator):
    """T2I Tree"""
    bl_label = "Tree"
    bl_idname = 'color.t2i_tree'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Clouds(bpy.types.Operator):
    """T2I Clouds"""
    bl_label = "Clouds"
    bl_idname = 'color.t2i_clouds'

    def execute(self, context):
        set_base_color(0xA02020, self.bl_label)
        return {'FINISHED'}


class T2I_Sky_Other(bpy.types.Operator):
    """T2I Sky Other"""
    bl_label = "Sky Other"
    bl_idname = 'color.t2i_sky_other'

    def execute(self, context):
        set_base_color(0x40AA40, self.bl_label)
        return {'FINISHED'}


class T2I_Hill(bpy.types.Operator):
    """T2I Hill"""
    bl_label = "Hill"
    bl_idname = 'color.t2i_hill'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Mountain(bpy.types.Operator):
    """T2I Mountain"""
    bl_label = "Mountain"
    bl_idname = 'color.t2i_mountain'

    def execute(self, context):
        set_base_color(0xC04040, self.bl_label)
        return {'FINISHED'}


class T2I_Rock(bpy.types.Operator):
    """T2I Rock"""
    bl_label = "Rock"
    bl_idname = 'color.t2i_rock'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Solid_Other(bpy.types.Operator):
    """T2I Solid Other"""
    bl_label = "Solid Other"
    bl_idname = 'color.t2i_solid_other'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Stone(bpy.types.Operator):
    """T2I Stone"""
    bl_label = "Stone"
    bl_idname = 'color.t2i_stone'

    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        return {'FINISHED'}


class T2I_Wood(bpy.types.Operator):
    """T2I Wood"""
    bl_label = "Wood"
    bl_idname = 'color.t2i_wood'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Cage(bpy.types.Operator):
    """T2I Cage"""
    bl_label = "Cage"
    bl_idname = 'color.t2i_cage'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Fence(bpy.types.Operator):
    """T2I Fence"""
    bl_label = "Fence"
    bl_idname = 'color.t2i_fence'

    def execute(self, context):
        set_base_color(0x60DBE0, self.bl_label)
        return {'FINISHED'}


class T2I_Net(bpy.types.Operator):
    """T2I Net"""
    bl_label = "Net"
    bl_idname = 'color.t2i_net'

    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        return {'FINISHED'}


class T2I_Railing(bpy.types.Operator):
    """T2I Railing"""
    bl_label = "Railing"
    bl_idname = 'color.t2i_railing'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Structural_Other(bpy.types.Operator):
    """T2I Structural Other"""
    bl_label = "Structural Other"
    bl_idname = 'color.t2i_structural_other'

    def execute(self, context):
        set_base_color(0xC0C000, self.bl_label)
        return {'FINISHED'}


class T2I_Fog(bpy.types.Operator):
    """T2I Fog"""
    bl_label = "Fog"
    bl_idname = 'color.t2i_fog'

    def execute(self, context):
        set_base_color(0x60E0E0, self.bl_label)
        return {'FINISHED'}


class T2I_River(bpy.types.Operator):
    """T2I River"""
    bl_label = "River"
    bl_idname = 'color.t2i_river'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_Sea(bpy.types.Operator):
    """T2I Sea"""
    bl_label = "Sea"
    bl_idname = 'color.t2i_sea'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Water_Other(bpy.types.Operator):
    """T2I Water Other"""
    bl_label = "Water Other"
    bl_idname = 'color.t2i_water_other'

    def execute(self, context):
        set_base_color(0x402F40, self.bl_label)
        return {'FINISHED'}


class T2I_Waterdrops(bpy.types.Operator):
    """T2I Waterdrops"""
    bl_label = "Waterdrops"
    bl_idname = 'color.t2i_waterdrops'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Ceiling_Other(bpy.types.Operator):
    """T2I Ceiling Other"""
    bl_label = "Ceiling Other"
    bl_idname = 'color.t2i_ceiling_other'

    def execute(self, context):
        set_base_color(0xC0C340, self.bl_label)
        return {'FINISHED'}


class T2I_Ceiling_Tile(bpy.types.Operator):
    """T2I Ceiling Tile"""
    bl_label = "Ceiling Tile"
    bl_idname = 'color.t2i_ceiling_tile'

    def execute(self, context):
        set_base_color(0xC0C020, self.bl_label)
        return {'FINISHED'}


class T2I_Carpet(bpy.types.Operator):
    """T2I Carpet"""
    bl_label = "Carpet"
    bl_idname = 'color.t2i_carpet'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Floor_Marble(bpy.types.Operator):
    """T2I Floor Marble"""
    bl_label = "Floor Marble"
    bl_idname = 'color.t2i_floor_marble'

    def execute(self, context):
        set_base_color(0xE02020, self.bl_label)
        return {'FINISHED'}


class T2I_Floor_Other(bpy.types.Operator):
    """T2I Floor Other"""
    bl_label = "Floor Other"
    bl_idname = 'color.t2i_floor_other'

    def execute(self, context):
        set_base_color(0xA0A020, self.bl_label)
        return {'FINISHED'}


class T2I_Floor_Stone(bpy.types.Operator):
    """T2I Floor Stone"""
    bl_label = "Floor Stone"
    bl_idname = 'color.t2i_floor_stone'

    def execute(self, context):
        set_base_color(0x20A0A0, self.bl_label)
        return {'FINISHED'}


class T2I_Floor_Tile(bpy.types.Operator):
    """T2I Floor Tile"""
    bl_label = "Floor Tile"
    bl_idname = 'color.t2i_floor_tile'

    def execute(self, context):
        set_base_color(0x2068A0, self.bl_label)
        return {'FINISHED'}


class T2I_Floor_Wood(bpy.types.Operator):
    """T2I Floor Wood"""
    bl_label = "Floor Wood"
    bl_idname = 'color.t2i_floor_wood'

    def execute(self, context):
        set_base_color(0xA02020, self.bl_label)
        return {'FINISHED'}


class T2I_Food_Other(bpy.types.Operator):
    """T2I Food Other"""
    bl_label = "Food Other"
    bl_idname = 'color.t2i_food_other'

    def execute(self, context):
        set_base_color(0x6060E0, self.bl_label)
        return {'FINISHED'}


class T2I_Fruit(bpy.types.Operator):
    """T2I Fruit"""
    bl_label = "Fruit"
    bl_idname = 'color.t2i_fruit'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Salad(bpy.types.Operator):
    """T2I Salad"""
    bl_label = "Salad"
    bl_idname = 'color.t2i_salad'

    def execute(self, context):
        set_base_color(0x808080, self.bl_label)
        return {'FINISHED'}


class T2I_Vegetable(bpy.types.Operator):
    """T2I Vegetable"""
    bl_label = "Vegetable"
    bl_idname = 'color.t2i_vegetable'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Cabinet(bpy.types.Operator):
    """T2I Cabinet"""
    bl_label = "Cabinet"
    bl_idname = 'color.t2i_cabinet'

    def execute(self, context):
        set_base_color(0x804040, self.bl_label)
        return {'FINISHED'}


class T2I_Counter(bpy.types.Operator):
    """T2I Counter"""
    bl_label = "Counter"
    bl_idname = 'color.t2i_counter'

    def execute(self, context):
        set_base_color(0xA0A020, self.bl_label)
        return {'FINISHED'}


class T2I_Cupboard(bpy.types.Operator):
    """T2I Cupboard"""
    bl_label = "Cupboard"
    bl_idname = 'color.t2i_cupboard'

    def execute(self, context):
        set_base_color(0x20A0A0, self.bl_label)
        return {'FINISHED'}


class T2I_Desk_Stuff(bpy.types.Operator):
    """T2I Desk (Stuff)"""
    bl_label = "Desk (Stuff)"
    bl_idname = 'color.t2i_desk_stuff'

    def execute(self, context):
        set_base_color(0xE06060, self.bl_label)
        return {'FINISHED'}


class T2I_Door_Stuff(bpy.types.Operator):
    """T2I Door (Stuff)"""
    bl_label = "Door (Stuff)"
    bl_idname = 'color.t2i_door_stuff'

    def execute(self, context):
        set_base_color(0x60E03E, self.bl_label)
        return {'FINISHED'}


class T2I_Furniture_Other(bpy.types.Operator):
    """T2I Furniture Other"""
    bl_label = "Furniture Other"
    bl_idname = 'color.t2i_furniture_other'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Light(bpy.types.Operator):
    """T2I Light"""
    bl_label = "Light"
    bl_idname = 'color.t2i_light'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Mirror_Stuff(bpy.types.Operator):
    """T2I Mirror (Stuff)"""
    bl_label = "Mirror (Stuff)"
    bl_idname = 'color.t2i_mirror_stuff'

    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        return {'FINISHED'}


class T2I_Shelf(bpy.types.Operator):
    """T2I Shelf"""
    bl_label = "Shelf"
    bl_idname = 'color.t2i_shelf'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Stairs(bpy.types.Operator):
    """T2I Stairs"""
    bl_label = "Stairs"
    bl_idname = 'color.t2i_stairs'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Table(bpy.types.Operator):
    """T2I Table"""
    bl_label = "Table"
    bl_idname = 'color.t2i_table'

    def execute(self, context):
        set_base_color(0x000000, self.bl_label)
        return {'FINISHED'}


class T2I_Cardboard(bpy.types.Operator):
    """T2I Cardboard"""
    bl_label = "Cardboard"
    bl_idname = 'color.t2i_cardboard'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Metal(bpy.types.Operator):
    """T2I Metal"""
    bl_label = "Metal"
    bl_idname = 'color.t2i_metal'

    def execute(self, context):
        set_base_color(0x808040, self.bl_label)
        return {'FINISHED'}


class T2I_Paper(bpy.types.Operator):
    """T2I Paper"""
    bl_label = "Paper"
    bl_idname = 'color.t2i_paper'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Plastic(bpy.types.Operator):
    """T2I Plastic"""
    bl_label = "Plastic"
    bl_idname = 'color.t2i_plastic'

    def execute(self, context):
        set_base_color(0xC00000, self.bl_label)
        return {'FINISHED'}


class T2I_Banner(bpy.types.Operator):
    """T2I Banner"""
    bl_label = "Banner"
    bl_idname = 'color.t2i_banner'

    def execute(self, context):
        set_base_color(0x40C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Blanket(bpy.types.Operator):
    """T2I Blanket"""
    bl_label = "Blanket"
    bl_idname = 'color.t2i_blanket'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Cloth(bpy.types.Operator):
    """T2I Cloth"""
    bl_label = "Cloth"
    bl_idname = 'color.t2i_cloth'

    def execute(self, context):
        set_base_color(0x20A0A0, self.bl_label)
        return {'FINISHED'}


class T2I_Clothes(bpy.types.Operator):
    """T2I Clothes"""
    bl_label = "Clothes"
    bl_idname = 'color.t2i_clothes'

    def execute(self, context):
        set_base_color(0x2020A0, self.bl_label)
        return {'FINISHED'}


class T2I_Curtain(bpy.types.Operator):
    """T2I Curtain"""
    bl_label = "Curtain"
    bl_idname = 'color.t2i_curtain'

    def execute(self, context):
        set_base_color(0x6060E0, self.bl_label)
        return {'FINISHED'}


class T2I_Mat(bpy.types.Operator):
    """T2I Mat"""
    bl_label = "Mat"
    bl_idname = 'color.t2i_mat'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Napkin(bpy.types.Operator):
    """T2I Napkin"""
    bl_label = "Napkin"
    bl_idname = 'color.t2i_napkin'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Pillow(bpy.types.Operator):
    """T2I Pillow"""
    bl_label = "Pillow"
    bl_idname = 'color.t2i_pillow'

    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        return {'FINISHED'}


class T2I_Rug(bpy.types.Operator):
    """T2I Rug"""
    bl_label = "Rug"
    bl_idname = 'color.t2i_rug'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Textile_Other(bpy.types.Operator):
    """T2I Textile Other"""
    bl_label = "Textile Other"
    bl_idname = 'color.t2i_textile_other'

    def execute(self, context):
        set_base_color(0x800000, self.bl_label)
        return {'FINISHED'}


class T2I_Towel(bpy.types.Operator):
    """T2I Towel"""
    bl_label = "Towel"
    bl_idname = 'color.t2i_towel'

    def execute(self, context):
        set_base_color(0x000080, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Brick(bpy.types.Operator):
    """T2I Wall Brick"""
    bl_label = "Wall Brick"
    bl_idname = 'color.t2i_wall_brick'

    def execute(self, context):
        set_base_color(0x008080, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Concrete(bpy.types.Operator):
    """T2I Wall Concrete"""
    bl_label = "Wall Concrete"
    bl_idname = 'color.t2i_wall_concrete'

    def execute(self, context):
        set_base_color(0x808000, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Other(bpy.types.Operator):
    """T2I Wall Other"""
    bl_label = "Wall Other"
    bl_idname = 'color.t2i_wall_other'

    def execute(self, context):
        set_base_color(0x0000A7, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Panel(bpy.types.Operator):
    """T2I Wall Panel"""
    bl_label = "Wall Panel"
    bl_idname = 'color.t2i_wall_panel'

    def execute(self, context):
        set_base_color(0x80FF80, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Stone(bpy.types.Operator):
    """T2I Wall Stone"""
    bl_label = "Wall Stone"
    bl_idname = 'color.t2i_wall_stone'

    def execute(self, context):
        set_base_color(0x804040, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Tile(bpy.types.Operator):
    """T2I Wall Tile"""
    bl_label = "Wall Tile"
    bl_idname = 'color.t2i_wall_tile'

    def execute(self, context):
        set_base_color(0x4040C0, self.bl_label)
        return {'FINISHED'}


class T2I_Wall_Wood(bpy.types.Operator):
    """T2I Wall Wood"""
    bl_label = "Wall Wood"
    bl_idname = 'color.t2i_wall_wood'

    def execute(self, context):
        set_base_color(0xC0C0C0, self.bl_label)
        return {'FINISHED'}


class T2I_Window_Blind(bpy.types.Operator):
    """T2I Window Blind"""
    bl_label = "Window Blind"
    bl_idname = 'color.t2i_window_blind'

    def execute(self, context):
        set_base_color(0xC0C040, self.bl_label)
        return {'FINISHED'}


class T2I_Window_Other(bpy.types.Operator):
    """T2I Window Other"""
    bl_label = "Window Other"
    bl_idname = 'color.t2i_window_other'

    def execute(self, context):
        set_base_color(0x404040, self.bl_label)
        return {'FINISHED'}


# T2I PANEL
class T2IPanel(bpy.types.Panel):
    bl_idname = "T2I_PT_Panel"
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
        scol.label(text="", icon_value=g.c_icons["t2i_undefined"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_person"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_backpack"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_eye_glasses"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_handbag"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_shoe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_suitcase"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tie"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_umbrella"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bird"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_dog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_elephant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_giraffe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_horse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sheep"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_zebra"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bench"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fire_hydrant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_parking_meter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_stop_sign"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_street_sign"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_traffic_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_baseball_bat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_baseball_glove"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_frisbee"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_kite"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_skateboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_skis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_snowboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sports_ball"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_surfboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tennis_racket"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_airplane"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bicycle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_boat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_car"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_motorcycle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_train"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_truck"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_blender"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_microwave"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_oven"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_refrigerator"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_toaster"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cell_phone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_keyboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_laptop"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mouse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_remote"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tv"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_apple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_banana"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_broccoli"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cake"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_carrot"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_donut"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hot_dog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_pizza"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sandwich"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bed"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_chair"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_couch"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_desk"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_dining_table"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_door"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mirror"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_potted_plant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_toilet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_window"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_book"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_clock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hair_brush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hair_drier"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_scissors"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_teddy_bear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_toothbrush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_vase"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bottle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bowl"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cup"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fork"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_knife"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_plate"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_spoon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wine_glass"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bridge"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_building_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_house"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_roof"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_skyscraper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tent"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_dirt"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_gravel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_ground_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mud"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_pavement"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_platform"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_playing_field"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_railroad"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_road"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sand"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_snow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_branch"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_flower"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_grass"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_leaves"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_moss"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_plant_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_straw"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tree"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_clouds"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sky_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hill"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mountain"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_rock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_solid_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wood"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cage"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fence"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_net"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_railing"].icon_id)
        scol.label(
            text="", icon_value=g.c_icons["t2i_structural_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_river"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sea"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_water_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_waterdrops"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_ceiling_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_ceiling_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_carpet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_marble"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_wood"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_food_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fruit"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_salad"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_vegetable"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cabinet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_counter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cupboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_desk_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_door_stuff"].icon_id)
        scol.label(
            text="", icon_value=g.c_icons["t2i_furniture_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mirror_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_shelf"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_stairs"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_table"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cardboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_metal"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_paper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_plastic"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_banner"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_blanket"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cloth"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_clothes"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_curtain"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_napkin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_pillow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_rug"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_textile_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_towel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_brick"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_concrete"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_panel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_wood"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_window_blind"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_window_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_undefined", text="Undefined")
        scol.operator("color.t2i_person", text="Person")
        scol.operator("color.t2i_backpack", text="Backpack")
        scol.operator("color.t2i_eye_glasses", text="Eye Glasses")
        scol.operator("color.t2i_handbag", text="Handbag")
        scol.operator("color.t2i_hat", text="Hat")
        scol.operator("color.t2i_shoe", text="Shoe")
        scol.operator("color.t2i_suitcase", text="Suitcase")
        scol.operator("color.t2i_tie", text="Tie")
        scol.operator("color.t2i_umbrella", text="Umbrella")
        scol.operator("color.t2i_bear", text="Bear")
        scol.operator("color.t2i_bird", text="Bird")
        scol.operator("color.t2i_cat", text="Cat")
        scol.operator("color.t2i_cow", text="Cow")
        scol.operator("color.t2i_dog", text="Dog")
        scol.operator("color.t2i_elephant", text="Elephant")
        scol.operator("color.t2i_giraffe", text="Giraffe")
        scol.operator("color.t2i_horse", text="Horse")
        scol.operator("color.t2i_sheep", text="Sheep")
        scol.operator("color.t2i_zebra", text="Zebra")
        scol.operator("color.t2i_bench", text="Bench")
        scol.operator("color.t2i_fire_hydrant", text="Fire Hydrant")
        scol.operator("color.t2i_parking_meter", text="Parking Meter")
        scol.operator("color.t2i_stop_sign", text="Stop Sign")
        scol.operator("color.t2i_street_sign", text="Street Sign")
        scol.operator("color.t2i_traffic_light", text="Traffic Light")
        scol.operator("color.t2i_baseball_bat", text="Baseball Bat")
        scol.operator("color.t2i_baseball_glove", text="Baseball Glove")
        scol.operator("color.t2i_frisbee", text="Frisbee")
        scol.operator("color.t2i_kite", text="Kite")
        scol.operator("color.t2i_skateboard", text="Skateboard")
        scol.operator("color.t2i_skis", text="Skis")
        scol.operator("color.t2i_snowboard", text="Snowboard")
        scol.operator("color.t2i_sports_ball", text="Sports Ball")
        scol.operator("color.t2i_surfboard", text="Surfboard")
        scol.operator("color.t2i_tennis_racket", text="Tennis Racket")
        scol.operator("color.t2i_airplane", text="Airplane")
        scol.operator("color.t2i_bicycle", text="Bicycle")
        scol.operator("color.t2i_boat", text="Boat")
        scol.operator("color.t2i_bus", text="Bus")
        scol.operator("color.t2i_car", text="Car")
        scol.operator("color.t2i_motorcycle", text="Motorcycle")
        scol.operator("color.t2i_train", text="Train")
        scol.operator("color.t2i_truck", text="Truck")
        scol.operator("color.t2i_blender", text="Blender")
        scol.operator("color.t2i_microwave", text="Microwave")
        scol.operator("color.t2i_oven", text="Oven")
        scol.operator("color.t2i_refrigerator", text="Refrigerator")
        scol.operator("color.t2i_sink", text="Sink")
        scol.operator("color.t2i_toaster", text="Toaster")
        scol.operator("color.t2i_cell_phone", text="Cell Phone")
        scol.operator("color.t2i_keyboard", text="Keyboard")
        scol.operator("color.t2i_laptop", text="Laptop")
        scol.operator("color.t2i_mouse", text="Mouse")
        scol.operator("color.t2i_remote", text="Remote")
        scol.operator("color.t2i_tv", text="TV")
        scol.operator("color.t2i_apple", text="Apple")
        scol.operator("color.t2i_banana", text="Banana")
        scol.operator("color.t2i_broccoli", text="Broccoli")
        scol.operator("color.t2i_cake", text="Cake")
        scol.operator("color.t2i_carrot", text="Carrot")
        scol.operator("color.t2i_donut", text="Donut")
        scol.operator("color.t2i_hot_dog", text="Hot Dog")
        scol.operator("color.t2i_orange", text="Orange")
        scol.operator("color.t2i_pizza", text="Pizza")
        scol.operator("color.t2i_sandwich", text="Sandwich")
        scol.operator("color.t2i_bed", text="Bed")
        scol.operator("color.t2i_chair", text="Chair")
        scol.operator("color.t2i_couch", text="Couch")
        scol.operator("color.t2i_desk", text="Desk")
        scol.operator("color.t2i_dining_table", text="Dining Table")
        scol.operator("color.t2i_door", text="Door")
        scol.operator("color.t2i_mirror", text="Mirror")
        scol.operator("color.t2i_potted_plant", text="Potted Plant")
        scol.operator("color.t2i_toilet", text="Toilet")
        scol.operator("color.t2i_window", text="Window")
        scol.operator("color.t2i_book", text="Book")
        scol.operator("color.t2i_clock", text="Clock")
        scol.operator("color.t2i_hair_brush", text="Hair Brush")
        scol.operator("color.t2i_hair_drier", text="Hair Drier")
        scol.operator("color.t2i_scissors", text="Scissors")
        scol.operator("color.t2i_teddy_bear", text="Teddy Bear")
        scol.operator("color.t2i_toothbrush", text="Toothbrush")
        scol.operator("color.t2i_vase", text="Vase")
        scol.operator("color.t2i_bottle", text="Bottle")
        scol.operator("color.t2i_bowl", text="Bowl")
        scol.operator("color.t2i_cup", text="Cup")
        scol.operator("color.t2i_fork", text="Fork")
        scol.operator("color.t2i_knife", text="Knife")
        scol.operator("color.t2i_plate", text="Plate")
        scol.operator("color.t2i_spoon", text="Spoon")
        scol.operator("color.t2i_wine_glass", text="Wine Glass")
        scol.operator("color.t2i_bridge", text="Bridge")
        scol.operator("color.t2i_building_other", text="Building Other")
        scol.operator("color.t2i_house", text="House")
        scol.operator("color.t2i_roof", text="Roof")
        scol.operator("color.t2i_skyscraper", text="Skyscraper")
        scol.operator("color.t2i_tent", text="Tent")
        scol.operator("color.t2i_dirt", text="Dirt")
        scol.operator("color.t2i_gravel", text="Gravel")
        scol.operator("color.t2i_ground_other", text="Ground Other")
        scol.operator("color.t2i_mud", text="Mud")
        scol.operator("color.t2i_pavement", text="Pavement")
        scol.operator("color.t2i_platform", text="Platform")
        scol.operator("color.t2i_playing_field", text="Playing Field")
        scol.operator("color.t2i_railroad", text="Railroad")
        scol.operator("color.t2i_road", text="Road")
        scol.operator("color.t2i_sand", text="Sand")
        scol.operator("color.t2i_snow", text="Snow")
        scol.operator("color.t2i_branch", text="Branch")
        scol.operator("color.t2i_bush", text="Bush")
        scol.operator("color.t2i_flower", text="Flower")
        scol.operator("color.t2i_grass", text="Grass")
        scol.operator("color.t2i_leaves", text="Leaves")
        scol.operator("color.t2i_moss", text="Moss")
        scol.operator("color.t2i_plant_other", text="Plant Other")
        scol.operator("color.t2i_straw", text="Straw")
        scol.operator("color.t2i_tree", text="Tree")
        scol.operator("color.t2i_clouds", text="Clouds")
        scol.operator("color.t2i_sky_other", text="Sky Other")
        scol.operator("color.t2i_hill", text="Hill")
        scol.operator("color.t2i_mountain", text="Mountain")
        scol.operator("color.t2i_rock", text="Rock")
        scol.operator("color.t2i_solid_other", text="Solid Other")
        scol.operator("color.t2i_stone", text="Stone")
        scol.operator("color.t2i_wood", text="Wood")
        scol.operator("color.t2i_cage", text="Cage")
        scol.operator("color.t2i_fence", text="Fence")
        scol.operator("color.t2i_net", text="Net")
        scol.operator("color.t2i_railing", text="Railing")
        scol.operator("color.t2i_structural_other", text="Structural Other")
        scol.operator("color.t2i_fog", text="Fog")
        scol.operator("color.t2i_river", text="River")
        scol.operator("color.t2i_sea", text="Sea")
        scol.operator("color.t2i_water_other", text="Water Other")
        scol.operator("color.t2i_waterdrops", text="Waterdrops")
        scol.operator("color.t2i_ceiling_other", text="Ceiling Other")
        scol.operator("color.t2i_ceiling_tile", text="Ceiling Tile")
        scol.operator("color.t2i_carpet", text="Carpet")
        scol.operator("color.t2i_floor_marble", text="Floor Marble")
        scol.operator("color.t2i_floor_other", text="Floor Other")
        scol.operator("color.t2i_floor_stone", text="Floor Stone")
        scol.operator("color.t2i_floor_tile", text="Floor Tile")
        scol.operator("color.t2i_floor_wood", text="Floor Wood")
        scol.operator("color.t2i_food_other", text="Food Other")
        scol.operator("color.t2i_fruit", text="Fruit")
        scol.operator("color.t2i_salad", text="Salad")
        scol.operator("color.t2i_vegetable", text="Vegetable")
        scol.operator("color.t2i_cabinet", text="Cabinet")
        scol.operator("color.t2i_counter", text="Counter")
        scol.operator("color.t2i_cupboard", text="Cupboard")
        scol.operator("color.t2i_desk_stuff", text="Desk (Stuff)")
        scol.operator("color.t2i_door_stuff", text="Door (Stuff)")
        scol.operator("color.t2i_furniture_other", text="Furniture Other")
        scol.operator("color.t2i_light", text="Light")
        scol.operator("color.t2i_mirror_stuff", text="Mirror (Stuff)")
        scol.operator("color.t2i_shelf", text="Shelf")
        scol.operator("color.t2i_stairs", text="Stairs")
        scol.operator("color.t2i_table", text="Table")
        scol.operator("color.t2i_cardboard", text="Cardboard")
        scol.operator("color.t2i_metal", text="Metal")
        scol.operator("color.t2i_paper", text="Paper")
        scol.operator("color.t2i_plastic", text="Plastic")
        scol.operator("color.t2i_banner", text="Banner")
        scol.operator("color.t2i_blanket", text="Blanket")
        scol.operator("color.t2i_cloth", text="Cloth")
        scol.operator("color.t2i_clothes", text="Clothes")
        scol.operator("color.t2i_curtain", text="Curtain")
        scol.operator("color.t2i_mat", text="Mat")
        scol.operator("color.t2i_napkin", text="Napkin")
        scol.operator("color.t2i_pillow", text="Pillow")
        scol.operator("color.t2i_rug", text="Rug")
        scol.operator("color.t2i_textile_other", text="Textile Other")
        scol.operator("color.t2i_towel", text="Towel")
        scol.operator("color.t2i_wall_brick", text="Wall Brick")
        scol.operator("color.t2i_wall_concrete", text="Wall Concrete")
        scol.operator("color.t2i_wall_other", text="Wall Other")
        scol.operator("color.t2i_wall_panel", text="Wall Panel")
        scol.operator("color.t2i_wall_stone", text="Wall Stone")
        scol.operator("color.t2i_wall_tile", text="Wall Tile")
        scol.operator("color.t2i_wall_wood", text="Wall Wood")
        scol.operator("color.t2i_window_blind", text="Window Blind")
        scol.operator("color.t2i_window_other", text="Window Other")

# T2I THINGS OUTDOOR PANEL


class T2IThingsOutPanel(bpy.types.Panel):
    bl_idname = "T2I_THINGS_OUT_PT_Panel"
    bl_label = "    Things Outdoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# T2I THINGS INDOOR PANEL
class T2IThingsInPanel(bpy.types.Panel):
    bl_idname = "T2I_THINGS_IN_PT_Panel"
    bl_label = "    Things Indoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# T2I STUFF OUTDOOR PANEL
class T2IStuffOutPanel(bpy.types.Panel):
    bl_idname = "T2I_STUFF_OUT_PT_Panel"
    bl_label = "    Stuff Outdoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout


# T2I STUFF INDOOR PANEL
class T2IStuffInPanel(bpy.types.Panel):
    bl_idname = "T2I_STUFF_IN_PT_Panel"
    bl_label = "    Stuff Indoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

# T2I THINGS OUTDOOR ACCESSORY PANEL


class T2ITOAccessoryPanel(bpy.types.Panel):
    bl_idname = "T2I_ACCESSORY_PT_PANEL"
    bl_label = "        Accessory"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_backpack"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_eye_glasses"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_handbag"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_shoe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_suitcase"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tie"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_umbrella"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_backpack", text="Backpack")
        scol.operator("color.t2i_eye_glasses", text="Eye Glasses")
        scol.operator("color.t2i_handbag", text="Handbag")
        scol.operator("color.t2i_hat", text="Hat")
        scol.operator("color.t2i_shoe", text="Shoe")
        scol.operator("color.t2i_suitcase", text="Suitcase")
        scol.operator("color.t2i_tie", text="Tie")
        scol.operator("color.t2i_umbrella", text="Umbrella")


# T2I THINGS OUTDOOR ANIMAL PANEL
class T2ITOAnimalPanel(bpy.types.Panel):
    bl_idname = "T2I_ANIMAL_PT_PANEL"
    bl_label = "        Animal"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_bear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bird"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_dog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_elephant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_giraffe"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_horse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sheep"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_zebra"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_bear", text="Bear")
        scol.operator("color.t2i_bird", text="Bird")
        scol.operator("color.t2i_cat", text="Cat")
        scol.operator("color.t2i_cow", text="Cow")
        scol.operator("color.t2i_dog", text="Dog")
        scol.operator("color.t2i_elephant", text="Elephant")
        scol.operator("color.t2i_giraffe", text="Giraffe")
        scol.operator("color.t2i_horse", text="Horse")
        scol.operator("color.t2i_sheep", text="Sheep")
        scol.operator("color.t2i_zebra", text="Zebra")


# T2I THINGS OUTDOOR OUTDOOR PANEL
class T2ITOOutdoorPanel(bpy.types.Panel):
    bl_idname = "T2I_OUTDOOR_PT_PANEL"
    bl_label = "        Outdoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_bench"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fire_hydrant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_parking_meter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_stop_sign"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_street_sign"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_traffic_light"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_bench", text="Bench")
        scol.operator("color.t2i_fire_hydrant", text="Fire Hydrant")
        scol.operator("color.t2i_parking_meter", text="Parking Meter")
        scol.operator("color.t2i_stop_sign", text="Stop Sign")
        scol.operator("color.t2i_street_sign", text="Street Sign")
        scol.operator("color.t2i_traffic_light", text="Traffic Light")


# T2I THINGS OUTDOOR SPORTS PANEL
class T2ITOSportsPanel(bpy.types.Panel):
    bl_idname = "T2I_SPORTS_PT_PANEL"
    bl_label = "        Sports"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_baseball_bat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_baseball_glove"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_frisbee"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_kite"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_skateboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_skis"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_snowboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sports_ball"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_surfboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tennis_racket"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_baseball_bat", text="Baseball Bat")
        scol.operator("color.t2i_baseball_glove", text="Baseball Glove")
        scol.operator("color.t2i_frisbee", text="Frisbee")
        scol.operator("color.t2i_kite", text="Kite")
        scol.operator("color.t2i_skateboard", text="Skateboard")
        scol.operator("color.t2i_skis", text="Skis")
        scol.operator("color.t2i_snowboard", text="Snowboard")
        scol.operator("color.t2i_sports_ball", text="Sports Ball")
        scol.operator("color.t2i_surfboard", text="Surfboard")
        scol.operator("color.t2i_tennis_racket", text="Tennis Racket")


# T2I THINGS OUTDOOR VEHICLE PANEL
class T2ITOVehiclePanel(bpy.types.Panel):
    bl_idname = "T2I_VEHICLE_PT_PANEL"
    bl_label = "        Vehicle"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_airplane"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bicycle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_boat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bus"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_car"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_motorcycle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_train"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_truck"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_airplane", text="Airplane")
        scol.operator("color.t2i_bicycle", text="Bicycle")
        scol.operator("color.t2i_boat", text="Boat")
        scol.operator("color.t2i_bus", text="Bus")
        scol.operator("color.t2i_car", text="Car")
        scol.operator("color.t2i_motorcycle", text="Motorcycle")
        scol.operator("color.t2i_train", text="Train")
        scol.operator("color.t2i_truck", text="Truck")


# Indoor
# T2I THINGS INDOOR APPLIANCE PANEL
class T2ITIAppliancePanel(bpy.types.Panel):
    bl_idname = "T2I_APPLIANCE_PT_PANEL"
    bl_label = "        Appliance"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_blender"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_microwave"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_oven"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_refrigerator"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sink"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_toaster"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_blender", text="Blender")
        scol.operator("color.t2i_microwave", text="Microwave")
        scol.operator("color.t2i_oven", text="Oven")
        scol.operator("color.t2i_refrigerator", text="Refrigerator")
        scol.operator("color.t2i_sink", text="Sink")
        scol.operator("color.t2i_toaster", text="Toaster")


# T2I THINGS INDOOR ELECTRONIC PANEL
class T2ITIElectronicPanel(bpy.types.Panel):
    bl_idname = "T2I_ELECTRONIC_PT_PANEL"
    bl_label = "        Electronic"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_cell_phone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_keyboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_laptop"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mouse"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_remote"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tv"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_cell_phone", text="Cell Phone")
        scol.operator("color.t2i_keyboard", text="Keyboard")
        scol.operator("color.t2i_laptop", text="Laptop")
        scol.operator("color.t2i_mouse", text="Mouse")
        scol.operator("color.t2i_remote", text="Remote")
        scol.operator("color.t2i_tv", text="TV")


# T2I THINGS INDOOR FOOD PANEL
class T2ITIFoodPanel(bpy.types.Panel):
    bl_idname = "T2I_FOOD_PT_PANEL"
    bl_label = "        Food"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_apple"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_banana"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_broccoli"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cake"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_carrot"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_donut"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hot_dog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_orange"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_pizza"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sandwich"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_apple", text="Apple")
        scol.operator("color.t2i_banana", text="Banana")
        scol.operator("color.t2i_broccoli", text="Broccoli")
        scol.operator("color.t2i_cake", text="Cake")
        scol.operator("color.t2i_carrot", text="Carrot")
        scol.operator("color.t2i_donut", text="Donut")
        scol.operator("color.t2i_hot_dog", text="Hot Dog")
        scol.operator("color.t2i_orange", text="Orange")
        scol.operator("color.t2i_pizza", text="Pizza")
        scol.operator("color.t2i_sandwich", text="Sandwich")


# T2I THINGS INDOOR FURNITURE PANEL
class T2ITIFurniturePanel(bpy.types.Panel):
    bl_idname = "T2I_FURNITURE_PT_PANEL"
    bl_label = "        Furniture"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_bed"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_chair"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_couch"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_desk"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_dining_table"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_door"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mirror"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_potted_plant"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_toilet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_window"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_bed", text="Bed")
        scol.operator("color.t2i_chair", text="Chair")
        scol.operator("color.t2i_couch", text="Couch")
        scol.operator("color.t2i_desk", text="Desk")
        scol.operator("color.t2i_dining_table", text="Dining Table")
        scol.operator("color.t2i_door", text="Door")
        scol.operator("color.t2i_mirror", text="Mirror")
        scol.operator("color.t2i_potted_plant", text="Potted Plant")
        scol.operator("color.t2i_toilet", text="Toilet")
        scol.operator("color.t2i_window", text="Window")


# T2I THINGS INDOOR INDOOR PANEL
class T2ITIIndoorPanel(bpy.types.Panel):
    bl_idname = "T2I_INDOOR_PT_PANEL"
    bl_label = "        Indoor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_book"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_clock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hair_brush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_hair_drier"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_scissors"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_teddy_bear"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_toothbrush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_vase"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_book", text="Book")
        scol.operator("color.t2i_clock", text="Clock")
        scol.operator("color.t2i_hair_brush", text="Hair Brush")
        scol.operator("color.t2i_hair_drier", text="Hair Drier")
        scol.operator("color.t2i_scissors", text="Scissors")
        scol.operator("color.t2i_teddy_bear", text="Teddy Bear")
        scol.operator("color.t2i_toothbrush", text="Toothbrush")
        scol.operator("color.t2i_vase", text="Vase")


# T2I THINGS INDOOR KITCHEN PANEL
class T2ITIKitchenPanel(bpy.types.Panel):
    bl_idname = "T2I_KITCHEN_PT_PANEL"
    bl_label = "        Kitchen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_THINGS_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_bottle"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bowl"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cup"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fork"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_knife"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_plate"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_spoon"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wine_glass"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_bottle", text="Bottle")
        scol.operator("color.t2i_bowl", text="Bowl")
        scol.operator("color.t2i_cup", text="Cup")
        scol.operator("color.t2i_fork", text="Fork")
        scol.operator("color.t2i_knife", text="Knife")
        scol.operator("color.t2i_plate", text="Plate")
        scol.operator("color.t2i_spoon", text="Spoon")
        scol.operator("color.t2i_wine_glass", text="Wine Glass")


# Stuff

# Outdoor
# T2I STUFF OUTDOOR BUILDING PANEL
class T2ISOBuildingPanel(bpy.types.Panel):
    bl_idname = "T2I_BUILDING_PT_PANEL"
    bl_label = "        Building"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_bridge"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_building_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_house"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_roof"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_skyscraper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tent"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_bridge", text="Bridge")
        scol.operator("color.t2i_building_other", text="Building Other")
        scol.operator("color.t2i_house", text="House")
        scol.operator("color.t2i_roof", text="Roof")
        scol.operator("color.t2i_skyscraper", text="Skyscraper")
        scol.operator("color.t2i_tent", text="Tent")


# T2I STUFF OUTDOOR GROUND PANEL
class T2ISOGroundPanel(bpy.types.Panel):
    bl_idname = "T2I_GROUND_PT_PANEL"
    bl_label = "        Ground"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_dirt"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_gravel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_ground_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mud"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_pavement"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_platform"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_playing_field"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_railroad"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_road"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sand"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_snow"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_dirt", text="Dirt")
        scol.operator("color.t2i_gravel", text="Gravel")
        scol.operator("color.t2i_ground_other", text="Ground Other")
        scol.operator("color.t2i_mud", text="Mud")
        scol.operator("color.t2i_pavement", text="Pavement")
        scol.operator("color.t2i_platform", text="Platform")
        scol.operator("color.t2i_playing_field", text="Playing Field")
        scol.operator("color.t2i_railroad", text="Railroad")
        scol.operator("color.t2i_road", text="Road")
        scol.operator("color.t2i_sand", text="Sand")
        scol.operator("color.t2i_snow", text="Snow")


# T2I STUFF OUTDOOR PLANT PANEL
class T2ISOPlantPanel(bpy.types.Panel):
    bl_idname = "T2I_PLANT_PT_PANEL"
    bl_label = "        Plant"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_branch"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_bush"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_flower"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_grass"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_leaves"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_moss"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_plant_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_straw"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_tree"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_branch", text="Branch")
        scol.operator("color.t2i_bush", text="Bush")
        scol.operator("color.t2i_flower", text="Flower")
        scol.operator("color.t2i_grass", text="Grass")
        scol.operator("color.t2i_leaves", text="Leaves")
        scol.operator("color.t2i_moss", text="Moss")
        scol.operator("color.t2i_plant_other", text="Plant Other")
        scol.operator("color.t2i_straw", text="Straw")
        scol.operator("color.t2i_tree", text="Tree")


# T2I STUFF OUTDOOR SKY PANEL
class T2ISOSkyPanel(bpy.types.Panel):
    bl_idname = "T2I_SKY_PT_PANEL"
    bl_label = "        Sky"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_clouds"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sky_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_clouds", text="Clouds")
        scol.operator("color.t2i_sky_other", text="Sky Other")


# T2I STUFF OUTDOOR SOLID PANEL
class T2ISOSolidPanel(bpy.types.Panel):
    bl_idname = "T2I_SOLID_PT_PANEL"
    bl_label = "        Solid"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_hill"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mountain"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_rock"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_solid_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wood"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_hill", text="Hill")
        scol.operator("color.t2i_mountain", text="Mountain")
        scol.operator("color.t2i_rock", text="Rock")
        scol.operator("color.t2i_solid_other", text="Solid Other")
        scol.operator("color.t2i_stone", text="Stone")
        scol.operator("color.t2i_wood", text="Wood")


# T2I STUFF OUTDOOR STRUCTURAL PANEL
class T2ISOStructuralPanel(bpy.types.Panel):
    bl_idname = "T2I_STRUCTURAL_PT_PANEL"
    bl_label = "        Structural"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_cage"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fence"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_net"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_railing"].icon_id)
        scol.label(
            text="", icon_value=g.c_icons["t2i_structural_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_cage", text="Cage")
        scol.operator("color.t2i_fence", text="Fence")
        scol.operator("color.t2i_net", text="Net")
        scol.operator("color.t2i_railing", text="Railing")
        scol.operator("color.t2i_structural_other", text="Structural Other")


# T2I STUFF OUTDOOR WATER PANEL
class T2ISOWaterPanel(bpy.types.Panel):
    bl_idname = "T2I_WATER_PT_PANEL"
    bl_label = "        Water"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_OUT_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_fog"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_river"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_sea"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_water_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_waterdrops"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_fog", text="Fog")
        scol.operator("color.t2i_river", text="River")
        scol.operator("color.t2i_sea", text="Sea")
        scol.operator("color.t2i_water_other", text="Water Other")
        scol.operator("color.t2i_waterdrops", text="Waterdrops")


# Indoor
# T2I STUFF INDOOR CEILING PANEL
class T2ISICeilingPanel(bpy.types.Panel):
    bl_idname = "T2I_CEILING_PT_PANEL"
    bl_label = "        Ceiling"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_ceiling_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_ceiling_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_carpet"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_ceiling_other", text="Ceiling Other")
        scol.operator("color.t2i_ceiling_tile", text="Ceiling Tile")
        scol.operator("color.t2i_carpet", text="Carpet")


# T2I STUFF INDOOR FLOOR PANEL
class T2ISIFloorPanel(bpy.types.Panel):
    bl_idname = "T2I_FLOOR_PT_PANEL"
    bl_label = "        Floor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_floor_marble"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_floor_wood"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_floor_marble", text="Floor Marble")
        scol.operator("color.t2i_floor_other", text="Floor Other")
        scol.operator("color.t2i_floor_stone", text="Floor Stone")
        scol.operator("color.t2i_floor_tile", text="Floor Tile")
        scol.operator("color.t2i_floor_wood", text="Floor Wood")


# T2I STUFF INDOOR FOOD PANEL
class T2ISIFoodPanel(bpy.types.Panel):
    bl_idname = "T2I_FOOD_PT_PANEL"
    bl_label = "        Food"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_food_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_fruit"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_salad"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_vegetable"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_food_other", text="Food Other")
        scol.operator("color.t2i_fruit", text="Fruit")
        scol.operator("color.t2i_salad", text="Salad")
        scol.operator("color.t2i_vegetable", text="Vegetable")


# T2I STUFF INDOOR FURNITURE PANEL
class T2ISIFurniturePanel(bpy.types.Panel):
    bl_idname = "T2I_FURNITURE_PT_PANEL"
    bl_label = "        Furniture"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_cabinet"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_counter"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cupboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_desk_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_door_stuff"].icon_id)
        scol.label(
            text="", icon_value=g.c_icons["t2i_furniture_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_light"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mirror_stuff"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_shelf"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_stairs"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_table"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_cabinet", text="Cabinet")
        scol.operator("color.t2i_counter", text="Counter")
        scol.operator("color.t2i_cupboard", text="Cupboard")
        scol.operator("color.t2i_desk_stuff", text="Desk (Stuff)")
        scol.operator("color.t2i_door_stuff", text="Door (Stuff)")
        scol.operator("color.t2i_furniture_other", text="Furniture Other")
        scol.operator("color.t2i_light", text="Light")
        scol.operator("color.t2i_mirror_stuff", text="Mirror (Stuff)")
        scol.operator("color.t2i_shelf", text="Shelf")
        scol.operator("color.t2i_stairs", text="Stairs")
        scol.operator("color.t2i_table", text="Table")


# T2I STUFF INDOOR RAW MATERIAL PANEL
class T2ISIRawMaterialPanel(bpy.types.Panel):
    bl_idname = "T2I_RAW_MATERIAL_PT_PANEL"
    bl_label = "        Raw Material"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_cardboard"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_metal"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_paper"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_plastic"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_cardboard", text="Cardboard")
        scol.operator("color.t2i_metal", text="Metal")
        scol.operator("color.t2i_paper", text="Paper")
        scol.operator("color.t2i_plastic", text="Plastic")


# T2I STUFF INDOOR TEXTILE PANEL
class T2ISITextilePanel(bpy.types.Panel):
    bl_idname = "T2I_TEXTILE_PT_PANEL"
    bl_label = "        Textile"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_banner"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_blanket"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_cloth"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_clothes"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_curtain"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_mat"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_napkin"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_pillow"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_rug"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_textile_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_towel"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_banner", text="Banner")
        scol.operator("color.t2i_blanket", text="Blanket")
        scol.operator("color.t2i_cloth", text="Cloth")
        scol.operator("color.t2i_clothes", text="Clothes")
        scol.operator("color.t2i_curtain", text="Curtain")
        scol.operator("color.t2i_mat", text="Mat")
        scol.operator("color.t2i_napkin", text="Napkin")
        scol.operator("color.t2i_pillow", text="Pillow")
        scol.operator("color.t2i_rug", text="Rug")
        scol.operator("color.t2i_textile_other", text="Textile Other")
        scol.operator("color.t2i_towel", text="Towel")


# T2I STUFF INDOOR WALL PANEL
class T2ISIWallPanel(bpy.types.Panel):
    bl_idname = "T2I_WALL_PT_PANEL"
    bl_label = "        Wall"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout

        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_wall_brick"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_concrete"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_other"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_panel"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_stone"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_tile"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_wall_wood"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_wall_brick", text="Wall Brick")
        scol.operator("color.t2i_wall_concrete", text="Wall Concrete")
        scol.operator("color.t2i_wall_other", text="Wall Other")
        scol.operator("color.t2i_wall_panel", text="Wall Panel")
        scol.operator("color.t2i_wall_stone", text="Wall Stone")
        scol.operator("color.t2i_wall_tile", text="Wall Tile")
        scol.operator("color.t2i_wall_wood", text="Wall Wood")


# T2I STUFF INDOOR WINDOW PANEL
class T2ISIWindowPanel(bpy.types.Panel):
    bl_idname = "T2I_WINDOW_PT_PANEL"
    bl_label = "        Window"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    bl_parent_id = 'T2I_STUFF_IN_PT_Panel'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        g.c_icons
        layout = self.layout
        srow = layout.row()
        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.label(text="", icon_value=g.c_icons["t2i_window_blind"].icon_id)
        scol.label(text="", icon_value=g.c_icons["t2i_window_other"].icon_id)

        scol = srow.column(align=True)
        scol.scale_y = 1.25
        scol.scale_x = 3.0
        scol.operator("color.t2i_window_blind", text="Window Blind")
        scol.operator("color.t2i_window_other", text="Window Other")


# T2I CLASSES
array_t2i = [
    T2IPanel,
    T2IThingsOutPanel,
    T2IThingsInPanel,
    T2ITOAccessoryPanel,
    T2ITOAnimalPanel,
    T2ITOOutdoorPanel,
    T2ITOSportsPanel,
    T2ITOVehiclePanel,
    T2ITIAppliancePanel,
    T2ITIElectronicPanel,
    T2ITIFoodPanel,
    T2ITIFurniturePanel,
    T2ITIIndoorPanel,
    T2ITIKitchenPanel,
    T2ISOBuildingPanel,
    T2ISOGroundPanel,
    T2ISOPlantPanel,
    T2ISOSkyPanel,
    T2ISOSolidPanel,
    T2ISOStructuralPanel,
    T2ISOWaterPanel,
    T2ISICeilingPanel,
    T2ISIFloorPanel,
    T2ISIFoodPanel,
    T2ISIFurniturePanel,
    T2ISIRawMaterialPanel,
    T2ISITextilePanel,
    T2ISIWallPanel,
    T2ISIWindowPanel,
    T2I_Undefined,
    T2I_Person,
    T2I_Backpack,
    T2I_Eye_Glasses,
    T2I_Handbag,
    T2I_Hat,
    T2I_Shoe,
    T2I_Suitcase,
    T2I_Tie,
    T2I_Umbrella,
    T2I_Bear,
    T2I_Bird,
    T2I_Cat,
    T2I_Cow,
    T2I_Dog,
    T2I_Elephant,
    T2I_Giraffe,
    T2I_Horse,
    T2I_Sheep,
    T2I_Zebra,
    T2I_Bench,
    T2I_Fire_Hydrant,
    T2I_Parking_Meter,
    T2I_Stop_Sign,
    T2I_Street_Sign,
    T2I_Traffic_Light,
    T2I_Baseball_Bat,
    T2I_Baseball_Glove,
    T2I_Frisbee,
    T2I_Kite,
    T2I_Skateboard,
    T2I_Skis,
    T2I_Snowboard,
    T2I_Sports_Ball,
    T2I_Surfboard,
    T2I_Tennis_Racket,
    T2I_Airplane,
    T2I_Bicycle,
    T2I_Boat,
    T2I_Bus,
    T2I_Car,
    T2I_Motorcycle,
    T2I_Train,
    T2I_Truck,
    T2I_Blender,
    T2I_Microwave,
    T2I_Oven,
    T2I_Refrigerator,
    T2I_Sink,
    T2I_Toaster,
    T2I_Cell_Phone,
    T2I_Keyboard,
    T2I_Laptop,
    T2I_Mouse,
    T2I_Remote,
    T2I_TV,
    T2I_Apple,
    T2I_Banana,
    T2I_Broccoli,
    T2I_Cake,
    T2I_Carrot,
    T2I_Donut,
    T2I_Hot_Dog,
    T2I_Orange,
    T2I_Pizza,
    T2I_Sandwich,
    T2I_Bed,
    T2I_Chair,
    T2I_Couch,
    T2I_Desk,
    T2I_Dining_Table,
    T2I_Door,
    T2I_Mirror,
    T2I_Potted_Plant,
    T2I_Toilet,
    T2I_Window,
    T2I_Book,
    T2I_Clock,
    T2I_Hair_Brush,
    T2I_Hair_Drier,
    T2I_Scissors,
    T2I_Teddy_Bear,
    T2I_Toothbrush,
    T2I_Vase,
    T2I_Bottle,
    T2I_Bowl,
    T2I_Cup,
    T2I_Fork,
    T2I_Knife,
    T2I_Plate,
    T2I_Spoon,
    T2I_Wine_Glass,
    T2I_Bridge,
    T2I_Building_Other,
    T2I_House,
    T2I_Roof,
    T2I_Skyscraper,
    T2I_Tent,
    T2I_Dirt,
    T2I_Gravel,
    T2I_Ground_Other,
    T2I_Mud,
    T2I_Pavement,
    T2I_Platform,
    T2I_Playing_Field,
    T2I_Railroad,
    T2I_Road,
    T2I_Sand,
    T2I_Snow,
    T2I_Branch,
    T2I_Bush,
    T2I_Flower,
    T2I_Grass,
    T2I_Leaves,
    T2I_Moss,
    T2I_Plant_Other,
    T2I_Straw,
    T2I_Tree,
    T2I_Clouds,
    T2I_Sky_Other,
    T2I_Hill,
    T2I_Mountain,
    T2I_Rock,
    T2I_Solid_Other,
    T2I_Stone,
    T2I_Wood,
    T2I_Cage,
    T2I_Fence,
    T2I_Net,
    T2I_Railing,
    T2I_Structural_Other,
    T2I_Fog,
    T2I_River,
    T2I_Sea,
    T2I_Water_Other,
    T2I_Waterdrops,
    T2I_Ceiling_Other,
    T2I_Ceiling_Tile,
    T2I_Carpet,
    T2I_Floor_Marble,
    T2I_Floor_Other,
    T2I_Floor_Stone,
    T2I_Floor_Tile,
    T2I_Floor_Wood,
    T2I_Food_Other,
    T2I_Fruit,
    T2I_Salad,
    T2I_Vegetable,
    T2I_Cabinet,
    T2I_Counter,
    T2I_Cupboard,
    T2I_Desk_Stuff,
    T2I_Door_Stuff,
    T2I_Furniture_Other,
    T2I_Light,
    T2I_Mirror_Stuff,
    T2I_Shelf,
    T2I_Stairs,
    T2I_Table,
    T2I_Cardboard,
    T2I_Metal,
    T2I_Paper,
    T2I_Plastic,
    T2I_Banner,
    T2I_Blanket,
    T2I_Cloth,
    T2I_Clothes,
    T2I_Curtain,
    T2I_Mat,
    T2I_Napkin,
    T2I_Pillow,
    T2I_Rug,
    T2I_Textile_Other,
    T2I_Towel,
    T2I_Wall_Brick,
    T2I_Wall_Concrete,
    T2I_Wall_Other,
    T2I_Wall_Panel,
    T2I_Wall_Stone,
    T2I_Wall_Tile,
    T2I_Wall_Wood,
    T2I_Window_Blind,
    T2I_Window_Other,
]
