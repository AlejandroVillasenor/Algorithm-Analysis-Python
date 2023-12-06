""" 
    Gaussian filter
"""
import cv2 as cv
import numpy as np

originalImg=cv.imread('vr46.jpg')
grayImg=cv.imread('vr46.jpg',0)
cv.imshow('original image',originalImg)
cv.imshow('gray image',grayImg)

#Image dimensions
print(np.shape(originalImg))
print(np.shape(grayImg))
rows,columns,channels=np.shape(originalImg)

#-----Gaussian filter-----
filterImg=np.zeros((rows,columns),dtype='uint8')

#Gaussian kernel 3x3
kernel =[[1,2,1],
         [2,4,2],
         [1,2,1]]

#Gaussian filter
for row in range(1,rows-1):
    for column in range(1,columns-1):
        sum = 0
        for i in range(3):
            for j in range(3):
                sum = sum + grayImg[row-1+i,column-1+j]*kernel[i][j]
        filterImg[row,column]=sum/16
cv.imshow('Gaussian filter',filterImg)
cv.waitKey()
cv.destroyAllWindows()







