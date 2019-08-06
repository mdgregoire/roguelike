import tcod as libtcod
from enum import Enum


class RenderOrder(Enum):
    CORPSE = 1
    ITEM = 2
    ACTOR = 3


def render_all(console, entities, player, game_map, fov_map, fov_recompute, screen_width, screen_height, colors):
    # Draw all tiles on the game map, using fov
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                if visible:
                    if wall:
                        libtcod.console_set_char_background(console, x, y, colors.get('light_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(console, x, y, colors.get('light_ground'), libtcod.BKGND_SET)
                    # Sets tiles the player has seen to explored
                    game_map.tiles[x][y].explored = True

                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(console, x, y, colors.get('dark_wall'), libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(console, x, y, colors.get('dark_ground'), libtcod.BKGND_SET)

    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)

    # Draw all entities on the list
    for entity in entities_in_render_order:
        draw_entity(console, entity, fov_map)

    # Health Bar
    libtcod.console_set_default_foreground(console, libtcod.white)
    libtcod.console_print_ex(console, 1, screen_height - 2, libtcod.BKGND_NONE, libtcod.LEFT,
                             'HP: {0:02}/{1:02}'.format(player.fighter.hp, player.fighter.max_hp))

    libtcod.console_blit(console, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(console, entities):
    for entity in entities:
        clear_entity(console, entity)


def draw_entity(console, entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
        libtcod.console_set_default_foreground(console, entity.color)
        libtcod.console_put_char(console, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(console, entity):
    # Erase the character that represents this object
    libtcod.console_put_char(console, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
