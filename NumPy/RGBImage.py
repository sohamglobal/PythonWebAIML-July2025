import numpy as np
from PIL import Image

# 100x100 RGB image
img = np.zeros((100, 100, 3), dtype=np.uint8)

img[:, :, 0] = 255   # Red channel full
img[:, :, 1] = np.linspace(0, 255, 100)  # Green gradient
img[:, :, 2] = 50    # Blue constant

image = Image.fromarray(img)
image.save("color_image.png")
