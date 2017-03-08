#!/usr/bin/python
# coding=utf-8
# Learning Python

# Bit operator (&,|,^,~,>>,<<)
'''
&    按位与
|    按位或
^    按位异或
~    按位取反
<<   左移运算符，高位丢弃，低位补0
>>   右移运算符，低位丢弃，高位补0
'''


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
print 'a:',a,'b:',b,'c:',c

c = a & b;        # 12 = 0000 1100
print 'a & b',c

c = a | b;        # 61 = 0011 1101 
print 'a | b',c

c = a ^ b;        # 49 = 0011 0001
print 'a ^ b',c

c = ~a;           # -61 = 1100 0011
print 'c = ~a',c

c = a << 2;       #  左移2位，240 = 1111 0000
print 'c = a << 2',c

c = a >> 2;       # 右移2位，15 = 0000 1111
print 'c = a >> 2',c
