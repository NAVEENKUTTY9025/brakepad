import os
import shutil
import glob
import re

brain_dir = r"C:\Users\navee\.gemini\antigravity\brain\f1b4d26b-9e17-4642-a757-abf4ed8d3078"
proj_dir = r"e:\GROWW projects\ROTAR"
images_dir = os.path.join(proj_dir, "images")

# Copy the images
image_files = glob.glob(os.path.join(brain_dir, "brake_*.png"))
for img_path in image_files:
    basename = os.path.basename(img_path)
    # Remove the timestamp from filename for cleaner names
    clean_name = re.sub(r'_\d+\.png$', '.png', basename)
    dest_path = os.path.join(images_dir, clean_name)
    shutil.copy2(img_path, dest_path)
    print(f"Copied {img_path} to {dest_path}")

# Now replace the image src in all HTML files
html_files = glob.glob(os.path.join(proj_dir, "*.html"))

# Map contexts to new images
image_mapping = {
    "brake_mechanic.png": "brake_mechanic.png",
    "brake_pads.png": "brake_pads.png",
    "brake_rotor.png": "brake_rotor.png",
    "brake_van.png": "brake_van.png"
}

# Simple heuristic to replace images
def replace_images_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace specific unsplash images or all images with our new ones
    # We will just replace all image src tags with a random choice of our 4 new images,
    # or specifically map them if they have keywords.
    
    # Let's find all src="..." 
    # This is a bit brute force. We will do a regex.
    def replacer(match):
        src_val = match.group(2)
        alt_val = match.group(0).lower()
        
        # Decide which image to use based on context
        new_img = "images/brake_mechanic.png"
        if "pad" in alt_val:
            new_img = "images/brake_pads.png"
        elif "rotor" in alt_val:
            new_img = "images/brake_rotor.png"
        elif "van" in alt_val or "mobile" in alt_val:
            new_img = "images/brake_van.png"
            
        return match.group(1) + new_img + match.group(3)

    new_content = re.sub(r'(src=")([^"]+)(")', replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for html_file in html_files:
    replace_images_in_file(html_file)

print("Done")
