class School(object):
    def __init__(self,name, roster={}):
        self.name=name
        self.roster=roster
    def add_student(self,student, number):
        self.roster[number]=student
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self): 
        for key in sorted(self.roster):
            print("%s: %s" % (key, self.roster[key]))