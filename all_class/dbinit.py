#! /usr/bin/env python3
# coding: utf-8

""" This script Drop the actual database and create a new one,
 Only one time when main.py is running """

import pymysql


class DatabaseInit:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='user_purbeurre',
                                          password='user_purbeurre',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

    def create(self):
        """Drop and create database."""
        try:
            with self.connection.cursor() as mysql:
                # DROP & CREATE Database
                mysql.execute("""DROP DATABASE IF EXISTS `pur_beurre`;""")
                mysql.execute("""CREATE DATABASE IF NOT EXISTS `pur_beurre`;""")
                mysql.execute("""USE `pur_beurre`""")
                # Create Tables
                mysql.execute("""CREATE TABLE Category(
                                                    id_category TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                                    category_name VARCHAR(255) NOT NULL UNIQUE)
                                                    ENGINE=INNODB;
                                                    """)

                mysql.execute("""CREATE TABLE Products(
                                                    id_t_prod SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                                    id_product BIGINT UNSIGNED NOT NULL,
                                                    product_name VARCHAR(200) NOT NULL,
                                                    nutritional_score SMALLINT NOT NULL,
                                                    url VARCHAR(255) NOT NULL,
                                                    ingredients TEXT,
                                                    category_name VARCHAR(255) NOT NULL,
                                                    purchase_place VARCHAR(200),
                                                    INDEX (id_product),
                                                    CONSTRAINT fk_category_name
                                                    FOREIGN KEY (category_name)
                                                    REFERENCES Category(category_name))
                                                    ENGINE=INNODB;
                                                    """)

                mysql.execute("""CREATE TABLE Substitute(
                                                    id_t_sub SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                                    id_product BIGINT UNSIGNED NOT NULL,
                                                    product_name VARCHAR(200) NOT NULL,
                                                    nutritional_score SMALLINT NOT NULL,
                                                    url VARCHAR(200) NOT NULL,
                                                    ingredients TEXT,
                                                    category_name TEXT NOT NULL,
                                                    purchase_place VARCHAR(200),
                                                    CONSTRAINT fk_id_product
                                                    FOREIGN KEY (id_product)
                                                    REFERENCES Products(id_product))
                                                    ENGINE=INNODB;
                                                    """)

                self.connection.commit()

        finally:
            self.connection.close()

    def check_bdd(self):
        try:
            with self.connection.cursor() as mysql:
                mysql.execute("""USE `pur_beurre`""")
                mysql.execute("""SELECT COUNT(*),(SELECT COUNT(*) FROM products) FROM category;""")
                check = mysql.fetchall()
                if check[0]["COUNT(*)"] == 20 and \
                        check[0]["(SELECT COUNT(*) FROM products)"] == 400:
                    check_bdd = 1
                else:
                    check_bdd = 0
                return check_bdd
        except:
            check_bdd = 0
            return check_bdd
