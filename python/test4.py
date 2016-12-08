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
def main():
	# path = raw_input("path:");
	path = os.getcwd();
	all_md5 = [];
	total_file = 0;
	total_delete = 0;
	start = now();
	outfile = open("md5.text",'w');
	for file in os.listdir(path):
		total_file += 1;
		real_path = os.path.join(path,file);
		if os.path.isfile(real_path) == True:
			filemd5 = getmd5(real_path);#如果两个文件的md5值相等，那么这两个文件不相等的概率基本为0
			if(file == 'name.txt' or file == 'names.txt'):
				outfile.write(file + ':' + filemd5 + '\n');
			else:
				outfile.write(filemd5 + '\n');

if __name__ == '__main__':
	main();

