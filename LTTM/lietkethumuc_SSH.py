# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:29:39 2022

@author: Dom Dai
"""
#lietke thuc muc dung ssh
import paramiko 

host='127.0.0.1'
user='Daicici'

#connect
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host,port=21,username=user)

#liet ke cac thu muc
stdin,stdout,stderr=ssh.exec_command('ls')
print(stdin)