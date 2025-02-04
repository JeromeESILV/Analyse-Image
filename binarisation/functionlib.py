# functionlib : librairie (module) perso de fonctions de traitement d'image

from PIL import Image  # librairie image PIL/Pillow (install par shell cmd : py -m pip install Pillow) (ou : python -m pip install Pillow)
import PIL.ImageOps  # librairie image PIL/Pillow

from numpy import *  # librairie numpy de tableaux (install par shell cmd : py -m pip install numpy)
import numpy as np  # librairie numpy de tableaux (install par shell cmd : py -m pip install numpy)

from math import *  # librairie maths

from scipy import signal  # librairie scipy de signal (install par shell cmd : py -m pip install scipy)
from scipy import misc
import matplotlib.pyplot as plt  # librairie matplotlib de maths (install par shell cmd : py -m pip install matplotlib)

# ---------------------------------------------------------------------------- #
def stack(I,J):  # fonction empilement de 2 images I et J (horizontal) -> image K
    NxI = I.size[0]  # Nx = cols, Ny = rows
    NyI = I.size[1]  # Nx = cols, Ny = rows
    NxJ = J.size[0]  # Nx = cols, Ny = rows
    NyJ = J.size[1]  # Nx = cols, Ny = rows
    NxK = NxI + NxJ  # Nx = cols, Ny = rows
    NyK = NyI  # Nx = cols, Ny = rows
    K = Image.new(I.mode,(NxK,NyK))  # PIL : reservation memoire image stack
    for y in range(NyK):  # range de 0 a NyK-1
        for x in range(NxI):  # range de 0 a NxI-1
            K.putpixel((x,y),I.getpixel((x,y)))  # PIL : ecriture du niveau de gris du pixel de coordonnees x,y
        for x in range(NxI,NxK):  # range de NxI a NxK-1
            K.putpixel((x,y),J.getpixel((x-NxI,y)))  # PIL : ecriture du niveau de gris du pixel de coordonnees x,y
    return K
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
def conversionimagetableau(I):  # fonction de conversion d'image PIL en tableau 2D numpy
    Itab = np.array(I)  # conversion image I en tableau numpy Itab ; pour info : I = Image.fromarray(Itab)  # conversion tableau numpy Itab en image I
    # print("Itab[y=0][x=0]=",Itab[0][0],"Itab[y=0][x=1]=",Itab[0][1],"Itab[y=1][x=0]=",Itab[1][0],"Itab[y=1][x=1]=",Itab[1][1])
    # print("Itab=",Itab)
    return Itab
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
def conversiontableauimage(Itab):  # fonction de conversion d'un tableau 2D numpy en image PIL
    size = np.shape(Itab)  # tuple size (Ny Nx)
    Nx = size[1]  # Nx = cols, Ny = rows
    Ny = size[0]  # Nx = cols, Ny = rows
    mode = 'L'  # mode image 256 niveaux de gris (8 bits par pixel)
    Sizetuple = (Nx,Ny)  # ecriture de size renverse en tuple (Nx Ny)
    # print('size=',size,'Sizetuple=',Sizetuple,'Nx=',Nx,'Ny=',Ny)
    I = Image.new(mode,Sizetuple)  # PIL : reservation memoire image traitee avec la meme taille que l'image initiale
    for y in range(Ny):  #  range de 0 a Ny-1
        for x in range(Nx):  # range de 0 a Nx-1
            s =int(Itab[y][x])
            I.putpixel((x,y),s)  # PIL : putpixel requiert un param scalaire s (putpixel n'accepte pas un element de tableau Jtab[y][x])
    return I
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
def binarisation(Itab, seuil):  # fonction binarisation
    size = np.shape(Itab)  # tuple size (Ny Nx)
    Nx = size[1]  # Nx = cols, Ny = rows
    Ny = size[0]  # Nx = cols, Ny = rows
    Jtab = np.zeros((Ny,Nx))  # tableau 2D de zeros de la meme taille que Itab
    for y in range(Ny):  # range de 0 a Ny-1
        for x in range(Nx):  # range de 0 a Nx-1
            if Itab[y][x] < seuil :
                Jtab[y][x] = 0
            else :
                Jtab[y][x] = 255
    return Jtab
# ---------------------------------------------------------------------------- #
