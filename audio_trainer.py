"""
Audio Trainer & Sound Ingestion Engine.
1. Analyzes filename tokens & acoustics.
2. Extracts semantic acoustic tags (drone, hum, metallic, water, mechanical, voice, etc.)
3. Generates whitelist-compliant GitHub raw URLs.
4. Registers audio tokens directly into the brain for Starfall bass.loadURL streaming.
"""

import os
import re
from typing import List, Dict
from dataclasses import dataclass
from token_registry import TokenRegistry, EnvironmentToken

# Acoustic tag dictionary mapping common sound indicators
SOUND_KEYWORDS = {
    "hum": ["ambient", "drone", "60hz", "electrical", "fluorescent", "monotonous", "low_freq"],
    "buzz": ["electrical", "fluorescent", "spark", "high_freq", "ballast", "irritating"],
    "drone": ["ambient", "dark", "hallway", "liminal", "heavy", "deep", "hypnotic"],
    "water": ["damp", "pipe", "dripping", "slosh", "sewer", "leak", "wet"],
    "drip": ["pipe", "isolated", "sharp", "water", "wet", "rhythmic"],
    "metal": ["impact", "creak", "industrial", "resonance", "steel", "door"],
    "creak": ["wooden", "door", "structure", "unsettling", "strain", "slow"],
    "static": ["white_noise", "radio", "glitch", "signal", "corrupted", "hiss"],
    "whisper": ["voice", "entity", "human", "distorted", "eerie", "paranoid"],
    "wind": ["hollow", "void", "tunnel", "vent", "cold", "open_space"],
    "footstep": ["presence", "entity", "pacing", "stalker", "rhythm"],
    "click": ["switch", "ballast", "breaker", "mechanical", "trigger"],
    "thud": ["impact", "heavy", "structural", "fall", "sub_bass"]
}

@dataclass
class AudioToken:
    id: str  # Direct Raw GitHub URL
    filename: str
    biome: str
    tags: List[str]
    volume: float = 1.0
    loop: bool = True

class AudioTrainer:
    def __init__(self, registry: TokenRegistry, github_repo: str = "username/backrooms_audio", branch: str = "main"):
        """
        github_repo: format 'Owner/Repository' (e.g. 'myuser/backrooms_assets')
        branch: branch name (e.g. 'main' or 'master')
        """
        self.registry = registry
        self.github_repo = github_repo
        self.branch = branch

    def train_audio_file(self, filepath_or_name: str, biome: str = "office") -> AudioToken:
        """
        Analyzes an audio file by filename & semantic cues,
        generates the official Starfall-whitelisted Raw GitHub URL,
        and registers it into the token registry.
        """
        filename = os.path.basename(filepath_or_name)
        clean_name = os.path.splitext(filename)[0].lower()
        
        # 1. Semantic Tag Extraction
        detected_tags = ["sound", "audio_stream", "http"]
        words = re.split(r'[/_.\d\s-]+', clean_name)
        
        for w in words:
            if not w:
                continue
            detected_tags.append(w)
            # Match against acoustic keywords
            for key, associations in SOUND_KEYWORDS.items():
                if key in w:
                    detected_tags.extend(associations)

        detected_tags = list(set(detected_tags))

        # 2. Build official Starfall-whitelisted URL (raw.githubusercontent.com)
        github_raw_url = f"https://raw.githubusercontent.com/{self.github_repo}/{self.branch}/audio/{filename}"

        # 3. Register into unified TokenRegistry
        is_ambient = any(t in detected_tags for t in ["drone", "hum", "loop", "ambient", "static"])
        token = EnvironmentToken(
            id=github_raw_url,
            name=f"Audio: {clean_name}",
            token_type="sound_emitter",
            biomes=[biome],
            tags=detected_tags,
            anchor="ceiling" if "hum" in detected_tags else "any",
            dimensions=[16.0, 16.0, 16.0]
        )
        self.registry.register(token)

        audio_obj = AudioToken(
            id=github_raw_url,
            filename=filename,
            biome=biome,
            tags=detected_tags,
            loop=is_ambient
        )

        return audio_obj

    def batch_train_folder(self, folder_path: str, default_biome: str = "office") -> List[AudioToken]:
        """
        Scans an entire local folder of MP3s / OGGs, trains the metadata,
        and prints out the exact paths ready for GitHub.
        """
        if not os.path.exists(folder_path):
            print(f"Folder not found: {folder_path}")
            return []

        results = []
        valid_exts = {".mp3", ".ogg", ".wav"}
        for f in os.listdir(folder_path):
            ext = os.path.splitext(f)[1].lower()
            if ext in valid_exts:
                token = self.train_audio_file(f, biome=default_biome)
                results.append(token)

        print(f"✅ Trained {len(results)} audio files from {folder_path}.")
        return results

if __name__ == "__main__":
    reg = TokenRegistry()
    trainer = AudioTrainer(reg, github_repo="myuser/backrooms_audio", branch="main")

    sample_files = [
        "60hz_fluorescent_ballast_hum_loop.mp3",
        "distant_pipe_water_leak.ogg",
        "subway_deep_drone_rumble.mp3",
        "creepy_radio_static_whispers.wav",
        "heavy_metal_door_slam.mp3"
    ]

    print("=== TESTING AUDIO TRAINER ===")
    for s in sample_files:
        res = trainer.train_audio_file(s, biome="office")
        print(f"\n🎵 File: {res.filename}")
        print(f"   URL:  {res.id}")
        print(f"   Loop: {res.loop}")
        print(f"   Tags: {res.tags[:6]}...")
