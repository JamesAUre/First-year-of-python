class Person:
    name = ""
    age = 0
    gender = None

    def __init__(self,name,age,gender):

        #If Person.name = name then it will change all names of every instance globally

        self.name = name
        self.age = age
        self.gender = gender

james = Person("James", 19, "Male")

print(james.name)