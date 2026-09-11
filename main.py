"""
Golden Bat - Main Entry Point

Author: Garrett Mandeville
Description: Initializes game state, imports system modules, and manages
             the primary gameplay input-evaluation loop.
"""

import pygame
from audio import audio
from story import get_story_text, scroll_text, pause, clear, GOLD, RESET
from rooms import get_rooms, get_room_description, get_item_description
from introduction import display_title, intro_sequence
from actions import handle_actions
from endings import check_endings

def get_user_input(current_room, inventory):
    """
    Displays the current player location and inventory state, then prompts for command input.

    Args:
        current_room (str): Name of the active room.
        inventory (list): List of items currently held by the player.

    Returns:
        list: Tokenized user command split into [action, target].
    """
    print(f"\nLocation: {current_room}\nInventory: {inventory}")
    user_input = input(
        "Action (laugh / room / path / search / go [direction] / get [item] / quit): "
    ).lower().split(maxsplit = 1)

    if not user_input:
        return ['none']
    return user_input

def main():
    """
    Main execution loop. Initializes game structures, handles prologue intro,
    and drives room music and player action processing.
    """
    # Game state initialization
    rooms = get_rooms()
    room_desc = get_room_description()
    item_desc = get_item_description()
    story = get_story_text()
    current_room = 'Ancient Tomb'
    inventory = []
    relics = ['Silver Baton', 'Red Cape', 'Swashbuckler Armor', 'Hydroflask', 'Kinesis Stone',
              'Spectral Reins', 'Icarus Data']
    secret_path_open = False

    # Launch sequence
    display_title()
    intro_sequence(story['prologue'])

    # Main gameplay loop
    while True:

        audio.get_room_music(current_room)

        room_data = rooms[current_room]

        # Check for endgame conditions
        if not check_endings(room_data, inventory, relics, story):
            break

        # Action handling
        user_input = get_user_input(current_room,inventory)
        current_room, secret_path_open, = handle_actions(
            user_input, current_room, room_data, rooms, inventory, item_desc, room_desc, secret_path_open
        )

        if current_room == 'quit':
            break

if __name__ == "__main__":
    main()
