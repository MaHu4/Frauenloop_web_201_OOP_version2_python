# it represents the data and functionality for a student from the real world. Each instance of that class (every time I do var = Student()) will be for one particular student that exists at some given time.

class Student:

    # class parametrized contructor: 
    # initializes class vairables / parameters to values passed
    def __init__(self, name, age, class_number):
        self.name = name
        self.age = age
        self.class_number = class_number
        self.grade = {} # dictionary of type: Dict[String: Character] | [subject:grade]

    # func to calculate the year of birth, since the age of the student is known.
    # using the current year
    def calculate_year_of_birth(self, current_year):
        pass

