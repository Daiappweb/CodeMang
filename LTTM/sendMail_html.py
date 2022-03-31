# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:48:27 2022

@author: Dom Dai
"""

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__=='__main__':
    from_addr = "daiappweb@gmail.com"
    to_addr = "daiappweb@gmail.com"
    password = "Dai@@28032001"
    smtp_server = "smtp.gmail.com"
    port = 465
    
    #soan noi dung
    #header
    message = MIMEMultipart("multipart") #bỏ multipart cho kết quả tương tự
    message["Subject"] = "Test email"
    message["From"] = from_addr
    message["To"] = to_addr
    
    #body
    #tao text va html
    
    body = """\
        Hello, this is a test email"""
        
    html = """\
        <html>
        <body>
        <p>Hello world</p>
        <a href="http://www.utc.edu.vn">UTC</a>
        
        </body>
        </html>

    """
    
    #ghep text va html
    ms1 = MIMEText(body,"plain")
    ms2 = MIMEText(html,"html")
    
    #attach vao message
    message.attach(ms1)
    message.attach(ms2)
    
    #tao ket noi
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server,port,context=context)
    
    #login
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,message.as_string())