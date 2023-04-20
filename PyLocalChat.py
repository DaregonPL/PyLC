'''PyLocalChat v.2.0'''
'''info() to see the instruction'''

import hashlib
import time
from datetime import datetime
import getpass
import socket
#                               GLOBAL VARIABLES
mh=None
at=None
Npassw = None
Nnick = None
acclist = None
loggedin = None
quickL=None
acclist=None
BREAK = False
#                               FUNCTIONS
#                               info
def info():
    print('F u n c t i u o n s :')
    time.sleep(0.5)
    print('start()    Main function, starts main menu. (Variables only for staff)')
    time.sleep(0.05)
    print('loop()     Starts main loop, which starts main menu')
    time.sleep(0.05)
    print('check()    Function, has couple of modes. Prints Accounts info.')
    time.sleep(0.05)
    print('auth()     Function, using for authification. Needs AccType, Quick-L code, Nickname.')
    time.sleep(0.05)
    print('reg()      Runs registration.')
    time.sleep(0.05)
    print('log_in()   Runs log in.')
    time.sleep(0.05)
    print('log_out()  Clears auth data.')
    time.sleep(0.05)
    print('delete_acc()  Delete account.')
    time.sleep(0.05)
    print('welcome()  Launch menu.')
    time.sleep(0.05)
    print('')
    time.sleep(0.05)
    print('N o t e s :')
    time.sleep(0.5)
    print('Use "welcome()" to avoid errors.')
    time.sleep(0.05)
    print("If you exited and you don't know what to do, restart programm or write "+'"welcome()","start()" or "loop()".')
    time.sleep(0.05)
    print('You cannot cancel deleting account after it is deleted.')
    time.sleep(0.05)
    print('We have no password restore system, so be careful:)')
    time.sleep(0.05)
    print('We see your feedback. Thanks for it :)')
#                               main
def start(AccType='user'):
    global at,loggedin,quickL,BREAK
    at=AccType
    authcheck=open('content/auth.sys','r')
    atext=authcheck.read()
    if atext == '' and loggedin == None:
        print('What are you going to do?')
        print('1. Log in.')
        print('2. Create new account.')
        print('3. EXIT')
        ans=input('|')
        if ans == '1':
            log_in()
        elif ans == '2':
            reg()
        elif ans == '3':
            BREAK=True
        else:
            pass
    elif atext == '' and loggedin != None:
        print('loggedin != None |=> error')
    elif atext != '' and loggedin == None:
        print('Do you want to log in using Quick-L?')
        print('1. Yes.')
        print('2. Log out.')
        ans=input('|')
        if ans == '1':
            print('Use code for Quick-L(ENTER if you forgot)')
            code=input('|')
            alist=atext.split('$$$')
            encode=hashlib.md5(code.encode()).hexdigest()
            if alist[2] == encode:
                print('Account: '+alist[1])
                log('logged in using Quick-L',alist[1])
                if alist[0] == 'admin':
                    print('AccType="admin"')
                    loggedin=['1',alist[1],code]
                    quickL = str(code)
                    start()
                elif alist[0] == 'user':
                    print('AccType="user"')
                    loggedin=['0',alist[1],code]
                    quickL = str(code)
                    start()
                else:
                    print('Wrong AccType.')
                start()
            elif code == '':
                print('Log in again')
            else:
                print('Code or AccType is wrong.')
        elif ans == '2':
            log_out()
            start()
        else:
            pass
    elif atext != '' and loggedin != None and quickL != None:
        if loggedin[0] == '1' and loggedin[2] == quickL:
            au=auth('admin',quickL,loggedin[1])
            if au == True:
                at='admin'
                print('What are you going to do?')
                print('0. Connect to chat')
                print('1. Change AccType.')
                print('2. Delete account.')
                print('3. Change my password.')
                print('4. Log out.')
                print('5. EXIT')
                print('(Enter option number)')
                ans=input('|')
                if ans == '1':
                    change_acctype()
                elif ans == '2':
                    delete_acc()
                elif ans == '3':
                    change_password()
                elif ans == '4':
                    log_out()
                elif ans == 'xxx':
                    rock(ans)
                elif ans == '5':
                    BREAK=True
                elif ans == '0':
                    chat()
                else:
                    pass
            else:
                print('Error: invalid data. Restart required. We need to restore data.')
        elif loggedin[0] == '0' and loggedin[2] == quickL:
            at='user'
            print('What are you going to do?')
            print('0. Connect to chat')
            print('1. Delete my account.')
            print('2. Change my password.')
            print('3. Log out.')
            print('4. EXIT')
            print('(Enter option number)')
            ans=input('|')
            if ans == '1':
                delete_acc()
            elif ans == '2':
                change_password()
            elif ans == '3':
                log_out()
            elif ans == '4':
                BREAK=True
            elif ans == '0':
                chat()
            else:
                pass
        else:
            print('Something went Wrong')
    else:
        print('Something went Wrong')
