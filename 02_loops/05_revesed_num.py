# num = 12345
# 
# print("Reversed number: ", end="")
# 
# # Loop until the number becomes 0
# while num > 0:
#     # 1. Get the last digit
#     last_digit = num % 10
#     
#     # 2. Print it immediately without jumping to a new line
#     print(last_digit, end=" ")
#     
# # Print an empty line at the end just to clean up the terminal output
# print()

list1 = [1,2]
list2 = [3,4]
list3 = [1,2]
list4 = [3,4]
list3 += list4
list1.extend(list2)
list1.extend(list3)
print(list1)