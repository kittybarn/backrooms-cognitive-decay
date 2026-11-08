"""
Scene Tagger and Image Ingestion Stub / Hook.
Supports ingestion from vision models, CLIP-like tag extractors, or manual text descriptions.
Extracts environmental attributes into the token format.
"""

from typing import List, Dict
import json
from token_registry import TokenRegistry, EnvironmentToken

class SceneTagger:
    def __init__(self, registry: TokenRegistry):
        self.registry = registry

    def ingest_description(self, item_id: str, label: str, description: str, detected_tags: List[str], biome: str, anchor: str = "floor", dimensions: List[float] = None):
        """
        Ingests an object identified from image descriptions or open-source vision taggers (e.g. CLIP / BLIP / Florence-2).
        """
        if dimensions is None:
            dimensions = [32.0, 32.0, 32.0]
            
        token = EnvironmentToken(
            id=item_id,
            name=label,
            token_type="prop",
            biomes=[biome],
            tags=[t.lower().strip() for t in detected_tags],
            anchor=anchor,
            dimensions=dimensions
        )
        self.registry.register(token)
        return token

    def query_by_tags(self, desired_tags: List[str], current_biome: str = None) -> List[tuple]:
        """
        Returns ranked tokens matching desired tags, along with their match score.
        """
        scores = {}
        for tag in desired_tags:
            tag_clean = tag.lower().strip()
            matching_ids = self.registry.tag_index.get(tag_clean, [])
            for tid in matching_ids:
                scores[tid] = scores.get(tid, 0) + 1.0

        # Small bonus for biome alignment (if not in full decay)
        if current_biome:
            for tid in scores:
                token = self.registry.tokens[tid]
                if current_biome.lower() in [b.lower() for b in token.biomes]:
                    scores[tid] += 0.5

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked
