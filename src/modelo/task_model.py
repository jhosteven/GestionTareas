from modelo.task_model import Task

tasks = []

def create_task(id, name, description, due_date):
    task = Task(id, name, description, due_date)
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def update_task(id, name=None, description=None, due_date=None, status=None):
    for task in tasks:
        if task.id == id:
            if name:
                task.name = name
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if status:
                task.status = status
            return task
    return None

def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task.id != id]
    return tasks
