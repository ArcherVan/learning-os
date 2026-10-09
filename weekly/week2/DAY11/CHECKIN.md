# Day 11 学习记录

## 一、今日主题

Python 装饰器进阶：

- `functools.wraps`
- `*args` 和 `**kwargs`
- 函数返回值处理
- 装饰器异常处理
- `raise` 重新抛出异常
- 通用日志装饰器

---

## 二、今日完成内容

### 1. 理解装饰器替换函数的过程

理解：

```python
@log
def add(a, b):
    return a + b
```

本质上相当于：

```python
add = log(add)
```

而 `log()` 返回的是 `wrapper`，因此装饰之后的 `add` 实际指向 `wrapper`。

---

### 2. 理解 `functools.wraps`

使用：

```python
from functools import wraps
```

并在包装函数上使用：

```python
@wraps(func)
def wrapper(*args, **kwargs):
    ...
```

验证了使用 `@wraps(func)` 后，包装函数仍然能够保留原函数的重要元信息。

例如：

```python
print(add.__name__)
print(add.__doc__)
```

可以得到原函数的名称和文档字符串。

---

### 3. 理解 `*args` 和 `**kwargs`

理解通用装饰器不能把参数形式写死：

```python
def wrapper(a, b):
```

因为不同函数可能具有不同的：

- 参数数量
- 位置参数
- 关键字参数

因此使用：

```python
def wrapper(*args, **kwargs):
```

可以接收不同形式的参数，并通过：

```python
func(*args, **kwargs)
```

将参数原样传递给原函数。

实际测试了：

```python
add(a, b)
greet(name)
introduce(name, age=20)
```

验证同一个装饰器可以处理不同参数形式的函数。

---

### 4. 获取并记录函数返回值

在装饰器中使用：

```python
result = func(*args, **kwargs)
```

保存原函数的返回值，然后进行日志记录：

```python
print("函数", func.__name__, "执行完成，返回值:", result)
```

最后：

```python
return result
```

保证装饰器不会丢失原函数的返回结果。

---

### 5. 装饰器异常处理

使用 `try / except` 对被装饰函数进行异常处理。

测试：

```python
@log
def divide(a, b):
    return a / b
```

正常调用：

```python
divide(10, 2)
```

能够正常记录返回值。

异常调用：

```python
divide(10, 0)
```

能够捕获：

```text
division by zero
```

并使用：

```python
raise
```

将原异常继续抛出。

---

## 三、今天的重要理解

### 1. 异常会中断正常执行流程

如果：

```python
result = func(*args, **kwargs)
```

发生异常，那么后面的普通代码不会继续执行。

因此：

```python
print("日志打印结束")
```

不会在异常发生后自动执行。

---

### 2. 不应该随意吞掉异常

不能简单使用：

```python
except Exception:
    pass
```

否则原函数发生异常后，调用者可能无法知道函数实际上执行失败。

日志装饰器可以记录异常，但应该保留异常的正常传播。

---

### 3. 装饰器应该具有通用性

不能把：

```python
add
```

等具体函数名称写死在装饰器中。

使用：

```python
func.__name__
```

可以动态获取当前被装饰函数的名称。

因此同一个装饰器可以用于：

```python
add()
greet()
introduce()
divide()
```

等不同函数。

---

## 四、今日代码能力

今天完成了一个能够：

- 接收任意参数
- 保留原函数元信息
- 执行原函数
- 获取返回值
- 记录正常执行
- 记录异常
- 继续抛出异常

的通用日志装饰器。

核心结构：

```python
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("打印开始日志")

        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("函数执行出现异常:", e)
            raise
        else:
            print("函数", func.__name__, "执行完成，返回值:", result)
            print("日志打印结束")
            return result

    return wrapper
```

---

## 五、今日遇到的问题

### 问题 1：误认为异常发生后后面的代码仍然会执行

最初认为：

> 不管函数是否出现异常，后面的代码都会执行。

后来理解：

> 未处理异常会中断当前正常执行流程，后面的普通语句不会继续执行。

---

### 问题 2：理解 `wrapper` 和 `log` 的关系

最初认为装饰后的函数最终指向 `log`。

后来理解：

```python
add = log(add)
```

而 `log()` 返回：

```python
wrapper
```

因此最终：

```text
add → wrapper
```

`log` 的作用是创建并返回包装函数。

---

## 六、今日总结

Day11 从“会使用装饰器”进一步理解到了装饰器的内部机制。

目前能够理解：

```text
原函数
  ↓
传入装饰器
  ↓
生成 wrapper
  ↓
wrapper 接收参数
  ↓
调用原函数
  ↓
处理返回值 / 异常
  ↓
返回结果或重新抛出异常
```

同时理解了 `@wraps`、`*args`、`**kwargs` 和 `raise` 在通用装饰器中的实际作用。

---

## 七、下一步

下一阶段将把装饰器知识继续应用到 `student_picker` 项目中，并逐步学习更加工程化的代码组织方式。

### Git 提交建议

学习仓库：

```text
Day 11: decorators advanced
```

项目仓库如果修改日志装饰器，则单独作为项目更新提交。