#                               login    
def log_in():
    global at,mh,loggedin,quickL
    nick=input('Nickname:')
    passw=input('Password:')
    fileread=open('content/AccBase.sys','r')
    acctxt=fileread.read()
    acclist=acctxt.split('\n')
    fileread.close()
    print('Finding your nickname')
    for checked in acclist:
        time.sleep(0.02)
        if checked == '':
                    pass
        else:
            check=checked.split('$$$')
            if nick==check[0]:
                print('>> '+check[0]+'          <<<')
                mh=True
                break
            else:
                print('>> '+check[0])
    if mh == True:
        print('MATCH FOUND')
        pe=hashlib.md5(passw.encode())
        pe=pe.hexdigest()
        if at == 'admin':
            if check[2] == 'admin':
                if pe == check[1]:
                    error=False
                    print('Welcome back admin, '+nick+'!')
                    code=input('Please input Quick-L code (4 numbers): ')
                    coc=0
                    for num in code:
                        coc=coc+1
                        if num == '0' or num == '1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9':
                            pass
                        else:
                            print('Incorrect symbol: '+num)
                            error=True
                    print(str(coc)+' numbers')
                    if error == True or coc != 4:
                        print('Code cannot be used: Incorrect symbol or wrong number of characters')
                        print('Log in again.')
                    else:
                        loggedin=['1',check[0],code]
                        quickL = str(code)
                        auth=open('content/auth.sys','w')
                        ne=hashlib.md5(loggedin[2].encode())
                        ne=ne.hexdigest()
                        auth.write('admin'+'$$$'+loggedin[1]+'$$$'+ne)
                        auth.close()
                        print('Use this code for quick-login later')
                        log('logged in as admin.',check[0])
                        start()
                else:
                    print('Password is incorrect.')
            else:
                print('You have no admin right')
                print('Log in as user(just EXIT and log in again)')
        elif at == 'user':
            if check[2] == 'user' or check[2] == 'admin':
                if pe == check[1]:
                    error=False
                    print('Welcome back, '+nick+'!')
                    code=input('Please input Quick-L code (4 numbers): ')
                    coc=0
                    for num in code:
                        coc=coc+1
                        if num == '0' or num == '1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9':
                            pass
                        else:
                            print('Incorrect symbol: '+num)
                            error=True
                    print(str(coc)+' numbers')
                    if error == True or coc != 4:
                        print('Code cannot be used: Incorrect symbol or wrong number of characters')
                        print('Log in again.')
                    else:
                        loggedin=['0',check[0],code]
                        quickL = str(code)
                        auth=open('content/auth.sys','w')
                        ne=hashlib.md5(loggedin[2].encode())
                        ne=ne.hexdigest()
                        auth.write('user'+'$$$'+loggedin[1]+'$$$'+ne)
                        auth.close()
                        print('Use this code for quick-login later')
                        log('logged in as user.',check[0])
                        start()
                else:
                    print('Password is incorrect.')
            else:
                print('Wrong AccType: "'+check[2]+'".')
        else:
            print('Wrong AccType.')
    else:
        print('No account named "'+nick+'" exist.')

