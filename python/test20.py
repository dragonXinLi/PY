#encoding=utf-8;

import os;

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if "":
    print(1);
elif []:
    print(2);
elif 2:
    print(3);
else:
    print(4);


s = input('brith: ');
birth = int(s);#str转变为int,int()函数发现一个字符串并不是合法的数字时就会报错
if birth < 2000:
    print('00前');
else:
    print('00后');