#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress for a given employee ID
using a REST API.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """Fetch and display the TODO list progress for a given employee ID"""
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch the employee's details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee = employee_response.json()

    # Fetch the employee's TODO list
    todos_url = f"{base_url}/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter the TODO list by the employee ID
    employee_todos = [todo for todo in todos if todo.get("userId") == employee_id]

    # Calculate the number of completed tasks
    completed_tasks = [todo for todo in employee_todos if todo.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(employee_todos)

    # Display the TODO list progress
    print(f"Employee {employee.get('name')} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
]
