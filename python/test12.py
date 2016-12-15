#encoding=utf-8;

import os;
import urllib2;
import re;
from bs4 import BeautifulSoup;

def stripHTMLTags(html):
    return re.sub('<([^!>]([^>] | n)*)>',html);

def fetch_URL(url,localfile,ignoreFansReq=False):
    html = urllib2.urlopen(url).read();
    html = unicode(html,'gb2312','ignore').encode('utf-8','ignore');
    content = BeautifulSoup(html).findAll(attrs={'class':'d_post_content'});
    myfile = open(localfile,'w');
    for item in content:
        item_formatted = stripHTMLTags(str(item).replace('<br/>','rn'));
        if ignoreFansReq == True:
            if len(item_formatted) < 100:
                continue;
        myfile.write(item_formatted);
        myfile.write('rn');
        print item_formatted;
    myfile.close();

def main():
    urlTarget = 'http://tieba.baidu.com/p/1234371208';
    localfileTarget = 'tieba.txt';
    fetch_URL(url=urlTarget,localfile=localfileTarget,ignoreFansReq=True);

if __name__ == '__main__':
    main();