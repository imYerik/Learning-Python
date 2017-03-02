#!/usr/bin/python
# coding=utf-8
# Learning Python

# Tuple  元组，相当于只读的 List

tup1 = (1,2,3,4,5)
tup2 = 1,2,3,4
tup3 = ('a',1,'hello',200,'world','abc')
print tup1,tup2,tup3
print tup1[2]
print tup1[2:4]          # 获取元组中的元素，下标范围[2,4)
print tup1[-2]           # 获取元组中的元素，倒数第二个
print tup1+tup2 
print tup2*2             # 复制多份

'''
元组不支持修改, 否则运行报错
tup[0] = 'A'
print tup[0]
'''

# 删除元组（删除整个元组，而不是元组中的某个元素）
tup1 = (1,2,3)
del tup1
# print tup1

# 获取元组长度
tup = (1,2,3,4)
print len(tup)

# 判断元素是否存在
tup = (1,2,3,4)
print 3 in tup


# 比较两个元组,  类似于 List 中的用法
tup1 = (1,2,3,4)
tup2 = (2,2,4)
print cmp(tup1,tup2)

# 返回元组中最大值、最小值
tup = (1,2,3,4)
print max(tup)
print min(tup)

# 将列表转换为元组,并不会改变 List 本身，而是生成一个新的元组
list = [1,2,3,4]
print list
tup = tuple(list)
print tup
print list


# 将字典转换为元组（字典中的 key 组成元组）
dic = {1:'a',2:'b',3:'c'}
print tuple(dic)

