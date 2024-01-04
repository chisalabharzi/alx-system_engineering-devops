#!/usr/bin/python3
"""extendes script that exports data in json format"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            y.get("id"): [{
                "task": x.get("title"),
                "completed": x.get("completed"),
                "username": y.get("username")
            } for x in requests.get(url + "todos",
                                    params={"userId": y.get("id")}).json()]
            for y in users}, jsonfile)
