#encoding=utf-8;

import os;
import struct

#struct

# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str


print(struct.pack('>I' , 10240099))

# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。


def is_bmp(d):
    if not os.path.isfile(d):
        print('The file path does not exist.')
        return
    try:
        with open(d , 'rb') as f:
            bitOfBmp = f.read()
            if(len(bitOfBmp) < 30):
                print('The file is not bitmap.')
            else:
                fileInfo = struct.unpack('<ccIIIIIHH' , bitOfBmp)
                if(fileInfo[0] == b'B' and fileInfo[1] == b'M'):
                    print('the size of BitMap is %s * %s , #color is %s' %fileInfo[6] %fileInfo[7] %fileInfo[9])
    except:
        print('not bitmap')
        return

d = input('the file path:')
is_bmp(d)