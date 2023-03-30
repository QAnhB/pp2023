from domain.information import information
import pickle

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
        file_open = open("students.pkl", "wb")
        pickle.dump(self.student_list, file_open)
        file_open.close()

        return list_student_ID, self.student_list
    
    