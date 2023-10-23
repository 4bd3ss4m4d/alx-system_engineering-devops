#!/usr/bin/python3

'''
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
'''

import csv
import requests
import sys


if __name__ == "__main__":
    userid = sys.argv[1]
    url_link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url_link + "users/{}".format(userid)).json()
    user_name = user.get("username")
    todo_list = requests.get(url_link + "todos", params={
                "userId": userid}).json()

    with open("{}.csv".format(userid), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow([userid, user_name, t.get("completed"),
                             t.get("title")]) for t in todo_list]
