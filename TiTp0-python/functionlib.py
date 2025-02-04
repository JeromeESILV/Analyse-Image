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
def nega256(I):  # fonction negatif d'image 256 niveaux de gris (8 bits par pixel)
    J = Image.new(I.mode,I.size)  # PIL : reservation memoire image traitee avec la meme taille que l'image initiale
    Nx,Ny = I.size  # Nx = cols, Ny = rows
    for y in range(Ny):  # range de 0 a Ny-1
        for x in range(Nx):  # range de 0 a Nx-1
            p = I.getpixel((x,y))  # PIL : lecture du niveau de gris du pixel de coordonnees x,y
            c = 255 - p  # complement a 255 : blanc devient noir , noir devient blanc
            J.putpixel((x,y),c)  # PIL : ecriture du niveau de gris du pixel de coordonnees x,y
    p00 = I.getpixel((0,0))
    c00 = 255 - p00
    print("Nx(cols)=",Nx,"Ny(rows)=",Ny,"p00=",p00,"c00=",c00)
    # print("I.size=",I.size)
    # print("I.mode=",I.mode)
    return J
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
def negaRGB(I):  # fonction negatif d'image couleur RGB (24 bits par pixel)
    J = Image.new(I.mode,I.size)  # PIL : reservation memoire image traitee avec la meme taille que l'image initiale
    Nx,Ny = I.size  # PIL : Nx = cols, Ny = rows
    C = np.array([0, 0, 0])  # vecteur de longueur 3    #  np.array([0, 0, 0]) equivalent a : np.zeros(3)
    C00 = np.zeros(3)  # vecteur de longueur 3    #  np.array([0, 0, 0]) equivalent a : np.zeros(3)
    for y in range(Ny):  # range de 0 a Ny-1
        for x in range(Nx):  # range de 0 a Ny-1
            # r,g,b = I.getpixel((x,y))  # PIL : lecture des 3 niveaux r,g,b du pixel de coordonnees x,y
            P = I.getpixel((x,y))  # PIL : lecture du vecteur des 3 niveaux r=P[0],g=P[1],b=P[2] du pixel de coordonnees x,y
            C[0] = 255 - P[0]  # complement a 255 : rouge clair devient rouge fonce , rouge fonce devient rouge clair
            C[1] = 255 - P[1]  # complement a 255 : vert clair devient vert fonce , vert fonce devient vert clair
            C[2] = 255 - P[2]  # complement a 255 : bleu clair devient bleu fonce , bleu fonce devient bleu clair
            J.putpixel((x,y),tuple(C))  # PIL : ecriture des 3 niveaux [r,g,b] du vecteur C converti en tuple de constantes (r,g,b)
            # J.putpixel((x,y),(C[0],C[1],C[2]))  # PIL : ecriture des 3 niveaux [r,g,b] du vecteur C converti en tuple de constantes (r,g,b)
    P00 = I.getpixel((0,0))
    C00[0] = 255 - P00[0]
    C00[1] = 255 - P00[1]
    C00[2] = 255 - P00[2]
    print("Nx(cols)=",Nx,"Ny(rows)=",Ny,"(P00)=",P00,"[C00]=",C00,"(C00)=",tuple(C00))
    # print("Nx(cols)=",Nx,"Ny(rows)=",Ny,"P00[0]=",P00[0],"C00[0]=",C00[0],"P00[1]=",P00[1],"C00[1]=",C00[1],"P00[2]=",P00[2],"C00[2]=",C00[2])
    # print("I.size=",I.size)
    # print("I.mode=",I.mode)
    return J
# ---------------------------------------------------------------------------- #

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

