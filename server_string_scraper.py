"""
Binary String Scraper & Server Asset Filter.
Scrapes raw string tables, text logs, or BSP/GMA binaries to extract only models (.mdl)
and materials (.vmt) that actually exist on the target server/game.
"""

import os
import re
import json
from typing import Set, List
from token_registry import TokenRegistry, EnvironmentToken

class ServerStringScraper:
    def __init__(self, registry: TokenRegistry):
        self.registry = registry

    def scrape_from_text(self, text_or_filepath: str) -> List[str]:
        """
        Scrapes model (.mdl) and material (.vmt) paths from server console logs,
        string dumps, or text files.
        """
        raw_text = text_or_filepath
        if os.path.exists(text_or_filepath):
            with open(text_or_filepath, "r", encoding="utf-8", errors="ignore") as f:
                raw_text = f.read()

        # Regex for standard Source engine model & material paths
        model_pattern = r'(models/[\w\d_/-]+\.mdl)'
        material_pattern = r'(materials/[\w\d_/-]+(?:\.vmt)?)'

        found_models = set(re.findall(model_pattern, raw_text, re.IGNORECASE))
        found_materials = set(re.findall(material_pattern, raw_text, re.IGNORECASE))

        print(f"Scraped {len(found_models)} valid server models and {len(found_materials)} materials.")
        
        # Ingest and auto-tag them into our token registry
        for mdl in found_models:
            self._ingest_scraped_asset(mdl.lower(), "prop")

        for mat in found_materials:
            clean_mat = mat.lower().replace(".vmt", "")
            is_floor = any(k in clean_mat for k in ["floor", "carpet", "tile", "road"])
            self._ingest_scraped_asset(clean_mat, "floor" if is_floor else "wall")

        return list(found_models)

    def scrape_from_binary(self, binary_path: str, min_length: int = 6) -> List[str]:
        """
        Strings utility for binary files (e.g. .bsp map lumps, cache files, .gma packages).
        Extracts printable ASCII strings and isolates .mdl and material references.
        """
        if not os.path.exists(binary_path):
            print(f"File not found: {binary_path}")
            return []

        with open(binary_path, "rb") as f:
            data = f.read()

        # Extract ASCII strings
        ascii_strings = re.findall(b'[\x20-\x7E]{' + str(min_length).encode() + b',}', data)
        decoded = [s.decode('ascii', errors='ignore') for s in ascii_strings]
        combined = "\n".join(decoded)

        return self.scrape_from_text(combined)

    def _ingest_scraped_asset(self, asset_path: str, token_type: str):
        parts = re.split(r'[/_.\d-]', asset_path)
        tags = [p for p in parts if len(p) > 2 and p not in ["models", "materials", "props", "mdl", "vmt"]]
        
        name = os.path.splitext(os.path.basename(asset_path))[0]
        anchor = "floor" if token_type in ["prop", "floor"] else "wall"

        token = EnvironmentToken(
            id=asset_path,
            name=name,
            token_type=token_type,
            biomes=["server_native"],
            tags=tags,
            anchor=anchor
        )
        self.registry.register(token)
