import json

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

def save(todos):
    try:
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(todos, file, indent=4)
        return True
    except OSError as error:
        print("Could not save data.json:", error)
        return False
