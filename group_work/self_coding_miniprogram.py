# create a simple "to-do" list miniprogram
"""
the "to-do list" main function:
1. add tasks (str)
2. mark_completed, then delete it
3. display all tasks 
(tags, overdue (if any) description, priority, due date, completion status)
4. export/import tasks to/from a file (json format)
5. adjust priority, due date, tags, then update the task
"""
#note that the entire main data structure is list and in the list we need to store
#dictionary-like data, but here we choose to create a self-defined data structure
#to make whole program more organized, easier and flexible to manage

#for time-related functions: need outside packages
from datetime import datetime, date

# self_defined data structure for task
class Task:
    
    def _init_(self, tsk, tgs, pri, due_d, cmpl):
        '''
        Initialize a Task (self-made data structure) object with the given attributes.
        Args:
            tsk (str): The task description.
            tgs (list): The tags associated with the task.
            pri (str): The priority of the task.
            due_d (date): The due date of the task.
            cmpl (bool): Whether the task is completed.
        '''
        self.tsk = tsk
        self.tgs = tgs if tgs else []
        self.pri = pri if pri in ['high', 'normal', 'low'] else 'normal'
        self.due_d = due_d
        self.cmpl = cmpl
        self.created_at = datetime.now()

    def _str_(self):
        '''
        return a string of all Task object
        '''
        stat = 'Y'if self.cmpl else 'N'
        due_d = f"due:{self.due_d}" if self.due_d else "" # consider the empty issue
        tgs = f"tags:{', '.join(self.tgs)}" if self.tgs else ""
        ov_d = self.is_overdue()
        return f"{ov_d}|[{stat}] {self.tsk} ({self.pri}) | {due_d} | {tgs}"
    
    def is_overdue(self):
        '''
        return True if the task is overdue, otherwise return False.
        the overdue is actually user-self setup, and the format is "YYYY-MM-DD" 
        '''
        if self.due_d is None:
            return False
        try:
            due_d = datetime.strptime(self.due_d, "%Y-%m-%d").date() #format YY-MM-DD
            return 'overdue' if due_d < date.today() else None #return the status
        except ValueError:
            return False

    def to_dict(self):
        '''
        Because we need to import/export the task object to/from json file,
        which only accept str, int, list, dict format
        we need to convert the Task object to dictionary format.
        (within the entrie list, the dict is needed)
        '''
        return {
            "task": self.tsk,
            "tags": self.tgs,
            "priority": self.pri,
            "due_date": self.due_d,
            "completed": self.cmpl,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S") 
            # convert datetime to string，time is recorded to seconds level, like 
            # "2025-10-25 14:30:12"
        }
    
    @classmethod
    def from_dict(cls, data):
        '''
        Convert dictionary format back to Task object.
        Because when we import from json file, the data is in dict format.
        Args:
            data (dict): The dictionary containing task attributes.
        Returns:
            Task: The Task object created from the dictionary.
        '''
        created_at = datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
        task = cls(
            tsk=data["task"],
            tgs=data.get("tags", []),
            pri=data.get("priority", "normal"),
            due_d=data.get("due_date"),
            cmpl=data.get("completed", False)
        )
        task.created_at = created_at
        return task
