# Day10 学习打卡

## 一、今日学习内容

### 1. 装饰器基础

学习了 Python 装饰器的基本结构：

```python
def log(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper
```

装饰器可以在不直接修改原函数代码的情况下，为函数增加额外功能。

---

### 2. `@log` 的作用

在 `Picker` 中：

```python
@log
def pick(self):
    ...
```

相当于：

```python
pick = log(pick)
```

因此，`log()` 接收到的 `func` 就是原来的 `pick` 函数。

---

### 3. `func.__name__`

使用：

```python
func.__name__
```

可以获取被装饰函数的名称。

因此：

```python
print("开始执行", func.__name__)
```

执行 `pick()` 时可以得到：

```text
开始执行 pick
```

相比直接写：

```python
print("开始执行 pick")
```

这种方式更加通用。

---

### 4. 保留原函数返回值

装饰器中使用：

```python
result = func(*args, **kwargs)
return result
```

可以保证原函数的返回值继续传递给调用者。

在 `student_picker` 中，`Picker.pick()` 返回的是 `Student` 对象，因此 `app.py` 仍然可以接收到抽取结果并显示在 GUI 中。

---

## 二、今日项目中的职责划分

### Picker

负责：

- 随机抽取学生
- 防止学生重复抽取
- 记录已经抽取的学生
- 返回 `Student` 对象

不负责 GUI 输出。

### logger

负责：

- 在函数执行前打印日志
- 在函数执行后打印日志
- 获取被装饰函数的名称

### app.py

负责：

- GUI 交互
- 调用 `Picker`
- 接收 `Picker` 返回的 `Student`
- 将抽取结果显示在界面中

---

## 三、今日最终代码

### logger.py

```python
def log(func):
    def wrapper(*args, **kwargs):
        print("开始执行", func.__name__)
        result = func(*args, **kwargs)
        print("日志打印结束")
        return result
    return wrapper
```

### 运行效果

抽取学生时：

```text
开始执行 pick
日志打印结束
```

同时 GUI 显示抽取到的学生。

---

## 四、今日理解

今天理解了装饰器的基本执行过程：

```text
调用 pick()
    ↓
wrapper()
    ↓
打印开始日志
    ↓
执行原来的 pick()
    ↓
得到 Student
    ↓
打印结束日志
    ↓
return result
    ↓
app.py 得到 Student
```

我理解了装饰器不仅可以增加额外逻辑，还需要正确传递原函数的参数和返回值。

---

## 五、今日关键词

- 装饰器
- `@`
- `wrapper`
- `*args`
- `**kwargs`
- `func`
- `func.__name__`
- `return result`
- 函数职责分离
- 日志