#!/usr/bin/python
#
#
#
#
#
#
import sys,ssl

#port for https
port = 443

#websites list
f = sys.argv[1]

#read website list into list
with open(f,'r') as a:
    w = a.read().split('\n')

for site in w:
    with ssl.SSLSocket() as c:
        try:
            c.settimeout(2)
            c.connect((site,port))
            cipher=c.cipher()
            print(site,cipher)
        except: pass
