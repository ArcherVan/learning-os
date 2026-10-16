\# Day 21 学习记录



\## 一、学习主题



迭代器协议、生成器组合、`yield from`。



\## 二、今日完成内容



1\. 理解 `iter()`、`next()` 和 `StopIteration` 的关系。

2\. 使用 `yield` 实现惰性数据产出。

3\. 使用 `yield from` 委托另一个生成器。

4\. 编写学生筛选生成器，根据学号筛选学生。

5\. 编写姓名转换生成器，将 Student 对象转换为姓名字符串。

6\. 在 student\_picker 项目中运行测试，确认输出符合预期。



\## 三、核心代码与知识点



\- `student\_generator()`：逐个产生学生对象。

\- `high\_id\_student\_generator()`：筛选学号大于等于 250 的学生。

\- `student\_names\_from\_students()`：将学生对象转换为姓名。

\- `student\_name\_generator()`：使用 `yield from` 委托姓名生成器。



\## 四、问题与收获



最初混淆了 `yield from` 的产出值与表达式返回值。通过拆分筛选、转换和委托三个职责，理解了生成器组合的基本结构。



\## 五、完成情况



\- \[x] 迭代器协议理解

\- \[x] 生成器组合练习

\- \[x] 项目生成器实战

\- \[x] 项目测试通过

\- \[ ] Git 提交与推送

