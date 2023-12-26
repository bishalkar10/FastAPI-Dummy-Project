import pytest
from fastapi.testclient import TestClient
from main import app
from person import Person
from employees import Employees
from custom_exceptions import DuplicateEmployeeIDError, EmptyEmployeeListError

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


# Test case to verify the root endpoint ("/") returns a successful response
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


# Test case to verify getting an existing employee by ID returns a successful response
def test_get_employee():
    reset_employees()
    response = client.get("/employees/3")
    assert response.status_code == 200
    assert response.json()["id"] == 3


# Test case to verify getting a nonexistent employee by ID returns a 404 response
def test_get_employee_invalid_id():
    response = client.get("/employees/10")
    assert response.status_code == 404


# Test case to verify getting all employees returns a successful response
def test_get_all_employees():
    reset_employees()
    response = client.get("/employees")
    assert response.status_code == 200
    assert len(response.json()) == 5


# Test case to verify adding a new employee returns a successful response
def test_add_employee():
    reset_employees()
    new_employee = {"id": 6, "name": "New Employee", "age": 30, "department": "IT"}
    response = client.post("/employees/add_employee", json=new_employee)
    assert response.status_code == 200
    assert response.json()["message"] == "Employee added successfully"


# Test case to verify adding a duplicate employee returns a 400 response
def test_add_duplicate_employee():
    reset_employees()
    duplicate_employee = {"id": 2, "name": "Jane Doe", "age": 25, "department": "IT"}
    response = client.post("/employees/add_employee", json=duplicate_employee)
    assert response.status_code == 400


# Test case to verify updating an existing employee returns a successful response
def test_update_employee():
    reset_employees()
    updated_employee = {
        "id": 3,
        "name": "Updated Mary",
        "age": 40,
        "department": "Finance",
    }
    response = client.put("/employees/update?id=3", json=updated_employee)
    assert response.status_code == 200
    assert response.json()["message"] == "Employee with ID 3 updated successfully"


# Test case to verify updating a nonexistent employee returns a 404 response
def test_update_nonexistent_employee():
    response = client.put(
        "/employees/update?id=10", json={"id": 10, "name": "New Employee"}
    )
    assert response.status_code == 404


# Test case to verify deleting an existing employee returns a successful response
def test_delete_employee():
    reset_employees()
    response = client.delete("/employees/delete?id=4")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee with ID 4 deleted successfully"


# Test case to verify deleting a nonexistent employee returns a 404 response
def test_delete_nonexistent_employee():
    response = client.delete("/employees/delete?id=10")
    assert response.status_code == 404


# Test case to verify deleting all employees returns a successful response
def test_delete_all_employees():
    reset_employees()
    response = client.delete("/employees/delete_all")
    assert response.status_code == 200
    assert response.json()["message"] == "All employees deleted successfully"


# Test case to verify deleting all employees from an empty list returns a 400 response
def test_delete_all_employees_empty():
    employees.employee_dict.clear()
    response = client.delete("/employees/delete_all")
    assert response.status_code == 200


# Test cases to validate the input validation for the Person class


# Test case to verify that the ID of a Person should be an integer
def test_person_id_should_be_integer():
    with pytest.raises(ValueError):
        Person(id="abc", name="Bishal", age=32, department="HR")


# Test case to verify that the ID of a Person should be greater than 0
def test_person_id_should_be_greater_than_0():
    with pytest.raises(ValueError):
        Person(id=0, name="Bishal", age=32, department="HR")


# Test case to verify that the name of a Person should not be empty
def test_person_name_should_not_be_empty():
    with pytest.raises(ValueError):
        Person(id=1, name="", age=32, department="HR")


# Test case to verify that the name of a Person should not be None
def test_person_name_should_not_be_none():
    with pytest.raises(ValueError):
        Person(id=1, name=None, age=32, department="HR")


# Test case to verify that the name of a Person should be at least 3 characters long
def test_person_should_be_at_least_3_character_long():
    with pytest.raises(ValueError):
        Person(id=1, name="a", age=32, department="HR")


# Test case to verify that the name of a Person should not be filled with spaces only
def test_person_name_should_not_be_filled_with_spaces():
    with pytest.raises(ValueError):
        Person(id=1, name="     ", age=32, department="HR")


# Test case to verify that the age of a Person should not be None
def test_age_should_not_be_none():
    with pytest.raises(ValueError):
        Person(id=1, name="None", age=None, department="HR")


# Test case to verify that the age of a Person should be an integer
def test_age_should_be_integer():
    with pytest.raises(ValueError):
        Person(id=1, name="Bishal", age="hk", department="HR")


# Test case to verify that the age of a Person should be greater than 0
def test_age_should_be_greater_than_0():
    with pytest.raises(ValueError):
        Person(id=1, name="Bishal", age=0, department="HR")


# Test case to verify that the department of a Person should not be empty
def test_department_should_not_be_empty():
    with pytest.raises(ValueError):
        Person(id=1, name="Bishal", age=20, department="")


# Test case to verify that the department of a Person should be at least 2 characters long
def test_department_should_be_at_least_2_character_long():
    with pytest.raises(ValueError):
        Person(id=1, name="Bishal", age=32, department="H")


# Test case to verify that the name of a Person should not be filled with spaces only
def test_department_should_not_be_filled_with_spaces():
    with pytest.raises(ValueError):
        Person(id=1, name="Bishal", age=32, department="   ")


# Test case to verify that an employee should be an instance of the Person class
def test_employee_should_be_instance_of_Person():
    employee = "Bishal"
    with pytest.raises(TypeError):
        employees.add_employee(employee)
