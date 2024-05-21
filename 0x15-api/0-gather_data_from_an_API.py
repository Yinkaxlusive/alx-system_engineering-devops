#!/usr/bin/python3
""" Python script which uses a REST API, for a given employee ID,
returns information about their TODO list progress. """

import json
import sys
import urllib
import urllib.request

# The base API url for getting the employee object
USER_API_URL = "https://jsonplaceholder.typicode.com/users/"

# The base API url for getting all todo objects for an employee
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos?userId="

# Employee ID passed as an argument to the script
emp_id: str = sys.argv[1] if len(sys.argv) > 1 else ""

# Get all the todos for a given employee ID
if emp_id.isdigit():
    try:
        user_url = f"{USER_API_URL}{emp_id}"
        todos_url = f"{TODO_API_URL}{emp_id}"

        emp_response = urllib.request.urlopen(user_url)
        todos_response = urllib.request.urlopen(todos_url)

        emp_data = emp_response.read()
        todos_data = todos_response.read()

        employee = json.loads(emp_data)
        todos = json.loads(todos_data)

        name = employee.get("name")
        done = len([todo for todo in todos if todo.get("completed")])
        total = len(todos)

        print(f"Employee {name} is done with tasks({done}/{total}):")
        for todo in todos:
            if todo.get("completed"):
                print(f"\t {todo.get('title')}")

    except urllib.error.URLError as err:
        print(f"An error occurred: {err}")
    except json.JSONDecodeError as err:
        print(f"Error decoding JSON: {err}")
