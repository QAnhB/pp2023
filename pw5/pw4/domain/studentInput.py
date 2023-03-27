from domain.information import information

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
        student_file = open("students.txt",'w')
        for i in range(n):
            ID = infor.get_ID()
            name = infor.get_name()
            birth = self.input_birth()
            self.student_list.update({ID: [name,birth]})
            list_student_ID.append(ID)
            student_file.write(ID)
            student_file.write("\n")
            student_file.write(name)
            student_file.write("\n")
            student_file.write(birth)
            student_file.write("\n")
        student_file.close()
        return list_student_ID, self.student_list