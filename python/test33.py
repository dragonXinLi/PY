#encoding=utf-8;

import os;
import hashlib

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def calc_md5(password):
    md5 = hashlib.md5
    md5.update(password.encode('uft-8'))
    pwd_md5 = md5.hexdigest()
    return pwd_md5
