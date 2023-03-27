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