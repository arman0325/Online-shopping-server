# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 15:37:40 2021

Student name: Yuen Yiu Man
Student ID: 12133174
Course: COMPS362F

This program is server-side program
"""

import socket
import _thread
import FuncPart # help to string to list
import DatabaseFunction
import time


dictBuy = {'admin0325':[[]]}
dictProduct = {}
def multi_threaded_client(connection):
    
    try:
        connection.send(str.encode('Server is working:'))
        db = DatabaseFunction.DatabaseFunc("shopping.db")
        #updateDictAmount(db)
        while True:
            adminData = connection.recv(1024)
            data = adminData.decode('utf-8')
            response = 'Server message: ' + data
            
            if data == "S":# stop the server and client
                FuncPart.stop()
                break
            
            elif data == "P":
                prodList = str(db.selectAllDatabase()) #using str() change the data to str that help sendall
                #print(prodList)
                
                response = prodList
                connection.send(bytes(1)) #send the type
                
            elif data == "Pr":
                prodList = str(db.selectAllDatabase()) #using str() change the data to str that help sendall
                #print(prodList)
                response = prodList
                connection.send(bytes(999)) #send the type
                
            elif data =="Pay":
                a_lock = _thread.allocate_lock()
                a_lock.acquire()
                name = str(connection.recv(1024),encoding='UTF-8')
                print(name)
                if db.QuantityInDatabase(dictBuy[name]):
                    print(dictBuy[name])
                    total = 0
                    for x in dictBuy[name]:
                        total += x[4]
                    
                    re="The total is {}$".format(total)
                    print(re)
                    connection.send(str.encode(re))
                    connection.send(bytes(105))
                    disCode = connection.recv(1024)
                    #print(disCode)
                    if disCode == bytes(106):
                        re = "No promo code"
                        disRe="Not discount"
                    else:
                        disCode = str(disCode,encoding='UTF-8')
                        dis = db.discountDB(disCode)
                        disRe=""
                        if dis != "None":
                            if dis[2] == "%":
                                total = total * dis[3]
                                re = "The discount is {}% off\nThe total is {}$ after discount".format(100 - dis[3]*100, total)
                                disRe="{}% off".format(100 - dis[3]*100)
                            else:
                                total -= dis[3]
                                re = "The discount is {}$\nThe total is {}$ after discount".format(dis[3], total)
                                disRe="{}$".format(dis[3])
                        else:
                            re = "This promo code is does not exist"
                            disRe="Not discount"
                    print(re)
                        
                    connection.send(str.encode(re))
                    connection.send(bytes(100))
                    confirm = connection.recv(1024)
                    if confirm == bytes(101):
                        print("confirm")
                        print(db.updateDB(dictBuy[name]))
                        #print(name)
                        #print(total)
                        print(disRe)
                        #print(dictBuy[name])
                        print(db.insertRecord(name, total, str(disRe), str(dictBuy[name])))
                        result = "Payment successful"
                        try:
                            del dictBuy[name]
                        except:
                            ("Del error")
                    else:
                        print("Cancel")
                else:
                    connection.send(bytes(103))
                    result = "Unsuccessful, since the Quantity is not enough"


                response = str(result)
                print(response)
                a_lock.release()
                connection.send(bytes(2))
                #pass

                
            elif data =="Show":
                name = str(connection.recv(1024),encoding='UTF-8')
                #print(name)
                
                connection.send(bytes(3))
                
                response = str(dictBuy[name])
            
            elif data =="Inseret":
                updateDictAmount(db)
                listBuy = FuncPart.StringToList(str(connection.recv(1024),encoding='UTF-8'))
                #print(listBuy)
                nameOfList = str(connection.recv(1024),encoding='UTF-8')
                #print(nameOfList)
                time.sleep(0.1)
                print(listBuy[0],listBuy[1])
                if listBuy[1]>dictProduct[listBuy[0]]:
                    print("more than")
                elif listBuy[1]<=0:
                    print("cannot zero or negative")
                else:
                    if nameOfList not in dictBuy:
                        newList = []
                        newList.append(listBuy)
                        dictBuy[nameOfList] = newList
                    else:
                        dictBuy[nameOfList].append(listBuy)
                        li = FuncPart.reList(dictBuy[nameOfList])
                        dictBuy[nameOfList] = li
                        #print(li)
                
                print(dictBuy)
                
                connection.send(bytes(4))
                response = "insert successful"
            
            elif data == "Del":
                name = str(connection.recv(1024),encoding='UTF-8')
                #print(nameOfList)
                time.sleep(0.1)
                PID = str(connection.recv(1024),encoding='UTF-8')
                
                time.sleep(0.1)
                POQ = str(connection.recv(1024),encoding='UTF-8')
                if name not in dictBuy:
                    print("The list not thos product")
                else:
                    #print(name,PID,POQ)
                    for x in dictBuy[name]:
                        if x[0] == int(PID):
                            if int(POQ)<=-1:
                                response = "All clear Operation successful"
                                dictBuy[name].remove(x)
                        
                            elif int(POQ) > x[1]:
                                response = "Operation unsuccessful. The Quantity is bigger than original."
                            else:
                                x[1] -= int(POQ)
                                response = "Operation successful"
                                x[4] = x[1]*x[3]#update the total
                
                print(dictBuy)
                
                connection.send(bytes(5))

            elif adminData == bytes(901):
                listItem = str(connection.recv(1024),encoding='UTF-8')
                nListItem = FuncPart.StringToList(listItem)
                print(nListItem)
                try:
                    print(db.insertItem(nListItem))
                    response = "Insert product successful"
                except:
                    response = "Insert product unsuccessful"
            elif adminData == bytes(902):
                listItem = str(connection.recv(1024),encoding='UTF-8')
                nListItem = FuncPart.StringToList(listItem)
                #print(nListItem)
                try:
                    print(db.updateProductDB(nListItem))
                    response = "Update product successful"
                except:
                    response = "Update product unsuccessful"

            elif adminData == bytes(903):
                listItem = str(connection.recv(1024),encoding='UTF-8')
                n = FuncPart.StringToList(listItem)
                try:
                    print(db.insertDiscount(n[0],n[1],n[2]))
                    response = "Insert discount successful"
                except:
                    response = "Insert discount unsuccessful"

            elif adminData == bytes(904):
                disCode = str(connection.recv(1024),encoding='UTF-8')
                print(disCode)
                try:
                    print(db.deleteDiscount(disCode))
                    response = "Delete discount successful"
                except:
                    response = "Delete discount unsuccessful"

            elif adminData == bytes(905):
                try:
                    response = str(db.showAllDisecount())
                    print("show the discount table")
                except:
                    response = "Cannot get the Discount Table"

            elif adminData == bytes(906):
                #print("?")
                try:
                    response = str(db.showRecord())
                    print("show the record table")
                except:
                    response = "Cannot get the record Table"
            
            elif not data:
                break
            connection.sendall(str.encode(response)) # send the final result
            
        connection.close()
    except:
        connection.sendall(str.encode("Fail"))
        connection.close()
    
def runServer():
    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    #ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    
    print('Server is running\nWaiting...')
    ServerSideSocket.listen(5)
    while True:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        _thread.start_new_thread(multi_threaded_client, (Client, ))
        #ThreadCount += 1
        #print('Thread Number: ' + str(ThreadCount))
        
    ServerSideSocket.close()

def updateDictAmount(db):
    prodList = str(db.selectAllDatabase()) #using str() change the data to str that help sendall
    #print(prodList)
    nList = FuncPart.StringToList(prodList)
    for x in nList:
        #print(x[4])
        dictProduct[x[0]] = x[4]
    print("Dict Amount Updated\n",dictProduct)
    
if __name__ == "__main__":
    runServer()
