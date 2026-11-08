"""
Audio Eeriness & Weight Scoring System.
Allows assigning priority weights to audio files so quintessential tracks
(like 'Still Life') have top selection frequency, while adding an optional
eeriness score (1.0 to 10.0) that biases selection based on the room's decay.
"""

from typing import Dict, List, Optional
import json
import os
import re

# Custom curated weights and eeriness scores
# Weight: relative probability multiplier (1.0 = standard, 5.0+ = top priority)
# Eeriness: 1.0 (subtle/melodic) to 10.0 (nightmarish/terrifying)
AUDIO_CURATED_WEIGHTS: Dict[str, Dict] = {
    # The Crown Jewel of Backrooms OST
    "still life": {
        "weight": 10.0,  # Highest weighted soundtrack in the system
        "eeriness": 9.2,
        "notes": "Iconic liminal dread, haunting drone and melancholic nostalgia"
    },
    "tunnel vision": {
        "weight": 5.0,
        "eeriness": 7.5,
        "notes": "Claustrophobic echoing synth"
    },
    "allcircuitbusy": {
        "weight": 6.5,
        "eeriness": 8.0,
        "notes": "Sterile telephony intercept"
    },
    "uvb76": {
        "weight": 5.5,
        "eeriness": 8.8,
        "notes": "Relentless shortwave buzzer"
    },
    "swedish rhapsody": {
        "weight": 6.0,
        "eeriness": 9.5,
        "notes": "Music box numbers station"
    }
}

class AudioWeightScorer:
    @staticmethod
    def evaluate_audio_weight(filename_or_title: str) -> Dict:
        """
        Calculates the sampling weight and eeriness score for an audio track.
        Matches against curated titles or calculates heuristically.
        """
        clean = filename_or_title.lower()
        
        # 1. Exact or Substring match against curated list
        for key, config in AUDIO_CURATED_WEIGHTS.items():
            if key in clean:
                return {
                    "weight": config["weight"],
                    "eeriness": config["eeriness"],
                    "priority_tag": "highest_priority" if config["weight"] >= 8.0 else "high_priority",
                    "reason": config["notes"]
                }

        # 2. Heuristic evaluation for unknown tracks
        base_weight = 1.0
        base_eeriness = 5.0
        tags = []

        # Acoustic indicators of liminal dread
        if any(w in clean for w in ["drone", "hum", "dark", "hallway", "liminal", "ambient", "static"]):
            base_weight += 1.5
            base_eeriness += 2.0
            tags.append("ambient_dread")

        if any(w in clean for w in ["distorted", "glitch", "whisper", "warning", "alarm"]):
            base_weight += 2.0
            base_eeriness += 3.0
            tags.append("acute_horror")

        if any(w in clean for w in ["phonk", "yodell", "caramell", "troll"]):
            # Meme or upbeat tracks get lower weight in serious Backrooms generation
            base_weight = 0.4
            base_eeriness = 2.0
            tags.append("unfitting_anomaly")

        return {
            "weight": round(base_weight, 2),
            "eeriness": min(10.0, round(base_eeriness, 2)),
            "priority_tag": "standard",
            "tags": tags
        }

if __name__ == "__main__":
    test_files = [
        "Backrooms (Original Score), Vol. 3 - Still Life.mp3",
        "Backrooms - Tunnel Vision.mp3",
        "uvb76_the_buzzer_shortwave_radio.mp3",
        "allcircuitbusy.mp3",
        "Caramell.mp3"
    ]
    print("=== TESTING AUDIO WEIGHT & EERINESS SCORER ===")
    for f in test_files:
        res = AudioWeightScorer.evaluate_audio_weight(f)
        print(f"\nTrack: {f}")
        print(f"  -> Weight:   {res['weight']} (Sampling multiplier)")
        print(f"  -> Eeriness: {res['eeriness']}/10.0")
        print(f"  -> Priority: {res['priority_tag']}")
