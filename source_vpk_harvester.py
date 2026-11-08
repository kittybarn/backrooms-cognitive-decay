"""
Official GMod Default VPK Harvester.
Scans the exact Source Engine VPK directory:
J:\\SteamLibrary\\steamapps\\common\\GarrysMod\\sourceengine

Extracts only interior, liminal-compliant models and materials:
- content_cstrike_dir.vpk (Counter-Strike: Source interiors, offices, furniture)
- content_hl2_dir.vpk (Half-Life 2 props, machines, fixtures)
- hl2_misc_dir.vpk
- hl2_textures_dir.vpk (Walls, carpets, ceiling tiles)
"""

import os
import re
import json
import vpk
from interior_filter import InteriorAssetFilter

VPK_DIR = r"J:\SteamLibrary\steamapps\common\GarrysMod\sourceengine"
DUMP_DIR = r"J:\backrooms_gmod_training_dump"

def harvest_default_source_vpks():
    vpk_files = [
        "content_cstrike_dir.vpk",
        "content_hl2_dir.vpk",
        "hl2_misc_dir.vpk",
        "hl2_textures_dir.vpk"
    ]

    harvested_interior_props = []
    harvested_interior_materials = []

    print(f"📦 Scanning default Source engine VPKs in: {VPK_DIR}...")

    for vpk_name in vpk_files:
        full_path = os.path.join(VPK_DIR, vpk_name)
        if not os.path.exists(full_path):
            print(f"Skipping {vpk_name} (not found)")
            continue

        print(f"  -> Opening {vpk_name}...")
        try:
            pak = vpk.open(full_path)
            for file_path in pak:
                clean_path = file_path.lower().replace("\\", "/")
                
                # Filter for props (.mdl)
                if clean_path.startswith("models/") and clean_path.endswith(".mdl"):
                    # Check our interior filter (skips rocks, trees, cliffs, vehicles)
                    if InteriorAssetFilter.is_interior_prop_or_mat(clean_path):
                        harvested_interior_props.append(clean_path)

                # Filter for materials (.vmt)
                elif clean_path.startswith("materials/") and clean_path.endswith(".vmt"):
                    if InteriorAssetFilter.is_interior_prop_or_mat(clean_path):
                        harvested_interior_materials.append(clean_path.replace(".vmt", ""))
        except Exception as e:
            print(f"Error reading {vpk_name}: {e}")

    # Remove duplicates
    unique_props = sorted(list(set(harvested_interior_props)))
    unique_mats = sorted(list(set(harvested_interior_materials)))

    print(f"\n✅ Harvest Complete!")
    print(f"  -> Total Interior Props:     {len(unique_props)}")
    print(f"  -> Total Interior Materials: {len(unique_mats)}")

    # Save to JSON manifest in the training dump
    out_manifest = os.path.join(DUMP_DIR, "source_default_interior_assets.json")
    with open(out_manifest, "w", encoding="utf-8") as f:
        json.dump({
            "source_directory": VPK_DIR,
            "total_props": len(unique_props),
            "total_materials": len(unique_mats),
            "props": unique_props,
            "materials": unique_mats
        }, f, indent=2)

    print(f"📁 Saved asset manifest to: {out_manifest}")

if __name__ == "__main__":
    harvest_default_source_vpks()
