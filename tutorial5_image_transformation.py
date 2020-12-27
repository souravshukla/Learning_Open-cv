import cv2 as cv
import numpy as np

img = cv.imread('Images/a.jpg')

cv.imshow('3098', img)

#translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -X--> left
# -y--> up
#  x--> right
#  y--> down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# rotation
def rotate(img,angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D( rotPoint, angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat, dimensions)

rotated = rotate(img,45)
cv.imshow('Rotated', rotated)

# resize

resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Flipping
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

# crop
cropped = img[: , 40:50]
cv.imshow('cropped', cropped)

cv.waitKey(0)