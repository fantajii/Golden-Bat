# GOLDEN BAT 🦇

**Golden Bat** is a text-based atmospheric adventure game written in Python. Explore the ruins of Atlantis, collect 7 legendary relics, and defeat the mysterious Dr. Nazō before the rogue planet Icarus crashes into Earth!

## 🌟 Features
- **Classic Text-Adventure Gameplay:** Navigate rooms, search for items, and uncover secrets using terminal commands.
- **Immersive Audio:** Features a fully integrated soundtrack and sound effects using `pygame.mixer` to set the mood for every room.
- **Multiple Endings:** Your inventory and exploration determine the fate of Earth. Can you unlock the True Ending?
- **Retro Terminal Aesthetic:** Dynamic scrolling text with inline delays, color formatting, and cinematic screen clears.

## 🎮 How to Play

### Playing the Executable (No Python Required)
1. Go to the **Releases** tab on the right side of this repository.
2. Download the `GoldenBat` executable for your operating system.
3. Double-click the file to launch the game! (A terminal window will open automatically).

### Running from Source
If you want to run or modify the raw Python code:
1. Ensure you have Python 3.x installed.
2. Clone this repository to your local machine.
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```
4. Run the main script:
   ```bash
   python main.py
   ```

## 🕹️ Commands
Type these actions when prompted to interact with the world:
- `go [direction]` - Move to an adjacent room (e.g., `go north`, `go east`).
- `get [item]` - Pick up a relic or item in the room (e.g., `get Red Cape`).
- `search` - Inspect your current surroundings for hidden items or secrets.
- `path` - View all available exits from your current location.
- `room` - Re-read the narrative description of your current location.
- `laugh` - Unleash the signature Golden Bat laugh!
- `quit` - Abandon the mission and exit the game.

## 🛠️ Built With
* **Python 3**
* **Pygame** - Utilized for the audio engine (BGM loops, SFX playback, and volume fading).

## 👨‍💻 Author
**Garrett Mandeville**
