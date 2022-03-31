# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:46:11 2022

@author: Dom Dai
"""
#server
import basemodule
host = basemodule.host
port = basemodule.port

def client_process(sk,addr):
    try:
        msg = basemodule.recv_msg(sk)
        print("{}:{}".format(addr,msg))
        basemodule.send_msg(sk, msg)
    except (ConnectionError,BrokenPipeError()):
        print("socket error")
    finally:
        sk.close()
if __name__=='__main__':
    sk = basemodule.create_socket(host, port)
    addr = sk.getsockname()
    print("listent on local port {} ".format(addr))
    while True:
        client_sk, addr = sk.accept()
        print("connection from: {} ".format(addr))
        client_process(client_sk, addr)