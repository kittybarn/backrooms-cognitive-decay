"""
YouTube / Web Audio Downloader for Backrooms Audio Training.
Uses yt-dlp + ffmpeg to download audio from URLs, extract high-quality MP3s,
save them directly to J:\\backrooms_gmod_training_dump, and auto-train them.
"""

import os
import sys
import subprocess
from audio_trainer import AudioTrainer
from token_registry import TokenRegistry

YT_DLP_EXE = r"C:\Users\bkare\AppData\Local\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe"
OUTPUT_DIR = r"J:\backrooms_gmod_training_dump"

def download_audio_from_url(url: str, custom_filename: str = None, biome: str = "office"):
    """
    Downloads audio from YouTube, SoundCloud, or any supported URL using yt-dlp,
    converts to MP3, and auto-ingests into the Backrooms token registry.
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    if custom_filename:
        out_template = os.path.join(OUTPUT_DIR, f"{custom_filename}.%(ext)s")
    else:
        out_template = os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s")

    cmd = [
        YT_DLP_EXE,
        "-x",  # Extract audio
        "--audio-format", "mp3",
        "--audio-quality", "0",  # Best VBR quality
        "-o", out_template,
        url
    ]

    print(f"📥 Fetching audio with yt-dlp from: {url}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("✅ Download and conversion complete!")
        
        # Train and update token registry
        reg = TokenRegistry()
        reg.load_from_json("seed_tokens.json")
        trainer = AudioTrainer(reg, github_repo="kittybarn/backrooms-cognitive-decay", branch="main")
        
        # Train all files in output dir
        trainer.batch_train_folder(OUTPUT_DIR, default_biome=biome)
        reg.save_to_json("seed_tokens.json")
        print("✅ Seed tokens updated with the new audio!")
    else:
        print(f"❌ yt-dlp error:\n{result.stderr}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        name = sys.argv[2] if len(sys.argv) > 2 else None
        download_audio_from_url(target_url, custom_filename=name)
    else:
        print("Usage: python download_audio.py <URL> [optional_filename]")
