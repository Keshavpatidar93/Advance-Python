class Marksheet_Bean():
    def __init__(self):
        self.__id = 0
        self.__roll_no = 0
        self.__name = ''
        self.__phy = 0
        self.__che = 0
        self.__maths = 0

    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_roll_no(self,roll):
        self.__roll_no = roll
    def get_roll_no(self):
        return self.__roll_no

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_phy(self,phy):
        self.__phy = phy
    def get_phy(self):
        return self.__phy

    def set_che(self,che):
        self.__che = che
    def get_che(self):
        return self.__che

    def set_maths(self,maths):
        self.__maths = maths
    def get_maths(self):
        return self.__maths