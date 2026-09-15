import json
from colorama import Fore

todos = []

def load_todos():
    global todos
    try:
        with open("todos.json", "r") as file:
            todos = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        todos = []

def save_todos():
    with open("todos.json", "w") as file:
        json.dump(todos, file)

def add_todo():
    task = input("Enter task: ")
    todos.append({"task": task, "done": False})
    print(Fore.GREEN + "Task added.")

def view_todos():
    if not todos:
        print(Fore.YELLOW + "No tasks yet.")
    else:
        for i, todo in enumerate(todos, start=1):
            status = "x" if todo["done"] else " "
            print(f"{i}. [{status}] {todo['task']}")

def complete_todo():
    view_todos()
    index = int(input("Enter the number of the task to mark done: ")) - 1
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        print(Fore.GREEN + "Task marked as done.")
    else:
        print(Fore.RED + "Invalid task number.")

def delete_todo():
    view_todos()
    index = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= index < len(todos):
        del todos[index]
        print(Fore.GREEN + "Task deleted.")
    else:
        print(Fore.RED + "Invalid task number.")


def run_menu():
    load_todos()
    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Back to main menu")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_todo()
            save_todos()
        elif choice == 2:
            view_todos()
        elif choice == 3:
            complete_todo()
            save_todos()
        elif choice == 4:
            delete_todo()
            save_todos()
        elif choice == 5:
            break
        else:
            print("Invalid option, try again.")
            
            

# Tester feature branch
