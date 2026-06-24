#mydict = {
#    "name":"akash",
#    "roll":5
#}
#print(f"{mydict["name"]}\n{mydict["roll"]}")

#sqrt = lambda x: x*x
#print(sqrt(5)) 
#try:
#    num = 10 / 0
#except ZeroDivisionError:
#    print("You cannot divide by zero!")
#finally:
#    print("Execution complete.")

#for i in range(0,11,2):
#    print(i)
#num = 12345
#print("Reversed number: ", end=" ")
#while num > 0:
#    print(num % 10, end="")
#    num = num // 10
college2  = ["avc", "cu", "bbc", "dc", "lcb", "pc", "bc"]
rev = []
for i in range(len(college2)-1, -1, -1):
    rev.append(college2[i])
print(rev)
