#!/usr/bin/python3
""" A Python script that exports data in the CSV format """
import csv
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

        username = employee.get("username")

        with open(f"{emp_id}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for todo in todos:
                todo_status = todo.get("completed")
                todo_title = todo.get("title")
                writer.writerow([emp_id, username, todo_status, todo_title])

    except urllib.error.URLError as err:
        print(f"An error occurred: {err}")
    except json.JSONDecodeError as err:
        print(f"Error decoding JSON: {err}")
