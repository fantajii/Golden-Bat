"""
Story & Formatting Utilities Module

Description: Controls typewriter terminal scrolling text parser, embedded tag handling
             (colors, audio triggers, delays), terminal window clears, and story scripts.
"""

import sys, time, os
from audio import audio

# ANSI Terminal Colors
GOLD = '\033[33m'
RESET = '\033[0m'

def pause(seconds = 2.0):
    """Execution delay helper."""
    time.sleep(seconds)

def clear():
    """Cross-platform terminal screen clear."""
    os.system('cls' if os.name == 'nt' else 'clear')

def scroll_text(text, delay = 0.03, color = None):
    """
    Prints text character-by-character while parsing inline brackets tags.

    Supports:
        Audio tags: [marie1], [marie2], [marie3], [laugh]
        Speed tags: [slow], [fast], [norm]
        Color tags: [gold], [reset]
        Wait tags:  [wait:seconds]
    """
    if color:
        sys.stdout.write(color)

    i = 0
    current_delay = delay
    while i < len(text):
        char = text[i]

        if char == "[":
            end_tag = text.find("]", i)
            if end_tag != -1:
                tag = text[i + 1:end_tag]

                # Audio triggers
                if tag in ["marie1", "marie2", "marie3", "laugh"]:
                    audio.play_sfx(tag)
                # Speed triggers
                elif tag == "slow":
                    current_delay = 0.1
                elif tag == "fast":
                    current_delay = 0.01
                elif tag == "norm":
                    current_delay = 0.03
                # Color triggers
                elif tag == "gold":
                    sys.stdout.write(GOLD)
                elif tag == "reset":
                    sys.stdout.write(RESET)
                # Pause delays
                elif tag.startswith("wait"):
                    try:
                        seconds = float(tag.split(":")[1])
                        time.sleep(seconds)
                    except (ValueError, IndexError):
                        pass

                i = end_tag + 1
                continue

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(current_delay)
        i += 1

    sys.stdout.write(RESET)
    print("\n")