def log_out():
    global loggedin,at
    auth=open('content/auth.sys','w')
    auth.write('')
    auth.close()
    if loggedin != None:
        log('logged out.',loggedin[1])
    else:
        log('Quick-L declined.')
    loggedin=None
    at=None

def auth(at,code,nick):
    auth=open('content/auth.sys','r')
    text=auth.read()
    filelist=text.split('$$$')
    ce=hashlib.md5(code.encode())
    ce=ce.hexdigest()
    if ce==filelist[2] and at == filelist[0] and nick == filelist[1]:
        return True
    else:
        return False
    auth.close()

def restore_password():
    pass

def change_password():
    global at,quickL,loggedin
    ch=auth(at,quickL,loggedin[1])
    if ch == True:
        print('You are going to change your password.')
        old=input('Current password:')
        new=input('New password:')
        fileread=open('content/AccBase.sys','r')
        acctxt=fileread.read()
        acclist=acctxt.split('\n')
        fileread.close()
        count=0
        for checked in acclist:
            if checked == '':
                pass
            else:
                chk=checked.split('$$$')
                count=count+1
                if loggedin[1]==chk[0]:
                    mh=True
                    break
        if mh == True:
            pe=hashlib.md5(old.encode()).hexdigest()
            if pe == chk[1] and new != '':
                npe=hashlib.md5(new.encode()).hexdigest()
                acclist.pop(count)
                acclist.pop(0)
                chk.pop(1)
                chk.insert(1, npe)
                chkready=chk[0]+'$$$'+chk[1]+'$$$'+chk[2]
                acclist.insert(count-1,chkready)
                file=open('content/AccBase.sys','w')
                file.write('')
                file.close()
                file=open('content/AccBase.sys','a')
                for accfilew in acclist:
                    file.write('\n'+accfilew)
                file.close()
                print('Password changed')
            else:
                print('Wrong password.')
        
    else:
        print('Wrong Auth')

def change_acctype():
    global at,quickL,loggedin,acclist
    ch=auth('admin',quickL,loggedin[1])
    if ch == True and at == 'admin':
        fileread=open('content/AccBase.sys','r')
        acctxt=fileread.read()
        acclist=acctxt.split('\n')
        fileread.close()
        count=0
        print('Select an user to change his AccType')
        for chec in acclist:
            if chec == '':
                pass
            else:
                count=count+1
                ch=chec.split('$$$')
                print(str(count)+'. '+ch[0]+'     '+ch[2])
        ans=input('|')
        con=0
        for check in acclist:
            if check == '':
                pass
            else:
                con=con+1
                chk=check.split('$$$')
                if str(con) == ans:
                    break
                else:
                    pass
        cod=[]
        for conlist in range(count):
            conlist=conlist+1
            cod.append(str(conlist))
        if chk[0] == loggedin[1]:
            print('You cannot cannot change your AccType')
        elif ans in cod:
            print('Selected : '+chk[0])
            print('Acctype  : '+chk[2])
            print('What AccType do you want to assign to '+chk[0]+'?')
            print('1. User')
            print('2. Admin')
            ans=input('|')
            acclist.pop(con)
            acclist.pop(0)
            if ans == '1':
                chk.pop(2)
                chk.insert(2,'user')
            elif ans == '2':
                chk.pop(2)
                chk.insert(2,'admin')
            else:
                print(chk[1]+"'s AccType change canceled.")
            chkready=chk[0]+'$$$'+chk[1]+'$$$'+chk[2]
            acclist.insert(con-1,chkready)
            file=open('content/AccBase.sys','w')
            file.write('')
            file.close()
            file=open('content/AccBase.sys','a')
            for accfilew in acclist:
                file.write('\n'+accfilew)
            file.close()
            
        else:
            print('Invalid answer')
    else:
        print('You need admin rights for this option')

