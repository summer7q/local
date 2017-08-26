# coding=utf-8
import sys;
import time;
print('happy')
print "welcome to python!"
print "你好！世界！"
if 1/3 == 0.333333333333333:
    print "True"
else:
    print "False"
days = ['Monday', 'Tuesday',
        'Friday']
print 'word',
print "hehe"
sys.stdout.write('std out\n')
print '''这是啥？
我也不知道'''
'''
据说这是注释
'''
# raw_input("\n\nPress the enter key to exit.")
var = 3.2 + 2.32j
data = "iloveguangzhou"
print data[5]
print data[-5:-1]

dict = {}
dict['Mon'] = "Monday"
dict[2] = 234
print dict

ade = 23.2
strade = str(ade)
print strade

ticks = time.time()
print time.localtime(ticks)


def printme(strd):
    "打印输入的字符串"
    print strd
    return


printme("word")
printme('= =')


def getdiff(a, b):
    "求a-b"
    return a-b

print getdiff(b=11, a=3)


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for varnum in vartuple:
        print varnum
    return arg1, vartuple




# 调用printinfo 函数
print printinfo(10)


print printinfo(70, 60, 50)