# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:24:52 2022

@author: Dom Dai
"""

#lay thong tin tu 1 web bang send va recive

import socket
import sys 

if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as err:
        print("Error: %s"%str(err))
        sys.exit()
    print("Da tao duoc socket")
    host ="www.linux.org"
    port = 80
    
    sk.connect((host,port))
    while True: 
        
        rq = "GET /HTTP/1.0\r\n\r\n"
        sk.send(rq.encode('utf-8')) #gui den sever
        
        #nhan du lieu tu sever
        data = sk.recv(4096)
        if not data:
            break
        print(data.decode('utf-8'))
    sk.close()
        
    