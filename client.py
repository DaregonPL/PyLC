import socket
import sys

#get[0]  is there something/type of msg
#get[1]  nick
#get[2]  msg
#get[3]  string

string=0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4=input('Address:')
port=input('Port:')
while True:
    nick=input('Nick:')
    if nick != '':
        break
    else:
        print('You must input something >:(')
server_address=(str(ipv4),int(port))
sock.connect(server_address)
data='sys$$$'+nick+'$$$j'
sock.sendall(data.encode())
sock.close()
while True:
    data='msg'+'$$$'+nick+'$$$'+input('<'+nick+'>')+'$$$'+str(string)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    sock.sendall(data.encode())
    inf=sock.recv(1024000)
    inf=inf.decode()
    msg=inf.split('####')
    if len(msg) != 1:
        string=string+len(msg)
        for stringnow in msg:
            if stringnow == '':
                pass
            else:
                got=stringnow.split('$$$')
                try:
                    print('<'+got[1]+'>'+got[2])
                except:
                    print(got[1])
            string=string+1
        string=string-1
    else:
        get=inf.split('$$$')
        ggg=get
        if get[0] == '0':
            pass
        elif get[0] == '1':
            print('<'+get[1]+'>'+get[2])
            string=string+int(get[3])
    sock.close()
