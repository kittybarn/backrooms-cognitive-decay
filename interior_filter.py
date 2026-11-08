"""
Interior Filter & Map Whitelist for Source / HL2 / GMod.
Explicitly skips massive outdoor maps (canals, coastlines, Wasteland, skyboxes)
and focuses purely on claustrophobic interior corridors, apartments, labs, and liminal spaces.
"""

import os
import re
from typing import List, Set

# Whitelist of pure interior chapters/maps from HL2 & classic GMod
INTERIOR_MAP_WHITELIST = {
    # HL2 Day 1: Trainstation & Apartments
    "d1_trainstation_01",  # Station arrivals / checkpoints
    "d1_trainstation_03",  # Apartment complex interiors / stairwells
    "d1_trainstation_05",  # Kleiner's Lab interior

    # HL2 Day 1: Black Mesa East
    "d1_eli_01",           # Underground lab facility
    "d1_eli_02",           # Lab rooms & airlocks

    # HL2 Day 2: Nova Prospekt Prison & Facility (Peak liminal / institutional corridors)
    "d2_prison_02",        # Cell blocks & narrow hallways
    "d2_prison_03",        # Showers, laundry rooms, corridors
    "d2_prison_04",        # Sub-level security hallways
    "d2_prison_05",        # Control rooms & checkpoints
    "d2_prison_07",        # Teleport core room

    # HL2 Day 3: City 17 Uprising (Buildings & Nexus)
    "d3_c17_09",           # Combine Nexus interior headquarters
    "d3_c17_10a",          # Ruined office / sniper building interior

    # HL2 Day 3: Citadel (Brutalist metal & light corridors)
    "d3_citadel_01",
    "d3_citadel_02",
    "d3_citadel_03",
    "d3_breen_01",

    # Counter-Strike Source Interiors (Clean office & indoor spaces)
    "cs_office",           # The ultimate source office interior
    "cs_agency",           # Modern corporate office
    "de_bank"              # Indoor lobby & vaults
}

# Explicit blacklist terms: massive outdoor vistas, skybox terrain, and vehicular maps
OUTDOOR_BLACKLIST_KEYWORDS = [
    "coast",        # Highway 17 coastal vistas
    "canals",       # Water canal waterways
    "waterhazard",  # Airboat waterways
    "airboat",
    "jeep",
    "skybox",
    "cliff",
    "ocean",
    "forest",
    "exterior",
    "wasteland",
    "desert",
    "mountains"
]

class InteriorAssetFilter:
    @staticmethod
    def is_interior_map(map_name: str) -> bool:
        """Checks if a map is designated as an interior environment."""
        clean = os.path.splitext(os.path.basename(map_name))[0].lower()
        
        # Check whitelist first
        if clean in INTERIOR_MAP_WHITELIST:
            return True
        
        # Check blacklist keywords
        if any(bad in clean for bad in OUTDOOR_BLACKLIST_KEYWORDS):
            return False

        # If it contains explicit indoor keywords
        indoor_cues = ["office", "prison", "lab", "hall", "room", "station", "interior", "corridor", "bunker", "hotel", "house", "apartment"]
        return any(cue in clean for cue in indoor_cues)

    @staticmethod
    def is_interior_prop_or_mat(path: str) -> bool:
        """Filters out outdoor props like pine trees, rocks, cliffs, boats, and skybox cards."""
        clean = path.lower().replace("\\", "/")
        
        # Drop skybox materials
        if "tools/toolsskybox" in clean or "skybox/" in clean:
            return False

        # Drop large outdoor terrain & foliage props
        outdoor_prop_patterns = [
            "foliage", "trees", "pine", "shrub", "rock", "cliff",
            "nature/", "grass/", "dirt/", "mud/", "water/",
            "vehicles", "airboat", "buggy", "crane", "bridge",
            "debris_exterior"
        ]

        if any(pat in clean for pat in outdoor_prop_patterns):
            return False

        return True
