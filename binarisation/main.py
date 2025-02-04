# main : programme principal utilisant librairies image publiques & perso

from PIL import Image  # librairie image PIL/Pillow (install par shell cmd : py -m pip install Pillow) (ou : python -m pip install Pillow)
import PIL.ImageOps  # librairie image PIL/Pillow

from numpy import *  # librairie numpy de tableaux (install par shell cmd : py -m pip install numpy)
import numpy as np  # librairie numpy de tableaux (install par shell cmd : py -m pip install numpy)

from math import *  # librairie maths

from scipy import signal  # librairie scipy de signal (install par shell cmd : py -m pip install scipy)
from scipy import misc
import matplotlib.pyplot as plt  # librairie matplotlib de maths (install par shell cmd : py -m pip install matplotlib)

from functionlib import *  # module perso fonctions functionlib.py dans le meme repertoire

""" partie a mettre en commentaire """

# ---------------------------------------------------------------------------- #
# binarisation d'image 256 niveaux de gris (8 bits par pixel) par fonction perso de functionlib.py
file = "coco.bmp"  # image 256 niveaux de gris (8 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
# Nx,Ny = I.size  # Nx = cols, Ny = rows
Itab = conversionimagetableau(I)  # tableau 2D Itab à partir de l'image I d'entrée
seuil = 150
Jtab = binarisation(Itab, seuil)  # fonction perso de functionlib.py : binarisation d'image 256 niveaux gris (8 bits par pixel)
J = conversiontableauimage(Jtab)  # image J de sortie à partir du tableau 2D Jtab
K = stack(I,J)  # fonction perso de functionlib.py : empilement de 2 images
# I.show()  # PIL : affichage image initiale (a traiter)
# J.show()  # PIL : affichage image traitee
K.show()  # PIL : affichage images initiale/traitee empilees
J.save('binar.jpg')  # PIL : enregistrement image traitee
K.save('coco+binar.jpg')  # PIL : enregistrement images initiale/traitee empilees
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
K.close()  # PIL : fermeture images initiale/traitee empilees
# ---------------------------------------------------------------------------- #

