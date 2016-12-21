#encoding=utf-8;

import os;
import sys;
import subprocess;
#import get_password_ll.py;

print sys.argv;#得到当前python文件的文件名和所有参数值

if __name__ == '__main__':
    print 'Program name',sys.argv[0]; #当前python文件的文件名

    masterAccount = int(sys.argv[1]);
    defaultNmae = 'LLong';
    if len(sys.argv) > 3:
        startValue = int(sys.argv[2]);
        endValue = int(sys.argv[3]);

        if len(sys.argv) > 4:
            defaultNmae = str(sys.argv[4]);
        differValue = endValue - startValue;
        for i in range(0, differValue + 1):
            #       print '开始创建账号 ： %d'%(i+ startValue);
            account = i + startValue;
            subprocess.call('rostertest -cp -a %d -name %s%d -n %d -p 12345' % (account, defaultNmae,i , masterAccount), shell=True);
            #      subprocess.call('get_password_ll.py %d' %account , shell=True);
            #     print '%d账号创建完成'%account;
            # print '%d%d' %(account,masterAccount);
            # subprocess.call('ls',shell=True);
    else:
        account = int(sys.argv[2]);
        if len(sys.argv) > 3:
            defaultNmae = str(sys.argv[3]);
        subprocess.call('rostertest -cp -a %d -name %s -n %d -p 12345' % (account, defaultNmae , masterAccount), shell=True);



