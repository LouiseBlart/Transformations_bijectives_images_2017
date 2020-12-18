# Transformations bijectives d'images (2017)
Louise Blart

Projet réalisé dans le cadre du cours "Algorithme et programmation 1" en première année de licence MASS (Université de Lille). Le but de ce projet est de manipuler des images avec le module Pillow de python.

Le fichier Projet_transformations_bijectives_dimages contient l'ensemble des fonctions créées pour ce pojet : 
- symetries (verticale, horizontale, centrale) : Ces fonctions créent une symétrie en fonction de l'axe vertical, horizontal ou central,
- défilements ( horizontal, vertical) : Ces fonctions permettent la modification de l'image en faisant défiler les pixels selon le sens souhaité,
- transformation du boulanger : Fonction basée sur la préparation d'une pate feuilletée que l'on applique à une image (étirement, demi-tour, pliage),
- transformation du photomaton : transformation d'une image en 4 exemplaires plus petits,
- transformation concentrique : cette fonction permet de concevoir une image comme succession de rectangles emboités,
- transformation boustropheon : deplacement des pixels vers la droite pour une ligne sur deux,
- fonction générique : 


Afin de finaliser le programme, nous avons réalisé une fonction générique qui prend en paramètres
une image et une transformation. Ensuite la fonction demande combien de fois il faut réaliser la
transformation. Cette fonction permet de rassembler l'ensemble des transformations en une
fonction.
Une deuxième fonction générique a été créée afin de ne pas réaliser tous les cycles si le nombre de
transformations demandées est supérieur à la période d'une transformation. Par exemple, si on veut
faire la transformation du boulanger 20 fois, il est inutile de transformer l'image 20 fois puisqu’au
bout de 17fois l'image revient à l'image de départ. On peut donc réaliser la transformation
seulement 3 fois.
Afin de trouver l'image mystère nous avons fait une fonction qui réalise les transformations subies
par l'image en sens inverse et grâce à la période de chaque fonction. L'image mystère a subi en
dernier 765765764675587676 transformations concentriques. On reproduit donc encore
26053891885774754174467201174650602109797382045171331015555396393029514649890676
4615494789307343736657843824
(2605389188577475417446720117465060210979738204517133101555539639302951464989067
64615494790073109501333431500- 765765764675587676) afin de boucler le cycle. On revient
donc à l'image avant la dernière transformation concentrique. On reproduit cette méthode pour
chacune des transformations. On a obtenu une fois une image à fond bleu avec des rayures de
différentes nuances de bleu mais nous n’avons jamais réussi à obtenir une nouvelle fois cette image.
Nous n’avons pas compris pourquoi.
Pour conclure, ce projet a été intéressant et enrichissant. Il nous a permis de consolider nos
connaissances sur le langage Python et de les mettre en pratique.
Nous avons trouvé beaucoup d’intérêt à faire ce travail, à chercher les solutions d’algorithmes, à
voir la progression du projet...
Et malgré le grand nombre d’heures passées sur ce projet, nous avons apprécié cette recherche.
