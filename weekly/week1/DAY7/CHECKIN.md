# Day 7 Check-in

## 一、今日主题

Python 异常处理

## 二、今日完成内容

- 学习 `try / except`
- 使用 `ValueError` 处理整数输入错误
- 编写 `input_int()`
- 编写 `input_positive_int()`
- 编写 `input_age()`
- 编写 `input_score()`
- 使用 `FileNotFoundError` 处理文件不存在
- 使用 `ValueError` 处理文件中的非法数据
- 使用 `raise` 主动抛出异常
- 创建自定义异常 `InvalidScoreError`
- 编写 `validate_score()`
- 使用多个 `except` 分别处理不同异常
- 学习模块导入及异常在函数之间的传递
- 完成综合练习 `load_scores()`

## 三、异常类型理解

### ValueError

用于处理值本身不符合要求的情况，例如将无法转换为整数的字符串传给 `int()`。

### FileNotFoundError

用于处理读取文件时文件不存在的情况。

### InvalidScoreError

自定义异常，用于处理成绩不符合业务规则的情况。

本次学习中按照异常产生的功能进行区分。

## 四、异常处理理解

`raise` 用于抛出异常。

`except` 用于捕获异常。

目前能够理解基本的异常处理流程：

```text
发生异常
    ↓
raise / Python 自动抛出
    ↓
try
    ↓
except 捕获
    ↓
处理异常
```

## 五、综合练习测试

`load_scores(filename)` 已完成以下情况测试：

1. 正常数据 → 正确返回成绩列表
2. 非整数数据 → 捕获 `ValueError`
3. 成绩超出范围 → 捕获 `InvalidScoreError`
4. 文件不存在 → 捕获 `FileNotFoundError`

以上测试均通过。

## 六、学习中的主要问题

程序运行流程比较容易混淆。

尤其需要继续理解：

- 异常在哪里产生
- 异常如何向调用方传递
- 哪个 `except` 会捕获异常
- 异常被处理后程序如何继续执行

## 七、自评

**8 / 10**

独立完成 `load_scores()`：

**基本能**

## 八、今日最大收获

学习到了自定义错误和程序流中的错误处理。

## 九、Day 7 总结

Day 7 已完成 Python 异常处理基础学习。

目前已经能够使用内置异常和自定义异常处理实际程序中的错误，并能够根据不同错误类型进行分别处理。

后续重点继续巩固异常在函数之间的传递和完整执行流程，而不是单纯增加异常类型。