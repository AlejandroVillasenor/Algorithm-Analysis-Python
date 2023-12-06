"""
    Tarea 4. Sustitución  de color
"""
import cv2 as cv
import numpy as np  

#Create a VideoCapture object
cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()
    img=cv.imread('nervousSys.jpg')
    img=cv.resize(img,(frame.shape[1],frame.shape[0]))
    cv.imshow('Camera',frame)
    cv.imshow('Image',img)
    
    #Press q to quit
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
    #Color range blue
    minBGR = np.array([110, 0, 0])
    maxBGR = np.array([255, 105, 105]) 
    
    #Create mask
    maskBGR = cv.inRange(frame,minBGR,maxBGR)
    mask_inv = cv.bitwise_not(maskBGR)
    resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)
    result_inv = cv.bitwise_and(img, img, mask = maskBGR)

    #Show result
    total=cv.add(resultBGR,result_inv)
    cv.imshow('Resultado final',total)

#Release the camera
cam.release()
cv.destroyAllWindows()
