class information:
    def __init__(self):
        self.__ID = str
        self.__name = str

    def get_ID(self):
        self.__ID = input("Enter ID: ")
        return self.__ID
    
    def get_name(self):
        self.__name = input("Enter name: ")
        return self.__name

class studentInput:
    def __init__(self):
        self.__birth = str
        self.student_list = {}
        
    def input_birth(self):
        self.__birth = input("Enter birthday: ")
        return self.__birth
    
    def student_info(self,n):
        infor = information()
        list_student_ID = []
        for i in range(n):
            ID = infor.get_ID()
            name = infor.get_name()
            birth = self.input_birth()
            self.student_list.update({ID: [name,birth]})
            list_student_ID.append(ID)
        return list_student_ID
    
    def list_student(self):
        print('List of student: ')
        for key, value in self.student_list.items():
            print(key, ":", value)

class courseInput:
    def __init__(self):
        self.courses_list = {}

    def courses_info(self,n):
        infor = information()
        for i in range(n):
            ID = infor.get_ID()
            name = infor.get_name()
            self.courses_list.update({ID:name})
        return self.courses_list
    
    def listing_course(self):
        print("List of course: ")
        for key, value in self.courses_list.items():
            print(key, ":", value)

class student_mark:
    def __init__(self,course_mark):
        self.course_mark = course_mark
    
    def choose_course(self):
        x = str(input("Choose a course: "))
        for key,value in self.course_mark.items():
            if x == key:
                return x
    
    def student_mark(self,k,list_student_id):
        marks = []
        #entering marks
        if k in self.course_mark.keys():
            for i in range(len(list_student_id)):
                print("Mark for: ", list_student_id[i])
                m = float(input())
                marks.append(m)
                
        else:
            print("Wrong ID")
        
        student_marks = dict(zip(list_student_id,marks)) #make a dict of student id and marks
        self.course_mark[k] = student_marks
    
    def listing_mark(self):
        for key, value in self.course_mark.items():
            print(key, ":", value)

if __name__ == "__main__":
    options = ['1. Enter number of student, student information',
           '2. Enter number of course, course information',
           '3. Choose a course for entering mark',
           '4. Exit']
    
    while True:
        print(*options, sep = "\n")
        user_input = int(input("Choose a number: "))

        if user_input == 1:
            x = int(input("Enter number of student: "))
            print("Number of student: ", x)
            student = studentInput()
            list_student = student.student_info(x)
            student.list_student()

        elif user_input == 2:
            n = int(input("Enter number of course: "))
            print("Number of student: ", n)
            course = courseInput()
            list_course = course.courses_info(n)
            course.listing_course()

        elif user_input == 3:
            mark = student_mark(list_course)
            k = mark.choose_course()
            mark.student_mark(k,list_student)
            mark.listing_mark()
        
        elif user_input == 4:
            break
        
        else:
            print("Wrong choice")