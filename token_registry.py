"""
Tag-based Knowledge Graph & Token Registry.
Stores semantic tags, bounding box data, surface attachment rules, and biomes.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json

@dataclass
class EnvironmentToken:
    id: str  # GMod model path, material path, or abstract token
    name: str
    token_type: str  # "prop", "wall", "floor", "ceiling", "light", "portal"
    biomes: List[str]  # e.g. ["office", "warehouse", "basement", "hospital", "hotel"]
    tags: List[str]  # e.g. ["metal", "storage", "box", "electrical", "sitting"]
    anchor: str  # "floor", "wall", "ceiling", "any"
    dimensions: List[float] = field(default_factory=lambda: [32.0, 32.0, 32.0]) # width, depth, height in Source units
    co_occurs_with: List[str] = field(default_factory=list)

class TokenRegistry:
    def __init__(self):
        self.tokens: Dict[str, EnvironmentToken] = {}
        self.tag_index: Dict[str, List[str]] = {} # tag -> list of token IDs
        self.biome_index: Dict[str, List[str]] = {} # biome -> list of token IDs

    def register(self, token: EnvironmentToken):
        self.tokens[token.id] = token
        
        for tag in token.tags:
            self.tag_index.setdefault(tag.lower(), []).append(token.id)
            
        for biome in token.biomes:
            self.biome_index.setdefault(biome.lower(), []).append(token.id)

    def save_to_json(self, path: str):
        data = {
            tid: {
                "id": t.id,
                "name": t.name,
                "token_type": t.token_type,
                "biomes": t.biomes,
                "tags": t.tags,
                "anchor": t.anchor,
                "dimensions": t.dimensions,
                "co_occurs_with": t.co_occurs_with
            }
            for tid, t in self.tokens.items()
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_json(self, path: str):
        with open(path, "r") as f:
            data = json.load(f)
            for tid, d in data.items():
                self.register(EnvironmentToken(**d))
