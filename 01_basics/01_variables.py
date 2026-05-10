"""
模块: 变量与基本数据类型
对应视频章节: 约 0:00:00 – 0:14:00

学习目标:
- int / float / str / bool 的声明与赋值
- type() 查看类型
- Python 变量是动态类型，与 Go/Java 的静态声明不同

Go/Java 对照:
- Go: var x int = 5 / x := 5；Java: int x = 5；Python: x = 5（无类型声明，运行时绑定）
"""
from decimal import Decimal
# ============================================================
# 概念速记 (3 分钟内自己能写出来才算会)
# ============================================================
# TODO: 用 1-3 行写下你对本节核心点的总结

# ============================================================
# 跟着视频敲一遍
# ============================================================
# TODO: 在这里跟着 Bro Code 视频写代码，不要复制粘贴
# String
first_name = "Raymond"
print(f"Your name is {first_name}")
# Integer
age = 20
print(f"Your age is {age}")
# Float
num_of_students = 20.99
print(f"These are {num_of_students} students in the class")
# Bool
online = True
if online:
    print("You are online")
else:
    print("You are offline")
# ============================================================
# 自己练习 (可参考下面的题目，也可以自己出)
# ============================================================
# 题目1: 定义 5 个不同类型的变量并打印它们的值与类型
# 题目2: 用一行交换两个变量的值（Python 特有写法）
# 题目3: 把 "3.14" (字符串) 转成 float，再加 1 后转回 str

# topic 1:
email = "XiaobinCao@gmail.com" # String
print(f"Your email is {email} - type:{type(email)}")

height = 180 # Integer
print(f"Your height is {height} - type:{type(height)}") 

price = 20.99 # Float
print(f"The price of this item is {price}$ - type:{type(price)}")

item_status = True # Bool
if item_status:
    print(f"{item_status}This item is now avaiable - type:{type(item_status)}")
else:
    print(f"{item_status}This item is not listed - type:{type(item_status)}")

hobbies = ["AI","computer"] # list
print(f"Your hobbies is {hobbies} - type:{type(hobbies)}")

# topic 2: 用一行交换两个变量的值
a = 10
b = 20
print(f"交换前: a = {a}, b = {b}")
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

# topic 3: 把 "3.14" (字符串) 转成 float, 再加 1 后转回 str
s = "3.14"
print(f"原始值: {s}, 类型: {type(s).__name__}")

f = float(s) + 1
print(f"加 1 后: {f}, 类型: {type(f).__name__}")

result = str(f)
print(f"转回字符串: {result}, 类型: {type(result).__name__}")

result_decimal = str(Decimal("3.14") + 1)
print(f"转回字符串: {result_decimal}, 类型: {type(result_decimal).__name__}")
# 一行写法
one_liner = str(float("3.14") + 1)
print(f"一行写法结果: {one_liner}")
# ============================================================
# 我的笔记 / 踩过的坑
"""
f 表示 f-string (格式化字符串字面量) 它允许你在字符串中直接嵌入变量或表达式用{}包起来
右边 b, a 先打包成一个元组 (b, a),再解包赋值给左边的 a, b。所以等价于:
temp = (b, a)   # 先打包
a = temp[0]     # 再解包
b = temp[1]
不需要中间变量,Python 自动处理。

注意到一个反直觉的现象:3.14 + 1 的结果是 4.140000000000001,而不是 4.14!

为什么会这样?——浮点数精度问题
这不是 Python 的 bug,所有遵循 IEEE 754 标准的语言(Java、Go、JavaScript、C...)都有这问题。

原因:计算机用二进制存浮点数,而 3.14 在二进制里是无限循环小数,只能近似表示。
"""
# ============================================================
# TODO: 写下让你卡住或反直觉的点，方便后面复习


if __name__ == "__main__":
    # TODO: 在这里调用你写的函数 / 运行测试
    pass
