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
def median3(I):  # fonction median 3x3 avec fonction median() de numpy
    Itab = np.array(I)  # conversion image I en tableau numpy Itab
    J = Image.new(I.mode,I.size)  # PIL : reservation memoire image traitee avec la meme taille que l'image initiale
    Nx,Ny = I.size  # Nx = cols, Ny = rows
    v = np.zeros(9)  # vecteur de longueur 9
    for y in range(1,Ny-1):
        for x in range(1,Nx-1):
            for i in range(3):
                for j in range(3):
                    v[3*i + j] = Itab[y+i-1][x+j-1]
            s = int(np.median(v))
            J.putpixel((x,y),s)  # PIL : putpixel requiert un param scalaire s
    return J
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
file = "boat256x256-8bpp.bmp"  # image 256 niveaux de gris (8 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
J = median3(I)  # fonction perso
I.show()  # PIL : affichage image initiale (a traiter)
J.show()  # PIL : affichage image traitee
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
# ---------------------------------------------------------------------------- #
