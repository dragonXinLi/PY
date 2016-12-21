#encoding=utf-8;

import os;
import sys;
import subprocess;
import get_password.py;

if __name__ == '__main__':
    print 'Program name',sys.argv[0]; #当前python文件的文件名
    masterAccount = int(sys.argv[1]);
    startValue = int(sys.argv[2]);
    endValue = int(sys.argv[3]);
    differValue = endValue - startValue;
    for i in range(0,differValue + 1):
        print '开始创建账号 ： %d'%(i+ startValue);
        account = i + startValue;
        subprocess.call('rostertest -cp -a %d -name LLong -n %d -p 12345'%(account,masterAccount), shell=True);
        subprocess.call('python get_password.py %d' %account , shell=True);
        print '%d账号创建完成'%account;
        # print '%d%d' %(account,masterAccount);
    # subprocess.call('ls',shell=True);