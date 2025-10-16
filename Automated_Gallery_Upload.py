"""
Sunbury Charters - Gallery Image Updater
This script helps you easily add new images to your gallery.html file

SETUP: Just put this script in the same folder as gallery.html
It will automatically find everything - works on ANY computer!
"""

import os
import shutil
from tkinter import Tk, filedialog

# ============================================
# CONFIGURATION - Automatic!
# ============================================

# Get the folder where THIS script is located
# This means you just put the script in your website folder and it works!
WEBSITE_FOLDER = os.path.dirname(os.path.abspath(__file__))

# The path to your gallery.html file
GALLERY_HTML = os.path.join(WEBSITE_FOLDER, "gallery.html")

# The folder where images should be stored
IMAGES_FOLDER = os.path.join(WEBSITE_FOLDER, "Images", "Gallery")

# ============================================
# MAIN SCRIPT - Don't need to edit below
# ============================================

def select_images():
    """Opens a file dialog to let you select images"""
    print("Opening file picker...")
    
    # Create a hidden Tkinter window
    root = Tk()
    root.withdraw()  # Hide the main window
    root.attributes('-topmost', True)  # Bring dialog to front
    
    # Open file picker - you can select multiple images
    file_paths = filedialog.askopenfilenames(
        title="Select images to add to gallery",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.gif *.webp"),
            ("All files", "*.*")
        ]
    )
    
    root.destroy()
    return file_paths


def copy_images_to_gallery(image_paths):
    """Copies selected images to the Images/Gallery folder"""
    
    # Create the Images/Gallery folder if it doesn't exist
    if not os.path.exists(IMAGES_FOLDER):
        os.makedirs(IMAGES_FOLDER)
        print(f"Created folder: {IMAGES_FOLDER}")
    
    copied_images = []
    
    for image_path in image_paths:
        # Get just the filename (like "fish.jpg")
        filename = os.path.basename(image_path)
        
        # Where the image will be copied to
        destination = os.path.join(IMAGES_FOLDER, filename)
        
        # Check if image already exists
        if os.path.exists(destination):
            print(f"⚠️  Skipped (already exists): {filename}")
            continue
        
        # Copy the image
        shutil.copy2(image_path, destination)
        print(f"✓ Copied: {filename}")
        copied_images.append(filename)
    
    return copied_images


def update_gallery_html(new_images):
    """Updates the gallery.html file with new image tags"""
    
    if not new_images:
        print("\nNo new images to add to HTML.")
        return
    
    # Read the current HTML file
    with open(GALLERY_HTML, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Find where to insert the new images (right after <div class="photo-grid">)
    insert_marker = '<div class="photo-grid">'
    
    if insert_marker not in html_content:
        print("ERROR: Couldn't find the photo-grid div in gallery.html")
        return
    
    # Create the new image tags
    new_img_tags = []
    for image_name in new_images:
        # Create the image tag in the same format as your existing ones
        img_tag = f'      <img src="/Images/Gallery/{image_name}" alt="">'
        new_img_tags.append(img_tag)
    
    # Join them with newlines
    new_images_html = '\n' + '\n'.join(new_img_tags)
    
    # Insert the new images right after the opening div tag
    insertion_point = html_content.find(insert_marker) + len(insert_marker)
    updated_html = (
        html_content[:insertion_point] + 
        new_images_html + 
        html_content[insertion_point:]
    )
    
    # Write the updated HTML back to the file
    with open(GALLERY_HTML, 'w', encoding='utf-8') as file:
        file.write(updated_html)
    
    print(f"\n✓ Added {len(new_images)} image(s) to gallery.html")


def main():
    """Main function that runs everything"""
    
    print("=" * 50)
    print("Sunbury Charters - Gallery Updater")
    print("=" * 50)
    print(f"Working in folder: {WEBSITE_FOLDER}")
    print()
    
    # Check if gallery.html exists
    if not os.path.exists(GALLERY_HTML):
        print(f"ERROR: gallery.html not found in this folder!")
        print(f"Make sure this script is in the same folder as gallery.html")
        print(f"Current folder: {WEBSITE_FOLDER}")
        input("\nPress Enter to close...")
        return
    
    # Step 1: Let user select images
    print("Step 1: Select the images you want to add")
    selected_images = select_images()
    
    if not selected_images:
        print("No images selected. Exiting.")
        input("\nPress Enter to close...")
        return
    
    print(f"\nYou selected {len(selected_images)} image(s)")
    print()
    
    # Step 2: Copy images to the gallery folder
    print("Step 2: Copying images to Images/Gallery/")
    copied_images = copy_images_to_gallery(selected_images)
    
    # Step 3: Update the HTML file
    print("\nStep 3: Updating gallery.html")
    update_gallery_html(copied_images)
    
    print("\n" + "=" * 50)
    print("Done! Your gallery has been updated.")
    print("=" * 50)
    input("\nPress Enter to close...")


# Run the script
if __name__ == "__main__":
    main()