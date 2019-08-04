import tcod as libtcod


def render_all(console, entities, game_map, screen_width, screen_height, colors):
    # Draw all tiles on the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                libtcod.console_set_char_background(console, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(console, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)
    # Draw all entities on the list
    for entity in entities:
        draw_entity(console, entity)

    libtcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(console, entities):
    for entity in entities:
        clear_entity(console, entity)


def draw_entity(console, entity):
    libtcod.console_set_default_foreground(console, entity.color)
    libtcod.console_put_char(console, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(console, entity):
    # Erase the character that represents this object
    libtcod.console_put_char(console, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
