#encoding=utf8;

import os;

'''
循环创建升序的py文件
'''

path = os.getcwd();
for i in xrange(10,21):
    # print i;
    filename = 'test' + '%s'%i + '.py';
    # print filename;
    open(filename,'w');
