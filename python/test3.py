# encoding=utf8;
import os;

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

a = os.walk('.');
for i in a:
	print i;
