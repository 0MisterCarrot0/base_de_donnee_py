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

def csv_vers_liste(file):
    with open(file, "r", newline="") as fichier:
        lecteur = csv.reader(fichier, delimiter=";")
        data = list(lecteur)
    return data

def rechercher():
    num_table=int(input("Veuillez choisir la table dans laquelle vous voulez rechercher : "))
    
    # Détermine le type de chemin du fichier
    if platform.system() in ["Darwin", "Linux"]:
        file_path = f"./stockage_table/table_{num_table}.csv"
    elif platform.system() == "Windows":
        file_path = f".\\stockage_table\\table_{num_table}.csv"
        
    # Test si la table existe
    if not(os.path.exists(file_path)):
        raise IndexError
    
    # Affiche la première ligne de la table
    header=[]
    with open(file_path, "r", newline="") as fichier:
        lecture=csv.reader(fichier, delimiter=";")
        header=next(lecture)
    for i in range(len(header)):
        print(f"|| {header[i]}", end=" ")
    print("")
    
    # Recherche la colonne
    attribut=input("Choisissez dans quel attribut vous voulez rechercher (marquez le '(int)' si il y est) : ")
    place=-1
    for i in range(len(header)):
        if header[i]==attribut:
            place=i
    colonne=[]
    if place==-1:
        raise ValueError
    else:
        colonne=extraire_colonne(file_path, place)
    print(colonne)
    
    # Recherche l'élément dans la colonne
    if len(colonne[0])>4 and colonne[0][-5:]=="(int)":
        a_chercher=int(input("Quelle valeur recherchez-vous : "))
    else:
        a_chercher=input("Que recherchez-vous : ")
    lieu=[]
    for i in range(len(colonne)):
        if colonne[i]==str(a_chercher):
            lieu.append(i)
    
    # Affichage des lignes correspondantes
    if lieu==[]:
        raise Exception
    else:
        for i in range(len(header)):
            print(f"|| {header[i]}", end=" ")
        print("")
        L=csv_vers_liste(file_path)
        for i in lieu:
            for j in range(len(L[i])):
                print(f"| {L[i][j]}", end=" ")
            print("|")