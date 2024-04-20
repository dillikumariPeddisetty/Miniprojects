class StudentReportCard():
    def __init__(self):
        self.name=input("Enter Student Name:")
        self.id=input("Enter ID:")
        self.dob=input("Enter DOB:")
        self.gmail=input("Enter Gmail:")
        self.sch=input("Enter School Name:")
        self.Unv=input("Enter University Name:")
        self.marks=list(map(float,input("Enter All Subject Marks").split()))
        print("=======================================")
        print("------------REPORT CARD----------------")
        print("========================================")
        print("Enter Student Name:",self.name)
        print("Enter ID:",self.id)
        print("Enter DOB:",self.dob)
        print("Enter Gmail:",self.gmail)
        print("Enter School Name:",self.sch)
        print("Enter University Name:",self.Unv)
        
    
    def TotalMarks(self):
        self.total=sum(self.marks)
        print("Total Marks:",self.total)
    def Percentage(self):
        self.percentage=self.total/600*100
        print("Percentage:",self.percentage)
    def Grade(self):
        if 80<self.percentage<100:
            print("Grade:A Grade")
        elif 60<self.percentage<80:
            print("Grade:B Grade")
        elif 45<self.percentage<60:
            print("Grade:C Grade")
        else:
            print("Grade:FAIL")
  
#main code
s1=StudentReportCard()

s1.TotalMarks()
s1.Percentage()
s1.Grade()
