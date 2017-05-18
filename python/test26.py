#encoding=utf-8;

import os;

# 函数的参数可以是默认参数，可变参数，关键字参数

def power(x):
    return x*x;
print (power(2))

def pw2(x,n):
    s = 1;
    while(n>0):
        n = n-1
        s = s * x;
    return s
print (pw2(2,4))

# 默认参数
def pw3(x,n=2):
    s = 1
    while(n>0):
        n=n-1
        s=s*x
    return s
print (pw3(2,5))

def adds(l=[]):
    l.append('end')
    return l
print (adds([222]))
print (adds([44]))
print (adds())
print (adds())
def adds2(l=None):
    if l is None:
        l=['end']
    l.append('end')
    return l
print(adds2([111]))
print (adds2())

# 可变参数
def calc(*numbers):
    sum = 0
    for x in numbers:
        sum = sum + x * x
    return sum
print (calc(1,2,3))

a = [1,2,3,4]
b = (1,2,3,4)
# 在list或者tuple前面加上*,表示变为可变参数传进去
print (calc(*a))
print (calc(*b))
print (calc())

# 关键字参数
def person(name,age,**kw):
    return {'name':name , 'age':age , 'other':kw}
print (person('ll',26,city=[1111],bo=33))

# 命名关键字参数
def person2(name,age,**kw):
    if 'city' in kw:
        print ('pass')
        pass
    if 'job' in kw:
        pass
    return {'name:', name, 'age:', age, 'other:', kw}
print person2('LL',343,city=389,job=4)
#warning person2 有问题

        # print ('name:',name , 'age:',age , 'other:',kw)

def person3(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person3('LL',33,city='23',job=23)