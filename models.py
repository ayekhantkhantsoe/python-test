import time

def create_todo(todo, status):
    new_todo = {
        "id": time.time_ns(),
        "todo": todo,
        "status": status,
    }

    return new_todo