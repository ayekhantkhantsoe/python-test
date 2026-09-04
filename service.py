from models import create_todo


def find_todo_by_id(todos, todo_id):
    for item in todos:
        if isinstance(item, dict) and str(item.get("id")) == todo_id:
            return item

    return None

def add_todo(todos,todo_text,status):
    if not todo_text:
        return None
    
    if status not in ["in progress", "done"]:
        print("Invalid status. Please enter 'in progress' or 'done'.")
        return None

    new_todo = create_todo(todo_text, status)
    todos.append(new_todo)
    
    return new_todo

def update_todo(todos,todo_id,new_todo_text,new_status):
    item = find_todo_by_id(todos, todo_id)

    if item is None:
        return None

    if not new_todo_text:
        print("Todo cannot be empty.")
        return None

    if new_status not in ["in progress", "done"]:
        print("Invalid status. Please enter 'in progress' or 'done'.")
        return None

    item["todo"] = new_todo_text
    item["status"] = new_status
    return item

def delete_todo(todos,todo_id):
    for item in todos:
        if isinstance(item, dict) and str(item.get("id")) == todo_id:
            todos.remove(item)
            return item
    print("Todo ID not found.")
