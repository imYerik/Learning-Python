#!/usr/bin/python
#coding=utf-8


'''
关于 Python模块中私有变量和函数的问题：

1. 私有变量和函数通常以单下划线（_）或者双下划线（__）开头命名，例如 _name, __age，__function()；

2. Python并没有一种方法可以完全限制访问private函数或变量的访问（跟访问普通变量和函数一样）；
但是，从编程习惯上不应该引用private函数或变量；所以，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用;

3. 私有变量和函数提供在模块内部互相调用，模块中尽可能因此相关的内部逻辑，只有外部需要的接口才定义为公有的，对外部公开访问，这也是一直非常有用的代码封装和抽象的方法；

'''

_myage = 28           # 定义私有变量


def hello(arg1):
	print 'Hello %s' %(arg1)


def goodbye(arg1):
	print 'Goodbye %s' %(arg1)

def _age():
	'定义私有的函数'
	print '年龄： %d' %(_myage)

if __name__=='__main__':
	hello('Yerik')
	goodbye('Food')
	_age()

