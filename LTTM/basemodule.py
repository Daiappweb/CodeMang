# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:30:52 2022

@author: Dom Dai
"""
#xay dung base modul

import socket
host = '127.0.0.1'
port = 9050

def create_socket(host,port):
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET
                  ,socket.SO_REUSEADDR, 1)
    sk.bind((host,port))
    sk.listen(10)
    return sk
def recv_msg(sk):
    #nhan cho den khi gap null
    data = bytearray()
    msg = ''
    while not msg:
        data_p = sk.recv(1024)
        if not data_p:
            raise ConnectionError()
        data = data + data_p
        #neu co null
        if b'\0' in data_p:
            msg = data.rstrip()
    msg = msg.decode('utf-8')
    return msg

#tao message (them ki tu null vao message)
def create_message(msg):
    msg = msg + '\0'
    return msg.encode('utf-8')
def send_msg(sk,msg):
    data = create_message(msg)
    sk.sendall(data)