def delete_acc():
    global at,quickL,loggedin
    ch=auth(at,quickL,loggedin[1])
    if ch == True:
        if at == 'admin':
            print('What account do you want to delete?')
            fileread=open('content/AccBase.sys','r')
            acctxt=fileread.read()
            acclist=acctxt.split('\n')
            fileread.close()
            count=0
            for chec in acclist:
                if chec == '':
                    pass
                else:
                    count=count+1
                    ch=chec.split('$$$')
                    print(str(count)+'. '+ch[0])
            ans=input('|')
            mh=False
            con=0
            for check in acclist:
                if check == '':
                    pass
                else:
                    con=con+1
                    chk=check.split('$$$')
                    if str(con) == ans:
                        break
                    else:
                        pass
            cod=[]
            for conlist in range(count):
                conlist=conlist+1
                cod.append(str(conlist))
            if chk[0] == loggedin[1]:
                log('requested deleting his/her account.',loggedin[1])
                print('Are you sure deleting your account?')
                print('1. Yes.')
                print('2. No.')
                ans=input('|')
                rev=False
                if ans == '1':
                    print('Why? (ENTER for skip)')
                    ans=input('|')
                    if ans != '':
                        rev=True
                    else:
                        pass
                    print('Last chance to cancel deleting account.')
                    lc=input('ENTER for continue or type something for cancel.')
                    if lc != '':
                        print('DELETING CANCELED.')
                    else:
                        if rev == True:
                            log('deleted his/her account. Reason: '+str(ans),loggedin[1],'content/review.sys')
                        acclist.pop(con)
                        acclist.pop(0)
                        f=open('content/AccBase.sys','w')
                        f.write('')
                        f.close()
                        f=open('content/AccBase.sys','a')
                        for delet in acclist:
                            f.write('\n' + delet)
                        log('deleted his/her account.',loggedin[1])
                        log_out()
                        f.close()
                        print('Account deleted successfully')
            elif ans in cod:
                rev=input('Reason: ')
                print('Deleting '+chk[0]+"'s account. Are you sure?")
                print('1. Yes')
                print('2. No')
                ans=input('|')
                if ans == '1':
                    log('deleted '+chk[0]+"'s account. Reason: "+str(rev),loggedin[1],'content/review.sys')
                    acclist.pop(con)
                    acclist.pop(0)
                    f=open('content/AccBase.sys','w')
                    f.write('')
                    f.close()
                    log('deleted '+chk[0]+"'s account.",loggedin[1])
                    f=open('content/AccBase.sys','a')
                    for delet in acclist:
                        f.write('\n' + delet)
                    print('Account deleted successfully')
                    f.close()
            else:
                print('Invadid answer')
        elif at == 'user':
            log('requested deleting his/her account.',loggedin[1])
            print('Are you sure deleting your account?')
            print('1. Yes.')
            print('2. No.')
            ans=input('|')
            rev=False
            if ans == '1':
                print('Why? (ENTER for skip)')
                ans=input('|')
                if ans != '':
                    rev=True
                else:
                    pass
                fileread=open('content/AccBase.sys','r')
                acctxt=fileread.read()
                acclist=acctxt.split('\n')
                fileread.close()
                coun=0
                mh=False
                for checked in acclist:
                    time.sleep(0.02)
                    if checked == '':
                        pass
                    else:
                        coun=coun+1
                        check=checked.split('$$$')
                        if loggedin[1]==check[0]:
                            print('>> '+check[0]+'          <<<')
                            mh=True
                            break
                        else:
                            print('>> '+check[0])
                if mh == True:
                    print('MATCH FOUND')
                    print('Last chance to cancel deleting account.')
                    lc=input('ENTER for continue or type something for cancel.')
                    if lc != '':
                        print('DELETING CANCELED.')
                    else:
                        if rev == True:
                            log('deleted account. Reason: '+str(ans),loggedin[1],'content/review.sys')
                        acclist.pop(coun)
                        acclist.pop(0)
                        f=open('content/AccBase.sys','w')
                        f.write('')
                        f.close()
                        f=open('content/AccBase.sys','a')
                        for delet in acclist:
                            f.write('\n' + delet)
                        log('deleted his/her account.',loggedin[1])
                        log_out()
                        f.close()
                        print('Account deleted successfully')
                else:
                    print("Account doesn't exist")
            elif ans == '2':
                start()
            else:
                pass
        else:
            print('Invalid AccType.')
    else:
        print('Error: invalid data. Restart required. We need to restore data.')

