from typing import Dict


class Student:
    def __init__(self, id, name, dob, clss, section):
        self.id = id 
        self.name = name
        self.dob = dob 
        self.clss = clss 
        self.section = section

class ClassPrepStudent(Student):
    def __init__(self, id, name, dob, section):
        super().__init__(id, name, dob, 0, section)
        self.obEnglishMarks = 0
        self.obMathMarks = 0
        self.obEvsMarks = 0
        self.totEnglishMarks = 100
        self.totMathMarks = 100
        self.totEvsMarks = 100


    def putMarks(self, eng : int, math : int, evs : int):
        self.obEnglishMarks = eng
        self.obMathMarks = math
        self.obEvsMarks = evs 


    def calculateTotal(self):
        return self.obEnglishMarks + self.obEvsMarks + self.obMathMarks
    
    def percentage(self):
        return int((self.calculateTotal()/(self.totEnglishMarks + self.totMathMarks + self.totMathMarks)) * 100)

    def createData(self):        
        data = {
            'id': self.id,
            'name' : self.name,
            'dob' : self.dob,                        
            'obEnglishMarks' : self.obEnglishMarks,
            'obMathMarks' : self.obMathMarks,
            'obEvsMarks' : self.obEvsMarks
        }
        return (self.clss, self.section, data)

    def printDetails(self):
        print(f"ID: {self.id}\tName: {self.name}\tDOB: {self.dob}\tClass: Prep\tSection: {self.section}")
        print(f"English: {self.obEnglishMarks}\tMaths: {self.obMathMarks}\tEVS: {self.obEvsMarks}")
    
       