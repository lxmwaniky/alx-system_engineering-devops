#!/usr/bin/python3
"""
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        userId = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, userId))
        employeeName = req.json().get("name")
        if employeeName is not None:
            treq = requests.get("{}todos?userId={}".format(url, userId)).json()
            totalTaskCount = len(treq)
            doneTasks = []
            for i in treq:
                if i.get("completed") is True:
                    doneTasks.append(i)
            doneTasksCount = len(doneTasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(employeeName, doneTasksCount, totalTaskCount))
            for title in doneTasks:
                print("\t {}".format(title.get("title")))
