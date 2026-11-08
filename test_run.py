from token_registry import TokenRegistry
from context_brain import ContextDecayBrain

reg = TokenRegistry()
reg.load_from_json('seed_tokens.json')
brain = ContextDecayBrain(reg, context_window_size=4, decay_rate=0.2)

for i in range(1, 6):
    room = brain.generate_room(i)
    confusion = room["confusion_level"]
    biome = room["biome_state"]
    print(f"=== ROOM {i} (Confusion: {confusion}, Biome: {biome}) ===")
    for elem in room['elements']:
        print(f"  [{elem['type']}] -> {elem['name']} ({elem['id']})")
    for log in room['logs']:
        if "NORMAL" not in log:
            print(f"    * COGNITIVE GLITCH: {log}")
    print()
