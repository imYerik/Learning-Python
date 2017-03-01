#!/usr/bin/python
# coding=utf-8
# Learning Python


# if statement
a = 10

if a == 10 : print 'a == 10'

if a == 10 : 
    print 'a == 10'


# if else statement
a = 10

if a > 3 :
    print 'a > 3'
else:
    print 'a <= 3'

if a > 3 and a < 20 :
    print 'a > 3 and a < 20'
else:
    print 'a <= 3 or a >= 20'

if (a > 3 and a < 5) or (a >10 and a < 20):
    print 'hello'
else:
    print 'undefined'

# if elif statement (like switch statement in othter language)
if a == 3:
    print 'boss'
elif a == 4:
    print 'worker'
elif a == 5:
    print 'manager'
else:
    print 'empolyee'


    