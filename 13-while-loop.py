#!/usr/bin/python
# coding=utf-8
# Learning Python



# while loop
i = 0

while i < 5 :
    print i
    i = i + 1

nums = [1,2,3,4,5,6,7,8,9,0]
even = []
odd = []

while len(nums) > 0 :
    number = nums.pop()
    if number % 2 == 0 :
        even.append(number)
    else:
        odd.append(number)

print 'even:',even
print 'odd:',odd


# continue statement
i = 0
while i <= 10 :
    if i % 2 > 0:
        i += 1
        continue
    print i 
    i += 1

print

# break statement
i = 0
while 1 :
    if i > 10 :
        break
    print i
    i += 1

print

# while-else statement
i = 0
while i < 5 :
    print i
    i += 1
else:
   print 'i >= 5' 



