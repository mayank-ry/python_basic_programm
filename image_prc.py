#image enhancement/processing
#flipping the image

"""from PIL import Image
img = Image.open("img_clg.jpeg")

#(img stored in form of metrices) ,transposing for flipping of image
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#convertion into a real image (flipped)
transposed_img.save('flipped_img.png')
print("Success")"""

#image enhancement : histogram equalisation technique (clahe)
import cv2
img = cv2.imread("img_clg.jpeg")

#preparation for CLAHE
clahe = cv2.createCLAHE()
#converting into grey scale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
enhanced_img = clahe.apply(gray_img)
print("Chal Chal Chal")
#save it to a file
cv2.imwrite('Chal.png',enhanced_img)
print("Chal Chal Chal")



