class Task:
    def __init__(self, id, name, description, due_date, status="Pendiente"):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"Task({self.id}, '{self.name}', '{self.description}', '{self.due_date}', '{self.status}')"