def log(action='',nick='',path='content/logs.sys'):
    global at
    lfile=open(path,'a')
    tim=datetime.now()
    ctim=str(tim.hour)+':'+str(tim.minute)+':'+str(tim.second)
    cdat=str(tim.year)+'-'+str(tim.month)+'-'+str(tim.day)
    event=cdat+' '+ctim+' | '+str(nick)+' '+str(action)
    lfile.write('\n'+event)
    lfile.close()

def reg():
    error=False
    global Nnick,Npassw,acclist
    print('You are going to create a new account. Do not use space and the $ symbol.')
    print('Your nickname have to be unique, not less than 4 characters and not longer than 20 characters.')
    print('Your password have to be not less than 6 characters.')
    print('You can cancel creating after filling form.')
    print('You can delete created account manually.')
    Nnick=input('Nickname:')
    Npassw=input('Password:')
    fileread=open('content/AccBase.sys','r')
    acctxt=fileread.read()
    acclist=acctxt.split('\n')
    fileread.close()
    coc=0
    for char in Nnick:
        coc=coc+1
        if char == ' ' or char == '$' or char == '#' or char == "'" or char == '&&&':
            print(char+'  <<< INCORRECT SYMBOL')
            error = True
        else:
            print(char)
    print('Nickname - '+str(coc)+' symbols')
    if coc >= 4 and coc <= 20:
        coc=0
        for char in Npassw:
            coc=coc+1
            if char == ' ' or char == '$':
                print(char+'  <<< INCORRECT SYMBOL')
                error = True
            else:
                print(char)
        print('Password - '+str(coc)+' symbols')
        if coc >= 6:
            if error == True:
                pass
            elif Nnick==Npassw:
                print('Do not use nickname as your password')
            else:
                reg_a()
        else:
            print('Error: the number of characters fewer than expected')
    else:
        print('Error: the number of characters is less or more than expected')

def reg_a():
    canc = False
    alrused=False
    global Nnick,Npassw,acclist
    print('Confirm the uniqueness of the nickname...')
    for checked in acclist:
        if checked == '':
                    pass
        else:
            check=checked.split('$$$')
            print('>> '+check[0])
            if Nnick==check[0]:
                alrused=True
                print('MATCH WITH '+Nnick)
                break
    if alrused==True:
        print('This nickname cannot be used twice')
    else:
        print('NO MATCH FOUND')
        print('')
        print('To create new account press ENTER 10 times')
        print('(or type something for cancel)')
        for x in range(10):
            a=input('|')
            if a !='':
                canc = True
                print('!REGISTRATION CANCELED!')
                break
        if canc == False:
            log('Account created.',str(Nnick)+':')
            print('initialization...')
            file=open('content/AccBase.sys','a')
            print('file opened')
            time.sleep(0.5)
            Npassw=hashlib.md5(Npassw.encode())
            Npassw=Npassw.hexdigest()
            file.write('\n' + Nnick + "$$$" + Npassw+"$$$"+'user')
            print('information saved')
            time.sleep(0.1)
            file.close()
            print('file closed')
            time.sleep(0.1)
            print('REGISTRATION COMPLETE')
            time.sleep(0.1)
            print('Your nickname is '+Nnick)
        else:
            pass

