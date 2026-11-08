"""
Dedicated Backrooms Canon & Level Image Harvester.
Connects directly to the Backrooms MediaWiki repository (Wikia/Fandom API)
and downloads 100+ authentic, canonical Level photos:
- Level 0 (Lobby), Level 1 (Habitable Zone), Level 2 (Pipe Dreams),
  Level 3 (Electrical Station), Level 4 (Abandoned Office),
  Level 5 (Terror Hotel), Level 6 (Lights Out), etc.

Saves directly into J:\\backrooms_gmod_training_dump\\images.
"""

import os
import re
import urllib.request
import json
import time

TARGET_DIR = r"J:\backrooms_gmod_training_dump\images"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BackroomsCollector/2.0'}

def harvest_backrooms_wiki_images(target_count: int = 110):
    os.makedirs(TARGET_DIR, exist_ok=True)
    existing_files = os.listdir(TARGET_DIR)
    downloaded = len([f for f in existing_files if f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))])

    print(f"📷 Starting canonical Backrooms Level image scrape (target: {target_count})...")
    print(f"   Currently have {downloaded} in dump.")

    api_url = "https://backrooms.fandom.com/api.php?action=query&list=allimages&aiprefix=Level&ailimit=150&format=json"

    try:
        req = urllib.request.Request(api_url, headers=HEADERS)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            images = data.get('query', {}).get('allimages', [])

            print(f"🔍 Found {len(images)} official Level images in database.")

            for img in images:
                if downloaded >= target_count:
                    break

                raw_url = img.get('url')
                name = img.get('name', 'backrooms_level')
                mime = img.get('mime', '')

                if not raw_url or 'gif' in mime:
                    continue

                clean_name = re.sub(r'[^\w\-_.]', '_', name)
                out_path = os.path.join(TARGET_DIR, f"{downloaded+1:03d}_{clean_name}")

                try:
                    img_req = urllib.request.Request(raw_url, headers=HEADERS)
                    with urllib.request.urlopen(img_req, timeout=12) as img_resp, open(out_path, 'wb') as f:
                        f.write(img_resp.read())

                    if os.path.getsize(out_path) > 5000:
                        downloaded += 1
                        print(f"  [{downloaded}/{target_count}] Downloaded: {clean_name}")
                    else:
                        os.remove(out_path)

                    time.sleep(0.1) # Polite pause
                except Exception as err:
                    print(f"  ⚠️ Error downloading {clean_name}: {err}")

    except Exception as e:
        print(f"API Error: {e}")

    print(f"\n🎉 Harvest Complete! Total Backrooms images in dump: {downloaded}")
    print(f"   Directory: {TARGET_DIR}")

if __name__ == "__main__":
    harvest_backrooms_wiki_images(target_count=110)
