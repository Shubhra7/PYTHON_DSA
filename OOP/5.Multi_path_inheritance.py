#page: 444

class Student:
    def name(self):
        print("Name...")
    
class Academic_performance(Student):
    def Acad_score(self):
        print('Academic Score..... 90% and above ')

class ECA(Student):
    def ECA_score(self):
        print('ECA score....... 60% and above')
    
class Result(Academic_performance, ECA):
    def Eligibility(self):
        print('****** Minimum Eligibility to Apply ********')
        self.Acad_score()
        self.ECA_score()

R=Result()
R.Eligibility()



