# -*- coding: utf-8 -*-
# Nom: Blart Louise L1 MASS

# Afin d'utiliser ce programme il faut que les différentes images utilisées soient dans le même dossier que ce document. De plus, afin de visualiser les différentes
# images il faut utiliser la fonction 'fonction_génératrice_tous_les_cycles' ou 'fonction_génératrice_ordre'. Elle utilisera alors les autres fonctions de transformation
from PIL import Image

def symetrie_horizontale (image,n=1):
    ''' Cette fonction permet, à partir d'une image, de créer la symétrie de cette image à partir de l'axe horizontal'''
    img= Image.open(image) # ouverture de l'image à traiter
    img2=Image.new(img.mode,img.size) # création d'une nouvelle image avec le meme mode et la même taille que la premiere
    colonne,ligne=img.size
    for i in range(n):
        for l in range (ligne) :
            for c in range(colonne):
                pixel= img.getpixel((c,l))# selectionner un pixel à la fois
                img2.putpixel((c,ligne-l-1),pixel) # implanter le pixel dans la meme colonne mais à la ligne opposée horizontalement de l'image initiale  
        img2.save('imagehorizontal.png')
        img=Image.open('imagehorizontal.png')
    return img

def symetrie_verticale(image,n=1):
    ''' Cette fonction permet, à partir d'une image, de créer la symétrie de cette image à partir de l'axe vertical'''
    img= Image.open(image) # ouverture de l'image à traiter
    img2=Image.new(img.mode,img.size) # création d'une nouvelle image avec le meme mode et la même taille que la premiere
    colonne,ligne=img.size
    for i in range(n):
        for l in range (ligne) :
            for c in range(colonne):
                pixel= img.getpixel((c,l))# selectionner un pixel à la fois
                img2.putpixel((colonne-c-1,l),pixel) # implanter le pixel dans la meme ligne mais à la colonne opposée verticalement de l'image initiale
        img2.save('imagevertical.png')
        img=Image.open('imagevertical.png')
    return img
                        
def symetrie_centrale(image, n=1):
    ''' Cette fonction permet, à partir d'une image, de créer la symétrie centrale de cette image, c'est à dire un 'demi-tour' de l'image '''
    img= Image.open(image) # ouverture de l'image à traiter
    img2=Image.new(img.mode,img.size) # création d'une nouvelle image avec le meme mode et la même taille que la premiere
    colonne,ligne=img.size
    for i in range(n):
        for l in range (ligne) :
            for c in range(colonne):
                pixel= img.getpixel((c,l))# selectionner un pixel a la fois
                img2.putpixel((colonne-c-1,ligne-l-1),pixel)
        img2.save('imagecentrale.png')
        img=Image.open('imagecentrale.png')
    return img


def défilement_horizontal (image,n):
    ''' Cette fonction permet de faire défiler n fois une image horizontalement'''
    img= Image.open(image) # ouverture de l'image à traiter
    img2=Image.new(img.mode,img.size) # création d'une nouvelle image avec le meme mode et la même taille que la premiere
    colonne,ligne=img.size
    for l in range (ligne) :
        for c in range(colonne):
            pixel= img.getpixel((c,l))# selectionner un pixel a la fois
            img2.putpixel(((c+n)%colonne,l),pixel)
    return img2
    

def défilement_vertical (image,n):
    ''' Cette fonction permet de faire défiler n fois une image verticalement'''
    img= Image.open(image) # ouverture de l'image à traiter
    img2=Image.new(img.mode,img.size) # création d'une nouvelle image avec le meme mode et la même taille que la premiere
    colonne,ligne=img.size
    for l in range (ligne) :
        for c in range(colonne):
            pixel= img.getpixel((c,l))# selectionner un pixel a la fois
            img2.putpixel((c,(l+n)%ligne),pixel)
    return img2

