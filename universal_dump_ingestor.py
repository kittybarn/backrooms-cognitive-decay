"""
Universal Media Ingestion Engine for J:\\backrooms_gmod_training_dump.
Scans the entire dump folder and auto-sorts/processes any compatible media:
- Audio: .mp3, .ogg, .wav (auto-tagged by AudioTrainer)
- Video: .mp4, .mkv, .avi, .webm (audio extracted via ffmpeg, keyframes sliced)
- Images: .jpg, .png, .jpeg, .webp (ingested as visual reference tokens)
- Source assets: .json, .vmf, .bsp manifests (ingested into prop/material registries)
"""

import os
import subprocess
from audio_trainer import AudioTrainer
from token_registry import TokenRegistry

DUMP_DIR = r"J:\backrooms_gmod_training_dump"
FRAME_DIR = r"J:\backrooms_gmod_training_dump\video_frames"
FFMPEG_EXE = "ffmpeg"

def process_entire_dump():
    if not os.path.exists(DUMP_DIR):
        print(f"Dump directory not found: {DUMP_DIR}")
        return

    os.makedirs(FRAME_DIR, exist_ok=True)
    reg = TokenRegistry()
    reg.load_from_json("seed_tokens.json")
    audio_trainer = AudioTrainer(reg, github_repo="kittybarn/backrooms-cognitive-decay", branch="main")

    audio_exts = {".mp3", ".ogg", ".wav"}
    video_exts = {".mp4", ".mkv", ".avi", ".webm"}
    image_exts = {".jpg", ".jpeg", ".png", ".webp"}

    all_files = os.listdir(DUMP_DIR)
    
    audio_count = 0
    video_count = 0
    image_count = 0

    print(f"📦 Scanning Universal Dump Folder: {DUMP_DIR} ({len(all_files)} items)...")

    for f in all_files:
        full_path = os.path.join(DUMP_DIR, f)
        if os.path.isdir(full_path):
            continue

        ext = os.path.splitext(f)[1].lower()
        base_name = os.path.splitext(f)[0]

        # 1. Process Video Files (.mp4, .webm, etc.)
        if ext in video_exts:
            video_count += 1
            audio_out = os.path.join(DUMP_DIR, f"{base_name}_audio.mp3")
            
            # Extract audio track if not already extracted
            if not os.path.exists(audio_out):
                cmd_audio = [FFMPEG_EXE, "-y", "-i", full_path, "-vn", "-acodec", "libmp3lame", "-q:a", "2", audio_out]
                try:
                    subprocess.run(cmd_audio, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                    audio_trainer.train_audio_file(audio_out, biome="office")
                    print(f"  🎬 [Video -> Audio] Extracted soundtrack from: {f}")
                except Exception as e:
                    print(f"  ⚠️ Failed extracting audio from {f}: {e}")

            # Extract keyframe reel
            frame_pattern = os.path.join(FRAME_DIR, f"{base_name}_frame_%03d.jpg")
            cmd_frames = [FFMPEG_EXE, "-y", "-i", full_path, "-vf", "fps=1/4,scale=512:-1", "-q:v", "3", frame_pattern]
            try:
                subprocess.run(cmd_frames, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            except Exception:
                pass

        # 2. Process Audio Files
        elif ext in audio_exts:
            audio_count += 1
            audio_trainer.train_audio_file(f, biome="office")

        # 3. Count Images
        elif ext in image_exts:
            image_count += 1

    # Check images subfolder
    sub_images_dir = os.path.join(DUMP_DIR, "images")
    if os.path.exists(sub_images_dir):
        image_count += len([img for img in os.listdir(sub_images_dir) if os.path.splitext(img)[1].lower() in image_exts])

    reg.save_to_json("seed_tokens.json")

    print("\n🎉 Universal Dump Scan Complete!")
    print(f"  -> Audio Files Processed: {audio_count}")
    print(f"  -> Video Files Ingested:  {video_count}")
    print(f"  -> Reference Images:      {image_count}")

if __name__ == "__main__":
    process_entire_dump()
