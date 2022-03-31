# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:34:32 2022

@author: Dom Dai
"""
#liet ke cac thu muc dung FTP
import ftplib
from ftplib import FTP

def Test(host,user):
    #ket noi
    ftp=ftplib.FTP(host,user)
    
    #liet ke thu muc
    f=ftp.dir()
    
    files=ftp.nlst()
    files.sort()
    
    #chuyen den thu muc nao do
    ftp.cwd('/ATBM')
    print(len(files))
if __name__=='__main__':
    Test(host='127.0.0.1',user='Daicici')

