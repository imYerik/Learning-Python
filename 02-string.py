#!/usr/bin/python
# coding=utf-8


# Learning Python (String)

'''
Python 字符串是 immutable 的，通过单引号（'）或双引号（"）来创建，可以通过类似数组下标str[index]的方式访问字符串中的字符；
字符串常用的操作包括：字符串更新、字符串截取、字符串格式化、字符串转义（如换行、回车、制表符等）；

'''


# 定义字符串
str = 'hello world'
print 'str: ',str

# 获取字符串中的字符
print str[3]
print str[0:2]
print str[4:]


# 字符串更新 !!!
str = 'Hello World'
# str[0] = 'J'                  # Error, string 类型为 immutable 的数据类型


# 转义字符

'''
\    续行符
\\   \反斜杠
\'   '单引号
\"   "双引号
\a   响铃
\b   退格
\000 空
\n   换行
\v   纵向制表符
\t   横向制表符
\r   回车
\f   换页
\0yy 八进制数，yy 代表字符，例如\012代表换行符
\xAA 十六进制数，AA 代表字符，例如\x0a代表换行符
\other 其他字符以普通格式输出

'''

print '续行符\: ', 'Hello '\
      'World'

print '反斜杠: ', 'Hello \\ World'

print '单引号: ', '\'Hello World\''

print '双引号: ','\"Hello World\"'

print '响铃: ','\a'

print '退格: ','Hello World\b '              # Python 中退格分两步，向前移动光标，并替换为\b后面的字符，所以退格实际上是用空格替换了前一个字符；
print '退格: ','Hello World\b\b\baaa'        # Python 中退格分两步，向前移动光标（移动次数按\b的个数定），并替换为\b后面的字符，所以退格实际上是用空格替换了前一个字符；

print '空(Null): ','Hello\000World'

print '换行: ','Hello \nWorld'

print '纵向制表符: ','Hello\vWorld'

print '横向制表符: ','Hello\tWorld'

print '回车: ','Hello\rWorld'                 # 注：回车是指光标移至行首

print '换页: ','Hello\fWorld'

print '八进制数：','Hello \012World'

print '十六进制数: ','Hello \x0aWorld'


# 字符串运算符
'''
+		字符串链接
*		重复输出字符串
[index]	通过索引获取字符
[:]		字符串截取, 左闭右开区间[x,y)
in  	指定的字符在字符串中存在返回 true
not in  指定的字符在字符串中不存在返回 true
r/R 	原始字符串（忽略转义）

'''

str1 = 'Hello'
str2 = 'World'
print 'str1 str2相加: ',str1 + str2

str = 'Hello '
print 'str * 3 = ',str * 3

str = 'Hello '
print 'str[1] 的字符：',str[1]

str = 'Hello'
print 'str[1:3] 的字符：',str[1:3]
print 'str[:3] 的字符：',str[:3]
print 'str[3:] 的字符：',str[3:]

str = 'Hello'
isHin = 'H' in str
print '字符 H 在 str 中: ',isHin

str = 'Hello'
isWNotin = 'W' not in str
print '字符 W 不在 str 中: ',isWNotin

str = R'\"Hello\nWorld\"'
print '原始字符串: ',str



# 字符串格式化
'''
%d	整数(Dec)
%f	浮点数
%c	字符
%s	字符串
%o	无符号八进制整数(Oct)
%x	无符号十六进制整数(Hex)
%X	无符号十六进制整数( 大写)
%%  输出%
#   八进制前显示0，十六进制前面显示0x或0X，如 %#x，%#o


'''
print 'I am %d years old.' %(20)
print 'My score is %f' %(97.5)    
print 'My score is %.2f' %(97.5)    # 保留2位小数

print 'My name is %s' %('Yerik')
print 'My grade is %c' %('A')
print 'Hello! My name is %s, I am %d years old now, my score is %f and my grade is %c !' %('Yerik', 20, 97.5, 'A')


nHex = 0x20
print "nHex = %x,nDec = %d,nOct = %o" %(nHex,nHex,nHex)
print "nHex = %#x,nDec = %d,nOct = %#o" %(nHex,nHex,nHex)


# 三引号
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# 典型的用例，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。


errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''



# 字符串相关函数
# 字母大小写处理
print 'hello world'.upper()			# 全部大写
print 'HELLO WORLD'.lower()			# 全部小写
print 'Hello World'.swapcase()		# 大小写互换
print 'hello WORLD'.capitalize()	# 第一个单词首字母大写，其余全小写
print 'hello WORLD'.title()			# 所有单词的首字母大写，其余全小写

# 字符串搜索
print 'hello world'.find('o')		# 搜索字母在字符串中第一次出现的下标，没有则返回-1
print 'hello world'.find('o',6)     # 从指定下标位置开始搜索相应字符所处的下标，没有则返回-1
print 'hello world'.find('w',2,5)   #指定下标位置范围搜索相应字符所处的下标，没有则返回-1
print 'hello world'.rfind('o')		# 从右侧向左开始搜索，搜索字母在字符串中第一次出现的下标，没有则返回-1
print 'hello world'.count('o')		# 统计字符出现的次数

# 字符串替换
print 'hello world'.replace('world','python') 		# 字符串替换
print 'hello world, world'.replace('world','python',1) # 指定最大替换次数（默认全部替换）

# 字符串去空格
print ' hello world '.strip()		#去掉字符串两边的空格
print ' hello world '.lstrip()		# 去掉字符串左边的空格
print ' hello world '.rstrip()		# 去掉字符串右边的空格

# 字符串分割为数组(默认为空格，可以指定分隔符)
print 'hello world'.split()
print 'hello-world'.split('-')


#字符串判断
print 'hello world'.startswith('hello')		# 判断是否以 hello 开头
print 'hello world'.endswith('world')		# 判断是否以 world 开头
print 'hello1world'.isalnum()				# 判断是否全为数字和字母组成
print 'helloworld'.isalpha()				# 判断是否纯字母
print '123123'.isdigit()					# 判断是否纯数字
print 'hello world'.islower()				# 判断是否全小写
print 'HELLO WORLD'.isupper()				# 判断是否全大写




