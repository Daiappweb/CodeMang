# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:15:09 2022

@author: Dom Dai
"""

import socket
import sys 

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as err:
        print("Error: %s"%str(err))
        sys.exit()
    print("Da tao duoc socket")
    host = input("Nhap host: ")
    port = int(input("Nhap port: "))
    try:
        sk.connect((host,port))
        print("Da ket noi den %s tren port %s"%(host,port))
        sk.shutdown(2)
    except socket.error as err:
        print("Error: %s"%str(err))
        sys.exit()