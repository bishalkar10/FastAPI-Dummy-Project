# FastAPI Dummy Project

## Description

This is a dummy project created to learn and experiment with FastAPI. The project includes routes for managing employee data using an ordered dictionary.

## Installation

1. Clone the repository: `git clone https://github.com/bishalkar10/fastapi-dummy-project.git`
2. Navigate to the project directory: `cd fastapi-dummy-project`
3. Create a virtual environment: `python -m venv fastAPI-venv`
4. Activate the virtual environment:
   - For Windows: `fastAPI-venv\Scripts\activate`
   - For macOS/Linux: `source fastAPI-venv/bin/activate`
5. Install the dependencies: `pip install -r requirements.txt`

## Usage

1. Start the FastAPI server:

```
uvicorn main:app --reload
```

2. Open your web browser and go to `http://localhost:8000`
3. To access the API documentation provided by Swagger UI go to [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc)
4. Use the available routes to interact with the employee data:
   - GET `/`: Retrieve the API's root path.
   - GET `/employees`: Retrieve a list of all employees.
   - GET `/employees/{id}`: Retrieve information about a specific employee by ID.
   - POST `/employees/add_employee`: Add a new employee to the database.
   - PUT `/employees/update`: Update the information of an existing employee.
   - DELETE `/employees/delete`: Delete a specific employee by ID.
   - DELETE `/employees/delete_all`: Delete all employees from the database.
