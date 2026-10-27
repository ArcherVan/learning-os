from dataclasses import dataclass, field

@dataclass
class Task:
    task_id: int
    title: str
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.task_id < 1:
            raise ValueError("任务编号必须大于0")
        if not self.title.strip():
            raise ValueError("任务标题不能为空")

task1 = Task(1, "学习 Python")
task2 = Task(2, "学习 Git")

task1.tags.append("基础语法")

print(task1.tags)
print(task2.tags)
print(task1.tags is task2.tags)