def check(type='n',des='Use "n" to get list of nicknames,"p" to get list of encoded passwords,"at" or "n+p".'):
    fileread=open('content/AccBase.sys','r')
    acctxt=fileread.read()
    acclist=acctxt.split('\n')
    fileread.close()
    if type == 'n':
        for checked in acclist:
            if checked == '':
                pass
            else:
                check=checked.split('$$$')
                print('>> '+check[0])
    elif type == 'p':
        for checked in acclist:
            if checked == '':
                pass
            else:
                check=checked.split('$$$')
                print('>> '+check[1])
    elif type == 'n+p' or type == 'p+n':
        for checked in acclist:
            if checked == '':
                pass
            else:
                check=checked.split('$$$')
                print('>> '+'N = '+check[0]+'   ,P = '+check[1])
    elif type == 'at':
        for checked in acclist:
            if checked == '':
                pass
            else:
                check=checked.split('$$$')
                print('>> Acctype: '+check[2]+'   N = '+check[0])
def loop(AT='u'):
    global BREAK
    if AT == 'u':
        while True:
            if BREAK == True:
                break
            else:
                start()
    elif AT == 'a':
        while True:
            if BREAK == True:
                break
            else:
                start('admin')
    BREAK=False

#                                      C  H  A  T

def chat():
    global loggenin
    nick=loggedin[1]
    string=0
    print('FORBIDDEN SYMBOLS:\n"$$$", "##", "'+"'"+'", "####", "\\n".')
    print('You are going to connect to chat. You can ask host for address and port.')
    while True:
        ipv4=input('Address:')
        port=input('Port:')
        try:
            server_address=(str(ipv4),int(port))
            break
        except:
            print('Wrong address or port. Example:\nAddress:172.0.0.1\nPort:1234')
    data='sys$$$'+nick+'$$$j$$$0'
    Mode='user'
    print('\nCOMMANDS\n/leave  --  leave chat\n/reply MessageID  --  reply message\n/file my_file.txt  --  send file\n/silent user  --  silent msg\n')
    print('ID')
    file=open('content/chats/sent.csf', 'w')
    file.write('')
    file.close()
    while True:
        leave=False
        if data == None:
            msg=input('<'+nick+'>')
            if '$' in msg or '#' in msg or "'" in msg or '#' in msg or "\n" in msg or '&&&' in msg:
                print('Forbidden symbol')
                data='str$$$'+str(string)
            elif msg == '':
                data='str$$$'+str(string)
            elif msg[0] == '/':

                
                if msg == '/leave':
                    data='sys'+'$$$'+nick+'$$$'+'l'
                    leave=True

                
                elif '/reply' in msg:
                    msg=msg.split()
                    if len(msg) == 2:
                        ID=msg[1]
                        if ID.isdigit():
                            rpl=input('{reply('+nick+'>>'+ID+')}')
                            if rpl != '':
                                if '$' in nick or '#' in nick or "'" in nick or '#' in nick or "\n" in nick or '&&&' in nick:
                                    print('Forbidden symbol')
                                else:
                                    data='reply'+'$$$'+nick+'$$$'+rpl+'##'+ID+'$$$'+str(string)
                            else:
                                data='str$$$'+str(string)
                        else:
                            print('Wrong Message ID')
                            data='str$$$'+str(string)
                    else:
                        print('Incorrect design. Example:\n\n01 <user1>Hi :)\n<user2>/reply 01\n{reply(user2>>01)}Hello @user1\n')
                        data='str$$$'+str(string)

                        
                elif '/file' in msg:
                    msg=msg.split()
                    if len(msg) == 2:
                        path=msg[1]
                        try:
                            fileop=open(path, 'rb')
                            filt=fileop.read()
                            data='str$$$'+str(string)
                        except FileNotFoundError as e:
                            print('File not found:\n')
                            print(e)
                            print('')
                            data='str$$$'+str(string)
                    else:
                        print('Incorrect design. Example:\n\n<user2>/file my_folder/my_file.txt\n')
                        data='str$$$'+str(string)

                        
                elif '/silent' in msg:
                    msg=msg.split()
                    if len(msg) == 2:
                        sil=input('{silent('+nick+'>>'+msg[1]+')}')
                        data='sil'+'$$$'+nick+'$$$'+sil+'##'+msg[1]+'$$$'+str(string)
                    else:
                        print('Incorrect design. Example:\n\n<user2>/silent user1\n{silent(user2>>user1)}hi:)\n')
                        data='str$$$'+str(string)

                        
                elif '/savechat' in msg:
                    msg=msg.split()
                    if len(msg) == 2:
                        path=msg[1]
                        file=open(path, 'w')
                        file.write('NOT WORKING FUNCTION')
                        file.close()
                        data='str$$$'+str(string)
                    else:
                        print('Incorrect design. Example:\n\n<user2>/savechat chat.txt\n')
                    data='str$$$'+str(string)


                elif '/mode' in msg:
                    msg=msg.split()
                    if len(msg) == 3:
                        if msg[1] == 'set':
                            if msg[2] == 'user':
                                Mode='user'
                            elif msg[2] == 'dev':
                                Mode='dev'
                            else:
                                print('Unknown mode')
                        else:
                            print('Unknown command')
                    else:
                        print('Unknown command')
                    data='str$$$'+str(string)


                elif '/sysfile' in msg:
                    if Mode == 'dev':
                        msg=msg.split()
                        if len(msg) == 3:
                            if msg[1] == 'print':
                                if msg[2] == 'sent':
                                    try:
                                        with open('content/chats/sent.csf', 'r') as file:
                                            sentfile=file.read()
                                        print(sentfile)
                                    except:
                                        print('File is not aviable')
                                elif msg[2] == 'got':
                                    string=0
                                else:
                                    print('Unknown value to print')
                            elif msg[1] == 'clean':
                                pass
                            else:
                                print('Unknown system file action')
                    else:
                        print('Command unaviable for this mode')
                    data='str$$$'+str(string)

                else:
                    print('Unknown command')
                    data='str$$$'+str(string)
            else:
                data='msg'+'$$$'+nick+'$$$'+msg+'$$$'+str(string)
        inb=len(data.encode())+3
        inb=len(str(inb))+inb
        data=str(inb)+'&&&'+data
        with open('content/chats/sent.csf', 'a') as file:
            file.write('\n'+data)
        if Mode == 'dev':
            print('Sent:'+data)
            
        #                   T A L K I N G
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(server_address)
            sock.sendall(data.encode())
            data=sock.recv(16)
            size=data.decode().split('&&&')
            if int(size[0]) > 16:
                numof=(int(size[0])-16)/16
                checkround=str(round(numof,1)).split('.')
                if checkround[1] != '0':
                    numof=int(checkround[0])+1
                else:
                    numof=int(checkround[0])
                for x in range(numof):
                    data=data+sock.recv(16)
            data=data.decode()
            data=data.split('&&&')[1]
            msglist=data.split('####')
            msg=None
            if msglist != ['']:
                for msg in msglist:
                    msg=msg.split('$$$')
                    ID=msg[3]
                    if msg[0] == 'msg':
                        print(ID+' <'+msg[1]+'>'+msg[2])
                    elif msg[0] == 'reply':
                        print(ID+' {'+msg[1]+' -> '+msg[2].split('##')[1]+'}'+msg[2].split('##')[0])
                    elif msg[0] == 'sil':
                        if msg[2].split('##')[1] == nick:
                            print(ID+' $il{'+msg[1]+' -> '+msg[2].split('##')[1]+'}'+msg[2].split('##')[0])
                        else:
                            msg[2]='not aviable for you'
                    elif msg[0] == 'sys':
                        if msg[2] == 'j':
                            print(ID+'    '+msg[1]+' joined this chat!')
                        elif msg[2] == 'l':
                            print(ID+'    '+msg[1]+' left.')
                    string=string+1
            time.sleep(0.1)
            sock.close()
            data=None
        except:            
            if leave == True:
                break
            print('Unable to establish connection')
            sock.close()
            ans=input('Do you want to reconnect? (y/n)|')
            if ans != 'y' and ans != '':
                break
        data=None
        if leave == True:
            break

