# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:21:29 2022

@author: Dom Dai
"""

import csv
import smtplib
import ssl
if __name__=='__main__':
    from_addr = "daiappweb@gmail.com"
    to_addr = "daiappweb@gmail.com"
    password ="Dai@@28032001"
    smtp_server ="smtp.gmail.com"
    port = 465
    message = """Subject : Gui diem
    Kinh gui {hoten},diem cua ban la {diem}
    """
    #login
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server,port,context=context)
    server.login(from_addr, password)
    
    #doc file csv
    filename = open("test.csv")
    data = csv.reader(filename)
    next(data)
    #duyet tat ca cac record(hang)
    for hoten, email, diem in data:
        server.sendmail(from_addr, email, message.fomat(hoten=hoten,diem=diem))
    