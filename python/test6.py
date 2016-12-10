#encoding=utf8;

import os;
import shutil;

'''
1.遍历当前目录下所有文件，判断是否是文件夹，是的话增加路径，得到最里层的绝对路径，然后再遍历
2.遍历文件后缀名为.txt和.rar的，复制到新建的文件夹中
'''

# def copyfile(file,path):
#     if os.path.exists(file):
#         shutil.copy(file,path);

path = os.getcwd();
if os.path.isdir(os.path.join(path,'aaa')):
    print 'sss';
else:
    os.makedirs(os.path.join(path,'aaa'));
# os.removedirs(os.path.join(path,'aaa'));
for filename in os.listdir(path):
    realpath = os.path.join(path,filename);
    if os.path.isdir(realpath):
        # if os.path.isdir(os.path.join(path,'aaa')):
        childpath = os.path.join(path,'aaa') + '/' + filename;
        if os.path.isdir(childpath) or filename == 'aaa':
            print 'sss';
        else:
            os.makedirs(childpath); 
        for childfilename in os.listdir(realpath):
            if os.path.splitext(childfilename)[1] == '.txt' or os.path.splitext(childfilename)[1] == '.rar' or os.path.splitext(childfilename)[1] == '.py':
                print childfilename;
                realchildpath = os.path.join(realpath,childfilename);
                if os.path.isfile(realchildpath):
                    if os.path.exists(os.path.join(realchildpath +'/' + childfilename)):
                        print '';
                    else:
                        shutil.copy(realchildpath, childpath);