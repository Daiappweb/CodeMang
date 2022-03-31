# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:25:15 2022

@author: Dom Dai
"""

#lay dia chi ip
import socket

#lay dia chi host
hostname= socket.gethostname()

#lay ip cua host o tren
ipaddr= socket.gethostbyname(hostname)

#in thong tin
print("hostname: "+hostname)
print("IP Address: "+ipaddr)