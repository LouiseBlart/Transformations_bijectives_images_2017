# Transformations bijectives d'images (2017)
Louise Blart

Projet réalisé dans le cadre du cours "Algorithmes et Programmation 1" (premier cours de python) en première année de licence MASS (Université de Lille). Le but de ce projet est de manipuler des images avec le module Pillow de python.

Le fichier Projet_transformations_bijectives_dimages contient l'ensemble des fonctions créées pour ce pojet : 
- symetries (verticale, horizontale, centrale) : Ces fonctions créent une symétrie en fonction de l'axe vertical, horizontal ou central,
- défilements ( horizontal, vertical) : Ces fonctions permettent la modification de l'image en faisant défiler les pixels selon le sens souhaité,
- transformation du boulanger : Fonction basée sur la préparation d'une pate feuilletée que l'on applique à une image (étirement, demi-tour, pliage),
- transformation du photomaton : transformation d'une image en 4 exemplaires plus petits,
- transformation concentrique : cette fonction permet de concevoir une image comme succession de rectangles emboités,
- transformation boustropheon : deplacement des pixels vers la droite pour une ligne sur deux,
- fonction générique : permet de générer l'ensemble des transformations précedemment sitées. 
- fonction générique ordre : deuxième fonction générique permettant de ne pas réaliser tous les cycles si le nombre de transformations demandées est supérieur à la période d'une transformation. ( optimisation de la première fonction générique)
- fonction 'retrouver_image' permettant de décoder une image mystère
