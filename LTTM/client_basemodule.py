# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:57:25 2022

@author: Dom Dai
"""

import basemodule
import socket
host = basemodule.host
port = basemodule.port

if __name__=='__main__':
    while True:
        try:
            sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sk.connect((host,port))
            print("Enter message (q to exit): ")
            msg = input()
            if msg == 'q':
                break;
            basemodule.send_msg(sk, msg)
            print("send: {}".format(msg) )
            msg = basemodule.recv_msg(sk)
            print("receive "+msg)
        except ConnectionError:
            print("socket error ")
            break
        finally:
            sk.close()