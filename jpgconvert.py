import os
from PIL import Image

# Set the input and output directories
input_dir = "images"
output_dir = "images/jpgs"

# Set the quality of the JPEGs (0-100, higher is better quality but larger file size)
quality = 75

# Set the size of the JPEGs as a percentage of the original size
size = 50  # 50% of the original size

# Loop through all the PNG files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        # Open the PNG file
        img = Image.open(os.path.join(input_dir, filename))
        # Resize the image to the desired percentage of the original size
        width, height = img.size
        img = img.resize((int(width * size / 100), int(height * size / 100)))
        # Convert the PNG to JPEG
        img = img.convert("RGB")
        # Save the JPEG to the output directory
        img.save(os.path.join(output_dir, filename.replace(".png", ".jpg")), "JPEG", quality=quality)
        # Close the image
        img.close()

print("Done!")
