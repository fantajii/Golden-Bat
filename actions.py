"""
Actions Handler Module

Description: Processes user inputs and handles game commands ('laugh', 'room',
             'path', 'search', 'go', 'get', 'quit'). Updates room status and state flags.
"""

import time
from audio import audio
from story import scroll_text, pause, clear, GOLD, RESET


def handle_actions(user_input, current_room, room_data, rooms, inventory, item_desc, room_desc, secret_path_open):
    """
    Evaluates player input and updates position, inventory, or environmental flags.

    Args:
        user_input (list): Tokenized input [action, target].
        current_room (str): Current active location key.
        room_data (dict): Dictionary representing current room connections/items.
        rooms (dict): Complete world map structure.
        inventory (list): Current items carried by the player.
        item_desc (dict): Descriptions for all inspectable items.
        room_desc (dict): Narrative descriptions for all locations.
        secret_path_open (bool): State flag tracking hidden passage unlock status.

    Returns:
        tuple: Updated (current_room, secret_path_open).
    """
    action = user_input[0].lower()
    target = user_input[1].title() if len(user_input) > 1 else ""

    # Character SFX command
    if action == 'laugh':
        scroll_text(f"\nManiacal laughter reverberates throughout the {current_room}."
        "..")
        audio.play_sfx("laugh")
        scroll_text(f"{GOLD}GOLDEN BAT: 'HA-HA-HA-HAAAA..!!!'{RESET}", delay = 0.1)
        pause()
        clear()

    # Room description command
    elif action == 'room':
        scroll_text(f"\n{room_desc.get(current_room)}")
        pause()
        clear()


    # Search environment command
    elif action == 'search':
        if 'item' in room_data:
            scroll_text(f"\nYou see the {room_data['item']} here.")
            pause()
            clear()
        elif current_room == 'Ancient Tomb' and secret_path_open == True:
            scroll_text('\nYou walk to the back of the tomb and see a small crack in the wall, leading north to '
                        'some secret room...')
            pause()
            clear()
        else:
            scroll_text(f"\nYou scour the {current_room}, and find nothing of use...")
            pause()
            clear()

    # Show exits command
    elif action == 'path':
        exits = [key for key in room_data if key not in ['item', 'villain']]
        scroll_text(f"\nVisible pathways: {', '.join(exits)}")
        pause()
        clear()

    # Movement command
    elif action == 'go':
        if target in room_data:
            current_room = room_data[target]
            scroll_text(f"\nYou move {target} to the {current_room}...")
            pause()
            audio.fade(500)
            clear()
        else:
            scroll_text("\nYou cannot go that way.")
            pause()
            clear()

    # Item collection command
    elif action == 'get':
        item_in_room = room_data.get('item', '')
        if item_in_room and target.lower() == item_in_room.lower():
            inventory.append(room_data.pop('item'))
            audio.play_sfx("item")
            scroll_text(f"\nYou picked up the {item_in_room}!")
            pause()
            scroll_text(f">> {item_desc.get(item_in_room)}")
            pause()

            # Unlock secret path puzzle condition
            if 'Kinesis Stone' in inventory and not secret_path_open:
                rooms['Ancient Tomb']['North'] = 'Echoing Gallery'
                secret_path_open = True
                scroll_text(f"(!) THE KINESIS STONE VIBRATES... (!)")
                pause()
            clear()
        elif target:
            scroll_text(f"\nYou reach for the {target}, but your hand only grasps thin air."
                        f"\nPerhaps it only exists in your mind...?")
            pause()
            clear()
        else:
            scroll_text("\nNo item name entered.")
            pause()
            clear()

    # Quit game command
    elif action == 'quit':
        audio.stop()
        audio.play_sfx("quit")
        scroll_text("\nEarth's fate remains uncertain...")
        time.sleep(5.0)
        return 'quit', secret_path_open

    # Idle input
    elif action == 'none':
        scroll_text("\nYou stand silently...")
        pause()
        clear()

    # Invalid command fallback
    else:
        scroll_text("\nInvalid action.")
        pause()
        clear()
    return current_room, secret_path_open