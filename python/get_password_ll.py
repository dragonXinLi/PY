#!/usr/bin/python

import pymongo
import sys
import os
from  xml.dom import  minidom

u_account=""

def getMongoInfo():
    filename = '/etc/sangfor/moa/moa.xml'
    doc = minidom.parse(filename)
    root = doc.firstChild
    childs = root.childNodes
    ip = '/tmp/mongodb-27017.sock'
    port = -1
    authFlag = 0
    for child in childs:
        if child.nodeType == child.TEXT_NODE:
            pass
        else:
            if child.getAttribute('name') == 'mongodb_ip':
                ip = child.childNodes[0].data
            elif child.getAttribute('name') == 'mongodb_port':
                port = child.childNodes[0].data
            elif child.getAttribute('name') == 'mongodb_need_auth':
              authFlag = child.childNodes[0].data
    return ip, int(port), int(authFlag)

def getMongoConnect() :
    ip, port, authFlag = getMongoInfo()
    conn = pymongo.Connection(ip, port)
    if authFlag == 1:
        out=os.popen('/usr/bin/mongo_user admin 1').read()
        account=out.split(' ')
        conn.admin.authenticate(account[0],account[1])
    return conn

table = getMongoConnect().auth.users

u_accountStart = str(sys.argv[1]);
if len(sys.argv) > 2:
    u_accountEnd = str(sys.argv[2]);
    differValue = int(u_accountEnd) - int(u_accountStart);
    for i in range(0,differValue + 1):
        u_account = str(i + int(u_accountStart));
        if table.find({"uname":u_account}).count() == 0 :
            print "not find user " + u_account
            # sys.exit(0)
        else:
            for use in table.find({"uname":u_account}) :
                if use.has_key("password") == False :
                    print  'account=%s,did=%ld,pid=%ld has been active, password removed' % (u_account, use['did'], use['pid'])
                else :
                    print  'account=%s,did=%ld,pid=%ld,password=%s' % (u_account, use['did'], use['pid'], str(use['password']))
else:
    u_account = str(u_accountStart);
    if table.find({"uname": u_account}).count() == 0:
        print "not find user " + u_account
        # sys.exit(0)
    else:
        for use in table.find({"uname": u_account}):
            if use.has_key("password") == False:
                print  'account=%s,did=%ld,pid=%ld has been active, password removed' % (u_account, use['did'], use['pid'])
            else:
                print  'account=%s,did=%ld,pid=%ld,password=%s' % (u_account, use['did'], use['pid'], str(use['password']))
