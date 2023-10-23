#!/usr/bin/python3

"""
This Python script fetches data from a REST API for a given employee ID and
exports their task information in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user_data.get("username")
    tasks_list = requests.get(base_url + "todos", params={
                                        "userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(
            {
                user_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username,
                    }
                    for task in tasks_list
                ]
            },
            json_file,
        )
