from PIL import Image

# Get the dimensions of a single image
img = Image.open("0001.jpg")
width, height = img.size

# Calculate the number of rows and columns needed to fit all images
cols = 30
rows = 24

# Calculate the size of the final image, while making sure it's no bigger than 5000 pixels in either direction
final_width = min(cols * width, 10000)
final_height = min(rows * height, 10000)

# Create a blank image with the calculated size
merged_image = Image.new('RGB', (final_width, final_height))

# Iterate through all images and add them to the grid
for i in range(1, 721):
    # Open the image
    img = Image.open("{:04d}.jpg".format(i))

    # Calculate the x and y coordinates of the current image
    x = ((i-1) % cols) * (final_width//cols)
    y = ((i-1) // cols) * (final_height//rows)

    # Paste the image onto the merged image
    merged_image.paste(img, (x, y))

# Save the merged image
merged_image.save("merged_image.jpg")
