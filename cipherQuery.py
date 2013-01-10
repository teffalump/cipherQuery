#!/usr/bin/python
#
#
#
#
#
#
import sys,ssl,socket

#ciphers
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.set_ciphers("ALL:NULL")

#port for https
port = 443

#websites list
f = sys.argv[1]

#read website list into list
with open(f,'r') as a:
    websites = a.read().split('\n')

#read ciphers into list
for site in websites:
    with socket.socket() as sock:
        try:
            con = context.wrap_socket(sock)
            con.settimeout(2)
            con.connect((site,port))
            cipher=con.cipher()
            print(site,cipher)
        except: pass
