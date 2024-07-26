class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_marksavg(self):
        
        sum = 0
        for val in self.marks:
            sum +=val
        print("hi", self.name,"yor avg marks is: ",sum/3)    

s1=Student("sankalp",[98,99,97])
s1.get_marksavg()