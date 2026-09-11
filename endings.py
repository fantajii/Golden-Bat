"""
Endgame Logic Module

Description: Evaluates win/lose conditions upon encountering boss rooms and renders
             the corresponding scripted endgame narrative sequences.
"""

import time, textwrap
from audio import audio
from story import scroll_text, clear, GOLD, RESET

def check_endings(room_data, inventory, relics, story):
    """
    Checks if a villain encounter condition is met, evaluates inventory achievements,
    and triggers cinematic credits sequences.

    Returns:
        bool: False if game ends; True if gameplay loop should continue.
    """
    if 'villain' in room_data:
        audio.stop()
        has_relics = all(item in inventory for item in relics)
        has_candy = 'Botan Rice Candy' in inventory

        # Route ending narrative branch
        if has_relics and has_candy:
            ending_beats = story['true_ending']
            audio.play_bgm("true_credits")
            ending_type = "THE TRUE ENDING!"
            final_msg = "You are a master of Atlantis."
        elif has_relics:
            ending_beats = story['win_ending']
            audio.play_bgm("win_credits")
            ending_type = "YOU WIN!"
            final_msg = "Earth is saved from the rogue planet Icarus."
        else:
            ending_beats = story['lose_ending']
            audio.play_bgm("lose_credits")
            ending_type = "GAME OVER!"
            final_msg = "Dr. Nazō has captured Golden Bat and Icarus impacts Earth."

        # Play narrative sequence
        clear()
        for beat in ending_beats:
            wrapped = textwrap.fill(beat["text"], width = 70)
            scroll_text(wrapped)
            time.sleep(beat["pause"])
            if beat["clear"]:
                clear()

        # Render final banner
        print("\n" + "*" * 30)
        scroll_text(ending_type, delay = 0.1, color = GOLD)
        scroll_text(final_msg, delay = 0.1)
        print("*" * 30)

        # Specific lose condition sfx
        if not has_relics:
            audio.stop()
            audio.play_sfx("icarus")

        audio.fade(10000)
        return False
    return True