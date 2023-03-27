import math
class student_mark:
    def __init__(self,course_mark):
        self.course_mark = course_mark
    
    def choose_course(self):
        x = input("Choose a course: ")
        for key,value in self.course_mark.items():
            if x == key:
                return x
    
    def student_mark(self,k,list_student_id):
        marks = []
        #entering marks
        mark_file = open("marks.txt", 'w')
        if k in self.course_mark.keys():
            for i in range(len(list_student_id)):
                print("Mark for: ", list_student_id[i])
                m = math.floor(float(input())) 
                marks.append(m)
                mark_file.write(k)
                mark_file.write(" ")
                mark_file.write(list_student_id[i])
                mark_file.write(" ")
                mark_file.write(str(m))
                mark_file.write("\n")
        else:
            print("Wrong ID")
            
        mark_file.close()
        
        student_marks = dict(zip(list_student_id,marks)) #make a dict of student id and marks
        self.course_mark[k] = student_marks
        return self.course_mark