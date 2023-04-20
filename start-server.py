import socket
import sys
import os
import time
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
while True:
    ans=input('Choose type of server:\n1. Public (by default) --- anyone from your wifi can connect to your server\n2. Local --- just on this device\n|')
    if ans == '' or ans == '1' or ans == '2':
        break
    else:
        print('Wrong answer')
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=input('Port:')
ch=checkdigit(port)
if ch == True:
    if ans == '' or ans == '1':
        sock.bind((str(socket.gethostbyname(socket.gethostname())), int(port)))
        print('Address: '+socket.gethostbyname(socket.gethostname()))
    else:
        sock.bind(('', int(port)))
        print('Address: 127.0.0.1')
    listn=input('Queue max len(ENTER for 16):')
    ch=checkdigit(listn)
    if ch == False:
        listn=16
    sock.listen(int(listn))
    print('Cleaning chat...')
    chatfile=open('content/chats/Chat.txt', 'w')
    chatfile.write('')
    chatfile.close()
    print('Server is ready for work')
    print('Queue started - waiting for clients')
    ID=0
    while True:
        connection, client_address = sock.accept()
        userleft=False
        data=connection.recv(16)
        size=data.decode().split('&&&')
        print('\nSize:'+size[0]+' bytes')
        if int(size[0]) > 16:
            numof=(int(size[0])-16)/16
            checkround=str(round(numof,1)).split('.')
            if checkround[1] != '0':
                numof=int(checkround[0])+1
            else:
                numof=int(checkround[0])
            for x in range(numof):
                data=data+connection.recv(16)
        data=data.decode()
        print('Got:'+data)
        msgdata=data.split('&&&')[1]
        msgsplit=msgdata.split('$$$')
        if msgsplit[0] != 'str' and msgsplit[0] != 'sys':
            ID=ID+1
            tofile=msgsplit[0]+'$$$'+msgsplit[1]+'$$$'+msgsplit[2]+'$$$'+str(ID)
            chatfile=open('content/chats/Chat.txt', 'a')
            chatfile.write('\n'+tofile)
            chatfile.close()
            string=int(msgsplit[3])
            print('ID given:'+str(ID))
        elif msgsplit[0] == 'str':
            string=int(msgsplit[1])
        elif msgsplit[0] == 'sys':
            ID=ID+1
            tofile=msgsplit[0]+'$$$'+msgsplit[1]+'$$$'+msgsplit[2]+'$$$'+str(ID)
            chatfile=open('content/chats/Chat.txt', 'a')
            chatfile.write('\n'+tofile)
            chatfile.close()
            if msgsplit[2] == 'l':
                userleft=True
            else:
                string=int(msgsplit[3])
            print('ID given:'+str(ID))
        if userleft==False:
            chatfile=open('content/chats/Chat.txt', 'r')
            chatdata=chatfile.read()
            chatdata=chatdata.split('\n')
            strnum=0
            tosend=''
            for msg in chatdata:
                if strnum > string:
                    if tosend == '':
                        tosend=msg
                    else:
                        tosend=tosend+'####'+msg
                strnum=strnum+1
            inb=len(tosend.encode())+3
            inb=len(str(inb))+inb
            tosend=str(inb)+'&&&'+tosend
            print('Size of message to send:'+str(inb))
            print('To send:'+tosend)
            connection.send(tosend.encode())
            time.sleep(0.1)
        connection.close()
sock.close()
