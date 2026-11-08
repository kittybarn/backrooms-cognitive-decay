import vpk, os

vpks = [
    r'J:\SteamLibrary\steamapps\common\GarrysMod\sourceengine\hl2_misc_dir.vpk',
    r'J:\SteamLibrary\steamapps\common\GarrysMod\sourceengine\content_hl2_dir.vpk',
    r'J:\SteamLibrary\steamapps\common\GarrysMod\sourceengine\content_cstrike_dir.vpk',
    r'J:\SteamLibrary\steamapps\common\GarrysMod\garrysmod\garrysmod_dir.vpk'
]

categories = {
    'wallpaper': [],
    'carpet': [],
    'ceiling': [],
    'tile': [],
    'plaster_walls': [],
    'concrete': [],
    'office': []
}

for v in vpks:
    try:
        pak = vpk.open(v)
        for f in pak:
            if not f.endswith('.vmt'): continue
            low = f.lower()
            if 'models/' in low: continue  # Looking for brush/world materials for walls & floors
            
            clean = f.replace('materials/', '').replace('.vmt', '')
            
            if 'wallpaper' in low:
                categories['wallpaper'].append(clean)
            if 'carpet' in low:
                categories['carpet'].append(clean)
            if 'ceiling' in low:
                categories['ceiling'].append(clean)
            if 'tile' in low and ('floor' in low or 'wall' in low or 'ceiling' in low):
                categories['tile'].append(clean)
            if 'plaster' in low and ('wall' in low or 'yellow' in low):
                categories['plaster_walls'].append(clean)
            if 'concrete' in low and ('floor' in low or 'wall' in low):
                categories['concrete'].append(clean)
            if 'office' in low:
                categories['office'].append(clean)
    except Exception as e:
        print(f"Error opening {v}: {e}")

output_summary = {}
for cat, lst in categories.items():
    uniq = sorted(list(set(lst)))
    output_summary[cat] = uniq
    print(f"=== {cat.upper()} ({len(uniq)}) ===")
    for item in uniq[:10]:
        print(f'  "{item}",')

import json
with open('curated_backrooms_materials.json', 'w') as out:
    json.dump(output_summary, out, indent=2)
print("Saved curated materials to curated_backrooms_materials.json")
