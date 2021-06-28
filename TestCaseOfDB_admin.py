# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:48:30 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program is auto test of DB function in admin
"""

import unittest
import DatabaseFunction

class Test(unittest.TestCase):
    
    def setUp(self):
        self.db = DatabaseFunction.DatabaseFunc("shopping.db")
        
    def testUpdateProduct(self):
        self.db.resetDB() # reset the database to test
        # test update the quantity of product to db
        data = [1, 50]
        self.assertEqual(self.db.updateProductDB(data), "Update successful")
        
    def testInsertItem(self):
        self.db.resetDB() # reset the database to test
        data = ['Watermelon', 'China', 12, 30]
        self.assertEqual(self.db.insertItem(data), "Insert success")
        
    def testDiscount(self):
        self.db.resetDB() # reset the database to test
        # test insert discount to db
        self.assertEqual(self.db.insertDiscount('promo25', '$', 25),"success")
        
        # test find the discount in db
        result = (2, 'PROMOCODE30', '$', 30)
        self.assertEqual(self.db.discountDB("PROMOCODE30"), result)
        
        # test not find the discount in db
        self.assertEqual(self.db.discountDB("PROMOCODE80"), "None")
        
        # test delete discount in db
        self.assertEqual(self.db.deleteDiscount('promo25'), "delete discount success")
        
        result = [(1, 'PROMOCODE90P', '%', 0.9), (2, 'PROMOCODE30', '$', 30), (3, 'PROMOCODE50P', '%', 0.5), (4, 'PROMOCODE100', '$', 100)]
        self.assertEqual(self.db.showAllDisecount(), result)
        
    def testRecord(self):
        self.db.resetDB() # reset the database to test
        # test show to buy record
        result = [(1, 'Tim', 130, '30$', "[[7, 2, 'Durian', 80, 160]]")]
        self.assertEqual(self.db.showRecord(), result)
        
        # test insert the record to db
        data = "[[7, 2, 'Durian', 80, 160],[3, 10, 'Banana', 5, 50]]"
        self.assertEqual(self.db.insertRecord('peter', 210, 'Not discount',data), "success")
        
        # test show to buy record affter update
        result1 = [(1, 'Tim', 130, '30$', "[[7, 2, 'Durian', 80, 160]]"), (2, 'peter', 210, 'Not discount', "[[7, 2, 'Durian', 80, 160],[3, 10, 'Banana', 5, 50]]")]
        self.assertEqual(self.db.showRecord(), result1)
        
if __name__ == "__main__":
    unittest.main()