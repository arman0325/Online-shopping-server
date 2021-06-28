# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 19:06:53 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program for sever-side call database function call to use
"""

import sqlite3

class DatabaseFunc():
    def __init__(self, dbName):
        self.dbName = dbName
        
    def setDB(self, dbName):
        self.dbName = dbName
    
    
    def updateDB(self, listItem):
        for x in listItem:
            db = sqlite3.connect(self.dbName)
            try:
                num = int(x[1])
                PID = int(x[0])
                db.execute("UPDATE product SET quantity = quantity-:num WHERE id = :id",
                           {"num":num, "id":PID})
                db.commit()
            except:
                return "Update fail"
        return "Update successful"
    
    def selectAllDatabase(self):#get data of database 
        db = sqlite3.connect(self.dbName)
        c = db.cursor()
        c.execute("SELECT * FROM product")
        data = c.fetchall()
        c.close()
        return data
    
    def QuantityInDatabase(self, listItem):
        for x in listItem:
            db = sqlite3.connect(self.dbName)
            c = db.cursor()
            c.execute("SELECT quantity FROM product WHERE id = :id",
                      {"id":x[0]})
            data = c.fetchone()
            #print(data[0])
            c.close()
            if data[0] < x[1]:
                return False
        else:
            return True  
        
    def updateProductDB(self, listItem):
        db = sqlite3.connect(self.dbName)
        try:
            db.execute("UPDATE product SET quantity = quantity + :num WHERE id = :id",
                           {"num":listItem[1], "id":listItem[0]})
            db.commit()
        except:
            return "Update fail"
        return "Update successful"
          
    def insertItem(self,listItem):
        try:
            db = sqlite3.connect(self.dbName)
            db.execute("INSERT INTO product (name, origin, price, quantity) VALUES (?, ?, ?, ?)", 
                       (listItem[0], listItem[1], listItem[2], listItem[3]))
            db.commit()
        except:
            return "Insert fail"
        return "Insert success"
        
    def resetDB(self):
        try:
            db = sqlite3.connect(self.dbName)
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
            dis = "30$"
            prodList = "[[7, 2, 'Durian', 80, 160]]"
            db.execute("INSERT INTO record (buyer, total, discount, productList) VALUES ('Tim', 130.0, ?, ?)",(dis, prodList))
            db.commit()

            db = sqlite3.connect('shopping.db')
            db.execute("DROP TABLE account")
            db.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, ac CHAR(100) NOT NULL, pw CHAR(100) NOT NULL)")
            db.execute("INSERT INTO account (ac,pw) VALUES ('admin0325','adminpw')")
            db.execute("INSERT INTO account (ac,pw) VALUES ('tim','123')")
            db.execute("INSERT INTO account (ac,pw) VALUES ('peter','321')")
            db.execute("INSERT INTO account (ac,pw) VALUES ('cindy','111')")
            db.commit()
            
            return "Reset successful"
        except:
            return "Reset fail"
    
    def insertDiscount(self, code, codeType, discount):
        db = sqlite3.connect(self.dbName)
        try:
            c = db.cursor()
            c.execute("INSERT INTO coupon (code, codeType, discount) VALUES (?,?,?)", (code,codeType,discount))
            c.close()
            db.commit()
            data = "success"
        except:
            data = "None"
        
        return data
    
    def deleteDiscount(self,disCode):
        db = sqlite3.connect(self.dbName)
        try:
            c = db.cursor()
            sql = "DELETE FROM coupon WHERE code = ?"
            c.execute(sql, (disCode,))
            db.commit()
            data = "delete discount success"
        except:
            data = "delete discount unsuccess"
        
        return data
        
    def discountDB(self, code):
        db = sqlite3.connect(self.dbName)
        try:
            c = db.cursor()
            c.execute("SELECT * FROM coupon WHERE code=:ID",{"ID":code})
            data = c.fetchall()[0]
            c.close()
        except:
            data = "None"
        
        return data
    
    def showAllDisecount(self):
        db = sqlite3.connect(self.dbName)
        try:
            c = db.cursor()
            c.execute("SELECT * FROM coupon")
            data = c.fetchall()
            c.close()
        except:
            data = "None"
        
        return data
    
    def insertRecord(self, name, to, dis, listItem):
        db = sqlite3.connect(self.dbName)
        try:
            c = db.cursor()
            #print((name, to, dis, listItem))
            c.execute("INSERT INTO record (buyer, total, discount, productList) VALUES (?, ?, ?, ?)",(name, to, dis, listItem))
            c.close()
            db.commit()
            data="success"
        except:
            data = "None"
        
        return data
        
    def showRecord(self):
        db = sqlite3.connect(self.dbName)
        try:
            c = db.cursor()
            c.execute("SELECT * FROM record")
            data = c.fetchall()
            c.close()
        except:
            data = "None"
        
        return data
        
    def checkAccount(self,ac,pw):
        db = sqlite3.connect(self.dbName)
        dictAC = {}
        try:
            c = db.cursor()
            c.execute("SELECT * FROM account")
            data = c.fetchall()
            #print(data)
            for x in data:
                dictAC[x[1]] = x[2]
                
            #print(dictAC)
            c.close()
            if ac in dictAC:
                if dictAC[ac] == pw:
                    #true pw
                    return True
                else:
                    # false pw
                    return False
            else:
                #not ac
                return False
            
        except:
            #input error
            return False
        
        
if __name__ == "__main__":
     d = DatabaseFunc("shopping.db")
     print(d.resetDB())
#    print("Original")
     print(d.selectAllDatabase())
#    
#    
#    print("\nAfter update")
#    print(d.updateDB([[1,5]]))
#    print(d.selectAllDatabase())
#    
#    print("\nCheck quantity")
#    print("check Product id 2 enough 25: ", end='')
#    print(d.QuantityInDatabase([[2, 25]]))
#    
#    print("check Product id 2 enough 5: ", end='')
#    print(d.QuantityInDatabase([[2, 5]]))
#    
#    
#    print("\nAfter insert")
#    listItem = ['Lemon', 'Thiland', 3, 105]
#    print(d.insertItem(listItem))
#    print(d.selectAllDatabase())
#    print("\nDiscount")
#    print(d.discountDB("PROMOCODE30"))
#    
#    dis = d.insertDiscount("YUU",'$',20)
#    print("Discount insert",dis)
#    
#    print(d.discountDB("YUU"))
#    print("show all deiscount")
#    print(d.showAllDisecount())
#    
#    #print("\n delete Discount")
#    #print(d.deleteDiscount("PROMOCODE30"))
#    #print("show all deiscount")
#    #print(d.showAllDisecount())
#    
#    
#    print("\ninsert record")
#    name = 'Ken'
#    total = 189
#    dis = "10.0% off"
#    prodList = "[[7, 2, 'Durian', 80, 160],[3, 10, 'Banana', 5, 50]]"
#    re = d.insertRecord(name, total, dis, prodList)
#    print(re)
#    
#    re = d.showeRecord()
#    print(re)
     print(d.checkAccount("tim","1243"))