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
def conversiontableauimage(Itab):  # fonction de conversion d'un tableau 2D numpy en image PIL
    size = np.shape(Itab)  # tuple size (Ny Nx)
    Nx = size[1]  # Nx = cols, Ny = rows
    Ny = size[0]  # Nx = cols, Ny = rows
    mode = 'L'  # mode image 256 niveaux de gris (8 bits par pixel)
    Sizetuple = (Nx,Ny)  # ecriture de size renverse en tuple (Nx Ny)
    I = Image.new(mode,Sizetuple)  # PIL : reservation memoire image traitee avec la meme taille que l'image initiale
    for y in range(Ny):
        for x in range(Nx):
            s = int(Itab[y][x])
            I.putpixel((x,y),s)  # PIL : putpixel requiert un param scalaire s
    return I
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
def Nagao(I):  # fonction lissage de Nagao
    Itab = np.array(I)  # conversion image I en tableau numpy Itab
    J = Image.new(I.mode,I.size)  # PIL : reservation memoire image traitee avec la meme taille que l'image initiale
    Nx,Ny = I.size  # Nx = cols, Ny = rows
    Jtab = np.zeros((Ny,Nx))  # reservation memoire tableau 2D image
    Tmp = np.zeros(9)  # vecteur de longueur 9
    Moy = np.zeros(9)  # vecteur de longueur 9
    Var = np.zeros(9)  # vecteur de longueur 9
    for y in range(2,Ny-2):
        for x in range(2,Nx-2):
            for j in range(3):
                for i in range(3):
                    for m in range(3):
                        for k in range(3):
                            Tmp[3*m + k] = Itab[y+j+m-2][x+i+k-2]
                    if (i*j != 1):
                        Moy[3*j + i] = Tmp.mean()
                    else:
                        Moy[3*j + i] = 0
                    if (i*j != 1):
                        Var[3*j + i] = max(Tmp) - min(Tmp)
                    else:
                        Var[3*j + i] = 255
            Mini = min(Var)
            for i in range(9):
                if (Var[i] == Mini):
                    Jtab[y-2][x-2] = np.uint8(Moy[i])
    J = conversiontableauimage(Jtab)
    return J
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
file = "./hand2.jpg"  # image 256 niveaux de gris (8 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
J = Nagao(I)  # fonction perso
I.show()  # PIL : affichage image initiale (a traiter)
J.show()  # PIL : affichage image traitee
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
# ---------------------------------------------------------------------------- #

