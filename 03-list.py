#!/usr/bin/python
# coding=utf-8
# Learning Python

'''
类似 Java 中的 ArrayList，可以动态增加删除的数组, 数组起始下标为0,同一个List 元素的类型可以不同，List 中可以嵌套 List
'''

# Define a List
list1 = [1,2,3,4,5]
list2 = ['a','b','c']
list3 = ['Hello','World',2]

print 'list1:',list1
print 'list2:',list2
print 'list3:',list3

# Get element of List
print '----------- Get element of List -----------'
print 'list1[3] ', list1[3]
print 'list1[1:3] ', list1[1:3]        #  取第1至3个元素
print 'list1[2:] ', list1[2:]          #  从第二个元素开始截取
print 'list1[-2] ', list1[-2]          #  倒数第二个元素

# Update List
print '----------- Update List -----------'
list = ['Hello','World','!']
list[1] = 'Python'
print list

# Delete element of List
print '----------- Delete element of List -----------'
list = ['Hello','World','!']
print list
del list[1]
print list

# Nested List
print '----------- Nested List -----------'
list1 = [1,2,3]
list2 = [4,5,6]
list = [list1,list2]
print list

# List operators len(), + , * , in , for x in [x,y,z,...]
list = [1,2,3,4]           # List 长度
print len(list)

list1 = [1,2,3]            # 合并 List
list2 = [4,5,6]
print list1+list2


list = ['a','b','c']       # 重复多次 List
print list*3

list = ['a','b','c']
print 'a' in list          # Return True


list = ['a','b','c']       # 遍历 List
for x in list: 
	print x

# List functions
list = [1,2,3]            
print max(list)            # List中最大元素
print min(list)            # List中最小元素


list1 = [1,2,3]
list2 = [4,5,6]
print cmp(list1,list2)





