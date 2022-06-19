from models.teacher import SchoolTeacher

class MathsTeacher(SchoolTeacher): 
    def __init__(self, name, class_teacher_of_class, room_number_of_main_class, other_classes_taught_math, room_number_of_other_classes_taught_math): 
                                    
        super().__init__(name = name) # ??? WHY name = name and not just name??; ony =, not == because it's a function; it's supposed to do something

        self.class_teacher_of_class = class_teacher_of_class # ??? WhAT DOES THIS LINE SAY???
        self.room_number_of_main_class = room_number_of_main_class 
        self.other_classes_taught_math = other_classes_taught_math
        self.room_number_of_other_classes_taught_math = room_number_of_other_classes_taught_math

    def get_name (self):  # function to get the name ?? does it make sense?? Or done in parent class??
        return self.name

    def get_class_teacher_of_class (self): 
        return self.class_teacher_of_class

    def get_room_number_of_main_class (self):
        return self.room_number_of_main_class
    
    def get_other_classes_taught (self):
        return self.other_classes_taught_math

    def get_room_number_of_other_classes_taught_math (self):
        return self.room_number_of_other_classes_taught_math


