## TOOD APP
import time
from datetime import datetime
import shlex

"""
list of dictionaries
[{id: 1, title: "new tast"}, {id: 2, title: "second task"}]
O(n)

dictionary of dictionaries

{
 1: { title: "New task"},
 2, {title: "Second Task"}
}
0(1)
"""
todo_storage = {}


def create_task(title, description=None, deadline=None):
    task = {
        "title": title,
        "description": description,
        "deadline": deadline,
        "is_completed": False
    }

    index = 0
    if len(todo_storage) > 0:
        index = max(list(todo_storage.keys())) + 1

    todo_storage[index] = task

    return {index: task}


def list_all_todo():
    todo_list = []
    for index, task in todo_storage.items():
        todo_list.append(task)
    return todo_list


def get_task(index):
    if todo_storage.get(index, None):
        return todo_storage[index]
    return None


def update_task(index, is_completed: str):

    task = get_task(index)
    if not task:
        return None

    if is_completed == "True":
        is_completed = True
    elif is_completed == "False":
        is_completed = False
    else:
        raise ValueError("Not a valid input")

    task["is_completed"] = is_completed


def parse_arguments(arg_string):
    try:

        tokens = shlex.split(arg_string)
        arg_dict = {}

        for token in tokens:
            if "=" in token:
                key, value = token.split("=")
                arg_dict[key.strip()] = value.strip()
        return arg_dict
    except Exception:
        return {}


def delete_task(index):
    task = get_task(index)
    if not task:
        return None
    

    del todo_storage[index]


name = 'main'
if name == "main":
    while 1:
        user_command = input("$$$ ")

        parts = user_command.split(" ", 1)
        command = parts[0].upper()

        if command == "QUIT":
            exit()

        elif command == "ADD":
            args = parse_arguments(parts[1])
            new_task = create_task(title=args.get("title"), description=args.get("description"))

        elif command == "ALL":
            for key, val in todo_storage.items():
                print(f"{key}: {val}")

        elif command == "GET":
            args = parse_arguments(parts[1])
            index = args.get("id")
            task = get_task(index)
            print(task)
            if not task:
                print(f"index {index} does not exist")
            else:
                print(task)

        else:
            print(command,":Command not found")