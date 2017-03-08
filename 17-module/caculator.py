#!/usr/bin/python
# coding=utf-8


# Learning Python (Module)

'''
本模块是简单的计算器测试模块，实现求和、平均数、
'''


def avg(arg1, *vartuple):
	'计算任意个参数的平均数'
	total = arg1
	count = 1.0
	for var in  vartuple:
		total += var
		count += 1

	return total/count


'''
当我们在命令行运行calculator模块文件时，Python解释器把一个特殊变量__name__置为__main__；
而如果在其他py 文件中导入该calculator模块时，if判断将失败将不直接执行（除非主动调用模块的函数），因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行模块测试。
'''

if __name__=='__main__':
	print '平均数测试: ',avg(1,2,3,4,5,6)




