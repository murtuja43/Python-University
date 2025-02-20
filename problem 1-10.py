# problem 1
a = int(input("Whats a for Perameter P:"))
p = 4 * a
print("Prarmeter:", p)



# problem 2
a = int(input("Whats a for area S:"))
S = a * a
print("Area:", S)



# problem 3
a = int(input("Rectangular side a: "))
b = int(input("Rectangular side b: "))
S = a * b
P = 2 * (a + b)
print("Area:", S)
print("Perameter:", P)



# problem 4
d = int(input("Whats d: "))
p = 3.14
L = p * d
print("Circumference:", L)



# problem 5
a = int(input("Whats a of a edge of a cube:"))
V = a ** 3
S = 6 * (a ** 2)
print("Volume:", V)
print("Area:", S)



# problem 6
a = int(input("Whats edge a for rectangular: "))
b = int(input("Whats edge b for rectangular: "))
c = int(input("Whats edge c for rectangular: "))
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print("Volume:", V)
print("Surface Area:", S)



# problem 7
r = int(input("Whats r for circle: "))
p = 3.14
L = 2 * p * r
S = p * (r ** 2)
print("Circumference:", L)
print("Area:", S)



# problem 8
a = int(input("Whats a for arithmetic mean: "))
b = int(input("Whats b for arithmetic mean: "))
A = (a + b) / 2
print("Arithmetic Mean:", A)



# problem 9
a = int(input("What's the first non-negative number a: "))
b = int(input("What's the first non-negative number b: "))

geometric_mean = (a * b) ** .5
print("Geometric mean:", geometric_mean)



# problem 10
a = int(input("First nonzero number a: "))
b = int(input("First nonzero number b: "))

sum_of_squares = a ** 2 + b ** 2
difference_of_squares = a ** 2 - b ** 2
product_of_squares = a ** 2 * b ** 2
quotient_of_squares = a ** 2 / b ** 2

print("Sum of their squres:",sum_of_squares)
print("Difference of their squres:", difference_of_squares)
print("Product of their squres:", product_of_squares)
print("Quotient of their squres:", quotient_of_squares)



'''From here started step: 3'''

#problem 13
R1 = int(input("Enter the first circle radius: "))
R2 = int(input("Enter the second circle radius: "))
p = 3.14
S1 = p * (R1 ** 2)
S2 = p * (R2 ** 2)
S3 = S1 - S2
print("Area of the first circle:", S1)
print("Area of the second circle:", S2)
print("Area of the ring:", S3)



#problem 16
x1 = int(input("Enter the first point x1: "))
x2 = int(input("Enter the second point x2: "))
print("Distance between the points:", abs(x2 - x1))



#problem 19
'''facing some problem'''



#problem 22
A = int(input("Enter value A: "))
B = int(input("Enter value B: "))
A , B = B , A
print("New value of A:", A)
print("New value of B:", B)



#problem 25
x = int(input("Enter the number x: "))
y = 3 * (x ** 6) - 6 * (x ** 2) - 7
print("The value of the function x = 3x^2-6x^2-7 is: ", y)



#problem 28
A = int(input("Enter number A: "))
A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5
print(A2, A3, A5, A10, A15)
