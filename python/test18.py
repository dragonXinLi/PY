#encoding=utf-8;

import os;
import sys;
import subprocess;
import commands;

# print sys.argv;#得到当前python文件的文件名和所有参数值

# print(os.getcwd())
# os.chdir('/Users/sangfor')

# subprocess.call('cd /Users/sangfor', shell=True);

# os.system('cmd /k cd /Users/sangfor/Desktop/appleSample-master')
# print('sfdsaf')
# os.system('cd /Users/sangfor/Desktop/每周分享 ')
# output = os.popen("cd /Users/sangfor/Desktop/每周分享 ")
# print output.read()
# commands.getoutput('ls')

# if os.path.exists('/Users/sangfor/Desktop/python/'):
#     pass
# else:
#     os.mkdir('/Users/sangfor/Desktop/python/')
#
# os.chdir('/Users/sangfor/Desktop/python/')
# os.system('git pull origin master')

print ('Program name ', sys.argv[0])  # 当前python文件的文件名
print ('Program name ',sys.argv[1])  # 当前python文件的文件名
# print ('Program name ',sys.argv[2])  # 当前python文件的文件名
# print ('Program name ', sys.argv[3])  # 当前python文件的文件名

if(sys.argv[1] == 'pull'):
    if (sys.argv[2] == 'oc'):
        if os.path.exists('/Users/sangfor/Desktop/Westward Journey'):
            pass
        else:
            print('没有%s文件夹路径' % sys.argv[1])

        os.chdir('/Users/sangfor/Desktop/Westward Journey')
        os.system('git pull origin master')
    elif (sys.argv[2] == 'py'):
        if os.path.exists('/Users/sangfor/Desktop/python/'):
            pass
        else:
            print('没有%s文件夹路径' % sys.argv[1])

        os.chdir('/Users/sangfor/Desktop/python/')
        os.system('git pull origin master')
        # stream = os.popen('git pull origin master')
        # allsh1 = stream.readlines()
        # print('1234567890',allsh1)
    elif (sys.argv[2] == 'js'):
        if os.path.exists('/Users/sangfor/HBuilderProjects/liaoxuefeng'):
            pass
        else:
            print('没有%s文件夹路径' % sys.argv[1])

        os.chdir('/Users/sangfor/HBuilderProjects/liaoxuefeng')
        os.system('git pull origin master')
elif(sys.argv[1] == 'push'):
    if (sys.argv[2] == 'oc'):
        if os.path.exists('/Users/sangfor/Desktop/Westward Journey'):
            pass
        else:
            print('没有%s文件夹路径' % sys.argv[1])

        os.chdir('/Users/sangfor/Desktop/Westward Journey')
        os.system('git add .')
        os.system('git diff')
        commitStr = sys.argv[3];
        os.system('git commit -m %s' %commitStr)
        os.system('git push origin master')
    elif (sys.argv[2] == 'py'):
        if os.path.exists('/Users/sangfor/Desktop/python/'):
            pass
        else:
            print('没有%s文件夹路径' % sys.argv[1])

        os.chdir('/Users/sangfor/Desktop/python/')
        os.system('git add .')
        os.system('git diff')
        commitStr = sys.argv[3];
        os.system('git commit -m "%s"' %commitStr)
        os.system('git push origin master')
    elif (sys.argv[2] == 'js'):
        if os.path.exists('/Users/sangfor/HBuilderProjects/liaoxuefeng'):
            pass
        else:
            print('没有%s文件夹路径' % sys.argv[1])

        os.chdir('/Users/sangfor/HBuilderProjects/liaoxuefeng')
        os.system('git add .')
        os.system('git diff')
        commitStr = sys.argv[3];
        os.system('git commit -m %s' % commitStr)
        os.system('git push origin master')


# if __name__ == '__main__':
#     # print 'Program name',sys.argv[0]; #当前python文件的文件名
#
#     index = int(sys.argv[1]);
#     if(index == 0):
#         var = {
#             # subprocess.call('cd /')
#             # print('fdsfs')
#
#         }

