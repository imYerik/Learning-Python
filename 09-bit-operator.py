#!/usr/bin/python
# coding=utf-8
# Learning Python

# Bit operator (&,|,^,~,>>,<<)

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

c = a << 2;       # 240 = 1111 0000
print 'c = a << 2',c

c = a >> 2;       # 15 = 0000 1111
print 'c = a >> 2',c