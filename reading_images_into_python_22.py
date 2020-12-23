from skimage import io, img_as_float

# Here skimage is in RGB
img = io.imread("Images/Buddha.jpg")
print(img.shape)

'''img2 = img_as_float(img)
print(img2.shape)'''

import cv2

# opencv stores files in BGR 
img_cv2 = cv2.imread("Images/Buddha.jpg")

grey_img = cv2.imread("Buddha.jpg", 0)
color_img = cv2.imread("Buddha.jpg", 1)

img_cv_rgb = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

