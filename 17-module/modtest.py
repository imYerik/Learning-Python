#!/usr/bin/python
# coding=utf-8


# Learning Python (Module)

'''
该文件为模块测试文件
引入模块的方式：
1. 引入模块中的全部函数 
import modulename

2. 引入模块中的部分函数
from modulename import function1[,function2[,...functionN]]   

from modulename import *   


'''


import caculator
import hellobye
#from hellobye import hello





print '模块调用avg 函数：', caculator.avg(1,2,3,4,5,6)

hellobye.hello('Yerik')        
#goodbye('Food')
hellobye._age()          # 调用模块 hellobye 中的私有函数（私有变量和函数可以像普通变量函数一样的方式被调用，只是不建议这样做，只是为了演示）


# dir( modulename ) 函数，返回一个模块中定义的所有变量和函数
print 'hellobye模块中所有的变量和函数：',dir(hellobye)







