# Problem 1
A = int(input("Enter a number: "))
is_positive = A > 0
print("Is A positive:", is_positive)



# Problem 5
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
is_A_positive = A >= 0
is_B_less_than_minus_2 = B < -2
print("Is A positive:", is_A_positive, "Is B less than 2:", is_B_less_than_minus_2)



# Problem 9
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
is_A_odd = A % 2 != 0
is_B_odd = B % 2 != 0
print("Is A odd:", is_A_odd, "Is B odd:", is_B_odd)



# Problem 13
A = int(input("Enter a number: "))
B = int(input("Enter a number: "))
C = int(input("Enter a number: "))
is_A_positive = A > 0
is_B_positive = B > 0
is_C_positive = C > 0
print("Is A positive:", is_A_positive, "Is B positive:", is_B_positive, "Is C positive:", is_C_positive)



# Problem 17
A = int(input("Enter a number: "))
is_three_digit_odd = 100 <= A <= 999 and A % 2 != 0
print("Is A a three-digit odd number:", is_three_digit_odd)



# Problem 21
X = int(input("Enter a number: "))
hundreds = X // 100
tens = (X // 10) % 10
ones = X % 10
is_increasing_order = hundreds < tens < ones
print("Are the digits in increasing order:", is_increasing_order)



# Problem 25
x = int(input("Enter x: "))
y = int(input("Enter y: "))
is_x_negative = x < 0
is_y_positive = y > 0
print("Is x negative:", is_x_negative)
print("Is y positive:", is_y_positive)
print("If both true then it's in the second quadrant")



# Problem 29
x = int(input("Enter x: "))
y = int(input("Enter y: "))
X1 = int(input("Enter X1 (bottom-left x): "))
Y1 = int(input("Enter Y1 (bottom-left y): "))
X2 = int(input("Enter X2 (top-right x): "))
Y2 = int(input("Enter Y2 (top-right y): "))

is_inside = (X1 < x < X2) and (Y1 < y < Y2)
print("Is the point inside the rectangle:", is_inside)




# Problem 33
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
can_form_triangle = a + b > c and a + c > b and b + c > a
print("Can these sides form a triangle:", can_form_triangle)



# Problem 37
X1 = int(input("Enter X1: "))
Y1 = int(input("Enter Y1: "))
X2 = int(input("Enter X2: "))
Y2 = int(input("Enter Y2: "))

can_move = abs(X2 - X1) <= 1 and abs(Y2 - Y1) <= 1
print("Can the king move in one move:", can_move)
