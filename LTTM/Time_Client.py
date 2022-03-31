# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:01:01 2022

@author: Dom Dai
"""

#client
import socket
import sys 

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as err:
        print("Error: %s"%str(err))
        sys.exit()
    print("Da tao duoc socket")
    host ="127.0.0.1"
    port = 9050
    
    sk.connect((host,port))
    
    data = "time"
    sk.send(data.encode('utf-8'))
    
    data = sk.recv(4096)
    
    print(data.decode('utf-8'))
    sk.close()