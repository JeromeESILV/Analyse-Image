# Python program to read image using OpenCV
 
# importing OpenCV(cv2) module and numpy
import cv2 as cv
import numpy as np
import math as m
 
#path = "./Images/coco.bmp"
path = "./Images/hand2.jpg"

# Save image in set directory
# Read RGB image
i = cv.imread(path)
 
# Output img with window name as 'image'
#cv.imshow('image', img)
 
# Maintain output window utill
# user presses a key
#cv.waitKey(0)       
 
# Destroying present windows on screen
#cv.destroyAllWindows()

def Nagao(img):
    Nx = img.shape[0]
    Ny = img.shape[1]
    
    Mean = [0]*Nx
    Variances = [0]*Ny
    tmp= [0]*Ny
    W = [[0]*Nx for i in range(Nx)]
    
    for y in range(2, Ny-3):
        for x in range(2, Nx-3):
            for j in range(3):
                for i in range(3):
                    for m in range(3):
                        for k in range(3):
                            tmp[(m*3)+k] = img[y+j+m-2][x+i+k-2]
                    if(i*j != 1 ):  Mean[(3*j)+i] = np.mean(tmp)
                    else:   Mean[(3*j)+i] = 0
                    
                    if(i*j != 1):   Variances[(3*j)+i] = np.max(tmp) - np.min(tmp)
                    else:   Variances[(3*j)+i] = 255
            Mini = min(Variances)
            for i in range(0, 9):
                if(Variances[i] == Mini):   W[y-2][x-2] = Mean[i]
    return W

def NormeGradient4Diff(img):
    Nx = img.shape[0]
    Ny = img.shape[1]
    
    d = [0]*4
    D = [0]*4
    NormGradient =[[0]*Nx for i in range(Nx)]
    
    for y in range(1, Ny-2):
        for x in range(1, Nx-2):
            d[0] = img[y,x]-img[y,x-1]
            d[1] = img[y-1,x]-img[y,x-1]
            d[2] = img[y-1,x]-img[y,x]
            d[3] = img[y-1,x-1]-img[y,x]
            
            for i in range(3):
                D = abs(d[i])
            NormGradient[y][x] = np.max(D)
    return NormGradient

cv.imshow('image', i)
cv.waitKey(0)
cv.destroyAllWindows()



NormeGradient4Diff(i)

cv.imshow('image', i)
cv.waitKey(0)
cv.destroyAllWindows()