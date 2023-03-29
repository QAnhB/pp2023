from domain.studentInput import studentInput
from domain.courseInput import courseInput
import os.path

def input_student():
    num_student = int(input("Enter number of student: "))
    print("Number of student: ", num_student)
    return num_student

def load_students(students: studentInput):
    file =  os.path.exists("students.txt")
    if file == True:
        with open('students.txt', 'r') as fin:
            list_students = fin.read().splitlines() 
            for student in list_students:
                id,name,dob = student.split(", ")
                list_student,student_list = students.student_append(id,name,dob)
            fin.close()
    return list_student,student_list
    
def input_course():
    num_course = int(input("Enter number of course: "))
    print("Number of course: ", num_course)
    return num_course

def load_courses(courses: courseInput):
    file =  os.path.exists("courses.txt")
    if file == True:
        with open('courses.txt', 'r') as fin:
            list_courses = fin.read().splitlines() 
            for student in list_courses:
                id,name = student.split(", ")
                course_list = courses.course_append(id,name)
            fin.close()
    return course_list