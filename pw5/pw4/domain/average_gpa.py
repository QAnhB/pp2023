import pandas as pd
import numpy as np

class average_gpa:
    def __init__(self,course_mark):
        self.course_mark = course_mark
    
    def course_credit(self):
        list_course = list(self.course_mark.keys())
        credit = []
        for i in list_course:
            print("Enter credit for ",i)
            c = int(input())
            credit.append(c)
        course_credit = dict(zip(list_course,credit))
        return course_credit

    def choose_student(self):
        n = input("Choose a student: ")
        return n
    
    def average(self,chosen_student,course_credit):
        student = pd.DataFrame(self.course_mark)
        credit_list = list(course_credit.values())
        credit_list = np.array(credit_list)
        chose = student.loc[chosen_student]
        chose_array = np.array(chose)
        numerator = 0
        denominator = 0
        for i in range(len(chose_array)):
            product = chose_array[i]*credit_list[i]
            numerator += product
        for i in range(len(credit_list)):
            denominator+=credit_list[i]
        weight_sum = numerator/denominator
        print("GPA of ", chosen_student, "is: ", weight_sum)
        return weight_sum
    
    def sort_gpa(self,list_student,course_credit):
        studentGPA = {}
        for i in list_student:
            w = self.average(i,course_credit)
            studentGPA.update({i:w})
        studentGPA = sorted(studentGPA.items(), key = lambda x:x[1], reverse=True)
        print(studentGPA)