"""
模块: 算术运算
对应视频章节: 约 0:27:00 – 0:35:00

学习目标:
- + - * / // % **
- 整除 // 与浮点除 / 的区别
- math 模块常用函数

Go/Java 对照:
- Python 的 / 是浮点除（不像 Java/Go 的整数除）；整除要用 //
"""

import math

# ============================================================
# 概念速记 (3 分钟内自己能写出来才算会)
# ============================================================
# TODO: 用 1-3 行写下你对本节核心点的总结

# ============================================================
# 跟着视频敲一遍
# ============================================================
# TODO: 在这里跟着 Bro Code 视频写代码，不要复制粘贴
friends = 10
"""
friends = friends + 2
friends += 2
friends = friends - 2
friends -= 2
friends = friends * 2
friends *= 2
friends = friends / 2
friends /= 2
friends = friends ** 2
friends **= 2
"""
remainder = friends % 3
print(remainder)

x = 3.14
y = -4
z = 5

x = round(x)  # 取整
print(x)
y = abs(y)  # 绝对值
print(y)
z = pow(z, 3)  # 幂次方
print(z)
a = max(x, y, z)
b = min(x, y, z)
print(f"Max value:{a} - Min value:{b}")
# ============================================================
# 自己练习 (可参考下面的题目，也可以自己出)
# ============================================================
# 题目1: TODO 计算出圆的周长
""" topic1:  C = 2pir"""
radius = float(input("Please enter the radius of the circle:"))
circumference = round(2 * math.pi * radius, 2)
print(f"The circumference of the circle is:2 * {math.pi} * {radius} = {circumference}")

# 题目2: TODO 计算出圆的面积
""" topic2:  """
radius_of_area = float(input("Please enter the radius of the circle:"))
area = math.pi * pow(radius,2)
print(f"The area of the circle is:{area}")

# 题目3: TODO 计算直角三角形斜边的长度
a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Side C = {c}")
# ============================================================
# 我的笔记 / 踩过的坑
# ============================================================
# TODO: 写下让你卡住或反直觉的点，方便后面复习


if __name__ == "__main__":
    # TODO: 在这里调用你写的函数 / 运行测试
    pass
