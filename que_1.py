#Define a class Student with attributes name, roll_number, and marks.
#Implement a method display_info() that prints the details of the student.
#Create an instance of Student and call the display_info() method to display
#the student's details.

class student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display_info(self):
        print(f"the name of the student is{self.name} with his roll no. being {self.roll_number} and marks being {self.marks} ")

s_1=student("ram",18,100)
s_1.display_info()

