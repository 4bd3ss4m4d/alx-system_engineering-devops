#!/usr/bin/python3

"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import json
import requests


def export_todo_list_to_json():
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{base_url}/users").json()

    todo_data = {}
    for user in users:
        user_id = user["id"]
        user_name = user["username"]
        todos = requests.get(f"{base_url}/todos", params={
                                "userId": user_id}).json()

        user_todos = [{"task": todo["title"], "completed": todo["completed"],
                       "username": user_name} for todo in todos]
        todo_data[user_id] = user_todos

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data, jsonfile, indent=4)


if __name__ == "__main__":
    export_todo_list_to_json()
