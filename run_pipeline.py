"""
Full pipeline demonstration: Generates 5 rooms of decaying machine thought
and outputs the StarfallEx Lua chip ready to copy into Garry's Mod.
"""

from token_registry import TokenRegistry
from context_brain import ContextDecayBrain
from starfall_exporter import StarfallLuaExporter

def main():
    reg = TokenRegistry()
    reg.load_from_json('seed_tokens.json')
    brain = ContextDecayBrain(reg, context_window_size=4, decay_rate=0.2)

    generated_rooms = []
    print("🧠 Simulating Machine Cognition & Context Loss...")
    for i in range(1, 6):
        room = brain.generate_room(i)
        generated_rooms.append(room)
        print(f" -> Room {i} generated with confusion {room['confusion_level']}")

    lua_code = StarfallLuaExporter.export_room_sequence_chip(generated_rooms)
    with open("decayed_backrooms.lua", "w") as f:
        f.write(lua_code)

    print("\n✅ Successfully compiled StarfallEx chip to: decayed_backrooms.lua")

if __name__ == "__main__":
    main()
