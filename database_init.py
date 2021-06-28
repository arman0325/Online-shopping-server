# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 17:22:18 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This is database setup
"""

import sqlite3
db = sqlite3.connect('shopping.db')
db.execute("DROP TABLE product")
db.execute("CREATE TABLE product (id INTEGER PRIMARY KEY, name CHAR(100) NOT NULL, origin CHAR(100) NOT NULL, price DECIMAL(4, 1) NOT NULL, quantity INTEGER(3) NOT NULL)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Apple', 'China', 7.5, 30)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Organe', 'USA', 9.5, 17)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Banana', 'China', 5.0, 15)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Mango', 'TaiWai', 12.0, 75)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Avocado', 'Mexico', 7.6, 30)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Cherry', 'China', 16.0, 55)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Durian', 'Thailand', 80.0, 27)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Grape', 'England', 53.5, 46)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Grapefruit ', 'China', 5.0, 53)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Guava', 'TaiWai', 11.2, 66)")
db.execute("INSERT INTO product (name, origin, price, quantity) VALUES ('Melon', 'Japan', 89, 12)")
db.commit()


db = sqlite3.connect('shopping.db')
db.execute("DROP TABLE coupon")
db.execute("CREATE TABLE coupon (id INTEGER PRIMARY KEY, code CHAR(100) NOT NULL, codeType CHAR(2) NOT NULL, discount DECIMAL(5, 2) NOT NULL)")
db.execute("INSERT INTO coupon (code, codeType, discount) VALUES ('PROMOCODE90P', '%', 0.9)")
db.execute("INSERT INTO coupon (code, codeType, discount) VALUES ('PROMOCODE30', '$', 30)")
db.execute("INSERT INTO coupon (code, codeType, discount) VALUES ('PROMOCODE50P', '%', 0.5)")
db.execute("INSERT INTO coupon (code, codeType, discount) VALUES ('PROMOCODE100', '$', 100)")
db.commit()

db = sqlite3.connect('shopping.db')
db.execute("DROP TABLE record")
db.execute("CREATE TABLE record (id INTEGER PRIMARY KEY, buyer CHAR(100) NOT NULL, total DECIMAL(10, 2) NOT NULL, discount CHAR(100) NOT NULL, productList CHAR(255) NOT NULL)")
dis = "(2, 'PROMOCODE30', '$', 30)"
prodList = "[[7, 2, 'Durian', 80, 160]]"
db.execute("INSERT INTO record (Buyer, Total, discount, productList) VALUES ('Tim', 160.0, ?, ?)",(dis, prodList))
db.commit()


db = sqlite3.connect('shopping.db')
db.execute("DROP TABLE account")
db.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, ac CHAR(100) NOT NULL, pw CHAR(100) NOT NULL)")
db.execute("INSERT INTO account (ac,pw) VALUES ('admin0325','adminpw')")
db.execute("INSERT INTO account (ac,pw) VALUES ('tim','123')")
db.execute("INSERT INTO account (ac,pw) VALUES ('peter','321')")
db.execute("INSERT INTO account (ac,pw) VALUES ('cindy','111')")
db.commit()