from employees import Employees
from person import Person
import pytest
from custom_exceptions import DuplicateEmployeeIDError, EmptyEmployeeListError

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


# Test cases


# Test case to verify that adding an employee with a duplicate ID raises an error
def test_duplicate_employee_id():
    reset_employees()
    with pytest.raises(DuplicateEmployeeIDError):
        employees.add_employee(Person(id=1, name="John Doe", age=32, department="HR"))


# Test case to verify that getting an employee with a nonexistent ID raises a KeyError
def test_get_employee_nonexistent_id():
    reset_employees()
    with pytest.raises(KeyError):
        employees.get_employee(10)


# Test case to verify that getting all employees from an empty list raises an EmptyEmployeeListError
def test_get_all_employees_empty():
    employees.employee_dict.clear()
    with pytest.raises(EmptyEmployeeListError):
        employees.delete_all()
