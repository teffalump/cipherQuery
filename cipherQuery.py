#!/usr/bin/python
import sys,ssl,socket

def website_cipher(url):
    with socket.socket() as sock:
        con = context.wrap_socket(sock)
        con.settimeout(5)
        try:
            con.connect((url,PORT))
            cipher=con.cipher()
            return {'site':url,'suite':cipher[0]}
        except: return {'site': url, 'suite': False, 'size': False}

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

#print
results = [ website_cipher(site) for site in WEBSITES ]

#cli output
#width=max(map(len, [result['site'] for result in results if result['site'] != False]))
#sformat="{:{width}}\t{:}"
#print(sformat.format("SITE", "SUITE", width=width))
#for result in results:
    #if result['suite'] == False: 
        #print("{0}".format(result['site']))
    #else:
        #print(sformat.format(result['site'], result['suite'], width=width))

#html output
print("<table><tr><td><b>Site</b></td><td><b>Suite</b></td></tr>")
for result in results:
    if result['suite'] == False: 
        print("<tr><td>{0}</td><td>{1}</td></tr>".format(result['site'], ""))
    else:
        print("<tr><td>{0}</td><td>{1}</td></tr>".format(result['site'], result['suite']))
print("</table>")
