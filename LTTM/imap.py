# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:06:43 2022

@author: Dom Dai
"""

import imaplib
import getpass
import pprint

imap_server = "imap.googlemail.com"
port = "993"
def receive_email(username,password):
    mailbox = imaplib.IMAP4_SSL()(imap_server,port)
    mailbox.login(username,password)
    mailbox.select("Inbox")
    tmp,data=mailbox.search(None,"ALL")
    for n in data[0].split():
        tmp,data=mailbox.fetch(n, '(RFC822)')
        print("Email: {0}".format(n))
        pprint.pprint(data[0][1])
        break
   
    mailbox.close()
    mailbox.logout()
if __name__=="__main__":
    username="daiappweb@gmail.com"
    password = getpass.getpass(prompt="Nhap password: ")
    receive_email(username, password)