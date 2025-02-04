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
# negatif d'image 256 niveaux de gris (8 bits par pixel) par fonction perso de functionlib.py
file = "boat256x256-8bpp.bmp"  # image 256 niveaux de gris (8 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
J = nega256(I)  # fonction perso de functionlib.py : negatif d'image 256 niveaux gris (8 bits par pixel)
K = stack(I,J)  # fonction perso de functionlib.py : empilement de 2 images
# I.show()  # PIL : affichage image initiale (a traiter)
# J.show()  # PIL : affichage image traitee
K.show()  # PIL : affichage images initiale/traitee empilees
K.save('result-nega256.jpg')  # PIL : enregistrement images initiale/traitee empilees
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
K.close()  # PIL : fermeture images initiale/traitee empilees
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# negatif d'image RGB (24 bits par pixel) par fonction perso de functionlib.py
file = "mandril200x290-24bpp.bmp"  # image couleur RGB (24 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
J = negaRGB(I)  # fonction perso de functionlib.py : negatif d'image RGB (24 bits par pixel)
K = stack(I,J)  # fonction perso de functionlib.py : empilement de 2 images
# I.show()  # PIL : affichage image initiale (a traiter)
# J.show()  # PIL : affichage image traitee
K.show()  # PIL : affichage images initiale/traitee empilees
K.save('result-negaRGB.jpg')  # PIL : enregistrement images initiale/traitee empilees
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
K.close()  # PIL : fermeture images initiale/traitee empilees
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# negatif d'image RGB (24 bits par pixel) par fonction de PIL/Pillow
file = "mandy256x246-24bpp.jpg"  # image couleur RGB (24 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
J = PIL.ImageOps.invert(I)  # PIL : negatif d'image couleur RGB (24 bits par pixel)
K = stack(I,J)  # fonction perso de functionlib.py : empilement de 2 images
# I.show()  # PIL : affichage image initiale (a traiter)
# J.show()  # PIL : affichage image traitee
K.show()  # PIL : affichage images initiale/traitee empilees
K.save('result-negaRGB-PIL.jpg')  # PIL : enregistrement images initiale/traitee empilees
I.close()  # PIL : fermeture de l'image initiale
J.close()  # PIL : fermeture de l'image traitee
K.close()  # PIL : fermeture images initiale/traitee empilees
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# conversion d'image PIL en tableau 2D numpy
file = "aquitaine.bmp"  # image 256 niveaux de gris (8 bits par pixel)
I = Image.open(file)  # PIL : ouverture fichier image dans le meme repertoire
Itab = conversionimagetableau(I)  # conversion d'image PIL en tableau 2D numpy
print("Itab[y=0][x=0]=",Itab[0][0],"Itab[y=0][x=1]=",Itab[0][1],"Itab[y=1][x=0]=",Itab[1][0],"Itab[y=1][x=1]=",Itab[1][1])
# I.show()  # PIL : affichage image initiale
I.close()  # PIL : fermeture de l'image initiale
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# conversion d'un tableau 2D numpy en image PIL : creation d'image 256 niveaux de gris (8 bits par pixel)
Nx = 256  # Nx = cols, Ny = rows
Ny = 200  # Nx = cols, Ny = rows
Itab = np.zeros((Ny,Nx))  # tableau 2D
for y in range(Ny):  # range de 0 a Ny-1
    for x in range(Nx):    # range de 0 a Nx-1
       Itab[y][x] = x  # mire
I = conversiontableauimage(Itab)  # conversion d'un tableau 2D numpy en image PIL
I.show()  # PIL : affichage image creee
I.save('result-mire.jpg')  # PIL : enregistrement images initiale/traitee empilees
I.close()  # PIL : fermeture de l'image creee
# ---------------------------------------------------------------------------- #

