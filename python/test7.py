#encoding=utf8;
import smtplib;
from cmath import e
from  email.mime.text import MIMEText;
from email.header import Header;
import sys;
reload(sys);
sys.setdefaultencoding('utf8');

#定义发送列表
mailto_list = ['cs1005744115@163.com'];
#设置服务器名称，用户名，密码以及邮件后缀
mail_host = 'smtp.163.com';
mail_user = 'l916617054';
mail_pass = 'cs1005744115';
mail_postfix = '163.com';

#发送邮件函数
def send_mail(to_list , sub , context,format = 'plain'):
    '''
    :param to_list: 发送给谁
    :param sub:主题
    :param context:正文
    :param format:正文格式
    :return:
    '''
    me = mail_user + '<' + mail_user + '@' + mail_postfix + '>';
    msg = MIMEText(context,format,'utf-8');
    msg['Subject'] = isunicode(sub);
    # msg['Subject'] = sub;#这里必须转换
    msg['From'] = me;
    msg['To'] = ','.join(to_list);
    msg['Accept-Language'] = 'zh-CN';
    msg['Accept-Charset'] = 'ISO-8859-1,utf-8';
    try:
        send_smtp = smtplib.SMTP();
        send_smtp.connect(mail_host);
        send_smtp.login(mail_user,mail_pass);
        send_smtp.sendmail(me,to_list,msg.as_string());
        send_smtp.close();
        return True;
    except(Exception,e):
        print (str(e));
        return False;
def isunicode(subject):
    if not isinstance(subject,unicode):
        subject = unicode(subject);
    return subject;
def isstr(body):
    if isinstance(body,unicode):
        body = str(body);
    return body;

if __name__ == '__main__':
    if(True == send_mail(mailto_list,'我是l916617054@163.com','我是通过python脚本发送给你的邮件-14')):
        print ('测试成功');
    else:
        print ('测试失败');