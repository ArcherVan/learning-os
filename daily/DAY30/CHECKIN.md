# Day30 学习记录：Python 单元测试与异常断言

## 一、今日学习内容

1. 使用 `unittest.TestCase` 组织测试用例。
2. 使用 `assertTrue()` 和 `assertFalse()` 验证函数返回值。
3. 使用 `assertRaises(ValueError)` 验证函数是否抛出预期异常。
4. 学习正常输入、边界输入和非法输入的测试设计。
5. 根据测试失败信息定位函数实现中的问题。

## 二、练习项目

测试函数：`is_pass(score)`

业务规则：
- 分数小于 0 或大于 100 时，抛出 `ValueError`。
- 分数大于等于 60 且不超过 100 时，返回 `True`。
- 分数小于 60 且不低于 0 时，返回 `False`。

## 三、测试用例

| 输入 | 预期结果 | 验证方式 |
|---|---|---|
| -1 | 抛出 ValueError | assertRaises |
| 0 | False | assertFalse |
| 59 | False | assertFalse |
| 60 | True | assertTrue |
| 100 | True | assertTrue |
| 101 | 抛出 ValueError | assertRaises |

测试结果：六个断言全部通过。

## 四、问题与解决

问题：最初的 `is_pass()` 只判断分数是否达到 60 分，没有校验分数的合法范围。

解决：在及格判断之前检查分数是否小于 0 或大于 100，超出范围时主动抛出 `ValueError`。

另一个问题是误将 `assertTrue()` 和 `assertFalse()` 当作上下文管理器使用。修正后，直接将函数返回值传给断言方法。

## 五、今日总结

理解了测试通过与测试覆盖范围的区别，能够使用异常断言验证非法输入，并根据测试失败信息定位实现缺陷。

## 六、后续改进

将不同场景拆分为独立测试方法，使测试报告更清晰，便于定位失败用例。
