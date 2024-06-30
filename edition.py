import os
import platform
import csv

def extraire_colonne(fichier, num_colonne):
    L=[]
    with open(fichier, "r") as fsrce:
        my_reader = csv.reader(fsrce, delimiter = ';')
        for ligne in my_reader:
            L.append(ligne[num_colonne])
    return L

def ajouter_entite():
    num_table=int(input("Veuillez choisir la table à incrementer : "))
    
    # Détermine le type de chemin du fichier
    if platform.system() in ["Darwin", "Linux"]:
        file_path = f"./stockage_table/table_{num_table}.csv"
    elif platform.system() == "Windows":
        file_path = f".\\stockage_table\\table_{num_table}.csv"
    
    # Test si la table existe
    if not(os.path.exists(file_path)):
        raise IndexError
    
    # Affiche les attributs de la table
    with open(file_path, "r", newline="") as fichier:
        lecture=csv.reader(fichier, delimiter=";")
        L=next(lecture)
    print("La table demandee est de la forme :\n|| ", end="")
    for i in range(len(L)):
        print(L[i], "",sep=" ", end="")
        print("|| ", end="")
        
    # Affiche les clées déjà existentes
    print("\nLes cles deja utilisees sont : ")
    cles=extraire_colonne(file_path,0)
    cles.pop(0)
    if len(cles)==0:
        cles.append("Aucune cle")
    elem_par_colonne=5
    for i in range(0, len(cles), elem_par_colonne):
        ligne=cles[i:i+elem_par_colonne]
        print(" ".join(map(str, ligne)))
    
    # Création de l'entité
    cle=int(input("Vous devez donner une cle differente des precedentes : "))
    if cle in cles:
        raise ValueError
    else:
        print("La cle est valide. Veuillez maintenant entrer les differents attributs : ")
    res=[cle]
    for i in range(1,len(L)):
        choix=input(L[i]+" : ")
        res.append(choix)
    with open(file_path, "a", newline="") as fichier:
        ecriture=csv.writer(fichier, delimiter=";")
        ecriture.writerow(res)

def supprimer_entite():
    num_table = int(input("Veuillez entrer le numero de la table dans laquelle vous voulez supprimer une entite : "))
    
    # Détermine le type de chemin du fichier
    if platform.system() in ["Darwin", "Linux"]:
        file_path = f"./stockage_table/table_{num_table}.csv"
    elif platform.system() == "Windows":
        file_path = f".\\stockage_table\\table_{num_table}.csv"
    
    # Vérification de l'existence de la table
    if not os.path.exists(file_path):
        raise IndexError("File does not exist")
    
    # Affichage de l'en-tête du fichier CSV
    with open(file_path, "r", newline="") as fichier:
        lecture = csv.reader(fichier, delimiter=";")
        L = next(lecture)
    print("La table est de la forme :\n|| ", end="")
    for i in range(len(L)):
        print(L[i], "", sep=" ", end="")
        print("|| ", end="")
    print("")
    
    # Affichage des clés
    print("Les clees existentes sont : ")
    cles = extraire_colonne(file_path, 0)
    cles.pop(0) # Retirer l'élément CLE de la colonne
    elem_par_colonne = 5
    for i in range(0, len(cles), elem_par_colonne):
        ligne = cles[i:i + elem_par_colonne]
        print(" ".join(map(str, ligne)))
    
    # Recherche de la ligne à partir de la clé
    cle_entite = input("Veuillez entrer la cle de l'entite a supprimer : ")
    if cle_entite not in cles:
        raise ValueError
    ligne = []
    nouv=[]
    with open(file_path, "r", newline="") as fichier:
        lecteur = csv.reader(fichier, delimiter=';')
        header = next(lecteur)
        for lignes in lecteur:
            if lignes[0] != cle_entite:
                nouv.append(lignes)
            else:
                ligne = lignes
    
    # Affichage de l'entite demandée
    print("| ", end="")
    for i in range(len(ligne)):
        print(ligne[i], end=" | ")
    print("")
    
    confirmation=input(f"Entrez 'oui' si vous voulez supprimer cette entite (cle {cle_entite}) de la table {num_table} : ")
    if confirmation=="oui":
        with open(file_path, "w", newline="") as fichier:
            lect = csv.writer(fichier, delimiter=";")
            lect.writerow(header)
            lect.writerows(nouv)
    else:
        raise Exception