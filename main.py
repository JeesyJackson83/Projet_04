#! /usr/bin/env python3
# coding: utf-8

""" Project 05 for Pur Beurre by Jessy
This script allow user to interract with OpenFoodFacts API
to find the better product in chosen category.
All informations you need is provide by the README.md"""

from all_class import dbinit as db
from all_class import bdd_data_manager as bddm
from all_class import navigation as nav


def data_init():
    init_db = db.DatabaseInit()
    fill_bdd = bddm.FillDatabase()
    check_bdd = init_db.check_bdd()
    if check_bdd == 1:
        print("Base de données déja intégrée")
    else:
        print("Création de la base de données")
        init_db.create()
        fill_bdd.category_update()
        fill_bdd.products_update()


def start():
    """ This method will manage user navigation"""
    user_nav = nav.Navigation()

    loop = True
    while loop:
        print("Bienvenue chez Pur Beurre,\n"
              "Ceci est un Proof of Concept. \n"
              "Le choix des catégories est limité à 20, \n"
              "Ainsi que le choix des produits par catégories.\n"
              "Pour naviguer entre les choix il vous suffit "
              "d'entrer les chiffres correspondant aux propositions \n \n")

        print("\n1 - Choisissez un aliment à remplacer")
        print("2 - Consulter les aliments précédemments remplacés")
        print("Pour quitter, tapez Q.")
        user_screen = input("Votre choix : ")

        if user_screen.lower() == "q":
            break
        try:
            user_screen = int(user_screen)
            if user_screen not in (1, 2):
                print("Entrez 1 ou 2")
        except:
            print("Veuillez entrer un choix valide.")

        if user_screen == 1:

            # Run user navigation:
            user_nav.category_choice()
            user_nav.product_choice()
            user_nav.find_substitute()
            user_nav.show_substitute()

        elif user_screen == 2:
            user_nav.show_save()


if __name__ == '__main__':
    data_init()
    start()
