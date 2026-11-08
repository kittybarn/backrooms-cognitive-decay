"""
Hierarchical Spatial Relationship & Affordance Graph.
Models physical spatial logic:
- 'surface_mount' (TVs, Radios, Monitors, Phones) MUST search for 'flat_surface' (Desks, Tables).
- 'seating' (Chairs, Stools) MUST search for nearby 'table' or 'desk' with facing orientation.
- 'wall_mount' (Payphones, Clocks, Breaker boxes) attaches to 'wall'.

Includes Rare Cognitive Mutations:
- Anomalous Scale Distortion (uncommon/rare: stretched along 1 axis, miniature, or gargantuan).
- Color Inversion / Corrupted Hue (rare: radioactive green, inverted negative, scorched black).
- Hologram RenderFX Glitches (ultra-rare: kRenderFxPulseFast, Strobe, Hologram jitter).
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import random
import json

@dataclass
class SpatialAffordance:
    id: str
    name: str
    role: str  # "surface_prop", "host_furniture", "seating", "fixture", "wall_mount"
    anchor_type: str  # "on_top_of", "adjacent_to", "wall_flat", "floor"
    requires_role: Optional[str] = None  # e.g. "surface_prop" requires "host_furniture"
    relative_offset: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])
    dimensions: List[float] = field(default_factory=lambda: [30.0, 30.0, 30.0])

class AffordanceResolver:
    def __init__(self):
        # Database of spatial affordance rules
        self.rules: Dict[str, SpatialAffordance] = {
            # Host furniture (creates surfaces that other things sit on)
            "models/props_c17/FurnitureDesk001a.mdl": SpatialAffordance(
                id="models/props_c17/FurnitureDesk001a.mdl",
                name="Office Desk",
                role="host_furniture",
                anchor_type="floor",
                dimensions=[64.0, 36.0, 30.0]
            ),
            "models/props_c17/FurnitureTable001a.mdl": SpatialAffordance(
                id="models/props_c17/FurnitureTable001a.mdl",
                name="Coffee / Dining Table",
                role="host_furniture",
                anchor_type="floor",
                dimensions=[48.0, 48.0, 28.0]
            ),
            # Surface props (need a host surface to rest on!)
            "models/props_c17/tv_monitor01.mdl": SpatialAffordance(
                id="models/props_c17/tv_monitor01.mdl",
                name="Vintage CRT Television",
                role="surface_prop",
                anchor_type="on_top_of",
                requires_role="host_furniture",
                dimensions=[20.0, 18.0, 18.0]
            ),
            "models/props_lab/monitor02.mdl": SpatialAffordance(
                id="models/props_lab/monitor02.mdl",
                name="Lab Computer Screen",
                role="surface_prop",
                anchor_type="on_top_of",
                requires_role="host_furniture",
                dimensions=[16.0, 16.0, 16.0]
            ),
            "models/props_lab/reciever01a.mdl": SpatialAffordance(
                id="models/props_lab/reciever01a.mdl",
                name="Shortwave Radio Receiver",
                role="surface_prop",
                anchor_type="on_top_of",
                requires_role="host_furniture",
                dimensions=[18.0, 14.0, 10.0]
            ),
            # Seating (wants to be adjacent to a table or desk)
            "models/props_c17/FurnitureChair001a.mdl": SpatialAffordance(
                id="models/props_c17/FurnitureChair001a.mdl",
                name="Office Chair",
                role="seating",
                anchor_type="adjacent_to",
                requires_role="host_furniture",
                dimensions=[22.0, 22.0, 36.0]
            )
        }

    def place_prop_with_affordance(self, prop_id: str, host_pos: List[float], host_dims: List[float], confusion: float) -> Dict:
        """
        Calculates exact 3D coordinates based on human spatial logic,
        but injects rare mutations (scale distortion, color corrupt, renderFX).
        """
        affordance = self.rules.get(prop_id)
        if not affordance:
            # Fallback default
            affordance = SpatialAffordance(id=prop_id, name="Generic Prop", role="surface_prop", anchor_type="on_top_of")

        placed_pos = list(host_pos)
        placed_ang = [0.0, 0.0, 0.0]
        
        # 1. NORMAL LOGICAL POSITIONING
        if affordance.anchor_type == "on_top_of":
            # Sits neatly on top of the host furniture surface
            table_height = host_dims[2] if host_dims else 30.0
            placed_pos[2] = host_pos[2] + table_height
            placed_pos[0] += random.uniform(-10.0, 10.0) # slight natural offset
            placed_pos[1] += random.uniform(-10.0, 10.0)
        elif affordance.anchor_type == "adjacent_to":
            # Tucked in front of the desk/table, pulled back ~24 units
            placed_pos[0] = host_pos[0] + 24.0
            placed_pos[1] = host_pos[1]
            placed_pos[2] = host_pos[2]
            placed_ang = [0.0, 180.0, 0.0] # facing toward the desk

        # 2. ANOMALOUS MUTATIONS (Uncommon / Rare Glitches)
        mutations = []
        final_scale = [1.0, 1.0, 1.0]
        final_color = [255, 255, 255, 255]
        render_fx = 0

        # A: Spatial Displacement Glitch (Cognitive Confusion)
        if confusion > 0.4 and random.random() < (confusion * 0.45):
            # The AI forgets where the top of the table was: places TV clipping inside or hovering
            placed_pos[2] += random.choice([-15.0, 25.0, -table_height])
            mutations.append("MISCALCULATED_SURFACE_HEIGHT: Embedded or floating above host furniture")

        # B: Scale Distortion (Uncommon/Rare: ~10% baseline, up to 30% under decay)
        if random.random() < (0.08 + (confusion * 0.20)):
            scale_type = random.choice(["stretched_z", "squashed_y", "gargantuan", "miniature"])
            if scale_type == "stretched_z":
                final_scale = [1.0, 1.0, round(random.uniform(1.8, 3.2), 2)]
            elif scale_type == "squashed_y":
                final_scale = [round(random.uniform(1.4, 2.0), 2), 0.25, 1.0]
            elif scale_type == "gargantuan":
                final_scale = [round(random.uniform(2.5, 4.0), 2)] * 3
            elif scale_type == "miniature":
                final_scale = [round(random.uniform(0.2, 0.4), 2)] * 3
            mutations.append(f"SCALE_ANOMALY: {scale_type} -> scale {final_scale}")

        # C: Color Inversion / Corrupted Tint (More Rare: ~4% baseline, up to 15%)
        if random.random() < (0.04 + (confusion * 0.12)):
            color_theme = random.choice(["decay_green", "scorched_black", "inverted_cyan", "blood_crimson"])
            if color_theme == "decay_green":
                final_color = [40, 240, 80, 255]
            elif color_theme == "scorched_black":
                final_color = [35, 35, 35, 255]
            elif color_theme == "inverted_cyan":
                final_color = [20, 220, 255, 255]
            elif color_theme == "blood_crimson":
                final_color = [200, 25, 25, 255]
            mutations.append(f"COLOR_CORRUPTION: {color_theme} -> RGBA {final_color}")

        # D: RenderFX Glitch (Most Rare: ~2% baseline, up to 8%)
        # 16 = kRenderFxPulseFast, 3 = kRenderFxHologram, 9 = kRenderFxStrobeSlow
        if random.random() < (0.02 + (confusion * 0.08)):
            render_fx = random.choice([3, 9, 16])
            mutations.append(f"RENDER_FX_GLITCH: applied GMod RenderFX ID {render_fx}")

        return {
            "model": prop_id,
            "name": affordance.name,
            "position": placed_pos,
            "angles": placed_ang,
            "scale": final_scale,
            "color": final_color,
            "render_fx": render_fx,
            "mutations": mutations
        }

if __name__ == "__main__":
    resolver = AffordanceResolver()
    desk_pos = [0.0, 0.0, 0.0]
    desk_dims = [64.0, 36.0, 30.0]

    print("=== SPATIAL AFFORDANCE & ANOMALY RESOLVER TEST ===")
    
    # Test normal TV placement on desk
    tv_normal = resolver.place_prop_with_affordance("models/props_c17/tv_monitor01.mdl", desk_pos, desk_dims, confusion=0.0)
    print(f"\n1. Normal TV on Desk:\n  Pos: {tv_normal['position']} | Scale: {tv_normal['scale']} | Color: {tv_normal['color']}")

    # Test high confusion with rare mutations
    print("\n2. Degraded State Placements (TV, Radio, Chair):")
    for prop in ["models/props_c17/tv_monitor01.mdl", "models/props_lab/reciever01a.mdl", "models/props_c17/FurnitureChair001a.mdl"]:
        res = resolver.place_prop_with_affordance(prop, desk_pos, desk_dims, confusion=0.85)
        print(f"\n  Prop: {res['name']}")
        print(f"  Pos:   {res['position']}")
        print(f"  Scale: {res['scale']} | Color: {res['color']} | RenderFX: {res['render_fx']}")
        for m in res["mutations"]:
            print(f"    * {m}")
