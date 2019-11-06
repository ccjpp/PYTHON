# 写入字符串到文件
# fo = open("test.txt", "w")
# fo.write("www,baidu.com\n")
import os
# 读取data.txt里面的内容
with open('data.txt', 'r') as f:
    data = f.read()
    print('context:{}'.format(data))

# 写入内容到data.txt里
with open('data.txt', 'w') as f:
    data = 'some data to be written to the fil'
    f.write(data)

# 获取目录列表
entries = os.scandir()
print("文件:")
with os.scandir('H:/pythonScript/study/FILE') as entries:
    for entry in entries:
        print(entry.name)

#列出子目录
basePath = 'H:/pythonScript'
print("目录")
with os.scandir(basePath) as entries:
    for entry in entries :
        if entry.is_dir():
            print(entry.name)

# 读取文件内容，并打印
# fo=open("test.txt","r+")
# str=fo.read(10)
# print("读取的字符串是：",str)
#
# #file的
# #关闭打开的文件
# fo.close()
