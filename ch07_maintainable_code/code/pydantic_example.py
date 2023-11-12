import pydantic
import json


class Person(pydantic.BaseModel):
    name: str
    age: int
    city: str


raw_api_data = '{"name":"Fred", "age":33, "city": "Panama"}'
api_data = json.loads(raw_api_data)
print(api_data)

person = Person(**api_data)
print(person)
# name='Fred' age=33 city='Panama'

raw_api_data = '{"name":"Sue", "age":"twenty", "city": "Leiden"}'
api_data = json.loads(raw_api_data)
another_person = Person(**api_data)
# 1 validation error for Person
# age
#   Input should be a valid integer, unable to parse string as an integer
