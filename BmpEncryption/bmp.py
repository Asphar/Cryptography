import numpy as np
from PIL import Image

# Open images
im1 = Image.open("encryptedtext1.bmp")
im2 = Image.open("encryptedtext2.bmp")

# Make into Numpy arrays
im1np = np.array(im1)
im2np = np.array(im2)

# XOR with Numpy
result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

# Convert back to PIL image and save
Image.fromarray(result).save('result.png')