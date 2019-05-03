#! /usr/bin/env python3
# coding: utf-8

""" This Class push Apidata to Mysql Database"""

import pymysql

from all_class import api_data_manager as apidm


class FillDatabase:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='user_purbeurre',
                                          password='user_purbeurre',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.mysql = self.connection.cursor()
        self.listing = apidm.GetDataApi()

    def category_update(self):
        list_cat = self.listing.getcategory()
        self.mysql.execute(""" USE pur_beurre""")
        i = 0
        while i < len(list_cat):
            self.mysql.execute("""INSERT INTO CATEGORY (category_name)\
                                VALUES (%s);""", (list_cat[i]))
            i += 1
        self.connection.commit()

    def products_update(self):
        list_prod = self.listing.getproducts()
        self.mysql.execute(""" USE pur_beurre""")
        i = 0
        while i < len(list_prod):
            self.mysql.execute("""INSERT INTO PRODUCTS (id_product, product_name, 
                                nutritional_score, url, ingredients, category_name, purchase_place)\
                                VALUES (%s, %s, %s, %s, %s, %s, %s);""", (list_prod[i]))
            i += 1
        self.connection.commit()
