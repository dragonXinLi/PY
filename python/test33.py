#encoding=utf-8;

import os;
import hashlib

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pwd_md5 = md5.hexdigest()
    return pwd_md5

def login(user,password):
    if user in db:
        print(password)
        if db[user] == calc_md5(password):
            print('welcome')
            return True
        else:
            print('密码错误')
            return False

user = str(input('请输入你的用户名:'))
password = str(input('请输入你的密码:'))
login(user,password)

