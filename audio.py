"""
Audio Controller Module

Description: Encapsulates Pygame Mixer BGM and SFX management, file path resolution,
             and automatic ambient sound playback per room location.
"""

import time, os, sys, pygame

class AudioManager:
    """Manages background music, sound effects, volume leveling, and fades."""

    def __init__(self):
        """Initializes Pygame mixer parameters and maps asset file paths."""
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.mixer.init()

        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        if hasattr(sys, '_MEIPASS'):
            base_dir = sys._MEIPASS
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assets_dir = os.path.join(base_dir, "assets")
        self.current_track = None

        # Background Music Registry
        self.music = {
            "title": os.path.join(self.assets_dir, "intro.mp3"),
            "true_credits": os.path.join(self.assets_dir, "credits_true.mp3"),
            "win_credits": os.path.join(self.assets_dir, "credits_win.mp3"),
            "lose_credits": os.path.join(self.assets_dir, "credits_lose.mp3"),
            "tomb": os.path.join(self.assets_dir, "tomb.mp3"),
            "tunnel": os.path.join(self.assets_dir, "tunnel.mp3"),
            "beach": os.path.join(self.assets_dir, "beach.mp3"),
            "cliffs": os.path.join(self.assets_dir, "cliffs.mp3"),
            "church": os.path.join(self.assets_dir, "church.mp3"),
            "cellar": os.path.join(self.assets_dir, "cellar.mp3"),
            "town": os.path.join(self.assets_dir, "town.mp3"),
            "armory": os.path.join(self.assets_dir, "armory.mp3"),
            "lab": os.path.join(self.assets_dir, "lab.mp3"),
            "observatory": os.path.join(self.assets_dir, "observatory.mp3"),
            "gallery": os.path.join(self.assets_dir, "street.mp3"),
        }

        self.master_sfx_volume = 0.4

        # Sound Effects Registry
        try:
            self.marie1 = pygame.mixer.Sound(os.path.join(self.assets_dir, "marie1.wav"))
            self.marie2 = pygame.mixer.Sound(os.path.join(self.assets_dir, "marie2.wav"))
            self.marie3 = pygame.mixer.Sound(os.path.join(self.assets_dir, "marie3.wav"))
            self.laugh = pygame.mixer.Sound(os.path.join(self.assets_dir, "laugh.wav"))
            self.bats = pygame.mixer.Sound(os.path.join(self.assets_dir, "bats.wav"))
            self.scifi = pygame.mixer.Sound(os.path.join(self.assets_dir, "scifi.wav"))
            self.item = pygame.mixer.Sound(os.path.join(self.assets_dir, "item.wav"))
            self.quit = pygame.mixer.Sound(os.path.join(self.assets_dir, "quit.wav"))
            self.icarus = pygame.mixer.Sound(os.path.join(self.assets_dir, "icarus_impact.wav"))

            # Set default volumes
            self.set_all_sfx_volume(self.master_sfx_volume)

        except pygame.error as e:
            # This will tell you exactly which file is missing or broken.
            print(f"Audio Loading Error: {e}")

    def set_all_sfx_volume(self, volume):
        """Sets master volume across all instantiated sound effect channels."""
        self.master_sfx_volume = volume
        for sound in [self.marie1, self.marie2, self.marie3, self.laugh, self.bats,
                      self.scifi, self.item, self.quit, self.icarus]:
            if sound is not None:
                sound.set_volume(volume)

    def play_bgm(self, key, volume = 0.2, fade = 500):
        """Loads and loops background music track if not already playing."""
        if key in self.music:
            if pygame.mixer.music.get_busy() and key == getattr(self, 'current_track', None):
                return
            pygame.mixer.music.load(self.music[key])
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1, fade_ms = fade)
            self.current_track = key

    def play_sfx(self, effect):
        """Plays a target sound effect by key lookup."""
        if effect == "marie1" and self.marie1:
            self.marie1.play()
        elif effect == "marie2" and self.marie2:
            self.marie2.play()
        elif effect == "marie3" and self.marie3:
            self.marie3.play()
        elif effect == "laugh" and self.laugh:
            self.laugh.play()
        elif effect == "bats" and self.bats:
            self.bats.play()
        elif effect == "scifi" and self.scifi:
            self.scifi.play()
        elif effect == "item" and self.item:
            self.item.play()
        elif effect == "quit" and self.quit:
            self.quit.play()
        elif effect == "icarus" and self.icarus:
            self.icarus.play()

    def stop(self):
        """Stops all active BGM and SFX channels."""
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        self.current_track = None

    def fade(self, duration = 5000):
        """Fades out audio tracks over specified duration in milliseconds."""
        pygame.mixer.music.fadeout(duration)
        pygame.mixer.fadeout(duration)
        self.current_track = None
        if duration >= 5000:
            time.sleep(duration / 1000)

    def get_room_music(self, current_room):
        """Triggers room-specific ambient background music."""
        if current_room == 'Ancient Tomb':
            self.play_bgm("tomb", volume=0.8)
        elif current_room == 'Secret Tunnel':
            self.play_bgm("tunnel", volume=0.4)
        elif current_room == 'Shipwrecked Beach':
            self.play_bgm("beach", volume=0.4)
        elif current_room == 'Ocean-Facing Cliffs':
            self.play_bgm("cliffs", volume=0.4)
        elif current_room == 'Abandoned Church':
            self.play_bgm('church', volume=0.4)
        elif current_room == 'Church Cellar':
            self.play_bgm("cellar", volume=0.4)
        elif current_room == 'Abandoned Residential District':
            self.play_bgm("town", volume=0.8)
        elif current_room == 'Rusted Armory':
            self.play_bgm("armory", volume=0.2)
        elif current_room == 'Ancient Atlantean Lab':
            self.play_bgm("lab", volume=1.0)
        elif current_room == 'Submerged Observation Deck':
            self.play_bgm("observatory", volume=0.6)
        elif current_room == 'Echoing Gallery':
            self.play_bgm("gallery", volume=0.6)

# Shared global instance
audio = AudioManager()