from .teacher import SchoolTeacher

# TODO Task2.1: This class inherits from parent class: SchoolTeacher
class EnglishTeacher(SchoolTeacher):

    # paramterized constructor: initializes class parameters name, xxx
    def __init__(self,name, class_teacher_of_class, room_number_of_main_class):

        # super() is a function call to the constructor of the parent class. 
        # (hint: check the parent class constructor definition.)
        super().__init__(name=name)
        self.class_teacher_of_class = class_teacher_of_class
        self.room_number_of_main_class = room_number_of_main_class

    # function to fetch class parameter values

    def get_class_teacher_of_class (self): 
        return self.class_teacher_of_class
    
    def get_room_number_of_main_class (self):
        return self.room_number_of_main_class

