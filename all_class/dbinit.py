#! /usr/bin/env python3
# coding: utf-8

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
                mysql.execute("""DROP DATABASE IF EXISTS `pur_beurre`""")
                mysql.execute("""CREATE DATABASE IF NOT EXISTS `pur_beurre`""")
                mysql.execute("""USE `pur_beurre`""")
                # Create Tables
                mysql.execute("""CREATE TABLE Category(
                                                    id_category BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                                    category_name TEXT NOT NULL)
                                                    ENGINE=INNODB;
                                                    """)

                mysql.execute("""CREATE TABLE Products(
                                                    id_t_prod BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                                    id_product BIGINT UNSIGNED NOT NULL,
                                                    product_name VARCHAR(100) NOT NULL,
                                                    nutritional_score SMALLINT NOT NULL,
                                                    url VARCHAR(200) NOT NULL,
                                                    ingredients TEXT,
                                                    category_name TEXT NOT NULL,
                                                    purchase_place VARCHAR(100))
                                                    ENGINE=INNODB;
                                                    """)

                mysql.execute("""CREATE TABLE Substitute(
                                                    id_t_sub BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                                    id_product BIGINT UNSIGNED NOT NULL,
                                                    product_name VARCHAR(80) NOT NULL,
                                                    nutritional_score SMALLINT NOT NULL,
                                                    url VARCHAR(200) NOT NULL,
                                                    ingredients TEXT,
                                                    category_name TEXT NOT NULL,
                                                    purchase_place VARCHAR(100))
                                                    ENGINE=INNODB;
                                                    """)

                self.connection.commit()

        finally:
            self.connection.close()