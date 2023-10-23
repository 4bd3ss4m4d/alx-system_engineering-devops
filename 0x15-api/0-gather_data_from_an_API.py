#!/usr/bin/python3

'''
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
'''
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_name = requests.get(url + "users/{}".format(sys.argv[1])).json()
    alltds = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    cptd_tds = [t.get("title") for t in alltds if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_name.get("name"), len(cptd_tds), len(alltds)))

    [print("\t {}".format(c)) for c in cptd_tds]
