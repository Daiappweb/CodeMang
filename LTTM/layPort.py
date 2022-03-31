# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:04:55 2022

@author: Dom Dai
"""

import socket


if __name__=='__main__':
    host = 'www.utc.edu.vn'
    ip_addr = socket.gethostbyname(host)
    port = 80
    while True:
        try:
            sk = socket.socket()
            kq = sk.connect((ip_addr,port))
            print("Port {0}: Open ".format(port))
            sk.close()
        except:
            print("Port {0} close".format(port))