# We are gonna understand the concept of calling a class in a different file using the same class's object
class Company:
    def __init__(self,ceo,name,e_no,turnover):
        self.ceo=ceo
        self.name=name
        self.e_no=e_no
        self.turnover=turnover
    def cal(self):
        self.monthin=self.turnover/12
    def m(self):
        return self.monthin
    def disp(self):
        print("The monthly turnover=",self.m())

    
