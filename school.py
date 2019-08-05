class School(object):
    def __init__(self,name, roster={}):
        self.name=name
        self.roster=roster
    def add_student(self,student, number):
        self.roster[number]=student
    def grade(self, grade):
        return self.roster[grade]