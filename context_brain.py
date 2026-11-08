"""
Fallible Machine Brain & Context Decay Simulator.
Generates rooms and contents, experiencing:
- Context FIFO window saturation and eviction
- Tag collision and improper lookup
- Confabulation and wrong-anchor replacement
"""

import random
from typing import List, Dict, Optional, Tuple
from collections import deque
from token_registry import TokenRegistry, EnvironmentToken

class ContextDecayBrain:
    def __init__(self, registry: TokenRegistry, context_window_size: int = 5, decay_rate: float = 0.15):
        self.registry = registry
        self.context_window_size = context_window_size
        self.decay_rate = decay_rate
        
        # FIFO context memory of recently hallucinated / recalled tokens
        self.memory_buffer: deque = deque(maxlen=context_window_size)
        
        # State tracking
        self.current_biome = "office"
        self.confusion_level = 0.0 # 0.0 (pristine) to 1.0+ (complete breakdown)

    def step_decay(self):
        """Simulates memory drift and creeping confusion."""
        self.confusion_level = min(1.0, self.confusion_level + self.decay_rate)
        
        # Spontaneous token corruption in memory
        if random.random() < self.confusion_level and len(self.memory_buffer) > 0:
            # Memory leak: randomly replace a memory token with a totally unrelated one
            corrupt_idx = random.randint(0, len(self.memory_buffer) - 1)
            all_tokens = list(self.registry.tokens.keys())
            if all_tokens:
                self.memory_buffer[corrupt_idx] = random.choice(all_tokens)

    def retrieve_token_fallible(self, intended_tags: List[str], required_anchor: str = "floor") -> Tuple[EnvironmentToken, str]:
        """
        Looks up a token matching the desired role/tags, but subject to machine confusion,
        weak tag collisions, and memory hallucination.
        """
        status_log = "EXACT_RECALL"

        # Roll against confusion level to see if memory lookup fails
        if random.random() < self.confusion_level:
            # Failure Mode 1: Confabulation from memory buffer (it uses whatever it just saw)
            if self.memory_buffer and random.random() < 0.4:
                remembered_id = random.choice(list(self.memory_buffer))
                token = self.registry.tokens[remembered_id]
                status_log = f"MEMORY_STUCK: Reused {token.name} due to token fixation."
                return token, status_log

            # Failure Mode 2: Weak Single-Tag Overlap Collision
            # The AI ignores most constraints and matches on 1 arbitrary tag (e.g. matching 'metal' instead of 'desk')
            scrambled_tag = random.choice(intended_tags)
            candidates = self.registry.tag_index.get(scrambled_tag.lower(), [])
            if candidates:
                chosen_id = random.choice(candidates)
                token = self.registry.tokens[chosen_id]
                status_log = f"TAG_COLLISION: Looked for {intended_tags}, but locked onto '{scrambled_tag}' -> grabbed {token.name}!"
                self.memory_buffer.append(token.id)
                return token, status_log

        # Normal / High Confidence Lookup
        scores = {}
        for tid, token in self.registry.tokens.items():
            # Check anchor match unless confused
            if self.confusion_level < 0.7 and required_anchor != "any" and token.anchor != required_anchor:
                continue
            
            # Count tag overlap
            overlap = len(set([t.lower() for t in token.tags]).intersection([t.lower() for t in intended_tags]))
            if self.current_biome in token.biomes:
                overlap += 1.5
            scores[tid] = overlap

        if not scores:
            # Desperation hallucination: grab literally anything
            chosen_id = random.choice(list(self.registry.tokens.keys()))
            token = self.registry.tokens[chosen_id]
            status_log = f"HALLUCINATION: Total context loss. Inserted random entity {token.name}."
        else:
            sorted_candidates = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            chosen_id = sorted_candidates[0][0]
            token = self.registry.tokens[chosen_id]
            status_log = f"NORMAL: Matched {token.name} for biome {self.current_biome}."

        self.memory_buffer.append(token.id)
        return token, status_log

    def generate_room(self, room_index: int) -> Dict:
        """
        Attempts to generate a single room scene, experiencing gradual drift.
        """
        self.step_decay()

        # Decide biome (with biome-drift when confused)
        if self.confusion_level > 0.5 and random.random() < 0.35:
            biomes = list(self.registry.biome_index.keys())
            old_b = self.current_biome
            self.current_biome = random.choice(biomes)
            biome_note = f"BIOME_DRIFT ({old_b} -> {self.current_biome})"
        else:
            biome_note = f"STABLE ({self.current_biome})"

        room_data = {
            "room_index": room_index,
            "confusion_level": round(self.confusion_level, 2),
            "biome_state": biome_note,
            "elements": [],
            "logs": []
        }

        # 1. Floor & Wall materials
        wall_token, w_log = self.retrieve_token_fallible(["wall_covering", "vertical"], required_anchor="wall")
        floor_token, f_log = self.retrieve_token_fallible(["floor_covering", "horizontal"], required_anchor="floor")
        light_token, l_log = self.retrieve_token_fallible(["light_source", "ceiling_anchored"], required_anchor="ceiling")

        room_data["elements"].append({"type": "wall", "id": wall_token.id, "name": wall_token.name})
        room_data["elements"].append({"type": "floor", "id": floor_token.id, "name": floor_token.name})
        room_data["elements"].append({"type": "light", "id": light_token.id, "name": light_token.name})
        room_data["logs"].extend([w_log, f_log, l_log])

        # 2. Props inside the room (Desk, Seating, Tech/Storage)
        prop_queries = [
            (["flat_surface", "furniture", "work"], "floor", "primary_furniture"),
            (["seating", "furniture", "rest"], "floor", "secondary_furniture"),
            (["technology", "box", "electronic"], "floor", "tech_accessory")
        ]

        for tags, anchor, label in prop_queries:
            prop_token, p_log = self.retrieve_token_fallible(tags, required_anchor=anchor)
            room_data["elements"].append({
                "type": label,
                "id": prop_token.id,
                "name": prop_token.name,
                "dimensions": prop_token.dimensions
            })
            room_data["logs"].append(p_log)

        return room_data
