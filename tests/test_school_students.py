from os import sched_get_priority_max
from views.school_students import SchoolStudents
from models.student import Student
 
class TestSchoolStudents: 
 
    #TODO Task1.0: write test
    def test_enroll_student(self):
        
        schoolStudents = SchoolStudents()  
        # schoolStudents = newly created object; SchoolStudents() = class
        print(type(schoolStudents))
    

        #  variable of type Student
        firstStudentInClass = Student(name="Maria", age=20, class_number=5)  # TestSchoolStudent is NOT a child class of Student
        secondStudentInClass = Student(name="Jyotsna", age=20, class_number=5)
        thirdStudentInClass = Student(name="Theresa", age=19, class_number=5)
        fourthStudentInClass = Student(name="Ayumi", age=19, class_number=5)
        fifthStudentInClass = Student(name="Nicole", age=21, class_number=5)
        sixthStudentInClass = Student(name="Ashgan", age=19, class_number=5)
        seventhStudentInClass = Student(name="Maren", age= 21, class_number=5)

        print(firstStudentInClass) # ?? How can I print the list of all enrolled students??
        
        # method to test
        schoolStudents.enroll_student(firstStudentInClass)  #enroll_student is method from class SchooStudents 
        schoolStudents.enroll_student(secondStudentInClass)
        schoolStudents.enroll_student(thirdStudentInClass)
        schoolStudents.enroll_student(fourthStudentInClass)
        schoolStudents.enroll_student(fifthStudentInClass)
        schoolStudents.enroll_student(sixthStudentInClass)
        schoolStudents.enroll_student(seventhStudentInClass)

        assert schoolStudents.enrolled_students == [firstStudentInClass, secondStudentInClass, thirdStudentInClass, fourthStudentInClass, fifthStudentInClass, sixthStudentInClass, seventhStudentInClass]

    

    # # TODO Task1.1: write test fetch_all_student_data()

    # def test_fetch_all_student_data(self):  

    #     # test-setup
    #     schoolStudents = SchoolStudents() # new object of SchoolStudents (not same object as in Task1.0)

    #     # variable of type Student
    #     firstStudentInClass = Student(name="Maria", age=20, class_number=5)
    #     secondStudentInClass = Student(name="Jyotsna", age=20, class_number=5)
    #     thirdStudentInClass = Student(name="Theresa", age=19, class_number=5)
    #     fourthStudentInClass = Student(name="Ayumi", age=19, class_number=5)
    #     fifthStudentInClass = Student(name="Nicole", age=21, class_number=5)
    #     sixthStudentInClass = Student(name="Ashgan", age=19, class_number=5)
    #     seventhStudentInClass = Student(name="Maren", age= 21, class_number=5)

    #     # enroll a student
    #     schoolStudents.enroll_student(firstStudentInClass)
    #     schoolStudents.enroll_student(secondStudentInClass)
    #     schoolStudents.enroll_student(thirdStudentInClass)
    #     schoolStudents.enroll_student(fourthStudentInClass)
    #     schoolStudents.enroll_student(fifthStudentInClass)
    #     schoolStudents.enroll_student(sixthStudentInClass)
    #     schoolStudents.enroll_student(seventhStudentInClass)

    #     # method to test
    #     all_student_data = schoolStudents.fetch_all_student_data()

    #     # assertion of actual result == expected result 
    #     assert all_student_data == [firstStudentInClass, secondStudentInClass, thirdStudentInClass, fourthStudentInClass, fifthStudentInClass, sixthStudentInClass, seventhStudentInClass]

    # TODO Task1.2: write test for fetch_data_with_student_name()

    # def test_fetch_data_with_student_name(self):

    #     # test-setup
    #     schoolStudents = SchoolStudents() 

    #     #variable of type Student
    #     firstStudentInClass = Student(name="Maria", age=20, class_number=5) # name, age and class are parameters defined in parent class
    #     secondStudentInClass = Student(name="Jyotsna", age=20, class_number=5)
    #     thirdStudentInClass = Student(name="Theresa", age=19, class_number=5)
    #     fourthStudentInClass = Student(name="Ayumi", age=19, class_number=5)
    #     fifthStudentInClass = Student(name="Nicole", age=21, class_number=5)
    #     sixthStudentInClass = Student(name="Ashgan", age=19, class_number=5)
    #     seventhStudentInClass = Student(name="Maren", age= 21, class_number=5)  


    #     # enroll a student
    #     schoolStudents.enroll_student(firstStudentInClass) 
    #     schoolStudents.enroll_student(secondStudentInClass)
    #     schoolStudents.enroll_student(thirdStudentInClass)
    #     schoolStudents.enroll_student(fourthStudentInClass)
    #     schoolStudents.enroll_student(fifthStudentInClass)
    #     schoolStudents.enroll_student(sixthStudentInClass)
    #     schoolStudents.enroll_student(seventhStudentInClass)

    #     # method to test
    #     data_with_student_name = schoolStudents.fetch_data_with_student_name() #?? What#s the difference to Task1.1???

    #     assert data_with_student_name == [firstStudentInClass, secondStudentInClass, thirdStudentInClass, fourthStudentInClass, fifthStudentInClass, sixthStudentInClass, seventhStudentInClass]

       
