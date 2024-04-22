#!/usr/bin/python3
'''
Export data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(url, verify=False).json()
    unDoc = {}
    uDoc = {}
    for user in req:
        uid = user.get("id")
        uDoc[uid] = []
        unDoc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [uDoc.get(i.get("userId")).append({"task": i.get("title"),
                                       "completed": i.get("completed"),
                                       "username": unDoc.get(
                                               i.get("userId"))})
     for i in todo]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(uDoc, jsf)