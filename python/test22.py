#encoding=utf-8;

import os;
import sys;
import subprocess;
import re;

print ('Program name ', sys.argv[0])  # 当前python文件的文件名

if __name__ == '__main__':
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
        if (size == 0):
            print('size默认值2G')
            reaSize = 4194304
        else:
            reaSize = size * 1024 * 1024 / 512
            print('size键入值为：%dG' %(size / 1024))
    else:
        print('size默认值2G')
        reaSize = 4194304
    returncode = subprocess.check_output('hdid -nomount ram://%d' % (reaSize), shell=True);
    print('%s' %returncode)
    index = re.findall(r"\d+\.?\d*",returncode)
    print(index[0])
    subprocess.check_output('newfs_hfs -v DerivedData /dev/rdisk%s' % (index[0]), shell=True);
    subprocess.check_output('diskutil mount -mountPoint ~/Library/Developer/Xcode/DerivedData %s' % (returncode), shell=True);