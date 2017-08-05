#encoding=utf-8;
# PY3
import os;


print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
pid1 = os.fork()
if pid == 0:
    print('I11 am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I11 (%s) just created a child process (%s).' % (os.getpid(), pid))

if pid1 == 0:
    print('I22 am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I22 (%s) just created a child process (%s).' % (os.getpid(), pid1))