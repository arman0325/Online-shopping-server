# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:16:45 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program is auto test of FuncPart.py
"""

import unittest
import FuncPart

class Test(unittest.TestCase):
        
    def testStringToList(self):
        # this test fot StringToList function
        strList = "[[1,0], [2,6]]"
        self.assertEqual(type(FuncPart.StringToList(strList)), list)
        
    def testPrintCommandList(self):
        # this test fot printCommandList function
        
        # case 1 normal user command List in main page
        self.assertEqual(FuncPart.printCommandList("Main"),'''L: Change Account
P: Product List
B: Buy Product
C: Command List
X: Stop the client page''')

        # case 2 normal user command list in buy page
        self.assertEqual(FuncPart.printCommandList("Buy"),'''\nCommand of Buy List\n
show:\tshow your buy list
insert:\tinsert the product to your buy list
delete:\tdelete the product in your buy list
payment:payment of buy list
back:\tback to menu''')    
        
        # case 3 admin command list in main page
        self.assertEqual(FuncPart.printCommandList("admin"),'''\nAdmin Command List:
L: Logout account
P: Product List
IP: Insert Product
UP: Replenish stock
IS: Insert dicsount code
DD: Delete discount code
SD: Show all discount
SR: Show all member shopping record
C: Command List
X: Stop the client page
S: Stop the server''')  
            
            
        
    def testPrintTable(self):
        # this test for printTable function
        title = ['ID', 'Quantity','Name']
        li2 = [[1, 5, 'apple'], [2, 10, 'organe']]
        self.assertEqual(FuncPart.printTable(title,li2),'''+----+----------+--------+
| ID | Quantity |  Name  |
+----+----------+--------+
| 1  |    5     | apple  |
| 2  |    10    | organe |
+----+----------+--------+''')
        
    def testReList(self):
        # this test for reList function
        #test month at Jan, 2021
    
        list1 = [[10, 10, 'Guava', 11.2, 112.0],[7, 2, 'Durian', 80, 160], [10, 10, 'Guava', 11.2, 112.0]]
        self.assertEqual(FuncPart.reList(list1), [[7, 2, 'Durian', 80, 160], [10, 20, 'Guava', 11.2, 224.0]])
    
    def testCheckCreditCard(self):
        # this test for checkCreditCard function
        # testing date is 26/01/2022
        
        # case 1 input the current value, return is true
        self.assertTrue(FuncPart.checkCreditCard("0123456789123456", 5, 22))
        
        # case 2 len of the number no enough 16
        # return will be false
        self.assertFalse(FuncPart.checkCreditCard("012345678912345", 1, 22))
        
        # case 3 len of the number more than 16
        # return will be false
        self.assertFalse(FuncPart.checkCreditCard("01234567891234567", 1, 22))
        
        #case 4 the Expiration date
        #return is false
        self.assertFalse(FuncPart.checkCreditCard("0123456789123456", 12, 19))
        
        #case 5 the card number has string
        #return false
        self.assertFalse(FuncPart.checkCreditCard("aa234567891234567", 3, 21))
        
        self.assertFalse(FuncPart.checkCreditCard("0123456789string", 3, 21))
        
        self.assertFalse(FuncPart.checkCreditCard("0223456t89123h56", 3, 21))
    
if __name__ == "__main__":
    unittest.main()