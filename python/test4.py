# encoding=utf8;

import time,datetime;
import urllib2;
import os;
import md5;
from time import clock as now;

# def chk_qq(qqnum):
# 	# chkurl = 'http://wpa.qq.com/pa?p=1:'+'qqnum'+':1';
# 	chkurl = 'http://www.baidu.com';
# 	a = urllib2.urlopen(chkurl);
# 	print a;
# 	length = a.headers.get("content-length");
# 	print length;
# 	a.close();
# 	print datetime.datetime.now();
# 	if length == '2329':
# 		return 'Online';
# 	elif length == '2262':
# 		return 'Offline';
# 	else:
# 		return 'Unknown Status!';

# qq = 916617054;
# stat = chk_qq(qq);
# print'qq' + 'is' + stat;

def getmd5(filename):
	file_txt = open(filename,'rb').read();
	m = md5.new(file_txt);
	return m.hexdigest();
# def main():
# 	# path = raw_input("path:");
# 	path = os.getcwd();
# 	all_md5 = [];
# 	total_file = 0;
# 	total_delete = 0;
# 	start = now();
# 	outfile = open("md5.text",'w');
# 	for file in os.listdir(path):
# 		total_file += 1;
# 		real_path = os.path.join(path,file);
# 		if os.path.isfile(real_path) == True:
# 			filemd5 = getmd5(real_path);#如果两个文件的md5值相等，那么这两个文件不相等的概率基本为0
# 			# if(file == 'name.txt' or file == 'names.txt'):
# 			# 	outfile.write(file + ':' + filemd5 + '\n');
# 			# else:
# 			# 	outfile.write(filemd5 + '\n');
# 			if filemd5 in all_md5:
# 				total_delete += 1;
# 				print "删除",file;
# 			else:
# 				all_md5.append(filemd5);
# 	end = now();
# 	time_last = end - start;
# 	print '文件总数：',total_file;
# 	print '删除个数：',total_delete;
# 	print '耗时：',time_last,'秒';

def main():
	# path = raw_input("path:");
	path = os.getcwd();
	all_md5 = {};
	all_size = {};
	total_file = 0;
	total_delete = 0;
	start = now();
	outfile = open("md5.text",'w');
	for file in os.listdir(path):
		total_file += 1;
		real_path = os.path.join(path,file);
		if os.path.isfile(real_path) == True:
			size = os.stat(real_path).st_size;
			# print size;
			name_and_md5 = [real_path,""];
			print name_and_md5;
			if size in all_size.keys():
				new_md5 = getmd5(real_path);
				if all_size[size][1] == "":
					all_size[size][1] = getmd5(all_size[size][0]);
				if new_md5 in all_size[size]:
					print "删除",file;
					total_delete += 1;
				else:
					all_size[size].append(new_md5);
			else:
				all_size[size] = name_and_md5;
	end = now();
	time_last = end - start;
	print '文件总数：',total_file;
	print '删除个数：',total_delete;
	print '耗时：',time_last,'秒';

if __name__ == '__main__':
	main();

