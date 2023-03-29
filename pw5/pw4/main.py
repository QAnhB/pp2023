from input_num import input_student,input_course,load_students,load_courses
import ouput
import json
from zipfile import ZipFile
import os.path
from domain.studentInput import studentInput
from domain.courseInput import courseInput
from domain.student_mark import student_mark
from domain.average_gpa import average_gpa

options = ['1. Enter number of student, student information',
           '2. Enter number of course, course information',
           '3. Choose a course for entering mark',
           '4. Calculate GPA',
           '5. Compress file',
           '6. Exit']

file_exists = os.path.exists('compress_file.zip')
if file_exists == True:
    with ZipFile('/Downloads/Clone/pp2023/pw5/pw4/compress_file.zip', 'r') as zip:
        zip.extractall('/Downloads/Clone/pp2023/pw5/pw4/')

while True:
    print(*options, sep = "\n")
    user_input = int(input("Choose a number: "))

    if user_input == 1:
        x = input_student()
        student = studentInput()
        list_student, student_infomation = load_students(student)
        ouput.listing_dict(student_infomation)

    elif user_input == 2:
        n = input_course()
        course = courseInput()
        list_course = load_courses(course)
        ouput.listing_dict(list_course)

    elif user_input == 3:
        mark = student_mark(list_course)
        k = mark.choose_course()
        c = mark.student_mark(k,list_student)
        with open('marks.txt', 'w') as fp:
            json.dump(c,fp)
        ouput.listing_dict(c)
        
    elif user_input == 4:
        gpa = average_gpa()
        gpa.read_file()
        credit = gpa.course_credit()
        gpa.sort_gpa(list_student,credit)
    
    elif user_input == 5:
        with ZipFile('compress_file.zip','w') as zipObj2:
            zipObj2.write('students.txt')
            zipObj2.write('courses.txt')
            zipObj2.write('marks.txt')

    elif user_input == 6:
        break    
        
    else:
        print("Wrong choice")