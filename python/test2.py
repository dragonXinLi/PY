# encoding=utf8;
import os;

#对当前文件夹的所有文件进行遍历，得到去掉文件名的后2位的 文件名字符串并写入到names.txt文本中
filenames = os.listdir(os.getcwd());
for name in filenames:
	filenames[filenames.index(name)] = name[:-2];
out = open('name.txt','w');
for name in filenames:
	out.write(name+'\n');
out.close();