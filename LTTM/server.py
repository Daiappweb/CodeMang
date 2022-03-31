# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:19:45 2022

@author: Dom Dai
"""
#SERVER
import socket
HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST,PORT)

if __name__=='__main__':
        serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serverSocket.bind(ADDR)
        serverSocket.listen(5)
        serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        while True:
            print("Waiting for connect")
            clientSocket, addr = serverSocket.accept()
            print("Connect from",addr)
            while True:
                data = clientSocket.recv(BUFSIZE)
                print("Recive : %s"%data.decode("UTF-8"))
                clientSocket.send(data)
                break
            break
                