import string


class SchoolTeacher:

    # parametrized contructor to initialize class variable name.
    def __init__(self, name, age, subject1, subject2):
        self.name = name
        self.age = age
        self.subject1 = subject1
        self.subject2 = subject2

    #function to get the name of the teacher
    def get_name(self) -> string:
        return self.name