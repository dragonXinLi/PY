#encoding=utf-8;

import os;
import base64

def safe_base64_decode(s):
    b = len(s)%4
    if b!=0:
        return base64.b64decode(s+b'='*(len(s)%4))
    else:
        return base64.b64decode(s)
    # if len(s) % 4 != 0:
        # a = b'='*(len(s) % 4)
        # s += a
        # # return base64.b64decode(s+b'='*(len(s) % 4))
        # # return base64.b64decode(s+b'='*(len(s)%4))
        # print(a)


print(safe_base64_decode('YWJjZA'))