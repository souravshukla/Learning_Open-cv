import cv2 as cv
import numpy as np

img = cv.imread('Images/3098.jpg')
#cv.imshow('3098',img)

blank = np.zeros(img.shape, dtype = 'uint8')
#cv.imshow('BLank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Graay', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blUR', blur)

# canny = cv.Canny(img, 125, 125)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255,  cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f' {len(contours)} contours(s) found! ')

cv.drawContours(blank, contours, -1, (0,255,0), 2)
cv.imshow('COntours drawn', blank )

cv.waitKey(0)