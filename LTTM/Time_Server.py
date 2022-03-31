# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:33:15 2022

@author: Dom Dai
"""

from time import ctime

#lay thoi gian he thong  : ctime
#host : "127.0.0.1", port = 9050
#bytes(ctime(),'utf-8')
#server
import socket
import sys 

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as err:
        print("Error: %s"%str(err))
        sys.exit()
    print("Da tao duoc socket")
    host = "127.0.0.1"
    port = 9050
    
    sk.bind((host,port))
    sk.listen(5)
    sk.setsockopt(socket.S0L_SOCKETL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        print("waiting for client")
        client_sk,client_addr = sk.accept()
        print("Dia chi client: ",client_addr)
        data = client_sk.recv(4096)
        if not data or data.decode("utf-8")!= 'time':
            break;
        client_sk.send(bytes(ctime(),'utf-8'))
        client_sk.close()
    sk.close()