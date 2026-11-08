"""
Property & Behavioral Entanglement System (Cognitive Cross-Wiring).
Allows entities, props, doors, and NPCs to have their numerical and behavioral variables
scrambled, transposed, or swapped due to context degradation.
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List
import random

@dataclass
class EntityBehaviorProfile:
    id: str
    category: str  # "door", "light", "npc", "prop_physics", "sound_emitter"
    attributes: Dict[str, Any] = field(default_factory=dict)

def create_sample_behavior_pool() -> Dict[str, EntityBehaviorProfile]:
    pool = {}

    # Door profile
    pool["door_sliding"] = EntityBehaviorProfile(
        id="prop_door_rotating",
        category="door",
        attributes={
            "speed": 100.0,          # Standard door open speed
            "distance": 90.0,        # Degrees of rotation
            "sound_open": "doors/door_metal_large_open1.wav",
            "sound_close": "doors/door_metal_large_close1.wav",
            "mass": 500.0,
            "color": [255, 255, 255],
            "scale": [1.0, 1.0, 1.0]
        }
    )

    # Fast Ceiling Fan / Motor profile
    pool["fan_motor"] = EntityBehaviorProfile(
        id="ambient_generic_fan",
        category="motor",
        attributes={
            "speed": 1800.0,         # High RPM speed
            "pitch": 120,            # High sound pitch
            "sound_loop": "ambient/machines/fan_loop1.wav",
            "mass": 40.0,
            "scale": [1.0, 1.0, 1.0]
        }
    )

    # Light Fixture profile
    pool["flicker_light"] = EntityBehaviorProfile(
        id="light",
        category="light",
        attributes={
            "brightness": 3.0,
            "flicker_rate": 0.05,
            "light_color": [255, 240, 200],
            "sound_buzz": "ambient/energy/spark1.wav",
            "range": 256.0
        }
    )

    # NPC / Stalker entity profile
    pool["npc_stalker"] = EntityBehaviorProfile(
        id="npc_fastzombie",
        category="npc",
        attributes={
            "walk_speed": 350.0,     # Sprinting speed
            "health": 50.0,
            "model": "models/zombie/fast.mdl",
            "voice_pitch": 85,
            "idle_animation": "idle01",
            "attack_damage": 15.0
        }
    )

    # Civilian / Standing NPC profile
    pool["npc_office_worker"] = EntityBehaviorProfile(
        id="npc_citizen",
        category="npc",
        attributes={
            "walk_speed": 70.0,      # Slow stroll
            "health": 100.0,
            "model": "models/humans/group01/male_07.mdl",
            "voice_pitch": 100,
            "idle_animation": "idle_subtle",
            "attack_damage": 0.0
        }
    )

    return pool

class VariableEntangler:
    """
    Simulates cross-wiring memory faults:
    Transposes numerical properties and cross-pollinates variables between mismatched entities.
    """
    def __init__(self, behavior_pool: Dict[str, EntityBehaviorProfile]):
        self.pool = behavior_pool

    def entangle_entities(self, target_key: str, confusion_level: float) -> Dict[str, Any]:
        """
        Takes a base entity profile and mutates it based on confusion level.
        Variables may be stolen from completely different entity types.
        """
        if target_key not in self.pool:
            return {}

        base_profile = self.pool[target_key]
        mutated_attrs = dict(base_profile.attributes)
        glitch_logs = []

        if confusion_level <= 0.1:
            return {"profile": base_profile.id, "category": base_profile.category, "attributes": mutated_attrs, "glitches": []}

        # Select a candidate entity from which to leak variables
        other_keys = [k for k in self.pool.keys() if k != target_key]
        donor_key = random.choice(other_keys)
        donor_profile = self.pool[donor_key]

        # Glitch Type A: Numerical Transposition (e.g. door inherits fan RPM speed)
        for key in list(mutated_attrs.keys()):
            if random.random() < (confusion_level * 0.7):
                # Search if donor has a similar or numerical variable
                donor_numerical = [k for k, v in donor_profile.attributes.items() if isinstance(v, (int, float))]
                if donor_numerical:
                    stolen_var = random.choice(donor_numerical)
                    stolen_val = donor_profile.attributes[stolen_var]
                    old_val = mutated_attrs[key]
                    
                    if isinstance(old_val, (int, float)):
                        mutated_attrs[key] = stolen_val
                        glitch_logs.append(f"CROSS_WIRE: {base_profile.category}['{key}'] replaced with {donor_profile.category}['{stolen_var}'] ({old_val} -> {stolen_val})")

        # Glitch Type B: Identity Leak / Wrong Model & Sound
        if confusion_level > 0.5 and random.random() < (confusion_level * 0.6):
            donor_strings = [k for k, v in donor_profile.attributes.items() if isinstance(v, str)]
            if donor_strings:
                stolen_str_key = random.choice(donor_strings)
                stolen_str_val = donor_profile.attributes[stolen_str_key]
                # If target has a model or sound attribute, swap it
                target_str_keys = [k for k, v in mutated_attrs.items() if isinstance(v, str)]
                if target_str_keys:
                    target_replace_key = random.choice(target_str_keys)
                    mutated_attrs[target_replace_key] = stolen_str_val
                    glitch_logs.append(f"IDENTITY_LEAK: {base_profile.category}['{target_replace_key}'] hijacked by {donor_profile.category} string ('{stolen_str_val}')")

        return {
            "profile": base_profile.id,
            "category": base_profile.category,
            "attributes": mutated_attrs,
            "glitches": glitch_logs
        }

if __name__ == "__main__":
    pool = create_sample_behavior_pool()
    entangler = VariableEntangler(pool)

    print("=== TESTING VARIABLE ENTANGLEMENT & CROSS-WIRING ===\n")
    for confusion in [0.2, 0.5, 0.85, 1.0]:
        print(f"--- Confusion Level: {confusion} ---")
        
        # Test on a door
        door_result = entangler.entangle_entities("door_sliding", confusion)
        print(f"Door speed: {door_result['attributes'].get('speed')} (Normal: 100.0)")
        for g in door_result["glitches"]:
            print(f"  * {g}")

        # Test on an NPC
        npc_result = entangler.entangle_entities("npc_office_worker", confusion)
        print(f"Citizen model: {npc_result['attributes'].get('model')} | Speed: {npc_result['attributes'].get('walk_speed')}")
        for g in npc_result["glitches"]:
            print(f"  * {g}")
        print()
