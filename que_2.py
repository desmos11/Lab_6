#Create a base class Animal with a method speak() that prints "Animal makes
#a sound". Derive a class Dog from Animal and override the speak() method
#to print "Dog barks". Instantiate the Dog class and call its speak() method.

class animal:
    def __init__(self,animal):
        self.animal=animal
    def speak(self):
        print(f"{self.animal}makes a sound")


class dog(animal):
    def __init__(self,animal):
        super().__init__(animal)
    def speak(self):
        print("dog barks")
    
d=dog("meow")
d.speak()

        