def get_story_text() -> dict:
    """Returns scripted beats for prologue and ending cinematics."""
    return {
        'prologue': [
            {
                "text": "DR. NAZŌ, A MYSTERIOUS MAD SCIENTIST, HAS SENT THE ROGUE PLANET ICARUS ON A "
                        "CRASH COURSE TOWARD EARTH.",
                "pause": 1.5, "clear": True},
            {
                "text": "CONTRACTED BY THE PEARL RESEARCH INSTITUTE, PROFESSOR MIRE, A RENOWNED FRENCH ARCHEOLOGIST, "
                        "JOINED BY MARIE MIRE,\nAND CREW ARE SEARCHING THE OCEAN BY SHIP FOR THE WHEREABOUTS OF "
                        "'THE LOST CONTINENT.'",
                "pause": 1.5, "clear": False},
            {
                "text": "THIS CONTINENT IS SAID TO CONTAIN A SPECIAL LENS, NECESSARY FOR THE INSTITUTE'S COMPLETION OF "
                        "THE SUPER DESTRUCTION BEAM CANNON TO DESTROY ICARUS.",
                "pause": 2.0, "clear": True},
            {
                "text": "[fast]WHILE ON THEIR EXPEDITION, DR. NAZŌ AND HIS MEN ATTACK THE CREW AND THEIR SHIP WITH THE "
                        "GIANT MECHANICAL ROBOT, FIVE FINGER.[norm]",
                "pause": 1.5, "clear": False},
            {
                "text": "SHIPWRECKED ON THE ISLAND RUINS OF ATLANTIS, ONLY MARIE MIRE SURVIVES WITH A BOOK CONTAINING "
                        "THE RESEARCH MATERIALS FROM HER FATHER.",
                "pause": 2.0, "clear": True},
            {
                "text": "AS THE RUINS ARE BEING OVERRUN BY THE EVIL SCIENTIST, MARIE FLEES AND DISCOVERS A HIDDEN "
                        "SECRET TUNNEL LEADING STRAIGHT INTO A DARK, ANCIENT TOMB…",
                "pause": 1.5, "clear": False},
            {"text": "LOCATED WITHIN THE TOMB IS A GOLDEN SARCOPHAGUS INSCRIBED WITH STRANGE HIEROGLYPHS.",
             "pause": 1.5, "clear": True},
            {
                "text": "SURPRISINGLY, MARIE FINDS TRANSLATIONS FROM THE DEPARTED PROFESSOR’S RESEARCH AND BEGINS TO "
                        "READ ALOUD:\n\nMARIE: [marie1][slow]'EVERY 10,000 YEARS, WHEN GREAT EVIL RETURNS, POUR A DROP "
                        "OF WATER ON THE SKELETON AND AWAKEN THE GOD OF JUSTICE, GOLDEN BAT.'[norm]",
                "pause": 2.0, "clear": True},
            {
                "text": "DISTRAUGHT FOR HER LATE FATHER, MARIE APPROACHES THE SARCOPHAGUS WITHIN THE TOMB AND OPENS IT. "
                        "INSIDE IS THE CORPSE OF A GOLDEN SKELETON.",
                "pause": 1.0, "clear": False},
            {
                "text": "USING SOME WATER FROM WHAT LITTLE RESERVES SHE HAS LEFT, SHE POURS A DROP ON THE "
                        "SKELETON’S CORPSE.\n\nMARIE: [marie2]'PLEASE GOD OF JUSTICE… HELP ME…'",
                "pause": 2.5, "clear": True},
            {
                "text": "[slow]THE TOMB BEGINS RUMBLING...[wait:1.5] [norm]AND WHAT ECHOES THROUGHOUT IS THE MANIACAL "
                        "LAUGHTER OF THE ANCIENT FIGURE OF LEGEND AS HE RISES FROM HIS SLUMBER:",
                "pause": 0.5, "clear": False}
        ],
        'true_ending': [
            {"text": "YOU ENTER AND FACE DR. NAZŌ WITH THE FULL MIGHT OF ATLANTIS.", "pause": 1.5, "clear": True},
            {
                "text": "GOLDEN BAT UNWRAPS THE BOTAN RICE CANDY AND EATS IT, GIVING HIM A BURST OF NOSTALGIC ENERGY, "
                        "WHILE THE 7 RELICS GLOW WITH BLINDING LIGHT!",
                "pause": 2.5, "clear": False},
            {
                "text": "\nGOLDEN BAT DOESN'T JUST DEFEAT FIVE FINGER AND DR. NAZŌ — HE TRANSFORMS INTO A GIANT GOLDEN "
                        "SILHOUETTE, OVERTAKING THE COSMOS AND SHATTERING THE PLANET ICARUS WITH A SINGLE HEROIC STRIKE.",
                "pause": 3.0, "clear": True},
            {"text": "[gold][slow]GOLDEN BAT: 'HA-HA-HA-HA-HA-HAAA...!!!'[norm]", "pause": 2.0, "clear": False}
        ],
        'win_ending': [
            {
                "text": "DR. NAZŌ STANDS IN THE MIDDLE OF THE ROOM, FACING AWAY FROM YOU, OVER AN ANCIENT "
                        "SPECTRAL CANNON...",
                "pause": 2.0, "clear": True},
            {
                "text": "DR. NAZŌ: 'So you've collected all the relics, Golden Bat? And retrieved the Icarus Data? "
                        "Regardless, I have the special lens, and you will never destroy Icarus!'",
                "pause": 2.5, "clear": False},
            {"text": "\n[gold]GOLDEN BAT: 'HA-HA-HA-HAAAA!'", "pause": 1.5, "clear": False},
            {"text": "\nDR. NAZŌ: 'What's so funny, you fool?'", "pause": 1.5, "clear": True},
            {
                "text": "GOLDEN BAT USES HIS SPECTRAL REINS AND GRAPPLES ON FIVE FINGER, SLASHING IT WITH A SINGLE "
                        "DOWNWARD STRIKE WITH HIS SILVER BATON. GOLDEN BAT SNATCHES THE SPECIAL LENS FROM DR. NAZŌ.",
                "pause": 2.5, "clear": False},
            {
                "text": "\nFIVE FINGER CRUMBLES UNDER ITS OWN WEIGHT AND BURSTS INTO FLAMES, AND BEGINS DIGGING "
                        "VIOLENTLY INTO THE GROUND.",
                "pause": 2.0, "clear": True},
            {"text": "DR. NAZŌ: 'CURSE YOU, GOLDEN BAT! I WILL RETURN!'", "pause": 2.0, "clear": False},
            {"text": "\nTHE MACHINE DISAPPEARS TUNNELING UNDERNEATH ATLANTIS, AND THE ISLAND BEGINS RUMBLING.",
             "pause": 2.0, "clear": True},
            {
                "text": "GOLDEN BAT RUSHES BACK TO THE SHIPWRECKED BEACH TO SEE MARIE. THE HERO FINDS MARIE, "
                        "AND HANDS HER THE SPECIAL LENS AND ICARUS DATA.",
                "pause": 2.0, "clear": False},
            {
                "text": "\nJUST THEN, THE FLYING SUPER CAR APPEARS ON THE BEACH INSTANTANEOUSLY DRIVEN BY "
                        "JAPANESE INVENTOR, PROFESSOR YAMATONE OF THE PEARL RESEARCH INSTITUTE.",
                "pause": 2.5, "clear": True},
            {
                "text": "PROF. YAMATONE: 'Quickly, Marie! Come with me back to the Pearl Research Institute, "
                        "before you meet the same fate as your father! With that lens and data, we can save the world!'",
                "pause": 2.5, "clear": False},
            {"text": "\nMARIE: 'Thank you, Golden Bat!'", "pause": 1.5, "clear": False},
            {"text": "\nPROF. YAMATONE: 'This is no time for solemn goodbyes!'", "pause": 1.5, "clear": True},
            {
                "text": "MARIE ENTERS THE SUPER CAR AND DISAPPEARS WITH PROFESSOR YAMATONE ALMOST AS FAST AS IT "
                        "ARRIVED, LEAVING GOLDEN BAT BEHIND ON THE BEACH.",
                "pause": 2.0, "clear": False},
            {
                "text": "\nTHE LOST ISLAND BEGINS SINKING UNDERWATER, WITH THE LINGERING LAUGHTER OF THE GOD "
                        "OF JUSTICE...",
                "pause": 2.0, "clear": True},
            {"text": "[gold][laugh][slow]GOLDEN BAT: 'HA-HA-HA-HA-HA-HAAA...!!!'[norm]", "pause": 3.0, "clear": False}
        ],
        'lose_ending': [
            {"text": "THE HALL APPEARS EMPTY, WITH AN ANCIENT SPECTRAL CANNON IN THE MIDDLE OF THE ROOM...",
             "pause": 2.0, "clear": True},
            {"text": "DR. NAZŌ: 'Golden Bat! Did you really think you could defeat me without all the relics?'",
             "pause": 2.5, "clear": False},
            {"text": "\nFIVE FINGER DESCENDS FROM THE CEILING, AND CAPTURES GOLDEN BAT IN ITS METALLIC GRIP.",
             "pause": 2.5, "clear": True},
            {"text": "DR. NAZŌ: 'There is nothing you can do to stop me! I will destroy Earth!'", "pause": 3.0,
             "clear": False}
        ]
    }