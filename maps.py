from PIL import Image
img = Image.open('test2.png')
rgb_im = img.convert('RGB')
r,g,b = rgb_im.getpixel((150,1)) #rgb value of particular pixel area
print(r,g,b)
