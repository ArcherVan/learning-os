# Day 6 学生管理系统设计说明

## 1. 项目目标

本项目是一个基于 Python 面向对象思想实现的简单学生管理系统。

项目主要用于练习：

- Python 类与对象
- 面向对象的职责划分
- 多个类之间的协作
- 模块化设计
- 文件持久化
- 方法返回值与业务状态传递
- `@staticmethod`
- `main.py` 与业务逻辑分离

当前系统支持：

1. 添加学生
2. 查看所有学生
3. 修改学生成绩
4. 查询学生是否及格
5. 保存学生数据
6. 加载学生数据
7. 退出系统

---

## 2. 项目结构

```text
daily/DAY6/
├── student.py
├── studentManager.py
├── file.py
├── main.py
├── students.txt
└── DESIGN.md
```

各文件职责：

| 文件 | 职责 |
|---|---|
| `student.py` | 定义学生对象及学生自身的属性和行为 |
| `studentManager.py` | 管理多个学生对象，负责学生相关业务逻辑 |
| `file.py` | 负责学生数据的文件保存和加载 |
| `main.py` | 负责程序启动、菜单和用户交互 |
| `students.txt` | 保存学生数据 |
| `DESIGN.md` | 记录项目设计和模块职责 |

---

## 3. 核心对象设计

### 3.1 Student

`Student` 表示系统中的一个学生。

每个学生具有以下属性：

```text
class_name   班级
name         姓名
student_id   学号
score        成绩
gender       性别
```

`Student` 负责与“单个学生”直接相关的行为：

- 修改自己的成绩
- 显示自己的信息
- 根据成绩判断是否及格

例如：

```text
Student
├── 属性
│   ├── class_name
│   ├── name
│   ├── student_id
│   ├── score
│   └── gender
│
└── 方法
    ├── update_score()
    ├── show_info()
    └── is_pass()
```

---

## 4. StudentManager 设计

`StudentManager` 负责管理多个 `Student` 对象。

内部使用：

```python
self.students = []
```

保存所有学生。

因此：

```text
StudentManager
│
├── Student
├── Student
├── Student
└── ...
```

### 4.1 为什么 StudentManager 不继承 Student

`StudentManager` 不是一种特殊的学生。

两者之间的关系是：

```text
StudentManager 管理 Student
```

而不是：

```text
StudentManager 是 Student
```

因此不使用继承：

```python
class StudentManager(Student):
    ...
```

而是通过组合/管理关系保存多个 `Student` 对象。

---

## 5. StudentManager 的业务职责

### 5.1 添加学生

添加学生时需要检查学号是否已经存在。

因为本项目规定：

> 学号具有唯一性。

处理逻辑：

```text
添加 Student
    ↓
检查已有学生的 student_id
    ↓
是否重复？
 ├── 是 → 不添加 → 返回 None
 └── 否 → 添加 → 返回 True
```

`StudentManager` 只返回业务结果，不直接负责向用户打印提示。

---

### 5.2 修改成绩

根据学号查找学生，然后调用该学生的：

```text
update_score()
```

处理逻辑：

```text
输入学号和新成绩
        ↓
StudentManager 查找学生
        ↓
找到 → 修改成绩 → 返回 True
没找到 → 返回 None
```

---

### 5.3 查询是否及格

根据学号查找学生。

找到学生后，通过 `Student.is_pass()` 判断成绩。

返回值具有以下含义：

```text
True
→ 找到学生，并且及格

False
→ 找到学生，但不及格

None
→ 没有找到该学生
```

这里需要区分 `False` 和 `None`：

```text
False ≠ None
```

`False` 表示查询成功，但结果是否定的；`None` 表示没有得到查询对象。

---

## 6. 模块职责分离

项目遵循以下职责划分：

```text
Student
    ↓
描述一个学生

StudentManager
    ↓
管理多个学生以及学生相关业务

File
    ↓
负责数据持久化

main.py
    ↓
负责用户交互
```

核心原则：

> 业务模块负责处理业务并返回结果，用户界面模块负责把结果展示给用户。

例如：

```text
StudentManager
    ↓
return None
    ↓
main.py
    ↓
print("学号不存在.")
```

而不是让 `StudentManager` 自己：

```python
print("学号不存在.")
```

这样可以避免业务逻辑和用户界面耦合。

---

## 7. File 设计

`File` 专门负责学生数据的持久化。

主要功能：

```text
save_students()
load_students()
```

### 7.1 保存

保存时将一个个 `Student` 对象的属性转换为文本：

```text
班级,姓名,学号,成绩,性别
```

例如：

```text
11班,张三,45,80,男
10班,李四,18,90,男
```

---

### 7.2 加载

加载文件时：

```text
students.txt
    ↓
读取每一行
    ↓
split(",")
    ↓
得到各字段
    ↓
转换学号和成绩
    ↓
创建 Student 对象
    ↓
加入 students 列表
```

