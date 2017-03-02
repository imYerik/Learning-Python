#!/usr/bin/python
# coding=utf-8
# Learning Python


# for loop

for i in range(0,5):          # Similar with for(i=0;i<5;i++) in C/C++, but more simple
    print i

for letter in 'Hello Wolrd' :
    print letter

list = ['Hello','World']
for word in list :
    print word

print

list = ['Hello','World']
for index in range(len(list)):
    print list[index]


# enumerate list
list = ['Hello','World']
for index,item in enumerate(list) :
    print index,item

print

for letter in 'Hello World':
    if letter == 'o' : break
    print 'Current letter:',letter

print

# continue statement
for letter in 'Hello World':
    if letter == 'l':
        continue
    print letter

print
