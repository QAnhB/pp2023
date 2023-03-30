from domain.information import information
import  pickle

class courseInput:
    def __init__(self):
        self.courses_list = {}

    def courses_info(self,n):
        """
        It takes the number of courses as an argument and creates a dictionary of courses with their IDs
        and names.
        
        :param n: number of courses
        :return: The courses_list dictionary is being returned.
        """
        infor = information()
        for i in range(n):
            ID = infor.get_ID()
            name = infor.get_name()
            self.courses_list.update({ID:name})
        file_open = open("courses.pkl", "wb")
        pickle.dump(self.courses_list, file_open)
        file_open.close()
        return self.courses_list