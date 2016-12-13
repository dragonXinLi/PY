#encoding=utf-8;
import os;

# open('~.xxx','w');
# os.remove(os.getcwd() + '/test8child.txt');
def scan(arg,dirname,names):
    for file in names:
        if file[0] == '~' or file[-4:] == '.bat':
            print '删除文件：',file;
            file == dirname + '\\' + file;
            os.remove(file);
            print '完成：',file;

path = raw_input("请输入要删除文件所在目录：（绝对路径）");
print os.getcwd();
if os.path.exists(path) == False:
    print "用户输入的目录不存在";
    os._exit(1);
os.path.walk(path,scan,0);
# os.system('pause');