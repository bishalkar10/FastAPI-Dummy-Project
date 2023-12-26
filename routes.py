from custom_exceptions import DuplicateEmployeeIDError, EmptyEmployeeListError
from employees import Employees
from fastapi import HTTPException, APIRouter
from person import Person

# create an API router instance
router = APIRouter()
# Create an instance of the Employees class
employees = Employees()

# Add some sample employees dummy data
employees.add_employee(Person(id=1, name="John Doe", age=32, department="HR"))
employees.add_employee(Person(id=2, name="Jane Doe", age=25, department="IT"))
employees.add_employee(Person(id=3, name="Mary Doe", age=36, department="Finance"))
employees.add_employee(Person(id=4, name="Jonny Lake", age=36, department="Finance"))
employees.add_employee(Person(id=5, name="Bishal Kar", age=24, department="IT"))


# Root endpoint
@router.get("/")
async def read_root():
    try:
        return {"Hello": "World"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# * Endpoint - GET request - get the employee by id
@router.get("/employees/{id}")
async def get_employee(id: int):
    try:
        return employees.get_employee(id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# * Endpoint - GET request - get all employees
@router.get("/employees")
async def get_all_employees():
    try:
        return employees.get_all_employees()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# * Endpoint - POST request - add an employee
@router.post("/employees/add_employee")
async def add_employee(employee: Person):
    try:
        employees.add_employee(employee)
        return {"message": "Employee added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DuplicateEmployeeIDError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# * Endpoint - PUT request - update an employee
@router.put("/employees/update")
async def update_employee(id: int, employee: Person):
    try:
        employees.update_employee(id, employee)
        return {"message": f"Employee with ID {id} updated successfully"}
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# * Endpoint - DELETE request - delete an employee by id
@router.delete("/employees/delete")
async def delete_employee(id: int):
    try:
        employees.delete_employee(id)
        return {"message": f"Employee with ID {id} deleted successfully"}
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except TypeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


# * Endpoint - DELETE request - delete all employees
@router.delete("/employees/delete_all")
async def delete_all_employees():
    try:
        employees.delete_all()
        return {"message": "All employees deleted successfully"}
    except EmptyEmployeeListError as e:
        raise HTTPException(status_code=200, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
