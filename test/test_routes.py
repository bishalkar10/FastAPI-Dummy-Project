from fastapi import HTTPException
import pytest
from fastapi.testclient import TestClient

import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app
from employees import Employees
from person import Person

client = TestClient(app)
employees = Employees()


# Helper function to reset the state of the Employees instance
def reset_employees():
    # Clear the employee dictionary and add some initial employees
    employees.employee_dict.clear()
    employees.add_employee(Person(id=1, name="John Doe", age=32, department="HR"))
    employees.add_employee(Person(id=2, name="Jane Doe", age=25, department="IT"))
    employees.add_employee(Person(id=3, name="Mary Doe", age=36, department="Finance"))
    employees.add_employee(
        Person(id=4, name="Jonny Lake", age=36, department="Finance")
    )
    employees.add_employee(Person(id=5, name="Bishal Kar", age=24, department="IT"))


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_employee():
    reset_employees()
    response = client.get("/employees/3")
    assert response.status_code == 200
    assert response.json() == {
        "id": 3,
        "name": "Mary Doe",
        "age": 36,
        "department": "Finance",
    }


def test_get_employee_invalid_id_key_error():
    employee_id = 999
    response = client.get(f"/employees/{employee_id}")
    print(response.status_code)


test_get_employee_invalid_id_key_error()
