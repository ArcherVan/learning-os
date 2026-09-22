# Day 6 学习打卡

## 1. 日期

2026-09-21

## 2. 今日主题

Python 面向对象基础进阶：完成一个模块化学生管理系统。

---

## 3. 今日完成内容

### Python 面向对象

完成并理解：

- `class` 类的定义
- `__init__()` 构造方法
- 实例属性
- 实例方法
- `self`
- `@staticmethod`
- 对象之间的协作
- 类与对象的职责划分

---

### 学生管理系统

完成以下模块：

```text
daily/DAY6/
├── student.py
├── studentManager.py
├── file.py
├── main.py
├── students.txt
├── DESIGN.md
└── CHECKIN.md
```

实现功能：

- 添加学生
- 查看所有学生
- 修改学生成绩
- 查询是否及格
- 保存学生数据
- 加载学生数据
- 退出系统

---

## 4. 今日核心理解

### 4.1 类的职责

`Student`：

> 表示一个学生，保存学生自己的数据，并提供与单个学生直接相关的行为。

`StudentManager`：

> 管理多个 `Student` 对象，并负责学生相关业务逻辑。

`File`：

> 负责学生数据的保存和加载。

`main.py`：

> 负责用户输入、菜单和结果显示。

整体结构：

```text
Student
    ↓
一个学生

StudentManager
    ↓
管理多个学生

File
    ↓
文件持久化

main.py
    ↓
用户交互
```

---

### 4.2 组合关系与继承关系

理解了：

```text
StudentManager 管理 Student
```

并不意味着：

```text
StudentManager 是 Student
```

因此 `StudentManager` 不应该继承 `Student`。

当前设计采用：

```text
StudentManager
    │
    ├── Student
    ├── Student
    └── Student
```

即管理/组合关系。

---

### 4.3 职责分离

理解了业务逻辑和用户交互应该分离。

例如：

```text
StudentManager
    ↓
负责查询
    ↓
返回 True / False / None
    ↓
main.py
    ↓
负责 print()
```

而不是让 `StudentManager` 直接向用户输出提示。

---

### 4.4 返回值表达业务状态

理解了不同返回值代表不同状态。

例如 `check_student_pass()`：

```text
True
→ 找到学生，并且及格

False
→ 找到学生，但不及格

None
→ 没找到学生
```

`add_student()`：

```text
True
→ 添加成功

None
→ 学号重复，添加失败
```

`update_student_score()`：

```text
True
→ 修改成功

None
→ 学号不存在
```

---

### 4.5 数据类型保持稳定

理解了 `load_students()` 在文件不存在时返回：

```python
[]
```

而不是：

```python
None
```

因为 `StudentManager.students` 本身就是列表：

```python
self.students = []
```

所以：

```text
文件存在
→ [Student, Student, ...]

文件不存在
→ []
```

两种情况下返回值的数据类型保持一致。

---

### 4.6 `@staticmethod`

理解了 `File` 的保存和加载操作不依赖某个 `File` 对象自己的实例状态。

因此可以使用：

```python
@staticmethod
```

而不需要：

```python
file = File()
```

也不需要 `self`。

---

## 5. 今日实际测试

### 查看学生

成功从文件加载并显示学生：

```text
班级号:11班,姓名:张三,学号:45,成绩:80,男
班级号:10班,姓名:李四,学号:18,成绩:90,男
```

---

### 修改成绩

验证：

```text
学号18
90 → 60
```

修改成功。

随后再次修改：

```text
60 → 59
```

修改成功。

---

### 及格判断

验证了两个边界：

```text
60 → True
59 → False
```

说明当前及格规则：

```python
score >= 60
```

运行结果符合预期。

---

### 不存在的学号

查询不存在的学号：

```text
学号不存在.
```

程序能够正确处理。

---

### 退出系统

退出时自动保存：

```text
系统退出.
```

程序正常退出。

---

## 6. 今日代码复盘

完成了 `StudentManager` 的职责优化。

### `add_student()`

现在会检查学号唯一性：

```text
学号已存在
→ 不添加
→ 返回 None

学号不存在
→ 添加
→ 返回 True
```

### `update_student_score()`

现在只负责查找和修改，不直接输出：

```text
找到
→ 修改
→ return True

没找到
→ return None
```

### `check_student_pass()`

现在只负责查询和判断：

```text
找到
→ return True / False

没找到
→ return None
```

由 `main.py` 决定最终显示什么。

---

## 7. 今日遇到并解决的问题

### 问题 1：`__init__` 拼写错误

最初构造方法写错，导致类无法正常初始化。

已理解：

```python
def __init__(self, ...):
```

是 Python 对象初始化方法。

---

### 问题 2：字符串使用 `%d`

班级名称类似：

```text
11班
```

属于字符串，不能使用 `%d`。

修改为：

```python
%s
```

---

### 问题 3：文件加载后的数据类型

文件读取出来的内容本身是字符串。

例如：

```text
45
80
```

读取后仍然是字符串，因此学号和成绩需要：

```python
int(parts[2])
int(parts[3])
```

转换成整数。

---

### 问题 4：`append()` 的使用

理解了：

```python
list.append(x)
```

一次添加一个元素。

因此不能使用：

```python
self.students.append(filename, self.students)
```

文件保存和加载应该交给 `File`。

---

### 问题 5：文件路径

理解了相对路径是相对于程序当前工作目录解析的。

因此项目中统一使用：

```text
daily/DAY6/students.txt
```

来访问数据文件。

---

## 8. 当前掌握程度

### 已掌握 / 能够独立使用

- Python 类和对象基础
- `__init__`
- 实例属性
- 实例方法
- `self`
- `@staticmethod`
- 创建对象
- 对象之间的协作
- `list` 管理多个对象
- 文件读写基础
- `with open()`
- `split()`
- 字符串与整数转换
- 模块导入
- `match/case`
- 菜单循环
- 基本模块职责划分
- 返回值表达业务状态

---

### 已接触但仍需继续强化

- 异常处理
- 输入合法性验证
- 更复杂的 OOP 设计
- 类之间的依赖关系
- 更规范的项目结构
- 更完整的测试
- 数据持久化的工程化处理

---

## 9. 今日项目成果

Day 6 已完成一个可以实际运行的 Python 学生管理系统。

目前程序已经形成：

```text
用户
 ↓
main.py
 ↓
StudentManager
 ↓
Student / File
 ↓
students.txt
```

并完成了实际运行测试。

---

## 10. Git 状态

Day 6 代码已经完成 Code Review。

下一步：

```bash
git status
git add .
git commit -m "Day 6: Python student management system"
git push
```

提交前需要确认没有错误文件、重复文件或不希望公开的数据。

---

## 11. Day 6 总结

今天最重要的收获不是完成了多少代码，而是开始理解：

> **一个程序应该如何按照职责拆分成多个模块，并让模块之间通过明确的接口和返回值协作。**

当前学生管理系统已经从“能运行的代码”进一步变成了一个具有基本结构和职责划分的 Python 小项目。

下一阶段需要继续通过项目练习强化：

```text
Python 基础
    ↓
面向对象
    ↓
模块化
    ↓
异常处理
    ↓
测试
    ↓
工程化项目
```