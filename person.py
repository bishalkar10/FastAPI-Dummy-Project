from pydantic import BaseModel, Field, field_validator


# * Data Model
class Person(BaseModel):
    id: int = Field(..., gt=0, description="The ID of the person")
    name: str = Field(..., min_length=3, description="The name of the person")
    age: int = Field(None, gt=0, description="The age of the person")
    department: str = Field(
        None, min_length=2, description="The department of the person"
    )

    # * if name is made of empty spaces, raise an error
    @field_validator("name")
    def validate_name(cls, name):
        if name.strip() == "":
            raise ValueError("Name shouldn't be filled with spaces")
        return name

    # * if department is made of empty spaces, raise an error
    @field_validator("department")
    def validate_department(cls, department):
        if department.strip() == "":
            raise ValueError("Department name shouldn't be filled with spaces")
        return department
