# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:18:58 2022

@author: Dom Dai
"""

import paramiko

def test_ssh(host,port,user,password,cmd):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #connect
    
    ssh.connect(host,port,user,cmd)
    
    
    #thuc hien lenh
    
    stdin,stdout,stderr=ssh.exec_command(cmd)
    output=stdout.read().decode()
    print(output)

if __name__=='__main__':
    host = '127.0.0.1'
    port = 22
    user = 'daicici'
    password = '123'
    cmd = 'ls'
    test_ssh(host, port, user, password, cmd)