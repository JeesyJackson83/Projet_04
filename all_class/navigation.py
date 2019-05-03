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

    def category_choice(self):
        print("Bienvenue chez Pur Beurre,\n"
              "Ceci est un Proof of Concept \n"
              "Le choix des catégories est limité à 20 \n"
              "Ainsi que le choix des produits par catégories limité à 20 \n \n"
              "Pour naviguer entre les catégories et produits, "
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
        print("\n\nSouhaitez-vous sauvegarder ce produit ?  Y/N !")


        # # Take the nutriscore of product
        # self.mysql.execute(""" USE pur_beurre""")
        # self.mysql.execute(""" SELECT nutritional_score FROM products
        #                                 WHERE product_name = %s; """,
        #                    self.list_pro[int(self.choice_pro)])
        # rowsp = self.mysql.fetchall()
        # for i in range(len(rowsp)):
        #     print(i, " - ", rowsp[i]['nutritional_score'])
        #     nutri_pro.append(rowsp[i]['nutritional_score'])
        # # Find the best nutriscore in category
        # self.choice_pro = -1
        # while self.choice_pro < 0 or self.choice_pro > len(rows):
        #     try:
        #         self.choice_pro = int(input("\nChoisissez un produit:  "))
        #     except:
        #         print("\nCe n'est pas un nombre !")
        # return self.choice_pro