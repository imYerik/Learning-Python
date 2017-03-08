#!/usr/bin/python
#coding=utf-8

# Learn Python (Function)



'''
显式声明:  函数名、参数、函数文档说明、函数体、返回值
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]

调用:传入参数
functionname( paramenters )


'''

# 函数声明和调用示例

def PrintHelloWorld( str ):
	'This function is used for printing HelloWorld.'
	print str
	return

PrintHelloWorld('Hello World!')


# 全局变量和局部变量
# 示例一
total = 0
def sum( arg1, arg2):
	total = arg1 + arg2
	print '局部变量 total = %d' %(total)
	return total
sum(10,20)
print '全局变量 total = %d' %(total)

# 示例二 global 关键字
total = 0
def sum( arg1, arg2):
        global total            # 在函数内声明为全局变量，这样就可以使用函数外部命名空间的全局变量
	total = arg1 + arg2
	print 'global 全局变量 total = %d' %(total)
	return total
sum(10,20)
print '全局变量 total = %d' %(total)

'''
参数传递
Python 中的变量都是对象，对象分mutable 和 immutable 对象；
Python 函数参数都是传递的对象地址，但是由于 immutable 对象不可更改，赋值会重新生成新的对象，所以实现了“传值”的效果；mutable 对象可以更改，赋值不会改变对象的地址，所以实现了“传址”的效果；

'''

# 传递 immutable 对象
def ChangeInt( a ):
	a = 10
	print '函数内 a 的值为: %d' %(a)

b = 2
ChangeInt(b)
print '函数外 b 的值为: %d' %(b)

# 传递 mutable 对象
def ChangeList( list ):
	list[1] = 'Python'
	list.append('!')
	print '函数内的 list: %s' %(list)

mylist = ['Hello','World']
ChangeList(mylist)
print '函数外的 mylist: %s' %(mylist)


'''
参数类型
必备参数：参数以正确的顺序传入，函数调用和函数声明的参数数量必须一样；
关键字参数：函数调用时用关键字参数名来匹配参数值，函数调用和声明的参数顺序可以不一致,也可以传入任意多个参数；
缺省参数：函数声明时指定缺省参数，函数调用时如果不传入该参数，会使用函数声明时指定的默认值；
不定长参数：函数声明时无法确定参数个数，可以通过一个参数元组来实现不定长参数；

'''



# 必备参数示例
def PrintInfo1( name, number):
	print '姓名：%s,编号：%d' %(name,number)

PrintInfo1('Yerik',1000)
#PrintInfo(1000,'Yerik')        # Error
#PrintInfo(1000)                # Error


# 关键字参数示例
def PrintInfo2( name, number,**kw):
	print '姓名：%s,编号：%d, other：%s' %(name,number,kw)

PrintInfo2('Yerik',1000)
PrintInfo2(name='Yerik',number=1000)
PrintInfo2(number=1000, name='Yerik')    #通过指定关键字，调用顺序可以与声明顺序不一致
PrintInfo2(number=1000, name='Yerik',city='Beijing',hobby='Roadbike')    # 通过声明 kw 参数,调用时指定参数关键字名，可以传入任意多个参数,函数内部将这些关键字自动组成字典

# 缺省参数
def PrintInfo3( name, number=1000):      # 函数声明时指定参数默认值
	print '姓名：%s,编号：%d' %(name,number)

PrintInfo3(number=2000,name='Yerik')     # 调用时指定参数则使用调用传入值
PrintInfo3(name='Yerik')                 # 调用时number未指定参数，则使用函数声明时的默认值


# 可变参数
def PrintInfo4( name, number, *vartuple):
	print '姓名：%s,编号：%d' %(name,number)
	for var in vartuple :
		print var
	return

PrintInfo4('Yerik',1000,'爱好：Roadbike','妙峰山 PR:65\'','主将：Tony MaTao')

# 参数组合：所有类型的参数可以组合，但必须以必选参数、默认参数、可变参数、关键字参数这样的顺序声明和调用函数；
def PrintInfo5( name, number=1000, *vartuple, **kw):
	print '姓名：%s,编号：%d, others：%s' %(name,number,kw)
	for var in vartuple :
		print var
	return

PrintInfo5('Yerik',1001,'爱好:Roadbike',Miaofeng=65,commander='Tony MaTao')



'''
匿名函数
Python 使用 lambda 表达式来创建匿名函数；
lambda 仅仅是一个表达式，函数体比 def 简单；
lambda 不是代码块，仅能封装有限的逻辑；
lambda 有自己的命名空间，不能访问参数列表之外或全局命名空间的参数；

lambda 表达式语法
lambda [arg1[,arg2,...,argn]]:expression

'''

# lambda 表达式示例1
suml = lambda arg1,arg2 : arg1+arg2;
print 'suml(10,20) = %d' %(suml(10,20))




# lambda 表达式在 map 函数中的应用
'''
map 函数：map(function,interable,...)，map 函数中有两个参数，function 代表一个函数或者 lambda 表达式，interable参数 代表一个可迭代的参数对象，如 list等；
map 函数可以理解为“针对 interable 参数中的每一个元素执行 function 操作”
如果有多个interable，那么将并行执行 function 操作（参考以下 map 函数示例4）

'''

# map  函数示例1
list = [1,2,3,4,5]
def addOneF(x):
	return x+1
print 'map-1: ', map(addOneF,list)

# map 函数示例2
list = [1,2,3,4,5]
addOneL = lambda x:x+1
print 'map-2: ', map(addOneL,list)

# map 函数示例3
print 'map-3: ', map(lambda x:x+1, range(1,6))

# map 函数示例4
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
print 'map-4: ', map(lambda x,y,z:x+y+z, list1, list2, list3 )           # [12, 15, 18]， list1，list2，list3中每个相同下标的元素相加（每个可迭代参数中的元素‘并行’的应用‘function‘）

# map 函数示例5
list = ['Hello','WORLD']
print 'map-5: ', map(lambda str:str.upper(), list)

