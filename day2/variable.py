# coding=utf-8
import math

a = 100
b = 12.345
c = 1 + 5j
d = 'hello , world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

########################################################
# 从键盘输入两个数来实现对两个整数的运算
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

#############################################################
# 运算符
a = 10
b = 3
a += b
a *= a + 2  # a=a*(a+2)
print(a)

##########################################################
# 华氏温度转换为摄氏温度
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print ('%.1f 华氏度=%.1f摄氏度' % (f, c))

# 输入圆的半径计算计算周长和面积
radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print ('周长：%.2f' % perimeter)
print ('面积 : %.2f' % area)

# 判断闰年
year = int(input('请输入年份：'))
is_leap = (year % 4 and year % 100 != 0) or \
          year % 400 == 0
print (is_leap)
