from os import sched_get_priority_max
from views.school_teachers import SchoolTeachers
from models.teacher import SchoolTeacher
 
class TestSchoolStudents: 

# Test to register school teachers
    def test_register_teacher(self):

        schoolTeachers = SchoolTeachers()

    #  variable of type SchoolTeacher
        firstTeacherofSchool = SchoolTeacher(name = "Hille", age="52", subject1 = "Maths", subject2= "English")

 # method to test
        schoolTeachers.register_teacher(firstTeacherofSchool) 

        assert schoolTeachers.registered_teachers == [firstTeacherofSchool]

