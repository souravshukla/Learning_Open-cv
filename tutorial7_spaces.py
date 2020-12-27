import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/3098.jpg')
cv.imshow('3098', img)

plt.imshow(img)
plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)




cv.waitKey(0)