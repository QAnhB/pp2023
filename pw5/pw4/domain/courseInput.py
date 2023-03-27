from domain.information import information

class courseInput:
    def __init__(self):
        self.courses_list = {}

    def courses_info(self,n):
        infor = information()
        course_file = open("courses.txt", 'w')
        for i in range(n):
            ID = infor.get_ID()
            name = infor.get_name()
            self.courses_list.update({ID:name})
            course_file.write(ID)
            course_file.write("\n")
            course_file.write(name)
            course_file.write("\n")
        course_file.close()
        return self.courses_list