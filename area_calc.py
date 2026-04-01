import numpy as np
from PIL import Image
height = 4
width = 5
arr = np.zeros([height,width,3],dtype=np.uint8)
img = Image.fromarray(arr)
img.save("test.png")
arr1 = np.zeros([100,200,3],dtype=np.uint8)
arr1[:,:100]=[110,128,0]  #orange color
arr1[:,100:] = [115,0,255] # blue color
img = Image.fromarray(arr1)
img.save("test2.png")