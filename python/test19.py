#encoding=utf-8;

import os;

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ['a','b','c'];
print(classmates[0]);
print(classmates[-1]);
print(classmates[-3]);
classmates.append('45');
print(classmates);
classmates.insert(1,1);
print(classmates);
# print(classmates.pop());
# print(classmates.pop(1));
# print(classmates);
classmates[1] = '2345'
print(classmates);
classmates.append([3,1,'fs']);
print(classmates);
print(len(classmates));

classmates2 = (1,2,'a','d');
print(classmates2)
print(classmates2[1]);

# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1)
print(t);
t1 = (1,)
print(t1);

# 指向不变，内容可变
t3 = ('a','b',['A','B']);
t3[2][0] = 'X';
print(t3);