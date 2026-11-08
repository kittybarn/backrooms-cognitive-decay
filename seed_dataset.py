"""
Seed dataset representing GMod/Source Engine models, textures, and structures across common Backrooms & Liminal biomes.
"""

from token_registry import TokenRegistry, EnvironmentToken

def build_default_dataset() -> TokenRegistry:
    registry = TokenRegistry()

    # --- OFFICE BIOME ---
    registry.register(EnvironmentToken(
        id="models/props_c17/FurnitureDesk001a.mdl",
        name="Office Desk",
        token_type="prop",
        biomes=["office", "classroom"],
        tags=["wood", "flat_surface", "work", "furniture", "floor_anchored", "horizontal"],
        anchor="floor",
        dimensions=[64.0, 36.0, 30.0],
        co_occurs_with=["models/props_c17/FurnitureChair001a.mdl", "models/props_lab/monitor02.mdl"]
    ))

    registry.register(EnvironmentToken(
        id="models/props_c17/FurnitureChair001a.mdl",
        name="Office Chair",
        token_type="prop",
        biomes=["office", "apartment", "classroom"],
        tags=["wood", "seating", "rest", "furniture", "floor_anchored", "small"],
        anchor="floor",
        dimensions=[24.0, 24.0, 36.0],
        co_occurs_with=["models/props_c17/FurnitureDesk001a.mdl"]
    ))

    registry.register(EnvironmentToken(
        id="models/props_lab/monitor02.mdl",
        name="CRT Computer Monitor",
        token_type="prop",
        biomes=["office", "lab"],
        tags=["electronic", "screen", "technology", "box", "small", "surface_mount"],
        anchor="floor",
        dimensions=[18.0, 18.0, 16.0],
        co_occurs_with=["models/props_c17/FurnitureDesk001a.mdl"]
    ))

    registry.register(EnvironmentToken(
        id="models/props_c17/filecabinet02.mdl",
        name="Filing Cabinet",
        token_type="prop",
        biomes=["office", "archive"],
        tags=["metal", "storage", "tall", "box", "furniture", "floor_anchored"],
        anchor="floor",
        dimensions=[24.0, 30.0, 54.0]
    ))

    # --- WAREHOUSE & INDUSTRIAL BIOME ---
    registry.register(EnvironmentToken(
        id="models/props_c17/oildrum001.mdl",
        name="Oil Drum",
        token_type="prop",
        biomes=["warehouse", "industrial", "basement"],
        tags=["metal", "cylinder", "storage", "industrial", "floor_anchored", "hazardous"],
        anchor="floor",
        dimensions=[24.0, 24.0, 36.0]
    ))

    registry.register(EnvironmentToken(
        id="models/props_wasteland/controlroom_desk001b.mdl",
        name="Control Terminal",
        token_type="prop",
        biomes=["industrial", "lab", "subway"],
        tags=["metal", "electronic", "flat_surface", "technology", "industrial", "floor_anchored"],
        anchor="floor",
        dimensions=[72.0, 36.0, 48.0]
    ))

    registry.register(EnvironmentToken(
        id="models/props_c17/substation_transformer01d.mdl",
        name="Substation Transformer",
        token_type="prop",
        biomes=["industrial", "utility"],
        tags=["metal", "electrical", "high_voltage", "box", "industrial", "tall", "floor_anchored"],
        anchor="floor",
        dimensions=[48.0, 48.0, 80.0]
    ))

    registry.register(EnvironmentToken(
        id="models/props_junk/wood_pallet001a.mdl",
        name="Wood Pallet",
        token_type="prop",
        biomes=["warehouse", "industrial"],
        tags=["wood", "flat_surface", "storage", "floor_anchored", "low"],
        anchor="floor",
        dimensions=[48.0, 48.0, 8.0]
    ))

    # --- HOSPITAL & MEDICAL BIOME ---
    registry.register(EnvironmentToken(
        id="models/props_interiors/Bed_Hospital.mdl",
        name="Hospital Bed",
        token_type="prop",
        biomes=["hospital", "asylum"],
        tags=["metal", "rest", "seating", "furniture", "medical", "floor_anchored", "horizontal"],
        anchor="floor",
        dimensions=[40.0, 80.0, 36.0]
    ))

    # --- STRUCTURAL & ARCHITECTURAL TOKENS ---
    registry.register(EnvironmentToken(
        id="materials/plaster/office_wallpaper_yellow",
        name="Yellow Mono Wallpaper",
        token_type="wall",
        biomes=["office", "hotel"],
        tags=["yellow", "paper", "indoor", "vertical", "wall_covering", "sterile"],
        anchor="wall",
        dimensions=[128.0, 16.0, 128.0]
    ))

    registry.register(EnvironmentToken(
        id="materials/concrete/warehouse_wall_c17",
        name="Raw Concrete Wall",
        token_type="wall",
        biomes=["warehouse", "basement", "industrial"],
        tags=["grey", "concrete", "brutal", "vertical", "wall_covering", "cold"],
        anchor="wall",
        dimensions=[128.0, 16.0, 128.0]
    ))

    registry.register(EnvironmentToken(
        id="materials/carpet/office_carpet_damp_01",
        name="Damp Commercial Carpet",
        token_type="floor",
        biomes=["office", "hotel"],
        tags=["fabric", "damp", "horizontal", "floor_covering", "brown", "beige"],
        anchor="floor",
        dimensions=[128.0, 128.0, 8.0]
    ))

    registry.register(EnvironmentToken(
        id="materials/concrete/floor_concrete01",
        name="Stained Concrete Floor",
        token_type="floor",
        biomes=["warehouse", "basement", "industrial"],
        tags=["stone", "concrete", "horizontal", "floor_covering", "grey", "cold"],
        anchor="floor",
        dimensions=[128.0, 128.0, 8.0]
    ))

    # --- LIGHTING FIXTURES ---
    registry.register(EnvironmentToken(
        id="models/props_c17/light_fluorescent01a.mdl",
        name="Fluorescent Ceiling Light Fixture",
        token_type="light",
        biomes=["office", "hospital", "warehouse"],
        tags=["light_source", "electronic", "ceiling_anchored", "humming", "white_light", "long"],
        anchor="ceiling",
        dimensions=[48.0, 12.0, 6.0]
    ))

    registry.register(EnvironmentToken(
        id="models/props_wasteland/light_caged01a.mdl",
        name="Industrial Caged Lamp",
        token_type="light",
        biomes=["industrial", "basement", "subway"],
        tags=["light_source", "metal", "caged", "yellow_light", "industrial", "ceiling_anchored"],
        anchor="ceiling",
        dimensions=[16.0, 16.0, 16.0]
    ))

    return registry

if __name__ == "__main__":
    reg = build_default_dataset()
    reg.save_to_json("seed_tokens.json")
    print(f"Created seed token dataset with {len(reg.tokens)} tokens across {len(reg.tag_index)} distinct tags.")
