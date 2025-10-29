# todo_app.py
from datetime import datetime
import json

class Task:
    def __init__(self, description, priority="normal", completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed
        self.created_at = datetime.now()

    def __str__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.description} ({self.priority})"

def add_task(tasks, desc, priority="normal"):
    task = Task(desc, priority)
    tasks.append(task)
    print(f"✅ 添加任务: {desc}")

def mark_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index].completed = True
        print("✅ 已标记为完成")

def display_tasks(tasks):
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def save_to_file(tasks, filename="tasks.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([t.__dict__ for t in tasks], f, ensure_ascii=False, indent=2)

def load_from_file(filename="tasks.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Task(**item) for item in data]
    except FileNotFoundError:
        return []

# 主程序
if __name__ == "__main__":
    tasks = load_from_file()
    while True:
        print("\n--- 待办清单 ---")
        display_tasks(tasks)
        cmd = input("\n命令 (add/mark/delete/save/load/quit): ").strip().lower()
        if cmd == "quit":
            break
        elif cmd == "add":
            desc = input("任务描述: ")
            priority = input("优先级 (low/normal/high): ") or "normal"
            add_task(tasks, desc, priority)
        elif cmd == "mark":
            idx = int(input("要标记的序号: ")) - 1
            mark_complete(tasks, idx)
        elif cmd == "save":
            save_to_file(tasks)
            print("💾 已保存")
        elif cmd == "load":
            tasks = load_from_file()
            print("📂 已加载")