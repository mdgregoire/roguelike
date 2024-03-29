
class Tile:
    """
    A Tile on a map, it may or may no be blocked and may or may not block sight
    """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        self.explored = False

        # By default if a tile is blocked it alos blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight
