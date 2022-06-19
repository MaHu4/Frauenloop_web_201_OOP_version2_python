from .teacher import SchoolTeacher

# This class inherits from parent class: SchoolTeacher
class PhysicsTeacher(SchoolTeacher):

    # paramterized constructor: initializes class parameters name, lab_number
    def __init__(self,name, lab_number): # "--> None" deleted

        super().__init__(name=name)  # super() is a function call to the constructor (parameters or methods) of the parent class. (hint: check the parent class constructor definition.)
        self.lab_number = lab_number

    def get_lab_number(self):  # function to get the lab number
        return self.lab_number