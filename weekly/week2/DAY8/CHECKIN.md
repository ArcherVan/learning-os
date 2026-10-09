# Day 8 学习打卡

## 一、今日学习主题

- Python 模块与包
- `import` / `from ... import ...`
- 学生管理系统模块拆分
- `StudentManager` 业务逻辑拆分
- `main.py` 用户交互与输入处理
- 异常处理
- 文件持久化
- `Student` 对象的保存与加载
- 文件脏数据处理
- 模块职责划分

---

## 二、今日完成内容

### 1. Python 模块与包

理解了 Python 中模块、包以及导入关系。

当前项目结构：

```text
student_system/
├── main.py
├── students.txt
├── student/
│   ├── __init__.py
│   └── student.py
└── manager/
    ├── __init__.py
    └── manager.py
```

理解了：

```python
from student.student import Student
from manager.manager import StudentManager
```

以及模块之间的依赖关系：

```text
main
 ↓
manager
 ↓
student
```

---

### 2. Student 类模块化

将之前学生管理系统中的 `Student` 类独立到：

```text
student/student.py
```

负责学生对象本身的数据。

---

### 3. StudentManager 模块化

将学生管理系统的核心数据管理逻辑放入：

```text
manager/manager.py
```

实现了：

- `find_student()`
- `add_student()`
- `show_students()`
- `update_student_score()`
- `delete_student()`
- `save_students()`
- `load_students()`

其中 `StudentManager` 使用：

```python
self.students
```

统一管理学生对象集合。

---

### 4. main.py 重构

`main.py` 主要负责：

- 显示菜单
- 接收用户输入
- 输入数据校验
- 调用 `StudentManager`
- 向用户显示操作结果

实现了：

```python
input_int()
input_score()
```

其中 `input_int()` 负责处理整数输入异常，`input_score()` 在此基础上进一步限制成绩范围。

---

## 三、异常处理

复用了 Day 7 学习的异常处理。

### 用户输入

处理：

```python
ValueError
```

例如输入：

```text
abc
```

程序不会崩溃，而是重新要求输入。

成绩同时限制：

```text
0 <= score <= 100
```

---

### 文件读取

`load_students()` 处理：

```python
FileNotFoundError
```

文件不存在时，将 Manager 的学生列表设置为空。

同时对文件中的每一行进行数据检查：

```text
空行
 ↓
跳过

字段数量 != 5
 ↓
数据格式错误
 ↓
跳过

数据类型无法转换
 ↓
ValueError
 ↓
数据类型错误
 ↓
跳过

数据正确
 ↓
创建 Student
```

---

## 四、文件持久化

实现了学生数据的保存和加载。

保存格式：

```text
class_name,name,student_id,score,gender
```

例如：

```text
11班,老弟,45,100,男
10班,小明,18,90,男
```

保存时：

```text
Student对象
    ↓
提取属性
    ↓
拼接成字符串
    ↓
写入 students.txt
```

加载时：

```text
students.txt
    ↓
逐行读取
    ↓
split(",")
    ↓
数据校验
    ↓
创建 Student 对象
    ↓
加入 students
    ↓
self.students
```

成功验证了：

```text
内存 → 文件 → 内存
```

的数据持久化过程。

---

## 五、今日遇到的问题

### 1. 模块运行方式问题

之前直接运行 `manager.py` 时出现过模块导入问题。

通过调整项目结构和运行方式，理解了当前项目应该从：

```text
student_system
```

作为运行环境，并通过：

```powershell
python -m main
```

运行主程序。

---

### 2. save/load 的职责问题

最开始考虑过是否应该让 `main.py` 负责保存和加载。

后来明确：

```text
main.py
→ 用户交互

StudentManager
→ 学生数据管理
→ 文件持久化
```

因此 `save_students()` 和 `load_students()` 放在 `StudentManager` 中。

---

### 3. 文件脏数据问题

在 `load_students()` 中考虑了：

- 空行
- 字段数量错误
- 整数类型错误

测试了错误数据：

```text
错误数据
10班,妞子,abc,80,男
```

程序能够跳过错误数据，同时继续加载正确数据。

---

## 六、今日重要理解

### 1. 模块化不是简单拆文件

真正的模块化需要考虑职责：

```text
Student
→ 描述学生

StudentManager
→ 管理学生数据和业务操作

main
→ 负责用户交互
```

---

### 2. Manager 管理自己的数据

因为：

```python
self.students
```

属于 `StudentManager`，所以：

```python
save_students()
load_students()
```

可以直接操作：

```python
self.students
```

而不需要额外传递学生列表。

---

### 3. 保存和加载必须遵循相同的数据格式

保存：

```text
class_name,name,student_id,score,gender
```

加载：

```text
parts[0] → class_name
parts[1] → name
parts[2] → student_id
parts[3] → score
parts[4] → gender
```

只有两边的数据协议一致，才能正确完成：

```text
Student → 文件 → Student
```

---

### 4. 错误数据不应该制造残缺对象

当文件中的某一行数据错误时，不创建一个不完整的 `Student` 对象，而是：

```python
continue
```

跳过当前错误数据，继续处理后面的数据。

---

## 七、今日掌握情况

### 已掌握

- [x] Python 模块导入
- [x] Python 包的基本结构
- [x] 模块之间的依赖关系
- [x] Student / Manager / main 职责划分
- [x] `input_int()` 输入异常处理
- [x] `input_score()` 数据范围校验
- [x] `FileNotFoundError`
- [x] `ValueError`
- [x] 文件逐行读取
- [x] 字符串拆分
- [x] Student 对象序列化为文本
- [x] 从文本重新创建 Student 对象
- [x] 基本文件持久化
- [x] 文件脏数据跳过

### 需要继续加强

- Python 包和模块的运行机制
- 更复杂的文件数据校验
- 更规范的异常设计
- 项目目录和路径管理
- 更大型项目中的模块职责划分

---

## 八、今日总结

Day 8 完成了学生管理系统从单文件程序向模块化程序的第一次重构。

当前程序已经具备：

```text
模块化
+
面向对象
+
异常处理
+
文件持久化
+
基本数据校验
```

相比之前单纯实现功能，现在开始理解程序不同部分应该承担什么职责。

本阶段的重点不是增加更多功能，而是建立：

```text
数据模型
    ↓
业务管理
    ↓
用户交互
    ↓
数据持久化
```

这种基本的软件结构意识。