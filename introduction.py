"""
Introduction & Title Module

Description: Handles terminal ASCII title card rendering, prologue playback, and
             introductory game initialization screens.
"""

import os, time, textwrap
from audio import audio
from story import scroll_text, pause, clear, GOLD, RESET

def display_title():
    """Displays ASCII title card and plays title BGM."""
    clear()
    audio.play_bgm("title")
    if 'TERM' not in os.environ:
        os.environ['TERM'] = 'xterm'

    title = r"""

    ______________________________________________________________________
        ______ ____   __     ____   ______ _   __     ____   ___   ______
       / ____// __ \ / /    / __ \ / ____// | / /    / __ ) /   | /_  __/
      / / __ / / / // /    / / / // __/  /  |/ /    / __  |/ /| |  / /
     / / / // /_/ // /___ / /_/ // /___ / /|  /    / /_/ // ___ | / /
     \____/ \____//_____//_____//_____//_/ |_/    /_____//_/  |_|/_/
    _____________________________________________________________________

    """

    print(GOLD + title + RESET)
    input(f"{GOLD}                           [ PRESS ENTER TO AWAKEN ]{RESET}")
    clear()

def intro_sequence(prologue):
    """Prompts player to read or skip prologue narrative beats."""
    while True:
        skip = input("\n\nWould you like to read the prologue? (y/n): ").lower()
        if skip == 'y':
            clear()
            for beat in prologue:
                wrapped = textwrap.fill(beat["text"], width = 70)
                scroll_text(wrapped)
                time.sleep(beat["pause"])
                if beat["clear"]:
                    clear()

            audio.play_sfx("laugh")
            scroll_text(f"{GOLD}GOLDEN BAT: 'ha-ha-ha-HA-HA-HAAA…!!!'{RESET}", delay=0.1)
            game_start_message()
            return False

        elif skip == 'n':
            game_start_message()
            return False

        else:
            print("\nInvalid input. Please try again and enter 'y' or 'n'.\n")
            pause(3.0)
            clear()

def game_start_message():
    """Displays opening objective header prior to entering world map loop."""
    clear()
    audio.stop()
    audio.play_sfx("scifi")
    scroll_text(f"\nWELCOME TO {GOLD}GOLDEN BAT{RESET}. EXPLORE THE RUINS OF ATLANTIS, FIND AND COLLECT 7 RELICS, "
                "AND DEFEAT THE MYSTERIOUS DR. NAZŌ...")
    pause(3.0)
    clear()
