todos = []
def add_todo():
todo = input("Enter a todo: ")
todos.append(todo)
add_todo(todo)
print("todo list:", todos)