def transformation_du_boulanger(image,n):
    ''' 
    Cette fonction est basée sur le système qu'utilise un boulanger pour préparer sa pate feuilletée. On étire donc une image de dimension l*h pour avoir une
    nouvelle image de dimension 2l*h/2. On découpe ensuite cette nouvelle image pour obtenir deux images de dimension l*h/2. On fait un demi-tour avec l'image de droite
    grace à la fonction symetrie_centrale. Finalement, on rassemble verticalement les deux images obtenues 
    '''
    img=Image.open(image)
    colonne,ligne=img.size
    img2=Image.new(img.mode,(2*colonne,int(ligne/2)))
    img3=Image.new(img.mode,(colonne,int(ligne/2)))
    img3bis=Image.new(img.mode,(colonne,int(ligne/2)))
    img4=Image.new(img.mode,img.size)
    liste_paire=[]
    liste_impaire=[]
    liste=[]
    liste2=[]
    for i in range (n):
        for l in range(ligne):
            for c in range(colonne):
                if l%2==0:
                    liste_paire.append((c,l))# les pixels des lignes paires vont dans liste_paire
                if l%2!=0:
                    liste_impaire.append((c,l))# les pixels des lignes impaires vont dans liste-impaire
        for p in range(len(liste_paire)):
            liste.append(liste_paire[p])
            liste.append(liste_impaire[p])# la liste 'liste' prend en alternance un tuple de la liste liste_paire puis un de la liste liste_impaire
        for l in range(img2.size[1]):
            for c in range(img2.size[0]):
                liste2.append((c,l))# la liste liste2 est composée de tous les pixels d'une image dans l'ordre habituel 
        for e in range(len(liste2)):
            pixel=img.getpixel(liste[e]) # On prend chaque tuple de la liste 'liste' 
            img2.putpixel(liste2[e],pixel)# et on l'injecte à la position du tuple numéro e de la liste 'liste2'
        img2.save('imageboulanger.png')
        img=Image.open('imageboulanger.png')
        colonne2,ligne2=img.size
        for l in range(ligne2):
            for c in range (colonne2):
                pixel = img.getpixel((c,l))
                if c<colonne2/2:
                    img3.putpixel((c,l),pixel)# on divise l'image 'img' en 2: img3 est la partie de gauche de l'image 'img'
                else:
                    img3bis.putpixel((c-int(colonne2/2),l),pixel)# l'image img3bis est la partie de droite de l'image 'img'
        img3bis.save('image_avant_demitour.png')
        img3bis=(symetrie_centrale('image_avant_demitour.png'))#demi-tour de l'image de droite
        for l in range (ligne):
            for c in range(colonne):
                if l<ligne/2:
                    pixel = img3.getpixel((c,l))
                    img4.putpixel((c,l),pixel) # injection de l'image img3 sur la partie supérieure de l'image 4
                if l>=ligne/2:
                    pixel=img3bis.getpixel((c,l-int(ligne/2)))# injection de l'image img3.bis sur la partie inférieure de l'image 4
                    img4.putpixel((c,l),pixel)
        img4.save('imageboulanger.png')
        img=Image.open('imageboulanger.png') # L'image finale a une taille identique que l'image de départ 
    return img

def transformation_du_photomaton (image,n):
    '''Cette fonction permet de "reproduire" une image de dimensions l*h en 4 image de dimensions l/2 * h/2 et à les placer aux quatre coins de l'image'''
    img=Image.open(image)
    colonne,ligne=img.size
    img2=Image.new(img.mode,img.size)
    for i in range (n): # On reproduit les actions n fois afin d'obtenir 4^n "petites représentations"
        for l in range(ligne):
            for c in range(colonne):
                pixel=img.getpixel((c,l))
                if l%2==0: # On divise l'image en lignes paires et impaires puis en colonnes paires et impaires 
                    if c%2==0:# Les pixels de lignes et colonnes paires sont disposés en haut à gauche de l'image
                        img2.putpixel((int(c/2),int(l/2)),pixel)# on obtient alors une premiere partie de l'image de dimension l/2 * h/2
                    elif c%2!=0:# Les pixels de lignes paires et colonnes impaires sont disposés en haut à droite de l'image
                      img2.putpixel((int(colonne/2+(c/2)),int((l/2))),pixel)# on obtient alors une deuxième partie de l'image de dimension l/2 * h/2
                elif l%2!=0:
                    if c%2==0:# Les pixels de lignes impaires et colonnes paires sont disposés en bas à gauche de l'image
                        img2.putpixel((int(c/2),int(ligne/2+(l/2))),pixel)# on obtient alors une troisième partie de l'image de dimension l/2 * h/2
                    elif c%2!=0:# Les pixels de lignes et colonnes impaires sont disposés en bas à droite de l'image
                        img2.putpixel((int(colonne/2+(c/2)),int(ligne/2+(l/2))),pixel)# on obtient la dernière image de dimension l/2 * h/2
        img2.save('imagephotomaton.png') # On enregistre une nouvelle image afin d'itérer n fois la transformation 
        img=Image.open('imagephotomaton.png')
    return img