def welcome():  
    print('Type "/info" for help with interface or "/exit" to exit.')
    print('Press ENTER to continue.')
    while True:
        answer=input('|')
        if answer == '/info':
            info()
        elif answer == '/exit':
            break
        elif '/log' in answer:
            try:
                file=open('content/logs.sys', 'r')
                if len(answer.split()) == 1:
                    print(file.read())
                elif len(answer.split()) == 3:
                    answer=answer.split()
                    if answer[1] == 'save':
                        wr=open(answer[2], 'w')
                        wr.write(file.read())
                        print('Log copied to '+answer[2]+'\nEnjoy reading:)')
                        wr.close()
                else:
                    print('Wrong command')
                file.close()
            except FileNotFoundError as e:
                print('Cannot open log file\n')
                print(e)
        elif answer == 'a':
            loop('a')
            break
        elif answer == '':
            loop()
            break
        else:
            print('Wrong command')

def rock(xxx):
    print('⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠉⠈⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣄⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣄⠀⠀⢀⠀⢀⣀⣤⠄⠀⠀⠀⠀⠀⠀⠀  ')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣉⣩⣤⠴⠶⠶⠒⠛⠛⠀⠀⠀⠀  ⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⣴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠒⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠤')
    print('⠀⠀⠀⠀⠀⠀⢀⣾⡍⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣫⣭⣷⠶⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠶⠶⠖⠚⠛⠛⣹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠴⠛⠛⠉⡁⠀⠀⠙⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡷⠷⢿⣦⣤⣈⡙⢿⣿⢆⣴⣤⡄⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⣠⣤⡀⣸⡄⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣟⣩⣤⣴⣤⣌⣿⣿⣿⣦⣹⣿⢁⣿⣿⣄⣀⡀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⢠⣿⠋⠻⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠛⢦⣽⣿⣿⢻⣿⣿⣿⣿⠋⠁⠘⣿⣿⣿⣿⣿⣿⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⢸⣿⠁⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠿⣿⣯⣼⣿⡿⠟⠃⠀⠀⠀⣿⣿⣿⣿⣿⡛⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⢸⣧⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⠟⠃⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⢁⣀⣀⣀⣀⣀⣠⣀⣀⢀⢀⢀')
    print('⠀⠀⢿⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠙⠛⠛⠙⢻⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⡇⠀⠘⠃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⡟⢿⣿⣆⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡼⠁⢀⣀⡀⠀⠀⠀⣦⣄⠀⣠⡄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣷⣬⢻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣰⣿⡿⠿⠦⢤⣴⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⣿⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠒⣿⣿⣿⡿⠟⠹⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⣿⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡖⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⡿⣾⣿⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣆⣀⣀⣤⣴⣶⣶⣾⣿⣷⣦⣴⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⡇⣿⣿⡛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡟⠛⠛⠻⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⠓⢁⣬⣿⠇⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⢰⡿⣻⠇⠀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⢐⣯⠞⠁⠀⠀⠀⠀⠀⠀⣄⠱⣄⠀⠀⠀⠀⠸⡧⠟⠆⠀⠀⠀⠀⠘⠿⢿⠿⠿⣿⡿⣿⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡈⠂⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢠⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⡄⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣦⣦⣼⡏⠳⣜⢿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢠⣷⣦⣤⣀⣀⣀⣴⣿⣿⣿⣿⣿⡿⠻⠆⠸⣎⣧⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣠⡄⠀⣿⢹⡇⢸⡀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿')
    print('Did you said '+xxx+'?')

print('Welcome to PyLocalChat!')
welcome()
print('Type "info()"')
