import cv2 as cv
import numpy as np

img = cv.imread('Images/3098.jpg')
cv.imshow('3098', img)

# averaging
avg = cv.blur(img,(3,3))
cv.imshow("average", avg)

# Gaussian
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('GaussianBlur', gauss)

#Median
median = cv.medianBlur(img, 3)
cv.imshow('MedianBlur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15 )
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)