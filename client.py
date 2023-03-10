import socket
import sys

#get[0]  is there something/type of message
#get[1]  nick
#get[2]  message from client
#string  the last string client has read

#           HI

string=0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#asking for client data
ipv4=input('Address:')
port=input('Port:')
while True:
    nick=input('Nick:')
    if nick != '':
        break
    else:
        print('You must input something >:(')
server_address=(str(ipv4),int(port))
to_send='j'
string=0

#           MAiN LooP

while True:
        #                       SENDING INFO TO SERVER
    msg_to_send=input('<'+nick+'>')
    if msg_to_send != '':
        data='msg'+'$$$'+nick+'$$$'+msg_to_send
        if to_send == 'j':
            to_send=data+'####sys$$$'+nick+'j&&&&&0'
        else:
            to_send=data+'&&&&&'+str(string)
    else:
        if to_send == 'j':
            to_send='####sys$$$'+nick+'$$$j&&&&&0'
        else:
            to_send='0'
        #trying to connect(this is important bcz if sock is alr. cnncted we'll get an error!)
    try:
        sock.connect(server_address)
    except:
            #just ZZZ
        pass
    sock.sendall(to_send.encode())
        #                       GETTING INFO FROM SERVER
        # sending number of the last string client has read
        # we want server to know what messages he have to send
        # recieving, decoding and splitting ('msg1####msg2' ==> ['msg1','msg2'])
    inf=sock.recv(102400)
    inf=inf.decode().split('####')
        #print messages
    if inf != '0':
        for msg in inf:
            print(msg)
            string=string+1
sock.close()
