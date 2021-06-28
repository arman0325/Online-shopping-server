# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:55:58 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program is auto test of DB function in user
"""

import unittest
import DatabaseFunction

class Test(unittest.TestCase):
    
    def setUp(self):
        self.db = DatabaseFunction.DatabaseFunc("shopping.db")
        
    def testCheckAccount(self):
        self.db.resetDB() #reset the database to test
        # this test for checkAccount function in db
        
        # case 1 current input, return true
        self.assertTrue(self.db.checkAccount("tim","123"))
        
        # case 2 wrong password, return false
        self.assertFalse(self.db.checkAccount("tim","1243"))
        
        # case 2 wrong username, return false
        self.assertFalse(self.db.checkAccount("john","1243"))
        
        
    def testSelectAllProduct(self):
        self.db.resetDB() #reset the database to test
        # this test for selectAllDatabase function
        #select all the product in the database
        result = [(1, 'Apple', 'China', 7.5, 30), 
                  (2, 'Organe', 'USA', 9.5, 17), 
                  (3, 'Banana', 'China', 5, 15), 
                  (4, 'Mango', 'TaiWai', 12, 75), 
                  (5, 'Avocado', 'Mexico', 7.6, 30), 
                  (6, 'Cherry', 'China', 16, 55), 
                  (7, 'Durian', 'Thailand', 80, 27), 
                  (8, 'Grape', 'England', 53.5, 46), 
                  (9, 'Grapefruit ', 'China', 5, 53), 
                  (10, 'Guava', 'TaiWai', 11.2, 66), 
                  (11, 'Melon', 'Japan', 89, 12)]
        self.assertEqual(self.db.selectAllDatabase(), result)
        
    def testUpdateDB(self):
         self.db.resetDB() #reset the database to test
         # this test for updateDB
         # if user payment that update the quantity
         data = [[1, 5]]
         self.assertEqual(self.db.updateDB(data), "Update successful")
         
         #multi value
         data2 = [[1, 5], [7,2]]
         self.assertEqual(self.db.updateDB(data2), "Update successful")
        
         # wrong vlaue
         data2 = [["df", 5]]
         self.assertEqual(self.db.updateDB(data2), "Update fail")
         
    def testQuantity(self):
        self.db.resetDB()#reset the database to test
        #enough
        data = [[1,5]]
        self.assertTrue(self.db.QuantityInDatabase(data))
        
        # product id 1 is not enough
        data2=[[1,50]]
        self.assertFalse(self.db.QuantityInDatabase(data2))
        
if __name__ == "__main__":
    unittest.main()