from domain.studentInput import studentInput
from domain.courseInput import courseInput
import os, pickle

def input_student():
    num_student = int(input("Enter number of student: "))
    print("Number of student: ", num_student)
    return num_student

def load_students(students: studentInput):
    list_student_ID = []
    file =  os.path.exists("students.pkl")
    if file == True:
        file_name = open("students.pkl","rb")
        loaded_file = pickle.load(file_name)
        for i in loaded_file:
            if type(i) is list:
                for item in i:
                    list_student_ID.append(item)
            else: 
                list_student_ID.append(i)
        file_name.close()
    return list_student_ID,loaded_file
    
def input_course():
    num_course = int(input("Enter number of course: "))
    print("Number of course: ", num_course)
    return num_course

def load_courses(courses: courseInput):
    file =  os.path.exists("courses.pkl")
    if file == True:
        file_name = open("courses.pkl", "rb")
        loaded_file = pickle.load(file_name)
        file_name.close()
    return loaded_file