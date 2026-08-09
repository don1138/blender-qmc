class Globals:
    def __init__(self):
        # Created during register() so enabling the add-on always starts with
        # a fresh Blender preview collection.
        self.c_icons = None

g = Globals()
