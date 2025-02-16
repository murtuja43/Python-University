# problem 1
a = int(input("Whats a for Perameter P:"))
p = 4 * a
print(p)



# problem 2
a = int(input("Whats a for area S:"))
S = a * a
print(S)



# problem 3
a = int(input("Rectangular side a: "))
b = int(input("Rectangular side b: "))
P = 2 * (a + b)
print(P)



# problem 4
d = int(input("Whats d: "))
p = 3.14
L = p * d
print(L)



# problem 5
a = int(input("Whats a of a edge of a cube:"))
V = a ** 3
S = 6 * (a ** 2)
print(V)
print(S)



# problem 6
a = int(input("Whats edge a for rectangular: "))
b = int(input("Whats edge b for rectangular: "))
c = int(input("Whats edge c for rectangular: "))
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(V)



# problem 7
r = int(input("Whats r for circle: "))
p = 3.14
L = 2 * p * r
S = p * (r ** 2)
print(L)
print(S)



# problem 8
a = int(input("Whats a for arithmetic mean: "))
b = int(input("Whats b for arithmetic mean: "))
A = (a + b) / 2
print(A)



# problem 9
a = int(input("What's the first non-negative number a: "))
b = int(input("What's the first non-negative number b: "))

geometric_mean = (a * b) ** .5
print(geometric_mean)


# problem 10
a = int(input("First nonzero number a: "))
b = int(input("First nonzero number b: "))

sum_of_squares = a ** 2 + b ** 2
difference_of_squares = a ** 2 - b ** 2
product_of_squares = a ** 2 * b ** 2
quotient_of_squares = a ** 2 / b ** 2

print(sum_of_squares)
print(difference_of_squares)
print(product_of_squares)
print(quotient_of_squares)