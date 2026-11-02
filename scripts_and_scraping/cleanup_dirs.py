import os
import shutil

# Remove any directory in public that looks like a file name
for root, dirs, files in os.walk('public', topdown=False):
    for d in dirs:
        if any(d.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.avif', '.mp4', '.gif', '.svg']):
            dirpath = os.path.join(root, d)
            print(f"Removing invalid directory: {dirpath}")
            shutil.rmtree(dirpath)

print("Cleaned up invalid directories.")

