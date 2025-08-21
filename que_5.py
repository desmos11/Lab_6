#Define a class Person with attributes name and age. Derive a class Employee
#from Person with additional attributes employee_id and salary. Implement a
#method display_employee() in Employee that prints all the details. Create an
#instance of Employee and display the information.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class employee(person):
    def __init__(self, name, age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.salary=salary
    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Age:{self.age}")
        print(f"Employee id: {self.employee_id}")
        print(f"Salary:{self.salary}")

emp = employee("ram",19,"E10111",500000)
emp.display_employee()
