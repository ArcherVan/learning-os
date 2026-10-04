Day 12：装饰器进阶与项目应用

1. 今日学习内容
- *args / **kwargs
- functools.wraps
- 装饰器的执行过程
- 日志装饰器
- __str__
- 将装饰器应用到 student_picker

2. 今日理解
- @log 本质上是函数重新赋值
- wrapper 接收原函数参数
- result 保存原函数返回值
- return result 保持原函数返回结果
- @wraps(func) 保留原函数信息
- logger 不应该依赖 Student 等具体业务类

3. 项目实践
- 创建 utils/logger.py
- 给 Picker.pick() 添加 @log
- 给 Student 添加 __str__
- 验证多次抽取功能正常

4. 测试结果
- 多次抽取正常
- 学生不会重复抽取
- 日志正常输出
- Student 学号和姓名正常显示

5. 今日总结
今天理解了装饰器从练习代码到实际项目中的应用，
并进一步理解了模块职责分离。