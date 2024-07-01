import os
import platform
import csv
import time

import crea_suppr_table
import edition
import affichage
import recherche

def clear():
    if platform.system()=="Darwin" or platform.system()=="Linux":
        os.system("clear")
    else:
        os.system("cls")

def main():
    clear()
    
    # Chemin du repertoire en fonction de l'OS + Création si rep n'existe pas
    if platform.system() in ["Darwin", "Linux"]:
        if not os.path.exists("./stockage_table"):
            os.mkdir("./stockage_table")
        repertoire="./stockage_table"
    else:
        if not os.path.exists(".\\stockage_table"):
            os.mkdir(".\\stockage_table")
        repertoire=".\\stockage_table"
    
    print("+==============================BASE DE DONNEES==============================+")
    print("|Bienvenue dans le gestionnaire de base de données, veuillez choisir parmi :|")
    print("|                                                                           |")
    print("| 1- Creation de table                                                      |")
    print("| 2- Suppression de table                                                   |")
    print("| 3- Edition de table                                                       |")
    print("| 4- Affichage de table                                                     |")
    print("| 5- Recherche                                                              |")
    print("| 6- Quitter                                                                |")
    print("+---------------------------------------------------------------------------+")
    choix=int(input("Quel est votre choix ? (1/2/3/4/5/6) : "))
    
    match choix:
        
        # Creation de table
        case 1:
            clear()
            print("Les tables existantes sont les tables : ", end="")
            if len(os.listdir(repertoire))!=0:
                for file in os.listdir(repertoire):
                    print(file[6])
            else:
                print("Aucune table")
            try:
                crea_suppr_table.creation_table()
                print("La table a été créée avec succès, retour au menu")
                time.sleep(3)
            except IndexError:
                print("La table existe déjà")
                time.sleep(2)
            except ValueError:
                print("Vous n'avez pas rentré une bonne valeur (str/int), la table a été supprimé, retour au menu")
                time.sleep(4)
            clear()
            main()
        
        # Suppression de table
        case 2:
            clear()
            print("Les tables existantes sont les tables : ", end="")
            if len(os.listdir(repertoire))!=0:
                for file in os.listdir(repertoire):
                    print(file[6])
            else:
                print("Aucune table a supprimer")
                time.sleep(2)
                clear()
                main()
            print("")
            try:
                crea_suppr_table.suppression_table()
                print("La table a été supprimé avec succès, retour au menu")
                time.sleep(3)
            except IndexError:
                print("La table n'existe pas, retour au menu")
                time.sleep(3)
            clear()
            main()
        
        # Edition de table
        case 3:
            clear()
            if len(os.listdir(repertoire))==0:
                print("Aucune table a editer, retour au menu")
                time.sleep(3)
                main()
            demande=input("Choisissez entre ajouter ou supprimer une entite (add/del) : ")
            match demande:
                
                # Ajouter une entite dans une table existente
                case "add":
                    clear()
                    try:
                        print("Les tables existantes sont : ", end="")
                        if len(os.listdir(repertoire))!=0:
                            for file in os.listdir(repertoire):
                                print(file[6], end=" ")
                        else:
                            print("Aucune table n'existe, retour au menu")
                            time.sleep(3)
                            main()
                        print("")
                        edition.ajouter_entite()
                        print("L'ajout a ete fait avec succes, retour au menu")
                        time.sleep(3)
                        main()
                    except IndexError:
                        print("La table n'existe pas, retour au menu")
                        time.sleep(2)
                        clear()
                        main()
                    except ValueError:
                        print("La cle est deja utilisee, retour au menu")
                        time.sleep(2)
                        clear()
                        main()
                
                # Supprimer entite dans une table existente
                case "del":
                    clear()
                    try:
                        print("Les tables existantes sont : ", end="")
                        if len(os.listdir(repertoire))!=0:
                            for file in os.listdir(repertoire):
                                print(file[6], end=" ")
                        else:
                            print("Aucune table n'existe, retour au menu")
                            time.sleep(3)
                            main()
                        print("")
                        edition.supprimer_entite()
                        print("L'entite a ete supprime avec succes, retour au menu")
                        time.sleep(3)
                        clear()
                        main()
                    except IndexError:
                        print("La table n'existe pas, retour au menu")
                        time.sleep(3)
                        clear()
                        main()
                    except ValueError:
                        print("La cle n'existe pas, retour au menu")
                        time.sleep(3)
                        clear()
                        main()
                    except Exception:
                        print("Vous n'avez pas valide la suppression, retour au menu")
                        time.sleep(3)
                        clear()
                        main()
                case _:
                    print("Vous n'avez pas rentrer un bon choix")
                    time.sleep(2)
                    clear()
                    main()
        
        # Affichage de table
        case 4:
            clear()
            try:
                print("Les tables existantes sont : ", end="")
                if len(os.listdir(repertoire))!=0:
                    for file in os.listdir(repertoire):
                        print(file[6], end=" ")
                    print("")
                else:
                    print("Aucune table n'existe, retour au menu")
                    time.sleep(3)
                    main()
                affichage.affichage_table()
                choixx=input("Ecrivez pour quitter : ")
                if choixx!="":
                    clear()
                    main()
                else:
                    affichage.affichage_table()
            except IndexError:
                print("La table n'existe pas, retour au menu")
                time.sleep(3)
                clear()
                main()
        
        # Rechercher un élément
        case 5:
            clear()
            try:
                print("Les tables existantes sont : ", end="")
                if len(os.listdir(repertoire))!=0:
                    for file in os.listdir(repertoire):
                        print(file[6], end=" ")
                    print("")
                else:
                    print("Aucune table n'existe, retour au menu")
                    time.sleep(3)
                    main()
                recherche.rechercher()
                choixx=input("Ecrivez pour quitter : ")
                if choixx!="":
                    clear()
                    main()
                else:
                    recherche.rechercher()
            except IndexError:
                print("La table n'existe pas, retour au menu")
                time.sleep(3)
                clear()
                main()
            except ValueError:
                print("Le nom de la colonne n'a pas été trouvé, retour au menu")
                time.sleep(3)
                clear()
                main()
            except Exception:
                print("Aucune correspondance dans la colonne, retour au menu")
                time.sleep(3)
                clear()
                main()
        
        # Quitter le programme
        case 6:
            print("Fermeture du programme")
        
        # Mauvais choix
        case _:
            print("Vous n'avez pas rentré un bon numéro")
            time.sleep(2)
            clear()
            main()