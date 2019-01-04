import numpy as np
import cv2

lena = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
dup = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
(IMG_LENGTH, IMG_HEIGHT) = lena.shape


def extractKBits(num, k, p):
    # convert number into binary first
    binary = bin(num)

    # remove first two characters
    binary = binary[2:]

    end = len(binary) - p
    start = end - k + 1

    # extract k  bit sub-string
    kBitSubStr = binary[start: end + 1]

    # convert extracted sub-string into decimal again
    return int(kBitSubStr, 2)

#show image in the window
cv2.imshow('Original Image', lena)

for i in range(IMG_HEIGHT):
    for j in range(IMG_LENGTH):
        dup[i][j] = extractKBits(lena[i][j], 8, 0)

#wait for a key press
cv2.waitKey(0)

cv2.imshow('7th bit plane', dup)
cv2.waitKey(0)



