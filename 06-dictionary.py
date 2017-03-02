#!/usr/bin/python
# coding=utf-8
# Learning Python

import copy

'''
Dictionary  词典，Key-Value 键值对类型的集合，通过Key 来获取 Value 的值; 
Key 可以是Number、String、Tuple 类型，且不可改变
Value 可以是任意类型，可以改变值
{key1:value1,key2:value2,...}
'''

# 定义并访问字典
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
print userDic
print userDic['Name']

# 修改字典键值
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDic['City'] = 'Shanghai'
print userDic

# 增加一个键值对 (给相应的 Key 赋值，如果 Key 不存在就添加一个 Key-Value)
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDic['Number'] = 1001
print userDic


# 删除字典的键值对
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
del userDic['Phone']
print userDic

# 清空字典的所有键值对
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDic.clear()
print userDic


# 比较字典 cmp()
'''
 比较规则：字典长度 --> Key --> Value
'''
userDic1 = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDic2 = {'Name':'Flood Liu','Gender':'male','City':'Beijing','Phone':18600000000}
userDic3 = {'Gender':'male','City':'Beijing','Phone':18600000000}
userDic4 = {'Name':'Flood Liu','City':'Beijing','Phone':18600000000}
userDic5 = {'Name':'Flood Liu','City':'Beijing','Phone':18600000000}
print cmp(userDic1,userDic2)
print cmp(userDic2,userDic3)
print cmp(userDic3,userDic4)
print cmp(userDic4,userDic5)


# 字典长度（Key 总数）
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
print len(userDic)

# 字典转换为字符串
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDicStr = str(userDic)
print type(userDic)              # 查看 userDic 的变量类型
print type(userDicStr)           # 查看 userDicStr 的变量类型

# 字典拷贝
'''
Python 中一切皆对象；
伟大的托尼.玛涛说，Python 中有两种对象，immutable object 和 mutable object，在赋值、传参、返回值 的时候用法不一样;
int、float、str、tuple 都是 immutable, list、dict、set 是 mutable;

immutable 对象：对象的值更改时，对象的引用所指向的地址空间也会更改(新开辟一块内存空间)
例如：
>>> a = 1
>>> id(a)
140721453579256
>>> a = 2
>>> id(a)
140721453579232

mutable 对象：对象的值更改时，对象的引用所指向的地址空间会更改；
例如：
>>> list1 = [1,2,3,4,5]
>>> list2 = list1
>>> list2
[1, 2, 3, 4, 5]
>>> id(list1),id(list2),id(list1[0]),id(list2[0])
(4430194592, 4430194592, 140721453579256, 140721453579256)
>>> list1[0]=0
>>> id(list1),id(list2),id(list1[0]),id(list2[0])
(4430194592, 4430194592, 140721453579280, 140721453579280)

浅拷贝(copy)：新拷贝的对象只有顶级对象开辟新的内存空间，嵌套对象依然指向原始对象的地址空间;  
       比如，一个字典中嵌套了一个 List 对象，通过浅拷贝生成的字典中的List 对象依然指向原对象的地址空间, 所以原字典对象中的 List 更新也会影响新拷贝的对象中的 List;

深拷贝(deepcopy)：新拷贝的对象完全开辟一块新的地址空间,不管是顶级对象还是嵌套的子对象全部开辟新的内存地址；

'''

userDic = {
              'Yerik':{'Gender':'male','City':'Beijing','Phone':18612345678},
              'Flood':{'Gender':'male','City':'Tianjin','Phone':18600000000},
              'Tony':'Ma Tao'
          }
userDic1 = userDic                                 #  原对象和新对象指向相同的地址空间
userDic2 = copy.copy(userDic)                      #  浅拷贝，顶级对象新开辟内存空间，嵌套对象指向原对象的内存空间
userDic3 = copy.deepcopy(userDic)                  #  深拷贝，顶级对象和嵌套对象完全开辟新的内存空间
userDic['Flood'] ['Gender'] = 'female'             #  修改嵌套对象
userDic['Tony'] = 'Diao Bao Le'                    #  修改顶级对象
print 'userDic :',userDic
print 'userDic1:',userDic1
print 'userDic2:',userDic2
print 'userDic3:',userDic3
print id(userDic2)
print id(userDic3)



# 判断字典中是否有某个 key
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
print userDic.has_key('Name')


#  返回字典中所有的 Key & Value
userDic = {
              'Yerik':{'Gender':'male','City':'Beijing','Phone':18612345678},
              'Flood':{'Gender':'male','City':'Tianjin','Phone':18600000000},
              'Tony':'Ma Tao'
          }
print userDic.keys()    
print userDic.values()


# 设置字典中 key 的值，如果不存在则添加并设置 default；setdefault(key,default)
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDic.setdefault('Phone',9999999999)
userDic.setdefault('Number',9999)
print userDic

#  获取字典中 key 的值，如果不存在则获取 default值；get(key,default)
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
print userDic.get('Number',9999)

# 返回字典中的元组
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
print userDic.items()

# 将字典2的 key-value 更新到字典1中(如果Key 存在则更新其 Value，不存在则增加一个 Key 并赋值)
userDic = {'Name':'Yerik Gao','Gender':'male','City':'Beijing','Phone':18612345678}
userDic1 = {'Name':'Flood','Number':0}            # Name存在将更新值，Number 不存在会新增该 Key
userDic.update(userDic1)
print userDic


# 通过元组、List中的 key 创建字典 dict.fromkeys(seq[,defaultValue])
keysTuple = ('Name','Number')
userDic = dict.fromkeys(keysTuple,9999)

keysList = ['Age','Gender']
userDic2 = dict.fromkeys(keysList)
print userDic
print userDic2






