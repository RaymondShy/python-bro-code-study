"""
模块: if / elif / else
对应视频章节: 约 0:58:00 – 1:10:00

学习目标:
- 条件表达式
- else if 在 Python 里写作 elif
- 缩进决定语句块

Go/Java 对照:
- 没有大括号，缩进就是语法的一部分（4 个空格）
"""

# ============================================================
# 概念速记 (3 分钟内自己能写出来才算会)
# ============================================================
# TODO: 用 1-3 行写下你对本节核心点的总结

# ============================================================
# 跟着视频敲一遍
# ============================================================
# TODO: 在这里跟着 Bro Code 视频写代码，不要复制粘贴
age = int(input("Enter your age:"))
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now to signed up")
elif age <0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")
# ============================================================
# 自己练习 (可参考下面的题目，也可以自己出)
# ============================================================
# 题目1: TODO 判断用户是否在线
online = True
if online:
    print("The user is online")
else:
    print("The user is offline")
# 题目2: TODO 判断用户是否想要食物
response = input("Would you like food? (Y/N)")
if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")
# 题目3: TODO 温度测量计算
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F)")
temp = float(input("Enter the temperature:"))
if unit == "C":
    temp = round((temp * 9)/5 + 32,1) # F = (C * 9/5)+32
    print(f"The temperature in Fahrenheit is: {temp}")
elif unit == "F":
    temp = round((temp - 32)* 5/9,1) # C = (F - 32) * 5/9
    print(f"The fahrenheit in temperature is: {temp}")
else:
    print(f"{unit} is an invalid unit of measurement")
# ============================================================
# 我的笔记 / 踩过的坑
# ============================================================
# TODO: 写下让你卡住或反直觉的点，方便后面复习


if __name__ == "__main__":
    # TODO: 在这里调用你写的函数 / 运行测试
    pass
