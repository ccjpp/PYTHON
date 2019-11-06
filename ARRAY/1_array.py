#数组在python里叫列表
#一些简单特性
print(['hi']*4)
print(3 in [1,2,3])#元素是否在列表中

#迭代
for x in [1,2,3]:
    print(x,end=" ")

#确定数组长度
print(len([1,2,3]))

#python 列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
print(L[2])#输出第三个元素
print(L[-2])#输出从右边起，倒数第二个元素
print(L[1:])#输出第一个元素后面的元素

print(L.append('taobo'))
print(L)