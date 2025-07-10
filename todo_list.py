class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def list_tasks(self):
        return self.tasks

    def mark_completed(self, task):
        for t in self.tasks:
            if t['task'] == task:
                t['completed'] = True

    def clear_tasks(self):
        self.tasks = []
