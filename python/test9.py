#encoding=utf8;

import os;

'''
循环创建升序的py文件
'''

path = os.getcwd();
for i in xrange(21,40):
    # print i;
    filename = 'test' + '%s'%i + '.py';
    # print filename;
    outfile = open(filename,'w');
    outfile.write('#encoding=utf-8;' + '\n' + '\n' + 'import os;')

