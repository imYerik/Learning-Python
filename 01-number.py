#!/usr/bin/python
# coding=utf-8

import math
import random


# Learning Python (Varilable Number)

'''
int：整型
float：浮点型，如 5.16，或者还可以用科学计数法表示（2.5e2 = 2.5 * 10^2）
long：长整型
complex：复数, 用 a + bj或者 complex(a,b)表示，其中 a为实部，b 为虚部

'''

# Number definition
print '--------- Number definition --------'

var_int1 = 10
var_int2 = -10
var_float1 = 10.21
var_float2 = 100 + 2.5e2
var_long = 12345678901234L
var_complex1 = 3.1+4j
var_complex2 = complex( 3.2 , 4 )

print var_int1
print var_int2
print var_float1
print var_float2
print var_long
print var_complex1
print var_complex2


# Number transformation
print '--------- Number transformation --------'

print int(var_float1)
print long(var_float1)
print float(var_int1)
print hex(var_int1)        # 将整数转换为十六进制字符串
print oct(var_int1)        # 将整数转换为八进制字符串

print str(var_float2)      # 将对象转换为字符串
print unichr(6)            # 将整数转换为 Unicode 字符


# Mathematical functions
print '--------- Mathematical functions --------'
print abs(var_int2)        		# 绝对值（返回整型）
print math.fabs(var_int2)       # 绝对值（返回 float 类型）
print math.ceil(var_float1)     # 上取整(需要引入math模块)
print math.floor(var_float1)    # 下取整
print math.modf(var_float1)     # 分离整数和小数部分
print round(math.pi,2)          # 四舍五入

print cmp(var_int1,var_int2)    # x < y 返回 -1，x > y 返回1， x == y 返回1
print cmp(var_int2,var_int1)    # x < y 返回 -1，x > y 返回1， x == y 返回1
print cmp(var_int1,var_int1)    # x < y 返回 -1，x > y 返回1， x == y 返回1

print max(var_int1,var_int2,var_float1,var_float2)    #  返回最大值，参数可以为序列
print min(var_int1,var_int2,var_float1,var_float2)    #  返回最小值，参数可以为序列


print math.log(var_int1)        # 自然对数，即 loge(x)
print math.log10(var_int1)      # 以 10 为底的对数，即 log10(x)

print math.sqrt(var_int1)       # 平方根
print pow(2,3)                  # x 的 y 次方(x ** y)


# Random number
print '--------- Random Number --------'
print random.random()           # 返回[0,1)的随机数
print random.choice(range(10))  # 从序列中返回一个随机数
print random.randrange(1,100,2) # 在指定范围内，按指定步长的递增集合中返回一个随机数 randrange(start,stop,step)

random.seed(10)                 # 生成随机数种子
print random.random()           # 生成同一个随机数
random.seed(10)                 # 生成随机数种子
print random.random()           # 生成同一个随机数

list = [3,2,1,6,10]
random.shuffle(list)            # 将序列随机排序,会修改序列的值
print list



# Trigonometric function
print '--------- Trigonometric function --------'
print math.acos(0.3)            # 反余弦弧度值
print math.asin(0.3)            # 反正弦弧度值
print math.atan(0.3)            # 反正切弧度值
print math.atan2(3,5)           # (x,y)坐标的反正切值
print math.cos(30)              # 弧度的余弦值
print math.sin(30)              # 弧度的正弦值
print math.tan(30)              # 弧度的正切值
print math.degrees(math.pi/2)   # 弧度转换为角度
print math.radians(90)          # 角度转换为弧度

# Constant

print math.pi                   # 圆周率 π 
print math.e                    # 自然常数 e



count = 100
name = 'yerik'

# String
str = 'hello world'
print 'str:',str
print str[3]
print str[0:2]
print str[4:]
print str+str
print str*2
