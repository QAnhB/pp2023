from input_num import input_student,input_course,load_students,load_courses
import ouput
import pickle
from zipfile import ZipFile
import os
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
    file_path = ZipFile('/Downloads/Clone/pp2023/pw6/compress_file.zip', 'r')
    with file_path as zip:  
        zip.extractall('/Downloads/Clone/pp2023/pw6')
    file_path.close()

while True:
    print(*options, sep = "\n")
    user_input = int(input("Choose a number: "))

    if user_input == 1:
        student = studentInput()
        list_student, student_infomation = load_students(student)
        ouput.listing_dict(student_infomation)

    elif user_input == 2:
        course = courseInput()
        list_course = load_courses(course)
        ouput.listing_dict(list_course)

    elif user_input == 3:
        mark = student_mark(list_course)
        k = mark.choose_course()
        c = mark.student_mark(k,list_student)
        file_open = open("marks.pkl", "wb")
        pickle.dump(c, file_open)
        file_open.close()
        ouput.listing_dict(c)
        
    elif user_input == 4:
        file_name = open("marks.pkl", "rb")
        load_file = pickle.load(file_name)
        gpa = average_gpa(load_file)
        credit = gpa.course_credit()
        gpa.sort_gpa(list_student,credit)
        file_name.close()
    
    elif user_input == 5:
        with ZipFile('compress_file.zip','w') as zipObj2:
            zipObj2.write('students.pkl')
            zipObj2.write('courses.pkl')
            zipObj2.write('marks.pkl')

    elif user_input == 6:
        break    
        
    else:
        print("Wrong choice")