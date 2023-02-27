#input number of student
def input_student():
    x = int(input('Enter numbers of students: '))
    print("Number of student: ", x)
    return x

#input student info
students = {}
list_student_id = []
def student_info(n):
    for i in range(n):
        student_id = str(input('Enter student id: '))
        name = str(input('Enter student name: '))
        birth = str(input('Enter DoB: '))
        students.update({student_id: [name,birth]})
        list_student_id.append(student_id)

#listing student
def listing_student():
    print('List of student: ')
    for key, value in students.items():
        print(key, ":", value)

#input number of course
def input_course():
    x = int(input('Enter number of courses: '))
    print("Number of course: ", x)
    return x

#input course infor
courses = {}
def course_info(a):
    for i in range(a):
        course_id = str(input("Enter course ID: "))
        name = str(input("Enter course name: "))
        courses.update({course_id:name})

#listing student
def listing_course():
    print("List of course: ")
    for key, value in courses.items():
        print(key, ":", value)

#choose a course for entering mark
def choose_course():
    x = str(input("Choose a course: "))
    for key,value in courses.items():
        if x == key:
            return x

#create a dict of mark
course_marks = {}
course_marks.update(courses) #coupy courses dict to course_marks

#function for entering and storing marks
def student_mark(k):
    marks = []
    
    #entering marks
    if k in courses.keys():
        for i in range(len(list_student_id)):
            print("Mark for: ", list_student_id[i])
            m = float(input())
            marks.append(m)
            
    else:
        print("Wrong ID")
    
    student_marks = dict(zip(list_student_id,marks)) #make a dict of student id and marks
    course_marks[k] = student_marks #make course id a key and student_marks value
    

#listing mark
def listing_mark():
    for key, value in course_marks.items():
        print(key, ":", value)

#main function
options = ['1. Enter number of student, student information',
           '2. Enter number of course, course information',
           '3. Choose a course for entering mark',
           '4. Exit']

#testing
while True:
    print(*options, sep = "\n")
    user_input = int(input("Choose a number: "))

    if user_input == 1:
        x = input_student()
        student_info(x)
        listing_student()

    elif user_input == 2:
        n = input_course()
        course_info(n)
        listing_course()

    elif user_input == 3:
        k = choose_course()
        student_mark(k)
        listing_mark()
    
    elif user_input == 4:
        break
    
    else:
        print("Wrong choice")