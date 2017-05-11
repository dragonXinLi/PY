#encoding=utf-8;

import os;

# for in ; while ; break; continue
print(list(range(4)));
for x in list(range(4)):
    print(x);


# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。


# dict,set([1,2,3]),"key" in d,d.get('key' , -2),pop(key)
t = (1,2);
print(t);
d = {};
d[t] = 'a';
if t in d:
    print(d);

a = set([1,2,34])
b = set([1,54]);
print('4232432',a & b);
print(a);
a.add(4);
print(a);
a.remove(4);
print(a)
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。