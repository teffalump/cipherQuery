#!/usr/bin/python
import sys,ssl,socket

def website_cipher(url):
    with socket.socket() as sock:
        con = context.wrap_socket(sock)
        con.settimeout(5)
        try:
            con.connect((url,PORT))
            cipher=con.cipher()
            return (url,cipher)
        except: return (url, False)

#port for https
PORT = 443

#read website list into list
f = sys.argv[1]
with open(f,'r') as a:
    WEBSITES = a.read().split()

#cipher string
if len(sys.argv) != 3: 
    CIPHER_STRING = "DEFAULT"
else:
    CIPHER_STRING = sys.argv[2]

#ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.set_ciphers(CIPHER_STRING)

#read ciphers into list
for site in WEBSITES:
    print(website_cipher(site))
