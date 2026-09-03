import json
import time


def load_todos():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            saved_todos = json.load(file)

        if not isinstance(saved_todos, list):
            print("Error: data.json must contain a JSON list.")
            return []

        return saved_todos
    except FileNotFoundError:
        print("data.json was not found. Starting with an empty todo list.")
        return []
    except json.JSONDecodeError:
        print("Error: data.json contains invalid JSON.")
        return []
    except OSError as error:
        print("Could not read data.json:", error)
        return []


todos = load_todos()


def save_todos():
    try:
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(todos, file, indent=4)
        return True
    except OSError as error:
        print("Could not save data.json:", error)
        return False


def add_todo():
    todo = input("Enter a todo: ").strip()
    status = input("Enter status ('in progress' or 'done'): ").strip().lower()

    if not todo:
        print("Todo cannot be empty.")
        return

    if status not in ["in progress", "done"]:
        print("Invalid status. Please enter 'in progress' or 'done'.")
        return

    new_todo = {
        "id": time.time_ns(),
        "todo": todo,
        "status": status,
    }
    todos.append(new_todo)
    if save_todos():
        print("Todo created:", new_todo)

def update_todo():
    todo_id = input("Enter the todo ID to update: ")

    for item in todos:
        if isinstance(item, dict) and str(item.get("id")) == todo_id:
            new_todo = input("Enter the updated todo: ").strip()
            new_status = input("Enter status ('in progress' or 'done'): ").strip().lower()

            if not new_todo:
                print("Todo cannot be empty.")
                return

            if new_status not in ["in progress", "done"]:
                print("Invalid status. Please enter 'in progress' or 'done'.")
                return

            item["todo"] = new_todo
            item["status"] = new_status
            if save_todos():
                print("Todo updated:", item)
            return

    print("Todo ID not found.")

def delete_todo():
    todo_id = input("Enter the todo ID to delete: ")

    for item in todos:
        if isinstance(item, dict) and str(item.get("id")) == todo_id:
            todos.remove(item)
            if save_todos():
                print("Todo deleted:", item)
            return

    print("Todo ID not found.")
    

try:
    print("1. Add todo")
    print("2. Update todo")
    print("3. Delete todo")
    print("4. Show todo list")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_todo()
    elif choice == "2":
        update_todo()
    elif choice == "3":
        delete_todo()
    elif choice == "4":
        print("Todo list:", todos)
    else:
        print("Invalid option.")
except (KeyboardInterrupt, EOFError):
    print("\nInput cancelled.")

print("Todo list:", todos)
