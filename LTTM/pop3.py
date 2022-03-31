# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:48:09 2022

@author: Dom Dai
"""

import poplib
import getpass

pop_server = "pop.googlemail.com"
port = "995"
def receive_email(username,password):
    mailbox = poplib.POP3_SSL(pop_server,port)
    mailbox.user(username)
    mailbox.pass_(password)
    n=len(mailbox.list()[1])
    print("Tong so email: {0}".format(n))
    for email in mailbox.retr(n)[1]:
        print(email)
    mailbox.quit()
if __name__=="__main__":
    username="daiappweb@gmail.com"
    password = getpass.getpass(prompt="Nhap password: ")
    receive_email(username, password)
    
    