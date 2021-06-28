# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:13:15 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program is degvelop some function will use in server-side.py and clinet-side.py
"""

import ast # help to string to list
from prettytable import PrettyTable #Table function
import os
from itertools import groupby
from datetime import datetime


def StringToList(String): 
    # help to change the string to list
    list_a = ast.literal_eval(String)
    return list_a

def printTable(listName,list_a):
    # this is print the table of list
    t = PrettyTable(listName)
    for x in list_a:
        t.add_row(x)
    return t.get_string()

def printCommandList(Type): 
    #return the command List
    # Command of Main page
    if Type == 'Main':
        command='''L: Change Account
P: Product List
B: Buy Product
C: Command List
X: Stop the client page'''

    # Command of Buy List
    if Type == "Buy":
        command='''\nCommand of Buy List\n
show:\tshow your buy list
insert:\tinsert the product to your buy list
delete:\tdelete the product in your buy list
payment:payment of buy list
back:\tback to menu'''

    if Type == 'admin':
        command='''\nAdmin Command List:
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
S: Stop the server'''


    return command

def reList(List):  
    # relist the same item in list
    nameDict = {}
    for x in List:
        if x[2] not in nameDict:
            nameDict[x[0]] = [x[2], x[3]]
    #print(nameDict)
    newList= []
    list2 = []
    for ID, count in groupby(sorted(List), key=lambda x: x[0]):
                                list2.append([ID, sum(v[1] for v in count)])
    
    newList.extend(list2)
    for x in newList:                            
        prod = list(filter(lambda y : y == x[0], nameDict))
        #print(prod)
        x.append(nameDict[prod[0]][0])
        x.append(nameDict[prod[0]][1])
        x.append(nameDict[prod[0]][1]*x[1])
    return newList
    
    
def stop():
    # use to stop the server-side or client-side
    os._exit(0)
    
def checkCreditCard(cardNum, month, year):
    # use to check the credit card value
    if len(cardNum) != 16 or cardNum.isdigit() == False:
        # the length is more or less than 16 length
        return False
    else:
        mm = int(datetime.today().strftime('%m'))
        yy = int(datetime.today().strftime('%y'))
        if year >= yy:
            if month >= mm:
                return True
            else:
                #month expired
                return False
        else:
            # year expired
            return False

if __name__ == "__main__":
    
#    Str1 = "[[1,0], [2,6]]"
#    print(type(Str1))
#    print(Str1)
#    listA = StringToList(Str1)
#    print(type(listA))
#    print(listA)
#    
#    
#    title = ['ID', 'Quantity','Name', 'Price', 'Total Price']
#    li2 = [[1, 5, 'apple', 7.5, 37.5], [2, 10, 'organe', 9.5, 95.0]]
#    print(printTable(title,li2))
#    
#    printCommandList("Main")
#    
#    title = ['ID', 'Quantity','Name', 'Price', 'Total Price']
#    li2 = [["None","None","None","None","None"]]
#    print(printTable(title,li2))
    print(checkCreditCard("0123456789123456",1,21))