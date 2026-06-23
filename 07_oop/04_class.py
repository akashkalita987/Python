class student:
    def __init__(self, Sname, Sroll):
        self.name = Sname
        self.roll = Sroll

s1 = student("akash",5)
s2 = student("bikash",6)
print(f"Student 1 detailes:\n{s1.name}\n{s1.roll}")

print(f"Student 1 detailes:\n{s2.name}\n{s2.roll}")

