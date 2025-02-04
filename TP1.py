# Python program to read image using OpenCV
 
# importing OpenCV(cv2) module and numpy
import cv2 as cv
import numpy as np
import math as m
 
#path = "./Images/coco.bmp"
path = "./Images/aquitaine.bmp"

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

def flip(img):
    Nx = img.shape[0]
    Ny = img.shape[1]
    
    rotated_img = np.copy(img)
    
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, round(Nx/2)): # in range 0 to Nx-1
            rotated_img[x,y] = img[Nx-x-1,y]
    
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            img[x,y] = rotated_img[x,y]

def rotate(img, shift):
#img shape returns a tuple with The number of rows, columns and the channels if any.
    Nx = img.shape[0]
    Ny = img.shape[1]

    rotated_img = np.copy(img)
    cv.line(rotated_img, (0,0), (Nx-1, Ny-1), (0,0), 1000)#black out the image

    rad = m.radians(shift)

    Cy = Ny/2 
    Cx = Nx/2 #center point of image has coordinates (Cx, Cy)

    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            xr = round((x - Cx)*m.cos(rad)-(y - Cy)*m.sin(rad) + Cx)
            yr = round((x - Cx)*m.sin(rad) + (y - Cy)*m.cos(rad) + Cy)
            if((0 <= xr < Nx) & (0 <= yr < Ny)):
                rotated_img[x,y] = img[xr, yr]
                
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            img[x,y] = rotated_img[x,y]
            
def rotatePolar(img, shift):
    Nx = img.shape[0]
    Ny = img.shape[1]

    rotated_img = np.copy(img)
    cv.line(rotated_img, (0,0), (Nx-1, Ny-1), (0,0), 1000)#black out the image

    rad = m.radians(shift)
    
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            r = m.sqrt(x*x + y*y)
            if (x != 0): alpha = m.atan(y/x)
            else: alpha =m.pi/2
            R = r
            beta = alpha + rad
            X = m.trunc(R*m.cos(beta))
            Y = m.trunc(R*m.sin(beta))
            if((0<=X<Nx) & (0<= Y < Ny)): rotated_img[x,y] = img[X,Y]
            
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            img[x,y] = rotated_img[x,y]
        
def zoomPolar(img, coeff):
    Nx = img.shape[0]
    Ny = img.shape[1]

    zoomed_img = np.copy(img)
    cv.line(zoomed_img, (0,0), (Nx-1, Ny-1), (0,0), 1000)#black out the image
    
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            r = m.sqrt(x*x + y*y)
            if (x != 0): alpha = m.atan(y/x)
            else: alpha =m.pi/2
            if (coeff >0):R = r/coeff
            else: R = r/-coeff
            beta = alpha
            X = m.trunc(R*m.cos(beta))
            Y = m.trunc(R*m.sin(beta))
            if((0<=X<Nx) & (0<= Y < Ny)): zoomed_img[x,y] = img[X,Y]
            
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            img[x,y] = zoomed_img[x,y]
            
def zoomCart(img, coeff):
    Nx = img.shape[0]
    Ny = img.shape[1]

    zoomed_img = np.copy(img)
    cv.line(zoomed_img, (0,0), (Nx-1, Ny-1), (0,0), 1000)#black out the image
    
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            X = round(x/coeff)
            Y = round(y/coeff)
            if((0<=X<Nx) & (0<= Y < Ny)): zoomed_img[x,y] = img[X,Y]
            
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            img[x,y] = zoomed_img[x,y]
            
def RecadDyn(img):
    Nx = img.shape[0]
    Ny = img.shape[1]
    L  = img.shape[2]
    
    Recad_img = np.copy(img)
    cv.line(Recad_img, (0,0), (Nx-1, Ny-1), (0,0), 1000)#black out the image
    
    mini = np.amin(img)
    maxi = np.amax(img)
    
    delta = 255/(maxi-mini)
    
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            for l in range(0, L):  # in range 0 to L-1
                Recad_img[x,y] = m.trunc((img[x,y,l]-mini)*delta)
            
    for y in range(0, Ny):  # in range 0 to Ny-1
        for x in range(0, Nx): # in range 0 to Nx-1
            img[x,y] = Recad_img[x,y]
            

#rotate(i, 22)
#flip(i)
#rotatePolar(i, 10)
#zoomPolar(i, 0.5)
#zoomCart(i, 0.7)
RecadDyn(i)

cv.imshow('image', i)
cv.waitKey(0)
cv.destroyAllWindows()