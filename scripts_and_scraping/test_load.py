# Python script to build the 100% exact PupJourney.jsx
import os

with open('scripts_and_scraping/exact_poses.js', 'r', encoding='utf-8') as f:
    poses_js = f.read()

with open('scripts_and_scraping/exact_pup_class.js', 'r', encoding='utf-8') as f:
    class_js = f.read()

with open('scripts_and_scraping/exact_pup_journey_core.js', 'r', encoding='utf-8') as f:
    journey_js = f.read()

print('Loaded all scraped JS source files!')
print('Poses len:', len(poses_js))
print('Class len:', len(class_js))
print('Journey len:', len(journey_js))

