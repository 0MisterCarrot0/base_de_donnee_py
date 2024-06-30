import os
import platform
import csv

def affichage_table():
    num_table=int(input("Veuillez choisir la table à afficher : "))
    
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
    largeur_case=15
    with open(file_path, "r", newline="") as fichier:
        lecture=csv.reader(fichier, delimiter=";")
        header=next(lecture)
    # Affichage de TABLE {num_table} en haut de la table
    largeur_table=largeur_case*len(header)+len(header)+1
    texte=f"TABLE {num_table}"
    align=f"^{largeur_table}"
    print(f"{texte:{align}}")
    # Design de la table
    for i in range(len(header)):
        print("+", end="")
        print("="*largeur_case, end="")
    print("+")
    
    # Affichage des entités de la table
    with open(file_path, "r", newline="") as fichier:
        lecteur=csv.reader(fichier, delimiter=";")
        for ligne in lecteur:
            for i in range(len(ligne)):
                print(f"|{ligne[i][:largeur_case+1]:<15}", end="")
            print("|")
            if ligne[0]=="CLE":
                for j in range(len(ligne)):
                    print("+", end="")
                    print("="*largeur_case, end="")
                print("+")
            else:
                print("-"*largeur_table)