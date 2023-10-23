#!/usr/bin/python3

"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

import json
import requests
import sys

if __name__ == "__main__":
    usrid = sys.argv[1]
    link_url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(link_url + "users/{}".format(usrid)).json()
    username = user_data.get("username")
    tds_lst = requests.get(link_url + "todos", params={"userId": usrid}).json()
    with open("{}.json".format(usrid), "w") as infile:
        json.dump(
            {
                usrid: [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": username,
                    }
                    for t in tds_lst
                ]
            },
            infile,
        )
