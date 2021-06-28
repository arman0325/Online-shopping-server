# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:37:40 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program is clinet-side program
"""

import socket
import FuncPart
import time
import DatabaseFunction

AC=""  # user name
comList = ['L', 'P', 'B', 'C'] 
PList = []
listBuy = []

def preRun():
    #this is prerun to get the Plist
    run("Pr")

def run(msg, msgType = 0):
    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    
    #print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    
    res = ClientMultiSocket.recv(1024)
   # while True:
        #Input = input('Hey there: ')
        
    if msgType == 0:
        ClientMultiSocket.send(msg.encode('utf-8'))
        num = ClientMultiSocket.recv(1024)
        if(num==bytes(999)): #Print the Product List
            res = ClientMultiSocket.recv(1024)
            list_a = FuncPart.StringToList(res.decode('utf-8'))
            PList.extend(list_a)
        
        if(num==bytes(1)): #Print the Product List
            res = ClientMultiSocket.recv(1024)
            printListTable(res.decode('utf-8'), 1)
        ClientMultiSocket.close()
        
            
    elif msgType == 10: #payment
        key = "Pay"
        ClientMultiSocket.sendall(key.encode('utf-8'))
        newMsg = str(msg)
        #print(newMsg)  #test listBuy
        ClientMultiSocket.sendall(newMsg.encode("utf-8"))
        reMsg = ClientMultiSocket.recv(1024)
        #total = ClientMultiSocket.recv(1024).decode('utf-8')
        #print("Y",bytes(reMsg))
        if reMsg != bytes(103):
            print(reMsg.decode('utf-8'))
            num = ClientMultiSocket.recv(1024)
            if num == bytes(105):
                while True:
                    Code = str(input("Enter the promo code(if none, enter '-1'): "))
                    if Code =="-1":
                        ClientMultiSocket.sendall(bytes(106))
                        break
                    elif Code != "-1":
                        ClientMultiSocket.sendall(Code.encode("utf-8"))
                        break
                    else:
                        continue
            reMsg = ClientMultiSocket.recv(1024)
            print(reMsg.decode('utf-8'))
            num = ClientMultiSocket.recv(1024)
            if num == bytes(100):
                while True:
                    confirm = input("Are you confirm the payment?(Y/N):")
                    if confirm =="Y":
                        ClientMultiSocket.sendall(bytes(101))
                        break
                    elif confirm =="N":
                        ClientMultiSocket.sendall(bytes(102))
                        break
                    else:
                        continue
        num = ClientMultiSocket.recv(1024)
        if num == bytes(2) :
            res = ClientMultiSocket.recv(1024)
            result = res.decode('utf-8')
            ClientMultiSocket.close()
            print(result)
            
        
    elif msgType == 11: #show the table of shopping cart
        key = "Show"
        ClientMultiSocket.sendall(key.encode('utf-8'))
        newMsg = str(msg)
        #print(newMsg)
        time.sleep(0.1)
        ClientMultiSocket.sendall(newMsg.encode("utf-8"))
        num = ClientMultiSocket.recv(1024)
        if num == bytes(3):
            res = ClientMultiSocket.recv(1024)
            result = res.decode('utf-8')
            ClientMultiSocket.close()
            return result
        
    elif msgType == 12: #insert to Buylist
        key = "Inseret"
        ClientMultiSocket.sendall(key.encode('utf-8'))
        newMsg = str(msg[0])
        name = str(msg[1])
        #print(newMsg,name)
        time.sleep(0.1)
        ClientMultiSocket.sendall(newMsg.encode("utf-8"))
        time.sleep(0.1)
        ClientMultiSocket.sendall(name.encode("utf-8"))
        num = ClientMultiSocket.recv(1024)
        if num == bytes(4):
            res = ClientMultiSocket.recv(1024).decode('utf-8')
            #print(res)
            ClientMultiSocket.close()
            return res
        
    elif msgType == 13: #insert to Buylist
        key = "Del"
        ClientMultiSocket.sendall(key.encode('utf-8'))
        
        name = str(AC)
        PID = str(msg[0])
        POQ = str(msg[1])
        #print(newMsg,name)
        time.sleep(0.1)
        ClientMultiSocket.sendall(name.encode("utf-8"))
        time.sleep(0.1)
        ClientMultiSocket.sendall(PID.encode("utf-8"))
        time.sleep(0.1)
        ClientMultiSocket.sendall(POQ.encode("utf-8"))
        num = ClientMultiSocket.recv(1024)
        if num == bytes(5):
            res = ClientMultiSocket.recv(1024).decode('utf-8')
            #print(res)
            ClientMultiSocket.close()
            return res
        
        
    elif msgType == 901:
        ClientMultiSocket.sendall(bytes(901))
        newMsg = str(msg)
        ClientMultiSocket.sendall(newMsg.encode("utf-8"))        
        re = ClientMultiSocket.recv(1024).decode('utf-8')
        ClientMultiSocket.close()
        print(re)
        
    elif msgType == 902:
        ClientMultiSocket.sendall(bytes(902))
        newMsg = str(msg)
        ClientMultiSocket.sendall(newMsg.encode("utf-8"))        
        re = ClientMultiSocket.recv(1024).decode('utf-8')
        ClientMultiSocket.close()
        print(re)
        
    elif msgType == 903:
        ClientMultiSocket.sendall(bytes(903))
        newMsg = str(msg)
        ClientMultiSocket.sendall(newMsg.encode("utf-8"))        
        re = ClientMultiSocket.recv(1024).decode('utf-8')
        ClientMultiSocket.close()
        print(re)
        
    elif msgType == 904:
        ClientMultiSocket.sendall(bytes(904))
        ClientMultiSocket.sendall(msg.encode("utf-8"))        
        re = ClientMultiSocket.recv(1024).decode('utf-8')
        ClientMultiSocket.close()
        print(re)    
        
    elif msgType == 905:
        ClientMultiSocket.sendall(bytes(905))
        re = ClientMultiSocket.recv(1024).decode('utf-8')
        ClientMultiSocket.close()
        printListTable(re, 3)
    
    elif msgType == 906:
        ClientMultiSocket.sendall(bytes(906))
        re = ClientMultiSocket.recv(1024).decode('utf-8')
        ClientMultiSocket.close()
        printListTable(re, 4)
        
    ClientMultiSocket.close()
    
    
def printListTable(List, Type):
    # ast.literal_eval is help to change the str to list
    if Type == 1:
        list_a = FuncPart.StringToList(List)
        title = ['ID', 'Name','Origin', 'Price', 'Quantity']
        print(FuncPart.printTable(title, list_a))
        
    if Type == 2:
        print("\nYour shopping cart:")
        try:
            title = ['ID', 'Quantity','Name', 'Price', 'Total Price']
            list_a = FuncPart.StringToList(run(AC, 11))
            #print(type(list_a))
            #print(list_a) #check the list in buylist
            print(FuncPart.printTable(title, list_a))
        except:
            print("Your shopping cart have not any Item")
            
    if Type == 3:
        print("\nThe disount table:")
        try:
            title = ['ID', 'Discount Code', 'Type', 'Discount']
            newList = FuncPart.StringToList(List)
            #print(type(list_a))
            #print(list_a) #check the list in buylist
            print(FuncPart.printTable(title, newList))
        except:
            print("No Discount")
    
    if Type == 4:
        print("\nThe record table:")
        try:
            title = ['ID', 'Buyer', 'Payment amount', 'Discount detail', 'Buy List']
            newList = FuncPart.StringToList(List)
            #print(type(list_a))
            #print(list_a) #check the list in buylist
            print(FuncPart.printTable(title, newList))
        except:
            print("No record")
    
    
def buyList():
    BuyListCommand = ['show', 'insert', 'delete', 'payment', 'back', 'C']
    while True:
        try:
            key = str(input("Enter the key (Buy List): "))
            
            if key in BuyListCommand:
                if key == "C":
                    print(FuncPart.printCommandList("Buy"))
                    continue
                
                elif key =="show":
                    try:
                        printListTable(listBuy, 2)
                    except:
                        pass
                    
                elif key =="insert":
                    try:
                        listB = []
                        PID = int(input("Enter the product ID: "))
                        # find the product in buy list
                        prod = list(filter(lambda y : y[0] == PID, PList))
                        QOP = int(input("Enter the Quantity of Product: "))
                        if QOP > prod[0][4]:
                            print("The quantity cannot more than product quantity")
                            break
                        elif QOP <= 0:
                            print("The quantity cannot a negative or zero")
                        else:
                            listB.append(PID)
                            listB.append(QOP)
                            # find the product name and total to buy list
                            prod = list(filter(lambda y : y[0] == PID, PList))
                            listB.append(prod[0][1])
                            listB.append(prod[0][3])
                            listB.append(QOP*prod[0][3])
                            #print(listB, AC)
                            msgList = [listB, AC]
                            print(run(msgList, 12))
                        
                    except:
                        break
                    
                elif key =="delete":
                    try:
                        PID = int(input("Enter the product ID was you wnat to delete: "))
                        QOP = int(input("Enter the Quantity of Product(if all, enter -1): "))
                        print(run([PID,QOP], 13))
                        
                    except:
                        break
                    
                elif key =="payment":
                    try:
                        CreditCard = str(input("Enter the 16 credit card number: "))
                        #print(CreditCard)
                        date = input("Enter the expiry date(mm/yy): ")
                        mm,yy = date.split("/")
                        #print(mm,yy)
                        print("Your credit card number: {}. \nThe expiry date: {}".format(CreditCard,date))
                        if FuncPart.checkCreditCard(CreditCard,int(mm),int(yy)):
                            run(AC,10)
                        else:
                            print("Credit Card input error")
                            break
                    except:
                        print("Input error")
                    
                elif key =="back":
                    break
            
        except:
            print("Please enter the key in command list")
            print("Command list can enter 'C'")
        
        
def main():
    
    global AC, comList
    print("\nHello, ",AC)
    while True:
        #print(comList)
        key = str(input("Enter the key: "))
        if key == 'C': # call command list
            if AC =="admin0325":
                print(FuncPart.printCommandList("admin"))
            else:            
                print(FuncPart.printCommandList("Main"))

        elif key == 'X': # stop the client
            FuncPart.stop()
            
        elif (key in comList):
            if key == 'L':
                break
                
                    
            if key == 'B':
                print(FuncPart.printCommandList('Buy'))
                buyList()
                
            if key == "IP":
                try:
                    prodName = str(input("Enter the prduct name: "))
                    prodOrigin = str(input("Enter the origin of product: "))
                    prodPrice = float(input("Enter the price of product: "))
                    POQ = int(input("Enter the Quantity of product: "))
                    IPList = [prodName, prodOrigin, prodPrice, POQ]
                    #print(IPList)
                    run(IPList, 901)
                except:
                    print("Input type is error")
            
            if key == "UP":
                try:
                    PID = int(input("Enter the product ID: "))
                    POQ = int(input("Enter the update quantity of product: "))
                    run([PID, POQ],902)
                except:
                    print("Input type is error")
                    
            
            if key == "IS":
                while True:
                    disCode = str(input("Enter at least 5 length the discount code(e.g PROMOCOD17):"))
                    if len(disCode)<5:
                        continue
                    else:
                        break
                    
                while True:
                    disType = str(input("Enter the type of discount('%' = precent, '$' = money):"))
                    if disType == '%' or disType == '$':
                        break
                    else:
                        continue
                    
                print("If the discount is '%', please enter percentage(e.g. 0.8)\nThe range is 0.2-0.99\n")
                print("If the discount is '$', please enter money amout(e.g. 30)\nThe range is 10-100")    
                while True:
                    discount = float(input("Enter the discount:"))
                    if disType == '%':
                        if discount < 0.2 or discount > 0.99:
                            print("The discount out of range")
                            continue
                        else:
                            break
                    if disType == '$':
                        if discount <10 or discount > 100:
                            print("The discount out of range")
                            continue
                        else:
                            break
                disMsg = [disCode, disType, discount]
                run(disMsg, 903)
                        
                        
            if key == "DD":
                disCode = str(input("Enter the discount code that you want to delete: "))
                db = DatabaseFunction.DatabaseFunc("shopping.db")
                discount = db.showAllDisecount()
                for x in discount:
                    if disCode == x[1]:
                        #print("Yes")
                        confirm = input("Are you confirm to delete discount code of '{}'?\(Y/N): ".format(disCode))
                        #print(disCode)
                        if confirm == 'Y':
                            run(disCode,904)
                        break
                else:
                    print("Not this discount code in database")
                pass
            
            if key == "SD":
                run("SD",905)
                pass
            
            if key == "SR":
                run("SR",906)
                pass
                
                
            else:
                run(key)
        
        else:
            print("Please enter the key in command list")
            print("Command list can enter 'C'")
    
def login():
    global AC, comList
    while True:
        userName = str(input("Enter the user name: "))
        pw = input("Enter the password: ")
        db = DatabaseFunction.DatabaseFunc("shopping.db")
        if db.checkAccount(userName,pw):
            AC = userName
            if AC == 'admin0325':
                
                print('\nPlease enter the key of command')
                print(FuncPart.printCommandList("admin"))
                comList = ['L', 'P', 'IP', 'UP', 'IS', 'DD', 'SD', 'SR', 'S', 'C','X']
            else:   
                print('\nPlease enter the key of command')
                print(FuncPart.printCommandList("Main"))
                comList = ['L', 'P', 'B', 'C']
            break
        else:
            print("username or password is wrong")
            continue

    
if __name__ == "__main__":
    while True:
        login()
        #print(AC)
        preRun()
        #print(PList) #check preRun successful
        main()
    