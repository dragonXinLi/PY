#encoding=utf-8;

import os;
import itertools

# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
# itertools


# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cycle()会把传入的一个序列无限重复下去：
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A' , 3)
print(ns)
for n in  ns:
    print(n)

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC' , 'XYZ'):
    print(c)

# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for (key , group) in itertools.groupby('AaaBBbcCAAa' , lambda c:c.upper()):
    print(key,list(group))