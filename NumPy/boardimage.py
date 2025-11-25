import numpy as np
from PIL import Image

# Image size
size = 400
num_squares = 8  # 8x8 like chessboard

# Create empty image
img = np.zeros((size, size), dtype=np.uint8)

square_size = size // num_squares

for i in range(num_squares):
    for j in range(num_squares):
        if (i + j) % 2 == 0:
            img[i*square_size:(i+1)*square_size, j*square_size:(j+1)*square_size] = 255  # white

image = Image.fromarray(img)
image.save("checkerboard.png")

print("Checkerboard saved as checkerboard.png")
