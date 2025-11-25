import numpy as np
from PIL import Image

# 200x200 random noise image
noise = np.random.randint(0, 256, (200, 200), dtype=np.uint8)

image = Image.fromarray(noise)
image.save("noise.png")

print("Noise image saved as noise.png")