def transformation_concentrique(image,n):
    ''' Cette fonction permet de concevoir une image comme succession de rectangles emboités'''
    img=Image.open(image)
    colonne,ligne=img.size
    img2=Image.new(img.mode,img.size)
    liste = []# On commence par prendre une liste vide
    carré=0 #Ceci est le numéro du carré sur lequel on travail
    nbre_carrés= int(ligne/2)# Ceci correspond au nombre de carrés emboités dans une image
    while carré<nbre_carrés:# On répéte l'action tant qu'il y a des carrés emboités 
        for c in range(carré,colonne-carré):# On adapte la fonction en fonction des carrés.
            '''Par exemple pour le premier carré, on prend les pixels de 0 jusqu'a la derniere colonne
de l'image alors que pour le dixieme carré, on prend les pixels de 0 jusqu'a la dernière colonne -10'''
            liste.append((c,carré))# On injecte à la liste vide les coordonnées des pixels de la ligne du haut du carré
        for l in range(carré,ligne-carré):
            liste.append((c,l))# On injecte à la liste vide les coordonnées des pixels de la colonne de droite du carré
        for c in range (colonne-carré-1,carré,-1):
            liste.append((c,l))# On injecte à la liste vide les coordonnées des pixels de la ligne du bas du carré
        for l in range(colonne-carré-1,carré,-1):
            liste.append((c,l))# On injecte à la liste vide les coordonnées des pixels de la ligne de droite du carré
        # La liste est donc maintenant une liste de tuple des coordonnées du carré numméro 'carré'(varible en haut du programme)
        b=0
        for e in liste:#'e' est un tuple de coordonnés d'un pixel
            a=liste[(n+b)%(len(liste))]#'a' est le tuple de coordonnées que devra prendre le pixel de coordonnées 'e'
            pixel=img.getpixel(e)# on prend le pixel de coordonnée 'e'
            img2.putpixel((a),pixel)# et on l'injecte aux niveau des coordonnées de 'a'dans l'image 2
            b=b+1
        carré+=1# on refait la meme chose avec le carré suivant
    return img2



def transformation_boustrophédon ( image,n):
    ''' 
    Cette fonction permet, à partir d'une image, de déplacer les pixels d'une position vers la droite pour une ligne sur deux et d'une position vers la gauche
    pour les autres lignes. Pour les pixels en bout de ligne on les déplace vers la ligne du dessous sauf pour la dernière ligne pour laquelle on revient à la
    première ligne.
    Cette fonction calcule la transformation itérée n fois sans calculer toutes les images intermédiaires. Cette fonction est plus efficace que la fonction
    transformation_boustrophédon2
    '''
    img = Image.open(image)
    img2=Image.new(img.mode,img.size)
    colonne,ligne=img.size
    liste=[]
    for l in range (ligne) :
        for c in range (colonne):
            if l%2 == 0:
                liste.append((c,l)) # On ajoute à la liste les pixels d'une ligne paire suivi des pixels d'une ligne impaire partant de la dernière colonne à la première
            if l%2!=0:
                liste.append((colonne-1-c,l))
    b=0
    for e in liste :
        a=liste[(n+b)%(len(liste))]# 'a' correspond à la position que le pixel de coordonnées 'e' devra prendre
        pixel=img.getpixel(e)
        img2.putpixel(a,pixel)
        b=b+1
    return img2

def transformation_boustrophédon2 ( image,n):
    ''' 
    Cette fonction permet, à partir d'une image, de déplacer les pixels d'une position vers la droite pour une ligne sur deux et d'une position vers la gauche
    pour les autres lignes. Pour les pixels en bout de ligne on les déplace vers la ligne du dessous sauf pour la dernière ligne pour laquelle on revient à la
    première ligne.
    Cette fonction calcule la transformation itérée n fois en calculant toutes les images intermédiaires. Elle est assez longue pour un paramètre n élevé. Il est
    préférable d'utiliser la fonction transformation_boustrophédon.
    '''
    img = Image.open(image)
    img2=Image.new(img.mode,img.size)
    colonne,ligne=img.size
    for i in range (n):
        for l in range (ligne) :
            for c in range (colonne):
                pixel=img.getpixel((c,l))
                if l%2 == 0: # on sépare d'abord les lignes paires et impaires. Les lignes paires se déplaceront vers la droite
                    if c!= colonne-1:# Cas le plus géneral, le pixel ne se trouve pas en bout de ligne
                        img2.putpixel((c+1,l),pixel)# le pixel est déplacé vers la droite
                    if c==colonne-1 and l!=ligne-1:# Cas où le pixel se trouve en bout de ligne mais pas en bout de colonne
                        img2.putpixel((c,l+1),pixel)# le pixel est déplacé vers le bas
                    if c==colonne-1 and l==ligne-1:#Car particulier: le pixel se trouve en bout de ligne et en bout de colonne; c'est à dire le coin droit de l'image si la ligne est paire
                        img2.putpixel((c,0),pixel)  # le pixel est déplacé dans la même colonne mais à la premiere ligne 
                if l%2!=0:# les lignes impaires se déplaceront vers la gauche 
                    if c!=0:# Cas le plus géneral, le pixel ne se trouve pas en début de ligne
                        img2.putpixel((c-1,l),pixel)# le pixel est déplacé vers la gauche
                    if c==0 and l!=ligne-1:# Cas où le pixel se trouve en début de ligne mais pas en bout de colonne
                        img2.putpixel((c,l+1),pixel)# le pixel est déplacé vers le bas
                    if c==0 and l==ligne-1 :#Car particulier: le pixel se trouve en début de ligne et en bout de colonne; c'est à dire le coin gauche de l'image si la ligne est impaire
                        img2.putpixel((c,0),pixel)# le pixel est déplacé dans la même colonne mais à la premiere ligne 
        img2.save('imageb.png')
        img=Image.open('imageb.png')
    return img.show()

