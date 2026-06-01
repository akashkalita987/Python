class student:

    def __init__(self, name, rollNo, cls):
        self.name = name
        self.rollNo = rollNo
        self.cls = cls

    def display(self):
        return f"{self.name} {self.rollNo} {self.cls}"
    
student1 = student("akash",5,"4th sem")
student2 = student("bikash",6,"2nd sem")

print ("Student detailes are____")
print(f"Student name:- {student1.name}")
print(student1.display())

