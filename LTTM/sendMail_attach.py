# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 07:26:31 2022

@author: Dom Dai
"""

import smtplib
import ssl
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase


if __name__=='__main__':
    from_addr = "daiappweb@gmail.com"
    to_addr = "daiappweb@gmail.com"
    password="Dai@@28032001"
    smtp_server="smtp.gmail.com"
    port=465
    
    #header
    message = MIMEMultipart()
    message["From"] = from_addr
    message["To"] = to_addr
    message["Subject"] = "Test email"
    message["Bcc"] = "maithuy1707van@gmail.com"
    
    #body
    body = "This is a test email with file attached"
    
    #add to message
    message.attach(MIMEText(body,"plain"))
    
    #attach file
    filename = "laydiachi_IP.py"
    #openfile
    file_attach = open(filename,"rb")
    attach = MIMEBase("application", "octect-stream")
    attach.set_payload(file_attach.read())
    
    #ma hoa thanh dang ascii
    encoders.encode_base64(attach)
    
    #key-value cho attachment
    attach.add_header("Content-Disposition", f"attachment; filename={filename}",)
    #add file attach vao message
    message.attach(attach)
    
    #login and send
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server,port,context=context)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, message.as_string())
    
    
    