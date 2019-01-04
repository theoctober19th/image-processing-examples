import cv2
import math

lena = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
dup = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
(IMG_LENGTH, IMG_HEIGHT) = lena.shape

print(lena)

#show image in the window
cv2.imshow('Original Image', lena)
#wait for a key press
cv2.waitKey(0)

val = 1
while val < 10:
    for i in range(IMG_LENGTH):
        for j in range(IMG_HEIGHT):
            dup[i][j] = int(val*math.log10(1 + float(lena[i][j])/255)*255)

    cv2.imshow('Transformed image ' + str(val), dup)
    cv2.waitKey(0)
    val = val + 0.5