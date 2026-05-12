# Python Bro Code 踏实补课工程

跟随 [Bro Code: Python Full Course for free 🐍 (2024)](https://www.youtube.com/watch?v=ix9cRaBkVe0) 系统补一遍 Python 基础。

## 这个项目怎么用

这不是一个完整代码仓库，是**一个练习骨架**。每个 `.py` 文件都是空模板，强迫你边看视频边动手写。

每个文件里有四个区块：

1. **概念速记** — 看完这一节后，用 1–3 行写下你的总结。逼自己用自己的话说一遍。
2. **跟着视频敲一遍** — 不要复制粘贴 Bro Code 的代码。暂停视频，自己写，再对答案。
3. **自己练习** — 部分文件预填了 2–3 道小题；其它文件请自己出题或随便写点小工具。
4. **我的笔记 / 踩过的坑** — 反直觉的、卡住的、查文档才搞明白的，记下来。这部分以后复习只看这一段。

## 目录结构

```
python-brocode-study/
├── 01_basics/                # 变量 / 类型 / 输入 / 字符串
├── 02_control_flow/          # if / 循环 / break / continue
├── 03_collections/           # list / tuple / set / dict
├── 04_functions/             # def / 默认参数 / *args **kwargs / 作用域
├── 05_modules_and_files/     # import / 异常 / 文件读写
├── 06_oop/                   # 类 / 继承 / 多态 / 魔术方法 / @property
├── 07_advanced/              # 装饰器 / 生成器 / 推导式 / 多线程
├── 08_gui_optional/          # tkinter（ML 路径上可跳过，时间紧的话先放着）
├── 09_mini_projects/         # 视频里的几个综合小项目
├── README.md
└── 进度追踪.md                 # 完成一节就在这里打勾
```

每个文件名前有数字前缀，按数字顺序学就行。

## 给 Go/Java 背景的你的几条提醒

- 文件头有 **Go/Java 对照** 一行，能让你快速锚定差异；语法相似的部分放心快进
- 真正花时间的应该是这些 Python 独有的东西：缩进作语法、动态类型、列表推导、`*args/**kwargs`、装饰器、生成器、`__魔术方法__`、`with` 上下文、鸭子类型
- `01_basics` 和 `02_control_flow` 大部分内容你能 1.5–2x 看完。**不要在这里花太多时间。**
- `06_oop`、`07_advanced` 才是和 Java 风味差异最大、值得放慢的部分

## 视频时间戳是估算

文件头的章节时间是按视频整体节奏估算的，可能有 5–10 分钟偏差。打开视频时点开 YouTube 描述看官方时间戳更准。

## 学习进度
- 学习中

## 完成判定

不是"看完了视频"，是：
- 进度追踪表所有项目打勾
- `09_mini_projects/` 里至少完成 4 个能跑的小项目
- 能看懂 NumPy 官方 quickstart 而不卡在 Python 语法上（这才是这门课的真正目的）
