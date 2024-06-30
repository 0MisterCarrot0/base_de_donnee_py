import os
import platform
import csv

def creation_table():
    num_table=int(input("Veuillez entrer le numéro de la nouvelle table : "))
    
    # Détermine le type de chemin du fichier
    if platform.system() in ["Darwin", "Linux"]:
        file_path=f"./stockage_table/table_{num_table}.csv"
    else:
        file_path=f".\\stockage_table\\table_{num_table}.csv"
    
    # Test d'existence du fichier
    if os.path.exists(file_path):
        raise IndexError(f"La table {num_table} existe déjà.")
    else:
        open(file_path, "w", newline='').close()
    
    # Création de la table
    nb_attribut=int(input("Veuillez entrer le nombre d'attributs de la table : "))
    L=["CLE"]
    for i in range(1,nb_attribut+1):
        choix=input("Veuillez rentrer le type du prochain attribut (str/int) : ")
        if choix=="str":
            L.append(input(f"Veuillez rentrez le nom de l'attribut {str(i)} : "))
        elif choix=="int":
            L.append(input(f"Veuillez rentrez le nom de l'attribut {str(i)} : ")+"(int)")
        else:
            os.remove(file_path)
            raise ValueError("Vous n'avez pas mis 'str' ou 'int'. La table n'a pas pu être créée, retour au menu")
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(L)

def suppression_table():
    num_table=int(input("Veuillez rentrer la table que vous voulez supprimer : "))
    
    # Détermine le type de chemin du fichier
    if platform.system() in ["Darwin", "Linux"]:
        file_path=f"./stockage_table/table_{num_table}.csv"
    else:
        file_path=f".\\stockage_table\\table_{num_table}.csv"
    
    # Suppression si table existe
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"La table {str(num_table)} a été supprimé. Retour au menu"
    else:
        raise IndexError(f"La table {str(num_table)} n'existe pas. Retour au menu")