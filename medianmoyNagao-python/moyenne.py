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
def moyenne3(I):  # fonction convolution d'image avec un masque moyenneur 3x3
    Itab = np.array(I)  # conversion image I en tableau numpy Itab
    mask = np.array([[ 1./9., 1./9., 1./9.],
                     [1./9., 1./9., 1./9.],
                     [ 1./9., 1./9., 1./9.]])
    Jtab = signal.convolve2d(Itab, mask)
    J = conversiontableauimage(Jtab)
    return J
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
file = "boat256x256-8bpp.bmp"  # image 256 niveaux de gris (8 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
J = moyenne3(I)  # fonction perso
I.show()  # PIL : affichage image initiale (a traiter)
J.show()  # PIL : affichage image traitee
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
# ---------------------------------------------------------------------------- #

