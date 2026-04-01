import numpy as np
from PIL import Image

img = Image.open('rose.jpg')
pixelMap = img.load()

img2 = Image.new("L", img.size)   # grayscale lena padega
pixelNew = img2.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):

        r, g, b = pixelMap[i, j]
        gray = (r + g + b) // 3   # convert to intensity

        if 0 <= gray <= 31:
            pixelNew[i,j] = 40
        elif 32 <= gray <= 63:
            pixelNew[i,j] = 70
        elif 64 <= gray <= 95:
            pixelNew[i,j] = 102
        elif 96 <= gray <= 127:
            pixelNew[i,j] = 130
        elif 128 <= gray <= 159:
            pixelNew[i,j] = 162
        elif 160 <= gray <= 191:
            pixelNew[i,j] = 195
        elif 192 <= gray <= 223:
            pixelNew[i,j] = 227
        elif 224 <= gray <= 255:
            pixelNew[i,j] = 255

img2.save('compressed.png')  