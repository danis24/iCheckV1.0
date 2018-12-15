import time
from machine import *
import os
import random, string

#waktu
def timex():
    t = time.localtime()
    hr = t.tm_hour
    mn = t.tm_min
    sc = t.tm_sec
    return '[{}:{}:{}] '.format(hr, mn, sc)

def logo():
    print "\n     _ _  _        _               ___   ___"
    time.sleep(0.3)
    print "  __| | || |  _ __| | ___ __ ___  / _ \ / _ \ _ __  ___"
    time.sleep(0.6)
    print " / _` | || |_| '__| |/ / '_ ` _ \| | | | | | | '_ \/ __|"
    time.sleep(0.9)
    print "| (_| |__   _| |  |   <| | | | | | |_| | |_| | | | \__ \ "
    time.sleep(1)
    print " \__,_|  |_| |_|  |_|\_\_| |_| |_|\___/ \___/|_| |_|___/\n"
    time.sleep(1.5)
    print "|create by     : d4rkm00ns"
    print "|contact person: d4rkm00ns@protonmail.com"
    print "|date created  : 7 desember 2018"
    print "|date update   : -"
    print "|tools version : 1.0"
    print "|what's new..? : -"
    print "|tools for     : Email Valid Checker + Email Filter"

logo()
time.sleep(0.5)

#creating golder Result
try:
    if not os.path.exists('Result'):
        os.makedirs('./Result')
    else:
        print ""
except OSError:
    print ('Error: Creating directory')
    print "Buatlah folder Result"
finally:
    print "\t\t\t**--+ [d4rkm00ns] +--**"

print "Note: Read 'PetunjukPenggunaan.txt' before using this Tools"
time.sleep(0.5)
print "List Tools ./d4rkm00ns"
print "#**********************#"
print "[1] Email Filter by domain ( like in bellow )"
print "[2] Email Valid Domain @gmail.com"
print "[3] Email Valid Domain @yahoo.com"
print "[4] Email Valid Domain @aol.com"
print "[5] Email Valid Domain @yandex.com"
print "[6] Email Valid Domain @outlook.com, @live.com, @hotmail"
print "[7] Email Valid Domain @orange.it"
print "[8] Email Valid Domain @alice.it"
print "[9] Email Valid Domain @gmx"
print "[10] Email Valid Domain @free"
print "[11] Email Valid Domain @t-online"
print "[12] Email Valid Domain @mail"
print "[13] Email Valid Domain @web"
print "[14] Email Valid Domain @Wanadoo"
print "[15] Email Valid Domain @Tiscali"
print "[98] Custom Email Filter by Domain"
print "[99] Custom Valid Email Server "
print "[0] EXIT"
print "#**********************#"
print "Copyright by d4rkm00ns. Please don't remove copyright"
print "Jangan hilangkan/merubah copyright/author, Hargailah authornya ;)"

#creating folder ResFiltered
try:
    if not os.path.exists('ResFiltered'):
        os.makedirs('./ResFiltered')
    else:
        print ""
except OSError:
    print ('Error: Creating directory')
    print "Buatlah folder ResFiltered"
finally:
    print "\t\t\t**--+ [Welcome to Undergrounds] +--**"

rd = ''.join(random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCEDFGHIJKLMNOPQRSTUVWXZY') for _ in range(4))

swit = input(timex()+"[+]Your Choose root@d4rkm00ns: ")

if swit == 1:
    print timex()+"[+]Set to Email Filter..!!"
    filter(rd)
elif swit == 2:
    print timex()+"[+]Set to Gmail Server"
    gmail(rd)
elif swit == 3:
    print timex()+"[+]Set to Yahoo Server"
    yahoo(rd)
elif swit == 4:
    print timex()+"[+]Set to AOL Server"
    aol(rd)
elif swit == 5:
    print timex()+"[+]Set to Yandex Server"
    yandex(rd)
elif swit == 6:
    print timex()+"[+]Set to Outlook Server"
    outhotliv(rd)
elif swit == 7:
    print timex()+"[+]Set to Orange Server"
    orange(rd)
elif swit == 8:
    print timex()+"[+]Set to Alice Server"
    alice(rd)
elif swit == 9:
    print timex()+"[+]Set to Gmx Server"
    gmx(rd)
elif swit == 10:
    print timex()+"[+]Set to Free Server"
    free(rd)
elif swit == 11:
    print timex()+"[+]Set to T-Online Server"
    tonline(rd)
elif swit == 12:
    print timex()+"[+]Set to Mail Server"
    mail(rd)
elif swit == 13:
    print timex()+"[+]Set to Web Server"
    web(rd)
elif swit == 14:
    print timex()+"[+]Set to Wanadoo Server"
    wanadoo(rd)
elif swit == 15:
    print timex()+"[+]Set to Tiscali Server"
    tiscali(rd)
elif swit == 98:
    print timex()+"[+]Set to Custom Email Filter by Domain"
    cusfil()
elif swit == 99:
    print timex()+"[+]Set to Custom Valid Email Server(IMAP)"
    cusval()
else:
    print timex()+"[!]Exit..!!"
    print timex()+"[+]See You Again..!!"
    print timex()+"[+]./d4rkm00ns"
    exit()


print "\n\t\t\t==--+ [Finished..!!] +--=="
print "==--+ [Thanks Was using Tools ./d4rkm00ns] +--=="

#DATA Important
#

#IMAP
# imap.mail.yahoo.com 993
# imap.gmail.com 993
# in.alice.it 143
# imap.mail.com 993
# imap-mail.outlook.com 993
# in.virgilio.it 110 POP
# imapmail.libero.it 993
# imap.tiscali.it 143
# imap.talktalk.net 993 tiscali.co.uk
# box.tin.it 110

#List Domain IT
#@hotmail.com
#@virgilio.it
#@live.it
#@fastwebnet.it
#@libero.it
#@alice.it
#@tiscali.it
#@volpeguglielmetti.it
#@tin.it
#@supereva.it
#@katamail.it
#@danieleleone.eu
#@supportopsicologico.it
#@blu.it
#@interfree.it
#@email.it
#@inwind.it
#@infinito.it