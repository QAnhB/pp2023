from domain.information import information

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