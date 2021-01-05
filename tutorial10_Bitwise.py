import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = 'uint8')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200),200,255,-1)

cv.imshow('rect', rect)
cv.imshow('circle', circle)

# bitwise_and = cv.bitwise_and(rect, circle)
# bitwise_or = cv.bitwise_or(rect,circle)

# xor = cv.bitwise_xor(rect,circle)
b_not = cv.bitwise_not(rect)

# cv.imshow('And', bitwise_and)
# cv.imshow('or', bitwise_or)
#cv.imshow('Xor', xor)
cv.imshow('NOT', b_not)
cv.waitKey(0)