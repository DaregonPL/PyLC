import socket
import sys
import os
#           GLOBAL

connectionlist=[]
numberclients=0
string=0

#           HELP FUNCTIONS

def checkdigit(check):
    error=False
    if check == '':
        return False
    for num in check:
        if num == '0' or num == '1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9':
            pass
        else:
            error=True
    if error == True:
        return False
    else:
        return True

#           HI

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=input('Port:')
ch=checkdigit(port)
if ch == True:
    sock.bind((str(socket.gethostbyname(socket.gethostname())), int(port)))
    print(socket.gethostbyname(socket.gethostname()))
    listn=input('Queue max len(ENTER for 16):')
    ch=checkdigit(listn)
    if ch == False:
        listn=16
    sock.listen(int(listn))
    print('Server is ready for work')
    print('Queue started - waiting for clients')
    while True:
        connection, client_address = sock.accept()
        data=connection.recv(1024)
        chat=open('content/Chat.txt','a')
        data=data.decode()
        print('got: '+data)
        get=data.split('$$$')
        if get[0] == 'msg':
            data=get[1]+'$$$'+get[2]
            string=int(get[3])
        elif get[0] == 'sys':
            if get[2] == 'j':
                get[2]=' joined this server.'
            elif get[2] == 'e':
                get[2]=' left.'
            data=get[1]+get[2]
        chat.write('\n'+data)
        chat.close()
        with open('content/Chat.txt', 'r') as file:
            strinfile = sum(1 for line in file)-1
        sendstr=str(strinfile-string)
        chat=open('content/Chat.txt','r')
        txt=chat.read()
        txt=txt.split('\n')
        if sendstr != 1 and get[0] == 'msg':
            data=''
            print(sendstr)
            while True:
                stringnow=txt[string]
                data=data+'####1$$$'+stringnow+'$$$1'
                string=string+1
                if strinfile == string:
                    break
            lastmsg=txt[len(txt)-1]
        else:
            lastmsg=txt[len(txt)-1]
        chat.close()
        if sendstr == 0:
            data='0$$$None'
        elif sendstr == 1:
            data='1$$$'+lastmsg+'$$$'+str(sendstr)
        print('sent: '+data)
        connection.send(data.encode())
        connection.close()
sock.close()
