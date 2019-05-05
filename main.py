#! /usr/bin/env python3
# coding: utf-8

""" Project 05 for Pur Beurre
fdfdf"""

import json

from all_class import dbinit as db
from all_class import api_data_manager as apid
from all_class import bdd_data_manager as bddm
from all_class import navigation as nav


init_db = db.DatabaseInit()
get_api = apid.GetDataApi()
fill_bdd = bddm.FillDatabase()

def start():
    """ This method will manage user navigation"""
    user_nav = nav.Navigation()

    loop = True
    while loop:
        print("\n1 - Choisissez un aliment à remplacer")
        print("2 - Consulter les aliments précédemments remplacés")
        print("Pour quitter, tapez Q.")
        user_screen = input("Votre choix : ")

        if user_screen.lower() == 'q':
            break
        try:
            user_screen = int(user_screen)
            if user_screen not in (1, 2):
                print("Entrez 1 ou 2")
        except:
            print("Veuillez entrer un choix valide.")

        if user_screen == 1:

            # Categories' choices :
            pick.choosecategory()

            # choose food :
            idswitchedproduct = pick.choosefood(pick.categoryname)

            if idswitchedproduct == 1:
                break

            # choose substitute or not :
            pick.choosesubstitute(idswitchedproduct)

        elif user_screen == 2:
            pick.getdetails()
            pass




if __name__ == '__main__':
    init_db.create()
    fill_bdd.category_update()
    fill_bdd.products_update()
    # start()


