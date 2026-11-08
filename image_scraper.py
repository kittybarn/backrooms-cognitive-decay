"""
Liminal & Backrooms Stock Image Scraper.
Scrapes high-resolution, public-domain liminal space, empty room,
corridor, and basement photos directly into J:\\backrooms_gmod_training_dump\\images.
Targets 100+ clean interior reference photos.
"""

import os
import re
import urllib.request
import json
import time

TARGET_DIR = r"J:\backrooms_gmod_training_dump\images"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BackroomsCollector/1.0'}

CATEGORIES = [
    'Category:Liminal_spaces',
    'Category:Corridors',
    'Category:Empty_rooms',
    'Category:Basements',
    'Category:Abandoned_interiors',
    'Category:Office_interiors'
]

def scrape_liminal_photos(target_count: int = 120):
    os.makedirs(TARGET_DIR, exist_ok=True)
    downloaded = 0
    seen_urls = set()

    print(f"📷 Starting scrape for {target_count}+ Liminal & Backrooms interior photos...")

    for cat in CATEGORIES:
        if downloaded >= target_count:
            break

        print(f"\n📂 Fetching category: {cat}...")
        api_url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle={cat}&gcmlimit=50&gcmtype=file&prop=imageinfo&iiprop=url|mime&format=json"

        try:
            req = urllib.request.Request(api_url, headers=HEADERS)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})

                for pid, page in pages.items():
                    if downloaded >= target_count:
                        break

                    img_info = page.get('imageinfo', [{}])[0]
                    img_url = img_info.get('url')
                    mime = img_info.get('mime', '')

                    if not img_url or 'image' not in mime or 'svg' in mime:
                        continue
                    if img_url in seen_urls:
                        continue
                    seen_urls.add(img_url)

                    # Create a safe, descriptive filename
                    title = page.get('title', 'liminal_photo').replace('File:', '')
                    clean_name = re.sub(r'[^\w\-_.]', '_', title)[:80]
                    if not clean_name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                        clean_name += '.jpg'

                    out_path = os.path.join(TARGET_DIR, f"{downloaded+1:03d}_{clean_name}")

                    try:
                        img_req = urllib.request.Request(img_url, headers=HEADERS)
                        with urllib.request.urlopen(img_req, timeout=15) as img_resp, open(out_path, 'wb') as f:
                            f.write(img_resp.read())
                        downloaded += 1
                        print(f"  [{downloaded}/{target_count}] Downloaded: {clean_name}")
                        time.sleep(0.15) # Polite delay
                    except Exception as err:
                        print(f"  ⚠️ Failed downloading {clean_name}: {err}")

        except Exception as e:
            print(f"Error querying {cat}: {e}")

    print(f"\n🎉 Scrape Complete! Successfully saved {downloaded} high-quality liminal photos to:")
    print(f"   {TARGET_DIR}")

if __name__ == "__main__":
    scrape_liminal_photos(target_count=120)
