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
    print('Cleaning Chat... \nPreparing for work...')
#    with open('content/Chat.txt', 'w') as file:
#        file.write('')
    print('Server is ready for work')
    print('Queue started - waiting for clients')

#           MAiN LooP
    
    while True:
        # accepting one client
        connection, client_address = sock.accept()
        # recieving data
        inf=connection.recv(1024)
        print('Got: '+inf.decode())
        got=inf.decode().split('&&&&&')
        inf=got[0].split('####')
        with open('content/Chat.txt','a') as file:
            for msg in inf:
                file.write('\n'+msg)
        #       SENDING INFO
        #   finding the string
        # how many Strings In File (SIF)
        with open('content/Chat.txt','r') as file:
            fs=file.read().split('\n')
        fs.pop(0)
        sif=len(fs)
        # decoding message
        stringmsg=int(got[1])
        print('Strings: '+str(stringmsg))
        # creating list of new messages for client
        to_send=[]
        count=0
        string=stringmsg
        if fs != stringmsg:
            for strnow in fs:
                count=count+1
                if count > stringmsg:
                    to_send.append(strnow)
                    string=string+1
            data=''
            for message in to_send:
                if data == '':
                    data=message
                else:
                    data=data+'####'+message
        else:
            data='0'
        print('Sent: '+data)
        #sending data
        connection.send(data.encode())
        connection.close()
sock.close()
