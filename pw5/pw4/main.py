from input_num import input_student,input_course
import ouput
from domain.studentInput import studentInput
from domain.courseInput import courseInput
from domain.student_mark import student_mark
from domain.average_gpa import average_gpa

options = ['1. Enter number of student, student information',
           '2. Enter number of course, course information',
           '3. Choose a course for entering mark',
           '4. Calculate GPA',
           '5. Exit']
    
while True:
    print(*options, sep = "\n")
    user_input = int(input("Choose a number: "))

    if user_input == 1:
        x = input_student()
        student = studentInput()
        list_student, student_infomation = student.student_info(x)
        ouput.listing_dict(student_infomation)

    elif user_input == 2:
        n = input_course()
        course = courseInput()
        list_course = course.courses_info(n)
        ouput.listing_dict(list_course)

    elif user_input == 3:
        mark = student_mark(list_course)
        k = mark.choose_course()
        c = mark.student_mark(k,list_student)
        ouput.listing_dict(c)
        
    elif user_input == 4:
        gpa = average_gpa(c)
        credit = gpa.course_credit()
        gpa.sort_gpa(list_student,credit)

    elif user_input == 5:
        break    
        
    else:
        print("Wrong choice")