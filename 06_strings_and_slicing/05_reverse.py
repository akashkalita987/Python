#reversing using reverse function
college = ["avc", "cu", "bbc"]
college.reverse()
print(f"the reversd array is: \n{college}")

#reversing uisng slicing
college1 = ["avc", "cu", "bbc"]
print(college1[::-1])

#reversing using loop
college2  = ["avc", "cu", "bbc", "dc", "lcb", "pc", "bc"]
rev = []
for i in range(len(college2) -1, -1, -1):
    rev.append(college2[i])
print(rev)
college2  = ["avc", "cu", "bbc", "dc", "lcb", "pc", "bc"]
print(college2[-1:-1:-1])