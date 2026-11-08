"""
Multi-Modal Video Ingestion Pipeline.
Handles videos (.mp4, .mkv, .avi, .webm):
1. Uses ffmpeg to extract the audio track directly as an MP3 -> feeds into Audio Trainer.
2. Uses ffmpeg to extract key visual frames (e.g., 1 frame every 4 seconds) -> feeds into Liminal Image Registry.
3. Allows Starfall chips to display video frame reels on CRT TVs / projectors using `render.createMaterial()`.
"""

import os
import subprocess
from audio_trainer import AudioTrainer
from token_registry import TokenRegistry

FFMPEG_EXE = "ffmpeg"
DUMP_DIR = r"J:\backrooms_gmod_training_dump"
FRAME_DIR = r"J:\backrooms_gmod_training_dump\video_frames"

class VideoTrainer:
    def __init__(self, registry: TokenRegistry, github_repo: str = "kittybarn/backrooms-cognitive-decay", branch: str = "main"):
        self.registry = registry
        self.audio_trainer = AudioTrainer(registry, github_repo=github_repo, branch=branch)
        os.makedirs(FRAME_DIR, exist_ok=True)

    def process_video(self, video_path: str, biome: str = "office"):
        """
        Processes a raw video file:
        - Extracts audio -> MP3 (for 3D audio playback).
        - Extracts key visual frames -> JPGs (for CRT TV display reels).
        """
        if not os.path.exists(video_path):
            print(f"Video file not found: {video_path}")
            return None

        filename = os.path.basename(video_path)
        base_name = os.path.splitext(filename)[0]

        print(f"\n🎬 Processing Video: {filename}...")

        # 1. Extract Audio Track using ffmpeg
        audio_out = os.path.join(DUMP_DIR, f"{base_name}_audio.mp3")
        audio_cmd = [
            FFMPEG_EXE, "-y",
            "-i", video_path,
            "-vn", # no video
            "-acodec", "libmp3lame",
            "-q:a", "2",
            audio_out
        ]
        try:
            subprocess.run(audio_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            print(f"  🎵 Extracted Audio: {os.path.basename(audio_out)}")
            # Train extracted audio
            self.audio_trainer.train_audio_file(audio_out, biome=biome)
        except Exception as e:
            print(f"  ⚠️ Could not extract audio from {filename}: {e}")

        # 2. Extract Key Video Frames (1 frame every 4 seconds)
        frame_pattern = os.path.join(FRAME_DIR, f"{base_name}_frame_%03d.jpg")
        frame_cmd = [
            FFMPEG_EXE, "-y",
            "-i", video_path,
            "-vf", "fps=1/4,scale=512:-1", # 1 frame per 4s, resized for fast texture streaming
            "-q:v", "3",
            frame_pattern
        ]
        try:
            subprocess.run(frame_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            # Count extracted frames
            frames = [f for f in os.listdir(FRAME_DIR) if f.startswith(base_name) and f.endswith(".jpg")]
            print(f"  🖼️  Extracted {len(frames)} key frames to {FRAME_DIR}")
        except Exception as e:
            print(f"  ⚠️ Could not extract frames from {filename}: {e}")

        print(f"✅ Video '{filename}' fully processed and integrated into training dump!")

if __name__ == "__main__":
    reg = TokenRegistry()
    reg.load_from_json("seed_tokens.json")
    vtrainer = VideoTrainer(reg)
    print("Video trainer initialized and ready to ingest .mp4, .webm, or .mkv files from J:\\backrooms_gmod_training_dump!")
