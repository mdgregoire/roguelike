from map_objects.rectangle import Rectangle
from map_objects.tile import Tile


class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Set all tiles to be non-passable
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self):
        # Create 2 rooms for demonstration purposes
        room1 = Rectangle(20, 15, 10, 15)
        room2 = Rectangle(35, 15, 10, 15)

        self.create_room(room1)
        self.create_room(room2)

    def create_room(self, room):
        # Iterate through the tiles in a rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
