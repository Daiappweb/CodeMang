# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:10:26 2022

@author: Dom Dai
"""

import smtplib
import ssl

if __name__=='__main__':
    #dung ssl
    
    port=465#cong dung ssl
    password="Dai@@28032001"
    smtp_server = "smtp.gmail.com"
    frommail = "daiappweb@gmail.com"
    tomail = "daiappweb@gmail.com"
    message = """\
        Subject: Test Email
        This is a test email
        """
        
    #tao context ssl
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    
    #login
    server.login("daiappweb@gmail.com", password)
    
    #sau khi login viet lenh gui email
    server.sendmail(frommail
                    , tomail, message)
    