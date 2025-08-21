#Define a class Person with attributes name and age. Define another class
#Address with attributes street, city, and zipcode. Create a Contact class that
#contains an instance of Person and Address. Implement methods to display
#the contact details. Create a Contact object and display its information.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class address:
    def __init__(self,street,city,zipcode):
        self.street=street
        self.city=city
        self.zipcode=zipcode


class contact:
    def __init__(self,person,address):
        self.person=person
        self.address=address
    def display(self):
        print(f"Name: {self.person.name}")
        print(f"Age: {self.person.age}")      
        print(f"Street: {self.address.street}")
        print(f"City: {self.address.city}")
        print(f"Zipcode: {self.address.zipcode}")

person_1 = person("John Doe", 30)
address_1 = address("123 Main St", "Springfield", "12345")
contact_1 = contact(person_1, address_1)
contact_1.display()

