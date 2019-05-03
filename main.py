#! /usr/bin/env python3
# coding: utf-8

""" Project 05 for Pur Beurre
fdfdf"""

import json

# from all_class import user_pick as up
from all_class import dbinit as db
from all_class import api_data_manager as apid
from all_class import bdd_data_manager as bddm
from all_class import navigation as nav




# is_good = 1
# Instanciation of the classes :


# def start():
#     print("\n\nBienvenue sur l'application de Pur Beurre")
#     print("Vous pourrez ici choisir des aliments plus sains\n\
#     et consulter ceux que vous avez déjà remplacés.\n")
#
#     pick = up.Pick()
#     loop = True
#
#     while loop:
#         print("\n1 - Choisissez un aliment à remplacer")
#         print("2 - Consulter les aliments précédemments remplacés")
#         print("Pour quitter, tapez Q.")
#         user_screen = input("Votre choix : ")
#
#         if user_screen.lower() == 'q':
#             break
#         try:
#             user_screen = int(user_screen)
#             if user_screen not in (1, 2):
#                 print("Entrez 1 ou 2")
#         except:
#             print("Veuillez entrer un choix valide.")
#
#         if user_screen == 1:
#
#             # Categories' choices :
#             pick.choosecategory()
#
#             # choose food :
#             idswitchedproduct = pick.choosefood(pick.categoryname)
#
#             if idswitchedproduct == 1:
#                 break
#
#             # choose substitute or not :
#             pick.choosesubstitute(idswitchedproduct)
#
#         elif user_screen == 2:
#             pick.getdetails()
#             pass


test_db = db.DatabaseInit()
test_api = apid.GetDataApi()
test_bdd = bddm.FillDatabase()
test_nav = nav.Navigation()

if __name__ == '__main__':
    test_db.create()
    # test_api.getproducts()
    test_bdd.category_update()
    test_bdd.products_update()
    test_nav.category_choice()
    test_nav.product_choice()
    test_nav.find_substitute()
    test_nav.show_substitute()
    # start()


