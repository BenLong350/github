class Doodad:
    def __init__(self, name, age, DOB, sex):
        self.name = name
        self.age = age
        self.date_of_birth = DOB
        self.sex = sex
        
        
person1 = Doodad("Ben", 18, "Jan 16", "Male")

print(person1.name)