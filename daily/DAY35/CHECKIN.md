# Day35 学习记录：pathlib 文件路径管理

## 一、今日学习目标

掌握 Python 标准库 pathlib，能够使用面向对象的方式处理文件路径、遍历目录、筛选文件和创建项目目录。

## 二、今日学习内容

### 1. Path 路径对象

- 使用 `Path()` 创建路径对象。
- 使用 `exists()` 判断路径是否存在。
- 使用 `is_file()` 判断是否为文件。
- 使用 `is_dir()` 判断是否为目录。
- 使用 `name` 获取文件名。
- 使用 `suffix` 获取文件扩展名。
- 使用 `parent` 获取父目录。

### 2. 目录遍历与文件筛选

- 使用 `iterdir()` 遍历目录中的直接子项目。
- 使用 `is_file()` 排除目录。
- 使用 `suffix` 判断文件扩展名。
- 使用列表的 `append()` 收集符合条件的文件名。
- 理解 `glob()` 的基本用途。

完成了 `find_files(directory, suffix)` 函数的实现。

### 3. 自动创建项目目录

- 使用 `/` 运算符拼接路径。
- 使用 `mkdir()` 创建目录。
- 理解 `parents=True` 的作用。
- 理解 `exist_ok=True` 的作用。
- 使用循环批量创建项目目录。

完成了 `create_project_dirs(base_dir)` 函数。

## 三、实践任务完成情况

### 任务1：文件路径信息提取

完成 `inspect_path(path)`。

能够提取：
- 路径是否存在
- 是否为文件
- 是否为目录
- 文件名
- 文件扩展名
- 父目录

测试了存在性判断和路径属性提取。

### 任务2：指定类型文件筛选

完成 `find_files(directory, suffix)`。

实现逻辑：
1. 创建 Path 对象。
2. 使用 iterdir() 遍历目录。
3. 使用 is_file() 排除目录。
4. 使用 suffix 筛选文件。
5. 使用 append() 收集文件名。
6. 返回结果列表。

代码逻辑已完成，但未创建测试数据目录，因此尚未完成实际运行验证。

### 任务3：自动创建项目目录

完成 `create_project_dirs(base_dir)`。

成功创建：

```text
project/
├── config/
├── data/
├── logs/
└── output/
```

通过目录结构截图确认创建成功。

## 四、今日遇到的问题

### 1. 类、实例、方法和属性的区别

最初混淆了 Path 类和 Path 实例。

正确理解：

```python
path_obj = Path(path)

path_obj.exists()
path_obj.is_file()
path_obj.is_dir()

path_obj.name
path_obj.suffix
path_obj.parent
```

实例方法需要调用括号，属性不需要括号。

### 2. 相对路径与当前工作目录

使用：

```python
Path("data")
```

时，Python 会根据当前工作目录解析相对路径。

使用：

```python
Path.cwd()
```

可以获取当前工作目录。

使用：

```python
Path(__file__).parent
```

可以获取当前 Python 脚本所在目录。

需要区分当前工作目录与脚本所在目录。

## 五、今日掌握的核心知识

1. Path 对象能够解析不存在的路径，不要求文件真实存在。
2. 路径解析与文件系统存在性判断是两回事。
3. iterdir() 遍历目录时不会自动递归进入子目录。
4. 文件和目录即使具有相同的名称后缀，也需要通过 is_file() 区分。
5. pathlib 的 `/` 运算符可以进行路径拼接。
6. mkdir() 配合 parents=True 和 exist_ok=True 可以实现可重复执行的目录初始化。

## 六、今日总结

今天掌握了 pathlib 的基础使用，能够独立编写路径信息提取、文件筛选和目录初始化函数。

实际练习中经历了从错误调用 Path 类，到正确使用 Path 实例的过程，也解决了相对路径导致的 FileNotFoundError。

下一步需要加强：
- 基于脚本位置构造稳定的项目路径。
- 实际运行文件筛选函数。
- 将 pathlib 应用到真实 Python 项目中。

**Day35 状态：核心代码完成，任务2待补充实际测试。**