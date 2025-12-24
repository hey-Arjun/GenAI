from pydantic import BaseModel,  Field
from typing import Optional

# it can do implicit  typee conversion
class Student(BaseModel):

    name : str
    age : Optional[int] = None
    cgpa : float = Field(gt = 0, lt = 10, default = 5, description = 'A decimal value representing the cgpa of the student')

new_student = {'name' : 'Arjun', 'age' : '32', 'cgpa': 5.6}
student = Student(**new_student)
student_dict = dict(student)

print(student_dict)
student_json = student.model_dump_json()
print(student_json)
