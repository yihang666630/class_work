import json
from datetime import datetime, date
from typing import List, Optional

class Task:
    def __init__(
        self,
        description: str,
        priority: str = "normal",          # low / normal / high
        completed: bool = False,
        due_date: Optional[str] = None,    # 格式: "YYYY-MM-DD"
        tags: List[str] = None             # 如 ["work", "urgent"]
    ):
        self.description = description
        self.priority = priority
        self.completed = completed
        self.due_date = due_date  # 保持为字符串便于 JSON 序列化
        self.tags = tags if tags else []

    def is_overdue(self) -> bool:
        if not self.due_date or self.completed:
            return False
        try:
            due = datetime.strptime(self.due_date, "%Y-%m-%d").date()
            return due < date.today()
        except ValueError:
            return False

    def __str__(self):
        status = "✓" if self.completed else "○"
        prio_icon = {"high": "❗", "normal": "➖", "low": "🔽"}.get(self.priority, "➖")
        
        # 截止日期显示
        due_str = f" | 截止: {self.due_date}" if self.due_date else ""
        
        # 标签显示
        tags_str = f" | 标签: {', '.join(self.tags)}" if self.tags else ""
        
        # 过期高亮（可选）
        prefix = "[过期]" if self.is_overdue() else ""
        
        return f"{prefix}[{status}] {self.description} ({prio_icon}){due_str}{tags_str}"

    def to_dict(self):
        return {
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "due_date": self.due_date,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            description=data["description"],
            priority=data.get("priority", "normal"),
            completed=data.get("completed", False),
            due_date=data.get("due_date"),
            tags=data.get("tags", [])
        )


# ========================
# 核心函数
# ========================

def add_task(
    tasks: List[Task],
    description: str,
    priority: str = "normal",
    due_date: Optional[str] = None,
    tags: List[str] = None
):
    task = Task(description, priority, due_date=due_date, tags=tags)
    tasks.append(task)
    print(f"✅ 已添加任务: {description}")


def mark_complete(tasks: List[Task], index: int):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        print("✅ 任务已标记为完成")
    else:
        print("❌ 无效序号")


def display_tasks(tasks: List[Task]):
    if not tasks:
        print("📝 暂无任务")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def save_to_file(tasks: List[Task], filename: str = "tasks.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=2)
    print(f"💾 已保存到 {filename}")


def load_from_file(filename: str = "tasks.json") -> List[Task]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    except FileNotFoundError:
        print("📂 未找到保存文件，将从空列表开始")
        return []
    except json.JSONDecodeError:
        print("⚠️  文件损坏，无法加载")
        return []


# ========================
# 主程序
# ========================

def main():
    tasks = load_from_file()

    while True:
        print("\n" + "="*50)
        print("📝 增强版待办清单 (支持截止日期 & 标签)")
        print("="*50)
        display_tasks(tasks)
        print("\n可用命令: add, complete, save, load, quit")
        cmd = input(">>> ").strip().lower()

        if cmd == "quit":
            save_to_file(tasks)  # 退出时自动保存
            print("👋 再见！")
            break

        elif cmd == "add":
            desc = input("任务描述: ").strip()
            if not desc:
                print("❌ 描述不能为空")
                continue

            prio = input("优先级 (low/normal/high) [默认 normal]: ").strip() or "normal"
            if prio not in ["low", "normal", "high"]:
                prio = "normal"

            due = input("截止日期 (YYYY-MM-DD, 可选): ").strip()
            if due:
                try:
                    datetime.strptime(due, "%Y-%m-%d")  # 验证格式
                except ValueError:
                    print("⚠️  日期格式错误，将不设置截止日期")
                    due = None

            tags_input = input("标签 (用逗号分隔, 如 work,urgent): ").strip()
            tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

            add_task(tasks, desc, prio, due, tags)

        elif cmd == "complete":
            if not tasks:
                print("❌ 没有任务可完成")
                continue
            try:
                idx = int(input("请输入要完成的任务序号: ")) - 1
                mark_complete(tasks, idx)
            except ValueError:
                print("❌ 请输入有效数字")

        elif cmd == "save":
            save_to_file(tasks)

        elif cmd == "load":
            tasks = load_from_file()

        else:
            print("❓ 未知命令，请重试")


if __name__ == "__main__":
    main()