最终返回：

```text
[Student, Student, ...]
```

如果文件不存在，则返回：

```python
[]
```

而不是 `None`。

原因是 `StudentManager.students` 本身就是一个列表：

```python
self.students = []
```

因此无文件时表示“当前没有学生”，返回空列表可以保持数据类型一致。

---

## 8. 为什么 File 使用 staticmethod

`File` 的保存和加载操作不依赖某个 `File` 对象自身的状态。

保存方法需要的数据已经通过参数提供：

```text
filename
students
```

加载方法需要：

```text
filename
```

因此没有必要创建：

```python
file = File()
```

也不需要使用：

```python
self
```

所以使用：

```python
@staticmethod
```

比较合适。

---

## 9. main.py 设计

`main.py` 是程序入口和用户交互层。

主要负责：

- 创建 `StudentManager`
- 加载学生数据
- 显示菜单
- 获取用户输入
- 调用 `StudentManager`
- 根据返回结果向用户显示信息
- 退出前保存数据

整体流程：

```text
main()
  ↓
创建 StudentManager
  ↓
加载 students.txt
  ↓
进入 menu()
  ↓
用户选择操作
  ↓
调用 StudentManager
  ↓
根据返回值显示结果
  ↓
继续菜单循环
  ↓
退出
  ↓
保存数据
```

---

## 10. 数据流

### 添加学生

```text
用户输入
   ↓
main.py
   ↓
创建 Student
   ↓
StudentManager.add_student()
   ↓
检查学号
   ↓
students[]
```

### 修改成绩

```text
用户输入学号
   ↓
StudentManager
   ↓
找到 Student
   ↓
Student.update_score()
   ↓
修改 Student.score
```

### 查询成绩是否及格

```text
用户输入学号
   ↓
StudentManager
   ↓
找到 Student
   ↓
Student.is_pass()
   ↓
True / False
   ↓
main.py
   ↓
显示结果
```

### 保存数据

```text
StudentManager
   ↓
File.save_students()
   ↓
students.txt
```

### 加载数据

```text
students.txt
   ↓
File.load_students()
   ↓
创建 Student 对象
   ↓
StudentManager.students
```

---

## 11. 返回值设计

本项目使用返回值在不同模块之间传递业务状态。

### `add_student()`

```text
True
→ 添加成功

None
→ 学号重复，添加失败
```

### `update_student_score()`

```text
True
→ 修改成功

None
→ 学号不存在
```

### `check_student_pass()`

```text
True
→ 学生存在且及格

False
→ 学生存在但不及格

None
→ 学号不存在
```

### `load_students()`

```text
[Student, ...]
→ 成功加载学生

[]
→ 没有学生数据，例如文件不存在
```

设计原则：

> 返回值负责传递状态，`main.py` 负责决定如何向用户展示状态。

---

## 12. 当前测试情况

Day 6 已经实际运行并验证：

### 查看学生

能够从 `students.txt` 加载：

```text
11班,张三,45,80,男
10班,李四,18,90,男
```

并正确显示。

### 修改成绩

已验证：

```text
90 → 60
```

修改成功。

### 及格边界

已验证：

```text
60 → True
59 → False
```

说明：

```python
score >= 60
```

的判断符合当前系统要求。

### 学号不存在

查询不存在的学号时能够得到：

```text
学号不存在.
```

### 退出保存

退出系统时会自动保存学生数据。

---

## 13. 当前设计的边界

当前版本主要用于学习 Python 面向对象和模块化设计，因此暂时没有加入复杂的输入校验。

例如：

```python
student_id = int(input(...))
score = int(input(...))
```

如果用户输入非数字内容，程序会产生异常。

此外，目前还没有加入：

- 成绩范围校验
- 性别输入规范化
- 班级格式校验
- 更复杂的异常处理
- 数据库持久化
- 图形界面
- Web 接口

这些内容不属于当前 Day 6 的核心学习目标，后续根据学习进度再逐步引入。

---

## 14. Day 6 设计总结

本项目的核心设计可以概括为：

```text
Student
    ↓
一个学生

StudentManager
    ↓
管理多个学生 + 业务逻辑

File
    ↓
数据持久化

main.py
    ↓
用户交互
```

核心原则：

1. 一个类尽量承担清晰的职责。
2. `StudentManager` 管理 `Student`，而不是继承 `Student`。
3. 文件操作集中在 `File` 中。
4. `main.py` 负责用户交互。
5. 业务逻辑通过返回值向上层传递状态。
6. `print()` 尽量集中在用户交互层。
7. 对相同数据使用稳定的数据类型，例如学生集合始终使用列表。
8. 学号作为学生的唯一标识。
9. 使用 `@staticmethod` 表示不依赖实例状态的操作。

Day 6 的重点不是实现一个复杂的学生管理系统，而是通过一个完整的小项目理解：

> **如何把一个程序拆成多个职责清晰、相互协作的模块。**