#pip install numpy
#pip install pillow

import numpy as np
from PIL import Image

# Create a 100x100 grayscale gradient image
img = np.zeros((100, 100), dtype=np.uint8)

for i in range(100):
    for j in range(100):
        img[i, j] = i + j   # simple gradient effect

# Convert NumPy array to image and save
image = Image.fromarray(img)
image.save("gradient.png")

print("Image saved as gradient.png")
