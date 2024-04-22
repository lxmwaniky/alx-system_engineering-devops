#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        userId = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, userId))
        employeeName = req.json().get("name")
        if employeeName is not None:
            treq = requests.get(
                "{}todos?userId={}".format(
                    url, userId)).json()
            totalTasks = len(treq)
            completedTasks = []
            for t in treq:
                if t.get("completed") is True:
                    completedTasks.append(t)
            count = len(completedTasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(employeeName, count, totalTasks))
            for title in completedTasks:
                print("\t {}".format(title.get("title")))