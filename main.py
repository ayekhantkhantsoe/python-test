from service import add_todo, update_todo, delete_todo
from storage import load_todos, save

todos = load_todos()

def handle_add_todo():
    todo_text = input("Enter a todo: ").strip()
    status = input("Enter status ('in progress' or 'done'): ").strip().lower()

    new_todo = add_todo(todos, todo_text, status)

    if not todo_text:
        print("Todo cannot be empty.")
        return

    if status not in ["in progress", "done"]:
        print("Invalid status. Please enter 'in progress' or 'done'.")
        return

    if save(todos):
        print("Todo created:", new_todo)

def handle_update_todo():
    todo_id = input("Enter the todo ID to update: ").strip()
    new_todo_text = input("Enter the updated todo: ").strip()
    new_status = input(
        "Enter status ('in progress' or 'done'): "
    ).strip().lower()


    for item in todos:
        if isinstance(item, dict) and str(item.get("id")) == todo_id:
            if not new_todo_text:
                print("Todo cannot be empty.")
                return

            if new_status not in ["in progress", "done"]:
                print("Invalid status. Please enter 'in progress' or 'done'.")
                return

            updated_todo = update_todo(
                todos,
                todo_id,
                new_todo_text,
                new_status,
            )

            if save(todos):
                print("Todo updated:", updated_todo)
            return

    print("Todo ID not found.")

def handle_delete_todo():
    todo_id = input("Enter the todo ID to delete: ").strip()

    deleted_todo = delete_todo(todos, todo_id)

    if not deleted_todo:
        return

    if save(todos):
        print("Todo deleted:", deleted_todo)

try:
    print("1. Add todo")
    print("2. Update todo")
    print("3. Delete todo")
    print("4. Show todo list")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        handle_add_todo()
    elif choice == "2":
        handle_update_todo()
    elif choice == "3":
        handle_delete_todo()
    elif choice == "4":
        print("Todo list:", todos)
    else:
        print("Invalid option.")
except (KeyboardInterrupt, EOFError):
    print("\nInput cancelled.")

