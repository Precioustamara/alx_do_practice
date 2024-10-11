#Exercise 1: Class Methods for Counting Instances Instruction:
class Book:
    total_books = 0
    def __init__(self, name):
        self.name = name
        Book.total_books += 1
        
    @classmethod
    def display_total_books(cls):
        print(f"Total books counted: {cls.total_books}")

book1 = Book("Science")
book2 = Book("Art")
book3 = Book("Religion")

Book.display_total_books()

#Exercise 2: Static Method for Utility Calculation Instruction:
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
print(Calculator.add(10, 10))
print(Calculator.multiply(10, 10))

#Exercise 3: Class Method for Factory Creation Instruction:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, age = 0):
        return age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

child = Person.create_child("Adam")
print(child)