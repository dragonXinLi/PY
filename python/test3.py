# encoding=utf8;
import os;
import shutil;

print os.getcwd();
#文件夹/文件名操作
print os.listdir(os.getcwd());#当前目录下的所有文件名

# print os.path.walk(os.getcwd(),visit,arg)

print os.path.split(os.getcwd());#分离成一个list，有一定的规则

print os.path.splitext(os.getcwd() + '.txt');#把文件名分成文件名称和扩展名

print os.path.dirname(os.getcwd());#把上级目录的名字提取出来

print os.path.basename(os.getcwd());#取得当前目录的文件组名

# print os.mkdir(os.getcwd() + '/一级目录');#在指定的目录下创建一个1级目录

# print os.makedirs(os.getcwd() + '/多级目录/一级目录/二级目录'); 同上，存在文件夹后不能再创建

# print os.removedirs(os.getcwd() + '/一级目录');
# print os.rmdir(os.getcwd() + '/一级目录'); #同上，文件夹必须为空才能删除

# a = os.walk('.');
# for i in a:
# 	print i;

# out = open('shutilcopy.txt','w');
# print shutil.copy(os.getcwd() + '/names.txt' , 'shutilcopy.txt');#将前者的文件内容复制给后者，若后者不存在，则会创建

# rootdir = os.getcwd();
# for parent , dirnames , filenames in os.walk(rootdir):
# 	#case1:
# 	for dirname in dirnames:
# 		print "parent is:" + parent;
# 		print "dirname is:" + dirname;#一个目录下所有的文件夹的名字
# 	#case2:
# 	for filename in filenames:
# 		print "parent is:" + parent;
# 		print "filename with full path:" + os.path.join(parent,filename);#一个目录下的所有文件的绝对路径

spath = os.getcwd();
#case1:分隔目录和文件名
p,f = os.path.split(spath);
print "dir is:"+p;
print "file is:"+f;

#case2:分隔盘符和文件名
drv,left = os.path.splitdrive(spath);
print "driver is:"+drv;
print "left is:"+left;

#case3:分隔文件和扩展名
f,ext = os.path.splitext(spath);
print "f is:"+f;
print "ext is:"+ext;

spam = ['cat','dog','mouse'];
for i in range(len(spam)):
	print(spam[i]);
for i in xrange(0,len(spam)):
	print(spam[i]);

spam2 = 0;
eggs = 0;
spam2 +=42;
eggs += 42;#需要初始值


