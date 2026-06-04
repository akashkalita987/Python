a = 10
b = 5

print("Value of a:", a)
print("Value of b:", b)

#1.Arithmetic Operators
print("\nArithmetic Operators")
print("Addition (a + b):", a + b)
print("Subtraction (a - b):", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b):", a / b)
print("Modulus (a % b):", a % b)
print("Exponent (a ** b):", a ** b)
print("Floor Division (a // b):", a // b)

#2.Comparison Operators
print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#3.Logical Operators
print("\nLogical Operators")
print("(a > 5 and b < 10):", (a > 5 and b < 10))
print("(a < 5 or b < 10):", (a < 5 or b < 10))
print("not(a > b):", not(a > b))

#4.Assignment Operators
print("\nAssignment Operators")
c = a
print("c = a:", c)
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)
c *= b
print("c *= b:", c)
c /= b
print("c /= b:", c)

#5.Bitwise Operators
print("\nBitwise Operators")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

#6.Membership Operators
print("\n--- Membership Operators ---")
list1 = [1, 2, 3, 4, 5]
print("3 in list1:", 3 in list1)
print("10 not in list1:", 10 not in list1)

#7.Identity Operators
print("\n--- Identity Operators ---")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)
print("x is z:", x is z)
print("x == z:", x == z)