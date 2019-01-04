import cv2
import tkinter
import math
import numpy as np

IMAGE_STANDARD = None
IMAGE_NORMALIZED = None

top = tkinter.Tk('Image Processing Lab')

def showOriginalImage():
    showImage('Original Image', IMAGE_STANDARD)

def showDigitalNegative():
    neg_img = digitalNegative(IMAGE_STANDARD)
    showImage('Original Image', IMAGE_STANDARD)
    showImage('Digital Negative', neg_img)

def showLogTransformedImage():
    showImage('Original Image', IMAGE_STANDARD)
    for i in range(1,6):
        log_trans_img = logTransform(i*0.5)
        showImage('Log Transformation (c = ' + str(i*0.5) + ')', log_trans_img)

def showGammaTransformedImage():
    showImage('Original Image', IMAGE_STANDARD)
    for i in range(1, 6):
        gamma = 0.001*10**i
        gamma_trans_img = gammaTransform(1, gamma)
        showImage('Gamma Transformation (c = 1, Gamma = ' + str(gamma) + ')', gamma_trans_img)

def bitPlaneSlicing():
    showImage('Original Image', IMAGE_STANDARD)
    x,y = IMAGE_STANDARD.shape
    for i in range(8):
        showImage('Bit Plane ' + str(i), slice(IMAGE_STANDARD, i))


def slice(image, bit):
    a = image.copy()
    x, y = image.shape
    for i in range(x):
        for j in range(y):
            a[i][j] = 2**bit if (image[i][j]>=2**bit) else 0
    return a

def prepareGUI():

    showOriginalImageBtn = tkinter.Button(top, text = 'Show Original Image', command = showOriginalImage)
    showOriginalImageBtn.pack()
    showDigitalNegativeBtn = tkinter.Button(top, text = 'Digital Negative', command = showDigitalNegative)
    showDigitalNegativeBtn.pack()
    logTransformBtn = tkinter.Button(top, text = 'Logarithmic Transform', command = lambda : showLogTransformedImage())
    logTransformBtn.pack()
    bitPlaneSlicingBtn = tkinter.Button(top, text = 'Bit Plane Slicing', command = bitPlaneSlicing)
    bitPlaneSlicingBtn.pack()
    gammaTransformBtn = tkinter.Button(top, text = 'Gamma Transformation', command = showGammaTransformedImage)
    gammaTransformBtn.pack()
    top.mainloop()



def prepareImage():
    global IMAGE_STANDARD;
    IMAGE_STANDARD= cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
    global IMAGE_NORMALIZED;
    IMAGE_NORMALIZED = [[x/255 for x in row]for row in IMAGE_STANDARD]

def showImage(title, image):
    cv2.imshow(title, image)

def digitalNegative(image):
    a = image.copy()
    x, y = image.shape
    for i in range(x):
        for j in range(y):
            a[i][j] = 255 - image[i][j]

    return a

def logTransform(multiplier):
    a = IMAGE_STANDARD.copy()
    x, y = IMAGE_STANDARD.shape

    for i in range(x):
        for j in range(y):
            a[i][j] = int( multiplier * math.log10(1 + IMAGE_NORMALIZED[i][j]) * 255 )
            if a[i][j] > 255:
                a[i][j] = 255

    return a

def gammaTransform(c, gamma):
    a = IMAGE_STANDARD.copy()
    x, y = IMAGE_STANDARD.shape

    for i in range(x):
        for j in range(y):
            a[i][j] = int( (c * IMAGE_NORMALIZED[i][j] ** gamma ) * 255)
            if a[i][j] > 255:
                a[i][j] = 255

    return a

if __name__ == '__main__':
    prepareImage()
    prepareGUI()