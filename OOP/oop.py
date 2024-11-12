# Classes and Objects
    # Class - an overviw of what the student data type is(template)
    # Object - is an actual student

class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
        
    def on_honor_roll(self):         # Functions inside of a class
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
    


