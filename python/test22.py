#encoding=utf-8;

import os;

s = 0
def add(a,b,c,d):
    global s
    s1 = 0
    print (len(d) <=1 and d or 2)
    for i in range(a , b):
        if(c <= 0):
            c = 1
        s += (i**c+sum(d))


add(1,10,1,[1])
print (s)