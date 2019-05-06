#! /usr/bin/env python3
# coding: utf-8

""" This script get data we need from OpenFoodfact """

import json
import requests
import unicodedata


class GetDataApi:
    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/"

    def getcategory(self):
        """ Get the OFF 20 first category and return a list for fill BDD """
        # Create the link
        link = self.url + "categories.json"

        # Make the request :
        r = requests.get(link)
        cat_file = json.loads(r.text)

        # Create category list :
        cat_list = []
        i = 0
        while i <= 22:
            cat_list.append(cat_file['tags'][i]['name'])
            cat_list[i] = unicodedata.normalize('NFKD', cat_list[i]).\
                encode('ascii', 'ignore').decode()
            i += 1
        cat_list_clean = cat_list[3:]
        return cat_list_clean

    def getproducts(self):
        """ Gets the 20 first products from the category
        and puts them in a list.
        """
        # get the 20 products by category
        categoryname = self.getcategory()
        product_for_bdd = []
        i = 0
        while i < len(categoryname):
            link = self.url + "categorie/" + \
                categoryname[i].replace(" ", "-") + ".json"
            r = requests.get(link)
            listjson = [r.content]
            for content in listjson:
                data = json.loads(content)
                j = 0

                # For each category, add the product in a tuple to a clean list
                while j < len(data["products"]):
                    id_product = data["products"][j]["code"]
                    product_name = data["products"][j]["product_name"]
                    product_name = unicodedata.normalize("NFKD", product_name). \
                        encode("ascii", "ignore").decode()
                    nutritional_score = data["products"][j]["nutrition_score_debug"]
                    nutritional_score = nutritional_score[-2:]
                    # If the nutritional score is missing, it takes the value 100
                    try:
                        nutritional_score = int(nutritional_score)
                    except:
                        nutritional_score = 100
                    url = data["products"][j]["url"]
                    ingredients = data["products"][j]["ingredients_text_debug"]
                    if ingredients:
                        ingredients = unicodedata.normalize("NFKD", ingredients). \
                            encode("ascii", "ignore").decode()
                    category_name = categoryname[i]
                    try:
                        purchase_place = data["products"][j]["purchase_places"]
                    except:
                        purchase_place = ""
                    # Create a tuple for all data needed
                    data_complete = (id_product, product_name, nutritional_score,
                                     url, ingredients, category_name, purchase_place)
                    product_for_bdd.append(data_complete)
                    j += 1
            i += 1
        # returns a list containing all product who belong to the 20 category
        return product_for_bdd
