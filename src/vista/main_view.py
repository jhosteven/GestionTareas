from logica import task_logic

def display_tasks():
    tasks = task_logic.list_tasks()
    if not tasks:
        print("No hay tareas.")
    else:
        for task in tasks:
            print(f"{task.id} - {task.name}: {task.description} (Vence: {task.due_date}, Estado: {task.status})")

def add_task():
    id = input("ID de la tarea: ")
    name = input("Nombre de la tarea: ")
    description = input("Descripción: ")
    due_date = input("Fecha de vencimiento (YYYY-MM-DD): ")
    task_logic.create_task(id, name, description, due_date)
    print("Tarea añadida.")

def update_task():
    id = input("ID de la tarea a actualizar: ")
    name = input("Nuevo nombre (dejar en blanco para no cambiar): ")
    description = input("Nueva descripción (dejar en blanco para no cambiar): ")
    due_date = input("Nueva fecha de vencimiento (dejar en blanco para no cambiar): ")
    status = input("Nuevo estado (dejar en blanco para no cambiar): ")
    task_logic.update_task(id, name, description, due_date, status)
    print("Tarea actualizada.")

def delete_task():
    id = input("ID de la tarea a eliminar: ")
    task_logic.delete_task(id)
    print("Tarea eliminada.")

def main_menu():
    while True:
        print("\nGestor de Tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Selecciona una opción: ")
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print("Opción inválida.")
