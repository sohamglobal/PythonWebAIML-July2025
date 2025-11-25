# pip install opencv-python

import numpy as np
from PIL import Image
import cv2  # for drawing the circle (optional but easier)

# Flag dimensions
height = 300
width = 450

# Create blank RGB image
img = np.zeros((height, width, 3), dtype=np.uint8)

# Colors (BGR format for CV2)
saffron = (0, 153, 255)
white   = (255, 255, 255)
green   = (0, 128, 0)
blue    = (255, 0, 0)

# Stripe heights
stripe = height // 3

# Fill stripes
img[0:stripe, :, :] = saffron
img[stripe:2*stripe, :, :] = white
img[2*stripe:3*stripe, :, :] = green

# Draw the Ashoka Chakra (center)
center = (width // 2, stripe + stripe // 2)
radius = stripe // 3

cv2.circle(img, center, radius, blue, 3)  # outline circle

# Convert and save
image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
image.save("indian_flag.png")

print("Indian flag saved as indian_flag.png")
