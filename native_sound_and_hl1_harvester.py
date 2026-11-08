"""
Source Engine Native Sound & HL1 Asset Harvester.
1. Scans HL2 sound VPKs for:
   - Iconic Citizen VO lines ("Sometimes... I dream about cheese", "Whoops", "Did you feel that?", "Hey!")
   - Pure Liminal Ambience: Fluorescent hums, water dripping, pipe reverberation, distant machinery.
2. Scans J:\\hl1\\hl1\\hl1_pak_dir.vpk for:
   - Half-Life 1 Source props (retro Black Mesa lab consoles, security desks, hazardous crates)
   - Retro GoldSource audio (HEV announcements, resonant water drips, classic sci-fi hums).
3. Saves clean asset lists directly into J:\\backrooms_gmod_training_dump.
"""

import os
import json
import vpk

DUMP_DIR = r"J:\backrooms_gmod_training_dump"
GMOD_SOURCE_DIR = r"J:\SteamLibrary\steamapps\common\GarrysMod\sourceengine"
HL1_DIR = r"J:\hl1\hl1"

def harvest_native_sounds_and_hl1():
    print("🔊 Harvesting Native Source Audio & HL1 Assets...")

    # 1. Citizen VO Voice Lines (HL2)
    vo_vpk_path = os.path.join(GMOD_SOURCE_DIR, "hl2_sound_vo_english_dir.vpk")
    citizen_vo_lines = []
    if os.path.exists(vo_vpk_path):
        pak = vpk.open(vo_vpk_path)
        # Select quintessential, uncanny, or hilarious citizen voice clips
        target_vo_cues = [
            "cheese", "whoops", "didyouhear", "behindyou", "help", "pain",
            "overhere", "finally", "lookout", "holdon", "run", "illcover",
            "nice", "sorry", "excuseme", "waitfor"
        ]
        for f in pak:
            clean = f.lower().replace("\\", "/")
            if "vo/npc/male01/" in clean or "vo/npc/female01/" in clean:
                if any(cue in clean for cue in target_vo_cues):
                    # In GMod sound.PlayFile or sound.play, we drop the leading "sound/"
                    sound_path = clean.replace("sound/", "")
                    citizen_vo_lines.append(sound_path)

    print(f"  -> Extracted {len(citizen_vo_lines)} curated Citizen VO sound clips.")

    # 2. Ambient Loops (Drips, Hums, Tunnels, Pipes)
    amb_vpk_path = os.path.join(GMOD_SOURCE_DIR, "hl2_sound_misc_dir.vpk")
    categorized_ambience = {
        "hum": [],
        "drip_water": [],
        "machinery": [],
        "wind_pipe": []
    }
    if os.path.exists(amb_vpk_path):
        pak = vpk.open(amb_vpk_path)
        for f in pak:
            clean = f.lower().replace("\\", "/")
            if clean.startswith("sound/ambient/"):
                sound_path = clean.replace("sound/", "")
                if any(w in clean for w in ["water", "drip", "slosh"]):
                    categorized_ambience["drip_water"].append(sound_path)
                elif any(w in clean for w in ["hum", "buzz", "fluorescent", "light"]):
                    categorized_ambience["hum"].append(sound_path)
                elif any(w in clean for w in ["machine", "motor", "engine", "generator"]):
                    categorized_ambience["machinery"].append(sound_path)
                elif any(w in clean for w in ["wind", "pipe", "tunnel", "vent"]):
                    categorized_ambience["wind_pipe"].append(sound_path)

    total_amb = sum(len(v) for v in categorized_ambience.values())
    print(f"  -> Extracted {total_amb} environment-based ambient loops (hum, drip, machinery, pipes).")

    # 3. Half-Life 1 Source Props & Audio
    hl1_vpk_path = os.path.join(HL1_DIR, "hl1_pak_dir.vpk")
    hl1_props = []
    hl1_audio = []
    if os.path.exists(hl1_vpk_path):
        pak = vpk.open(hl1_vpk_path)
        for f in pak:
            clean = f.lower().replace("\\", "/")
            if clean.startswith("models/") and clean.endswith(".mdl"):
                # Avoid player characters or outdoor foliage
                if not any(b in clean for b in ["player", "tree", "plant"]):
                    hl1_props.append(clean)
            elif clean.startswith("sound/") and (clean.endswith(".wav") or clean.endswith(".mp3")):
                if "ambient/" in clean or "buttons/" in clean or "fvox/" in clean:
                    hl1_audio.append(clean.replace("sound/", ""))

    print(f"  -> Extracted {len(hl1_props)} HL1 Source props and {len(hl1_audio)} HL1 retro sounds.")

    # Save to JSON manifest in the dump folder
    out_path = os.path.join(DUMP_DIR, "native_citizen_ambient_hl1_manifest.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "citizen_vo": citizen_vo_lines,
            "ambient_by_biome": categorized_ambience,
            "hl1_props": hl1_props,
            "hl1_audio": hl1_audio
        }, f, indent=2)

    print(f"📁 Manifest saved to: {out_path}")

if __name__ == "__main__":
    harvest_native_sounds_and_hl1()
