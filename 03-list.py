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

list = ['a','b','c']       # 判断元素是否存在
print 'a' in list          # Return True


list = ['a','b','c']       # 遍历 List
for x in list: 
	print x

# List functions
list = [1,2,3]            
print max(list)            # List中最大元素
print min(list)            # List中最小元素

'''
List 比较 cmp(list1,list2)
如果元素是相同类型的，执行比较，并返回结果。如果元素是不同的类型，检查，看看他们是否是数字
1. 如果是数字必要时强制进行数字比较
2. 如果任一元素是数字，然后在另一元素是“大”(数字是“最小”)
3. 否则，类型是按名称字母顺序排序
4. 如果到达了列表中的一个的结束，较长的列表是“大”。如果耗尽列表和共享相同的数据，其结果是并列的，这意味着返回 0
'''
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list2 + [4]
list4 = [1,2,3]
print cmp(list1,list2)
print cmp(list2,list1)
print cmp(list2,list3)
print cmp(list1,list4)

list1 = ['a',2,3]
list2 = [4,5,6]
print cmp(list1,list2)




# 追加一个元素到 List
list = [1,2,3,4]
list.append('a')
print list


# List  追加一个序列( 与 list 相加的区别是，extend 会改变原有的 list 本身)
list1 = [1,2,3,4]
list2 = [5,6,7]
list1.extend(list2)
print list1


# 向 List 指定下标位置插入一个元素
list = [1,2,3,4]
list.insert(2,'a')
print list


# 移除 List 中指定下标的元素并返回该元素值( 默认最后一个元素，可以指定下标来移除指定的元素)
list = [1,2,3,4,5,6]
lastElement = list.pop()
secondElement = list.pop(2)
print lastElement
print secondElement
print list


# 移除 List 中 指定值的元素
list = [1,2,'a',4,5,6]
list.remove('a')
print list


# List 翻转
list = [1,2,'a',4,5,6]
list.reverse()
print list


# 统计Element 在 List 中出现的次数
list = ['a',3,2,4,2,'a',2]
print list.count('a')
print list.count(2)

# 获取指定元素值第一次出现的下标
list = ['a',3,2,4,2,'a',2]
print list.index('a')



# List 排序,sort(func)方法中的 func 函数是可选参数，也可以指定自定义的排序 function
list1 = [2,9,3,7,1]
list2 = ['a',1,'f',5]
print list1
print list2
list1.sort(cmp)
list2.sort()
print list1
print list2


# 二维 List，可以通过list[index1][index2]下标的方式访问二维数组元素
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]
list = [list1,list2]
print list
print list[1][2]
list[0][0] = 0                    
print list


#  通过列表解析的方式来生成 List

'''
列表解析格式：
[expr for iter_var in iterable]
[expr for iter_var in iterable if cond_expr]

第一种语法：首先迭代iterable里所有内容，每一次迭代，都把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。
第二种语法：加入了判断语句，只有满足条件的内容才把iterable里相应内容放到iter_var中，再在表达式中应用该iter_var的内容，最后用表达式的计算值生成一个列表。

'''

list1 = [i for i in range(10)]
list2 = [i for i in range(50,80)]
list3 = [i for i in range(50,80,2)]
list4 = [i+1 for i in range(10)]
list5 = [str.upper() for str in ['HELLO','worlD']]
listZero = [0 for i in range(10)]           # 元素全部为0的 List 
print list1
print list2
print list3
print list4
print list5
print listZero

