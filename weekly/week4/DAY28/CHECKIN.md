# Day28 学习记录：生成器异常处理与惰性数据管道

## 一、今日学习目标

- 理解生成器执行过程中异常的传播与捕获。
- 掌握 `try-except` 的作用范围。
- 理解 `continue` 在生成器中的作用。
- 使用生成器实现容错数据读取，跳过无效数据并继续处理后续记录。
- 理解 `for` 循环消费生成器与手动调用 `next()` 的区别。

## 二、任务完成情况

- [x] 任务1：分析生成器的执行顺序与完整输出。
- [x] 任务2：诊断异常捕获范围与异常传播。
- [x] 任务3：实现容错数据读取生成器。
- [x] 完成运行结果检查。
- [x] 创建 Git 提交并推送到远程仓库。

## 三、知识点总结

### 1. 生成器的执行过程

调用生成器函数时，不会立即执行函数体，而是返回一个生成器对象。

调用 `next()` 后，生成器开始执行，直到遇到 `yield` 并返回数据，然后暂停执行。下一次调用 `next()` 时，会从暂停的位置继续执行。

当生成器正常执行完毕后，再次调用 `next()` 会触发 `StopIteration`。

### 2. continue 在生成器中的作用

`continue` 会跳过当前循环剩余的代码，直接进入下一轮循环。

在数据读取场景中，可以使用 `continue` 跳过无效记录，避免一条错误数据影响后续数据的处理。

### 3. 异常捕获范围

`try-except` 只能捕获执行过程中进入对应 `try` 代码块并与 `except` 类型匹配的异常。

例如：

```python
try:
    value = int(record)
except ValueError:
    print(f"跳过无效数据：{record}")
    continue
```

这里的 `ValueError` 来自 `int(record)` 的转换失败。捕获异常后，程序执行 `continue`，继续处理下一条记录。

如果 `try-except` 没有包住 `int(record)`，那么转换产生的 `ValueError` 不会被这个 `except` 捕获，而会向调用方传播；如果没有其他代码捕获它，生成器就会因异常而终止。

### 4. ValueError 与 StopIteration 的区别

- `ValueError`：表示操作接收了不合适的值，例如 `int("abc")`。
- `StopIteration`：表示迭代器已经没有更多数据，生成器正常耗尽时会触发。

调用方的 `except StopIteration` 不能捕获 `ValueError`，因为两者是不同的异常类型。

使用 `for` 循环消费生成器时，Python 会自动处理迭代结束，不需要手动捕获 `StopIteration`。

### 5. 惰性数据处理

生成器逐条处理数据，不需要提前构造包含全部结果的新列表。

对于可能包含无效记录的数据源，可以将转换、异常处理和 `yield` 组合起来，形成容错的数据读取过程。

## 四、今日实践代码

文件：`daily/DAY28/practice.py`

```python
def read_valid_numbers(records):
    for record in records:
        try:
            value = int(record)
        except ValueError:
            print(f"跳过无效数据：{record}")
            continue

        yield value

    print("读取结束")


records = ["12", "abc", "25", "", "38", "error", "50"]
reader = read_valid_numbers(records)

for number in reader:
    print(number)
```

### 运行结果

```text
12
跳过无效数据：abc
25
跳过无效数据：
38
跳过无效数据：error
50
读取结束
```

### 代码设计说明

1. 使用 `for` 循环逐条读取记录。
2. 使用 `int()` 尝试转换数据。
3. 使用 `except ValueError` 捕获转换失败。
4. 使用 `continue` 跳过无效记录。
5. 使用 `yield value` 返回有效整数。
6. 在循环结束后打印一次结束提示。
7. 使用 `for` 循环消费生成器，自动处理迭代结束。

## 五、今日诊断与复盘

### 已掌握的内容

- 能够分析生成器在 `yield` 处暂停和恢复执行的过程。
- 能够解释 `continue` 如何跳过无效数据。
- 能够区分 `ValueError` 与 `StopIteration`。
- 能够判断异常是否处于对应的 `try-except` 捕获范围内。
- 能够独立编写容错数据读取生成器，并正确处理多条无效记录。
- 能够使用 `for` 循环完整消费生成器。

### 需要继续巩固的内容

- 分析多次调用 `next()` 时生成器的具体执行位置。
- 精确区分生成器正常结束与异常终止时的行为。
- 进一步练习多个生成器串联形成数据管道的执行过程。

### 今日总结

今天完成了生成器异常处理与容错数据读取练习。实践中通过 `try-except` 捕获数据转换错误，并使用 `continue` 跳过无效记录，使后续有效数据能够继续处理。

同时，进一步理解了异常类型与捕获范围的关系，以及使用 `for` 循环消费生成器的优势。

下一步可以继续学习更复杂的生成器数据管道与异常处理设计，并在实践中加强对执行顺序和异常传播的分析能力。
