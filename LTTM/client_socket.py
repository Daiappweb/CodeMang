# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:51:29 2022

@author: Dom Dai
"""

#socket dung TCP
#client
import socket
HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST,PORT)


if __name__=='__main__':
        clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        #connect
        clientSocket.connect(HOST,ADDR)
        data = "Hello"
        try:
            while True:
                clientSocket.send(data.encode("UTF-8"))
                datal = clientSocket.recv(BUFSIZE)
                print(repr(datal))
        except Exception:
            pass
        finally:
            pass
                


