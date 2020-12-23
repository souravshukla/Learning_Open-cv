import cv2 as cv

img = cv.imread('Images/buddha.jpg')
# cv.imshow('Buddha', img)
print(img.shape)

# 1. Converting to grayscale
# gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# 2. converting to blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# 3. Edge cascade
# canny = cv.Canny(img, 125,175 )
# cv.imshow('Canny Edges', canny)

# 4. Dilating the image
# dilated = cv.dilate(canny, (3,3), iterations = 3)
# cv.imshow('dilated', dilated)

# 5. Eroding the image
# erode  = cv.erode(dilated,(3,3), iterations = 1)
# cv.imshow('Erode', erode)

#resize
resized = cv.resize(img, (640, 500), interpolation = cv.INTER_AREA)
cv.imshow("Resized", resized)
# INTER_CUBIC INTER_LINEAR

#cropped
cropped = resized[:400, 200:470]
cv.imshow("Cropped", cropped)

cv.waitKey(0)