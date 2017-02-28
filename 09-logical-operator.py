#!/usr/bin/python
# coding=utf-8
# Learning Python



# Logical Operator (and,or,not)

a = 10
b = 20
print 'a:',a,'b:',b

if ( a and b ):
   print '1 - 变量 a 和 b 都为 true'
else:
   print '1 - 变量 a 和 b 有一个不为 true'

if ( a or b ):
   print '2 - 变量 a 和 b 都为 true，或其中一个变量为 true'
else:
   print '2 - 变量 a 和 b 都不为 true'

# 修改变量 a 的值
a = 0
print 'a:',a

if ( a and b ):
   print '3 - 变量 a 和 b 都为 true'
else:
   print '3 - 变量 a 和 b 有一个不为 true'

if ( a or b ):
   print '4 - 变量 a 和 b 都为 true，或其中一个变量为 true'
else:
   print '4 - 变量 a 和 b 都不为 true'

if not( a ):
   print '5 - 变量 a 为false'
else:
   print '5 - 变量 a 为true'

if not( a and b ):
   print '6 - 变量 a 和 b 都为 false，或其中一个变量为 false'
else:
   print '6 - 变量 a 和 b 都为 true'