subjects = ["DBMS", "OS", "AWP", "AT", "Python"]
print(f"befor reversed: {subjects}")
re_list = []

left = 0
right = len(subjects) -1

while left < right:
    subjects[left], subjects[right] = subjects[right], subjects[left]

    left += 1
    right -= 2

print(subjects)