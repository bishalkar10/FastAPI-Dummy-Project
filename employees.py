from collections import OrderedDict
from person import Person
from custom_exceptions import DuplicateEmployeeIDError, EmptyEmployeeListError


# * Employee Class to store employees in an Ordered dictionary and methods to perform CRUD operations
class Employees:
    def __init__(self):
        self.employee_dict: OrderedDict = OrderedDict()

    def add_employee(self, employee: Person):
        # Check if the employee is an instance of the Person class
        if not isinstance(employee, Person):
            raise TypeError("Employee must be of type Person")
        # Check if the employee ID already exists in the dictionary
        if employee.id in self.employee_dict:
            raise DuplicateEmployeeIDError(
                f"Employee with ID {employee.id} already exists"
            )
        # Add the employee to the dictionary
        self.employee_dict[employee.id] = employee

    def get_employee(self, id: int) -> Person | None:
        if not isinstance(id, int):
            raise TypeError(f"ID must be an integer")
        # Check if the employee ID exists in the dictionary
        if id not in self.employee_dict:
            raise KeyError(f"Employee with ID {id} does not exist")
        # Return the employee object
        return self.employee_dict.get(id)

    # Method to get all employees
    def get_all_employees(self) -> list[Person]:
        # Return a list of all employee objects
        return list(self.employee_dict.values())

    # Method to update an employee
    def update_employee(self, id: int, employee: Person):
        if not isinstance(employee, Person):
            raise TypeError("Employee must be of type Person")
        if not isinstance(id, int):
            raise TypeError(f"ID must be an integer")
        # Check if the employee ID exists in the dictionary
        if id not in self.employee_dict:
            raise KeyError(f"Employee with ID {id} does not exist")
        # Update the employee in the dictionary
        self.employee_dict[employee.id] = employee

    # Method to delete an employee
    def delete_employee(self, id: int):
        if not isinstance(id, int):
            raise TypeError(f"ID must be an integer")
        # Check if the employee ID exists in the dictionary
        if id not in self.employee_dict:
            raise KeyError(f"Employee with ID {id} does not exist")
        # Remove the employee from the dictionary and return it
        return self.employee_dict.pop(id)

    # Method to delete all employees
    def delete_all(self):
        # Check if the employee dictionary is empty
        if len(self.employee_dict) == 0:
            raise EmptyEmployeeListError("Employee list is empty")
        # Clear the employee dictionary
        self.employee_dict.clear()