def fonction_générique_tous_les_cycles(img,T):
    ''' 
    Les différentes transformations T peuvent être:
        - la transformation du boulanger tapper transformation_du_boulanger
        - la transformation du photo-maton tapper transformation_du_photomaton
        - la symetrie horizontale ou verticale tapper symetrie_horizontale ou symetrie_verticale
        - la symetrie centrale tapper symetrie_centrale
        - le défilement horizontal ou vertical tapper défilement_horizontal ou défilement_vertical
        Cette fonction renvoie une nouvelle image résultant de la transofmation de img par T
        Elle calcule tous les cycles d'une permutation T
    '''
    try:
        n=input("combien de fois voulez-vous appliquer la transformation?")
        n=int(n)
        image=(T(img,n))
        return image
    except:
        print ("l'image ou la transformation n'est pas définie, vérifiez le nom de l'image et de la transformation, vérifier que l'image est bien dans le même dossier que ce document ")


def fonction_générique_ordre(img,T):
    ''' 
    Les différentes transformations T peuvent être:
        - la transformation du boulanger tapper transformation_du_boulanger
        - la transformation du photo-maton tapper transformation_du_photomaton
        - la symetrie horizontale ou verticale tapper symetrie_horizontale ou symetrie_verticale
        - la symetrie centrale tapper symetrie_centrale
        - le défilement horizontal ou vertical tapper défilement_horizontal ou défilement_vertical
   Cette fonction renvoie une nouvelle image résultant de la transofmation de img par T
   Elle calcule l'ordre d'une permutation T 
   '''
    try:
        if T ==symetrie_verticale or symetrie_horizontale or symetrie_centrale:
            periode=2
        if T ==transformation_du_boulanger:
            periode=17
        if T==transformation_du_photomaton:
            periode=8
        if T==transformation_boustrophédon:
            periode=65536
        if T == transformation_concentrique:
            periode=26000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        n=input("combien de fois voulez-vous appliquer la transformation?")
        n=int(n)
        n=n%periode
        n=int(n)
        image=(T(img,n))
        image.save('C:/Users/louis/OneDrive/Bureau/test.png')
        return image
    except:
        print ("l'image ou la transformation n'est pas définie, vérifiez le nom de l'image et de la transformation, vérifier que l'image est bien dans le même dossier que ce document ")


def retrouver_image ():
    '''
    Afin de retrouver l'image originale, on fait les différentes transformations de la dernière subit par l'image à la premiere.
    Chaque transformation a une période T au bout de laquelle elle redevient l'image initialte.
    Pour chaque transformation, on itére celle-ci par : n= T-le nombre de transformation subit par l'image
    '''
    img=(transformation_concentrique('imagemystere.png',(260538918857747541744672011746506021097973820451713310155553963930295146498906764615494790073109501333431500-765765764675587676)))
    img.save('imagemys.png')
    img=(transformation_du_photomaton('imagemys.png',(8-5)))
    img.save('imagemys.png')
    img=(transformation_concentrique('image mys.png',(260538918857747541744672011746506021097973820451713310155553963930295146498906764615494790073109501333431500-9868756755876)))
    img.save('imagemys.png')
    img=(transformation_boustrophédon('image mys.png',(65536-10000)))
    img.save('imagemys.png')
    img=(transformation_du_boulanger('image mys.png',(17-1)))
    # L'image mystere était donc à fond bleu, avec différentes rayures de différentes teintes de bleu sur le dessus. 
    return img.show()


