from PIL import Image

# Load the uploaded image
image_path = "./plots/THIS.png"
image = Image.open(image_path)

# Convert the image to SVG format
svg_path = "THIS.svg"
image.save(svg_path, format="SVG")
