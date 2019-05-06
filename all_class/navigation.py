#! /usr/bin/env python3
# coding: utf-8

""" This Class is for interaction between user and database """

import pymysql


class Navigation:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='user_purbeurre',
                                          password='user_purbeurre',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.mysql = self.connection.cursor()
        self.choice_cat = ""
        self.choice_pro = ""
        self.list_cat = []
        self.list_pro = []
        self.id_min = int()
        self.save = ""

    def category_choice(self):
        print("\nPour naviguer entre les catégories et produits, "
              "il vous suffit de rentrer les chiffres correspondants. \n \n")
        # Show category list
        self.mysql.execute(""" USE pur_beurre""")
        self.mysql.execute(""" SELECT category_name from category; """)
        rows = self.mysql.fetchall()
        for i in range(len(rows)):
            print(i, " - ", rows[i]['category_name'])
            self.list_cat.append(rows[i]['category_name'])
        # User need to choose an available category
        self.choice_cat = -1
        while self.choice_cat < 0 or self.choice_cat > len(rows):
            try:
                self.choice_cat = int(input("\nChoisissez une catégorie:  "))
            except:
                print("\nCe n'est pas un nombre !")
        return self.choice_cat

    def product_choice(self):
        print("\nVoici la liste des produits appartenant à votre choix\n"
              "Pour naviguer entre les catégories et produits, "
              "il vous suffit de rentrer les chiffres correspondants. \n \n")
        # Show product list belong in choosen category
        self.mysql.execute(""" USE pur_beurre""")
        self.mysql.execute(""" SELECT product_name FROM products 
                        WHERE category_name = %s; """, self.list_cat[int(self.choice_cat)])
        rows = self.mysql.fetchall()
        for i in range(len(rows)):
            print(i, " - ", rows[i]['product_name'])
            self.list_pro.append(rows[i]['product_name'])
        # User need to choose a product
        self.choice_pro = -1
        while self.choice_pro < 0 or self.choice_pro > len(rows):
            try:
                self.choice_pro = int(input("\nChoisissez un produit:  "))
            except:
                print("\nCe n'est pas un nombre !")
        return self.choice_pro

    def find_substitute(self):
        print("\nVous avez fait votre choix:\n"
              "\nNous recherchons actuellement un produit de remplacement !\n"
              "----------------------------------------------------------\n\n")
        # Take all nutriscore in the choosen category
        self.mysql.execute(""" USE pur_beurre""")
        self.mysql.execute(""" SELECT id_product, nutritional_score FROM products
                                WHERE category_name = %s; """,
                           self.list_cat[int(self.choice_cat)])
        rows = self.mysql.fetchall()
        # make a list with nutriscore, find the smaller and retrieve is index
        nutri_pro = []
        for i in range(len(rows)):
            nutri_pro.append(rows[i]['nutritional_score'])
        low_nutri = nutri_pro.index(min(nutri_pro))
        self.id_min = rows[int(low_nutri)]['id_product']
        return self.id_min

    def show_substitute(self):
        self.mysql.execute(""" USE pur_beurre""")
        self.mysql.execute(""" SELECT id_product, product_name,
                                nutritional_score, url, ingredients,
                                category_name, purchase_place FROM products
                                WHERE id_product = %s; """, self.id_min)
        detail = self.mysql.fetchall()
        print("---------------------------------------------------------------------------\n"
              "-                                                                         -\n"
              "-                                DETAILS                                  -\n"
              "-                                                                         -\n"
              "---------------------------------------------------------------------------\n")
        print("\nNom du produit: ", detail[0]['product_name'])
        print("\nId du produit: ", detail[0]['id_product'])
        print("\nScore nutritionnel: ", detail[0]['nutritional_score'])
        print("\nURL: ", detail[0]['url'])
        print("\nIngrédients: ", detail[0]['ingredients'])
        print("\nCatégorie: ", detail[0]['category_name'])
        print("\nLieu d'achat: ", detail[0]['purchase_place'])
        # Save the product ?
        self.save = 0
        while self.save < 1 or self.save > 2:
            try:
                self.save = int(input("\n\nSouhaitez-vous sauvegarder ce produit ?  1-OUI 2-NON : "))
            except:
                print("Entrez 1 pour sauvegarder votre produit ou "
                      "2 pour revenir au choix des catégories !")
        if self.save == 1:
            self.mysql.execute("""INSERT INTO substitute (id_product, product_name,
                                        nutritional_score, url, ingredients, category_name, purchase_place)\
                                        VALUES (%s, %s, %s, %s, %s, %s, %s);""",
                               (detail[0]['id_product'], detail[0]['product_name'], detail[0]['nutritional_score'],
                                detail[0]['url'], detail[0]['ingredients'], detail[0]['category_name'],
                                detail[0]['purchase_place']))
            self.connection.commit()
            print("\n Votre recherche est sauvegardée !"
                  "\n RETOUR A L'ACCUEIL !")
        else:
            print("\n Votre recherche n'est pas sauvegardée !"
                  "\n RETOUR A L'ACCUEIL !")

    def show_save(self):
        self.mysql.execute(""" USE pur_beurre""")
        self.mysql.execute(""" SELECT id_product, product_name,
                                        nutritional_score, url, ingredients,
                                        category_name, purchase_place FROM substitute """)
        detail = self.mysql.fetchall()
        if not detail:
            print("\n\nVous n'avez pas encore de produit sauvegardé!\n\n"
                  "\nRETOUR A L'ACCUEIL !\n")

        if detail:
            i = 0
            while i < len(detail):
                print("---------------------------------------------------------------------------\n"
                      "-                                                                         -\n"
                      "-                                DETAILS                                  -\n"
                      "-                                                                         -\n"
                      "---------------------------------------------------------------------------\n")
                print("\nNom du produit: ", detail[i]['product_name'])
                print("\nId du produit: ", detail[i]['id_product'])
                print("\nScore nutritionnel: ", detail[i]['nutritional_score'])
                print("\nURL: ", detail[i]['url'])
                print("\nIngrédients: ", detail[i]['ingredients'])
                print("\nCatégorie: ", detail[i]['category_name'])
                print("\nLieu d'achat: ", detail[i]['purchase_place'])
                print("\n---------------------------------------------------------------------------\n\n")
                i += 1
