# problem 1
x = int(input("Enter a number: "))
if x > 0:
    x = x +1
    print(f"After adding 1, new number is: {x}")



# problem 5
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))  
c = int(input("Enter third number: "))  

positive_count = 0  
negative_count = 0  

if a > 0:  
    positive_count += 1  
elif a < 0:  
    negative_count += 1  

if b > 0:  
    positive_count += 1  
elif b < 0:  
    negative_count += 1  

if c > 0:  
    positive_count += 1  
elif c < 0:  
    negative_count += 1  

print("Positive numbers:", positive_count)  
print("Negative numbers:", negative_count)  



# problem 9
A = int(input("Enter first number A: "))  
B = int(input("Enter second number B: "))

if A < B:
    print(f"The smaller value is A: {A}")
    print(f"The larger value is B: {B}")
elif A > B:
    A , B = B , A
    print(f"The smaller value is A: {B}")
    print(f"The larger value is B: {A}")



# problem 13
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))  
c = int(input("Enter third number: "))  

if (a > b and a < c) or (a < b and a > c):  
    middle = a  
elif (b > a and b < c) or (b < a and b > c):  
    middle = b  
else:  
    middle = c  

print("Middle number:", middle)  



# problem 17
A = int(input("Enter first number A: "))  
B = int(input("Enter second number B: "))
C = int(input("Enter second number C: "))

if (A > B > C) or (A < B < C):
    A, B, C = 2*A, 2*B, 2*C
    print(f"The doubled numbers are: {A, B, C}")
else:
    A, B, C = -A, -B, -C
    print(f"After replacing with their negative: {A, B, C}")



# problem 21
X = int(input("Enter X coordinate: "))  
Y = int(input("Enter Y coordinate: "))  

if X == 0 and Y == 0:  
    print(0) 
elif Y == 0:  
    print(1)  
elif X == 0:  
    print(2)  
else:  
    print(3)



# problem 25
x = int(input("Enter a number: "))

if x < -2 or x > 2:
    print("f(x) = 2.x")
else:
    print("f(x) = -3.x")



# problem 29
x = int(input("Enter a number: "))

if (x < 0) and (x % 2 == 0):
    print("X is a negative even number")
elif (x < 0) and (x % 2 != 0):
    print("X is a negative odd number")
elif (x > 0) and (x % 2 != 0):
    print("X is a positive odd number")
elif (x > 0) and (x % 2 == 0):
    print("X is a positive even number")
elif x == 0:
    print("X is zero")# Here we will solve if else problems
