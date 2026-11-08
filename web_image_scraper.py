"""
Robust Web Liminal Image Scraper using DDGS.
Searches DuckDuckGo Images across tailored Backrooms & Liminal queries:
- 'The Backrooms level 0 yellow wallpaper'
- 'empty corporate hallway liminal space'
- 'monochromatic damp carpet fluorescent lights'
- 'abandoned office cubicles liminal'
- 'underground concrete utility basement'
- 'creepy liminal hotel corridor'

Downloads at least 100 high-res reference photos directly into:
J:\\backrooms_gmod_training_dump\\images
"""

import os
import re
import time
import urllib.request
from duckduckgo_search import DDGS

TARGET_DIR = r"J:\backrooms_gmod_training_dump\images"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

QUERIES = [
    "The Backrooms level 0 yellow wallpaper empty",
    "liminal space empty office corridor",
    "monochromatic yellow wallpaper damp carpet",
    "abandoned corporate office cubicles liminal",
    "creepy empty hotel hallway carpet",
    "underground brutalist concrete basement utility room",
    "sterile hospital corridor empty at night liminal",
    "subway transit corridor empty liminal space"
]

def scrape_backrooms_photos(target_total: int = 110):
    os.makedirs(TARGET_DIR, exist_ok=True)
    existing_files = os.listdir(TARGET_DIR)
    downloaded_count = len([f for f in existing_files if f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))])
    
    print(f"📷 Target: {target_total} photos. Currently have {downloaded_count} in dump.")
    
    seen_urls = set()
    per_query = max(15, (target_total - downloaded_count) // len(QUERIES) + 5)

    with DDGS() as ddgs:
        for q in QUERIES:
            if downloaded_count >= target_total:
                break

            print(f"\n🔍 Searching for: '{q}'...")
            try:
                results = list(ddgs.images(q, max_results=per_query))
                print(f"  -> Found {len(results)} images.")

                for item in results:
                    if downloaded_count >= target_total:
                        break

                    img_url = item.get("image")
                    if not img_url or img_url in seen_urls:
                        continue
                    seen_urls.add(img_url)

                    # Determine extension
                    ext = "jpg"
                    if ".png" in img_url.lower():
                        ext = "png"
                    elif ".webp" in img_url.lower():
                        ext = "webp"

                    clean_title = re.sub(r'[^\w\-_]', '_', item.get("title", "backrooms"))[:45]
                    filename = f"img_{downloaded_count+1:03d}_{clean_title}.{ext}"
                    filepath = os.path.join(TARGET_DIR, filename)

                    try:
                        req = urllib.request.Request(img_url, headers=HEADERS)
                        with urllib.request.urlopen(req, timeout=8) as resp, open(filepath, "wb") as f:
                            f.write(resp.read())
                        
                        # Verify file is not tiny or corrupt
                        if os.path.getsize(filepath) > 8000:
                            downloaded_count += 1
                            print(f"  [{downloaded_count}/{target_total}] Saved: {filename}")
                        else:
                            os.remove(filepath)
                    except Exception:
                        pass
                    
                    time.sleep(0.08)

            except Exception as e:
                print(f"  ⚠️ Error searching query '{q}': {e}")

    print(f"\n🎉 Finished! Total images now in dump: {downloaded_count}")

if __name__ == "__main__":
    scrape_backrooms_photos(target_total=110)
