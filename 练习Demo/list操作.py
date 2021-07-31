# list操作

demo_list = []

# 增加

# append()方法：在末尾添加元素
demo_list.append("how", )

# insert()方法：在指定位置添加元素或者列表
demo_list.insert(3, "insert1")
demo_list.insert(4, ["insert2", "insert3"])

# extend()方法：可迭代，分解成元素添加在末尾。
demo_list.extend("find")


# 删
# pop()方法： 按照下标索引删除指定的值
demo_list.pop(0)

# remove()方法：按元素删除指定的值
demo_list.remove("insert1")

# clear()方法：清空列表内数据
# demo_list.clear()

#del ：删除列表、也可以进行切片删除
del demo_list[0:1]


# 改
# s[ ] = '  '  #元素赋值
demo_list[1] = "r"
# 切片赋值 ??
# demo_list[0:2] =('a')


# 方法
# index()方法：获取指定元素的下标
print(demo_list.index("f"))

# count()方法：计算元素出现的次数
print(demo_list.count("r"))

# sort()方法：进行排序，默认是正向排序，想要反向排序需要加：（reverse=True） ,reverse返转的意思
demo_list.sort(reverse=True)

# 翻转
demo_list.reverse()



print(demo_list)