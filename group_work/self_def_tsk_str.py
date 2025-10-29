from datetime import datetime, date
class Task:
    def __init__ (self, tsk, tgs, due_d, pir = 'normal', cmpl=False):
        '''
        Initialize a Task (self-made data structure) object with the given attributes.
        if the tags are not provided, it will be an empty list.
        if the due date is not provided, it will be the current date.
        if the priority is not provided, it will be 'normal'.
        if the completion status is not provided, it will be False.
        Args:
            tsk (str): The task description.
            tgs (list): The tags associated with the task.
            due_d (date): The due date of the task.
            pir (str): The priority of the task.
            cmpl (bool): Whether the task is completed.(mark as completed or not)
        '''
        self.tsk = tsk 
        self.pir = pir if pir in ['low', 'normal', 'high'] else 'normal'
        self.cmpl = cmpl
        self.tgs = tgs if tgs else []
        self.due_d = due_d
        self.created_dt = datetime.now() #datetime object


    def __str__ (self):
        '''
        Return a string representation of the Task object.
        '''
        status = "✓" if Task.cmpl == True else "×"
        due_d = f" |due: {self.due_d}" if self.due_d else "" #if due_d is empty, it will not be displayed
        tgs = f" | tags: {', '.join(self.tgs)}" if self.tgs else "" #if tags is empty, it will not be displayed
        ov_d = f"overdue" if self.overdue() else "" #if the task is overdue, it will be displayed
        return f"{tgs}:[{status}] {self.tsk} ({self.pir}){due_d}"
        
    
    def overdue(self):
        '''
        Return True if the task is overdue, otherwise return False.
        '''
        if self.due_d is None:
            return False
        try:
            due_d = datetime.strptime(self.due_d, "%Y-%m-%d").date() #format YY-MM-DD
            return due_d < date.today()
        except ValueError:
            return False
