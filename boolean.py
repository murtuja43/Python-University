# problem 1
A = int(input("Enter a number: "))
print(A>0)


# problem 5
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
print(A>=0, B<=2)


# problem 9
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
print(A % 2 != 0, B % 2 != 0)
# problem..............


# problem 13
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))
print(A>0, B>0, C>0)


# problem 17
A = int(input("Enter a number: "))
b = 100 <= A >= 999 and A % 2 != 0
print(b)
# problem..................


# problem 21
X = int(input("Enter a number: "))
a = X // 100
b = (X // 10) % 10
c = X % 10
print(a < b < c)


# problem 25
x = int(input("Enter x : "))
y = int(input("Enter y : "))
print(x < 0)
print(y > 0)


# problem 29
x = int(input("Enter x : "))
y = int(input("Enter y : "))
x1 = 0
x2 = 6
y1 = 2
y2 = 8
print(x1 < x < y2, y1 < y < y2)


# problem 33
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = a + b > c 
e = a + c > b 
f = b + c > a 
print(d and e and f)


# problem 37
x1 = int(input("Enter x1 : "))
x2 = int(input("Enter x2 : "))
y1 = int(input("Enter y1 : "))
y2 = int(input("Enter y2 : "))

able_or_not = (x2 - x1) <= 0 and (y2 - y1) <=0
print(able_or_not)
