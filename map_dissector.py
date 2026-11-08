"""
Map & VPK Ingestion Module.
Uses open-source Source engine parsers (such as srctools or regex/KeyValues)
to extract entities, prop positions, textures, and adjacency from maps.
"""

import os
import re
from typing import List, Dict, Tuple
from token_registry import TokenRegistry, EnvironmentToken

class SourceMapDissector:
    def __init__(self, registry: TokenRegistry):
        self.registry = registry

    def parse_vmf_file(self, vmf_path: str, default_biome: str = "office"):
        """
        Parses a Valve Map Format (.vmf) file to extract props, lights, and textures.
        Works directly or can hook into `srctools.vmf.VMF`.
        """
        if not os.path.exists(vmf_path):
            print(f"File not found: {vmf_path}")
            return []

        with open(vmf_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Extract prop_static and prop_physics entities
        prop_matches = re.findall(r'entity\s*\{[^}]*?"classname"\s*"(prop_[a-z]+)"[^}]*?"model"\s*"([^"]+)"[^}]*?"origin"\s*"([^"]+)"[^}]*?\}', content, re.DOTALL)
        
        extracted_tokens = []
        for classname, model_path, origin_str in prop_matches:
            # Clean model path
            clean_model = model_path.replace("\\", "/").lower()
            
            # Auto-generate baseline tags from model path
            tags = self._extract_tags_from_path(clean_model)
            
            token = EnvironmentToken(
                id=clean_model,
                name=os.path.splitext(os.path.basename(clean_model))[0],
                token_type="prop",
                biomes=[default_biome],
                tags=tags,
                anchor="floor"
            )
            self.registry.register(token)
            extracted_tokens.append(token)

        # Extract materials from solid sides
        mat_matches = set(re.findall(r'"material"\s*"([^"]+)"', content))
        for mat in mat_matches:
            clean_mat = mat.replace("\\", "/").lower()
            tags = self._extract_tags_from_path(clean_mat)
            is_floor = "floor" in clean_mat or "carpet" in clean_mat or "tile" in clean_mat
            token_type = "floor" if is_floor else "wall"
            
            token = EnvironmentToken(
                id=clean_mat,
                name=os.path.basename(clean_mat),
                token_type=token_type,
                biomes=[default_biome],
                tags=tags + ([ "horizontal", "floor_covering" ] if is_floor else [ "vertical", "wall_covering" ]),
                anchor="floor" if is_floor else "wall"
            )
            self.registry.register(token)
            extracted_tokens.append(token)

        print(f"Extracted {len(prop_matches)} props and {len(mat_matches)} materials from {os.path.basename(vmf_path)}.")
        return extracted_tokens

    def _extract_tags_from_path(self, path: str) -> List[str]:
        """Splits model/texture directory tokens into semantic tags."""
        words = re.split(r'[/_.\d-]', path)
        meaningful = [w.lower() for w in words if len(w) > 2 and w not in ["models", "props", "materials", "vmt", "mdl"]]
        return list(set(meaningful))
