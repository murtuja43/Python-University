#problem 1
L = int(input("Enter a distance in centimeters: "))
m = L // 100
print("The distance in meters is: ", m)


#problem 2
M = int(input("Enter a mass in kilogram: "))
t = M // 1000
print("The mass in tons is: ", t)


#problem 3
b = int(input("Enter files size in bytes: "))
kb = b / 1024
print("The file size in kilobytes is: ", kb)


#problem 4
A = int(input("Enter a positive integer: "))
B = int(input("Enter a positive integer: "))
count = A // B
print("The number of times B can be inside A is: ", count)


#problem 5
A = int(input("Enter A: "))  
B = int(input("Enter B: "))  
remaining_length = A % B
print(remaining_length)


#problem 6
a = int(input("Enter a two digit number: "))
tens = a // 10
ones = a % 10
print("The tens digit is: ", tens)
print("The ones digit is: ", ones)


#problem 7
a = int(input("Enter a two digit number: "))
tens = a // 10
ones = a % 10
sum = tens + ones
product = tens * ones
print("The sum of the digits is: ", sum)
print("The product of the digits is: ", product)


#problem 8
a = int(input("Enter a two digit number: "))
tens = a // 10
ones = a % 10
new_number = ones * 10 + tens
print("The number with the digits swapped is: ", new_number)


#problem 9
a = int(input("Enter a three digit number: "))
hundreds = a // 100
print("The first digit (hundreds) is: ", hundreds)


# problem 10
num = int(input("Enter a three digit number: "))
ones = num % 10       # Extract the last digit (ones place)
tens = (num // 10) % 10  # Extract the middle digit (tens place)
print(ones, tens)


# problem 11
num = int(input("Enter a three digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
sum = hundreds + tens + ones
product = hundreds * tens * ones
print("The sum of the digits is: ", sum)
print("The product of the digits is: ", product)


# problem 12
num = int(input("Enter a three digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
new_number = ones * 100 + tens * 10 + hundreds
print(new_number)


#problem 13
num = int(input("Enter a three digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
new_number = tens * 100 + ones * 10 + hundreds
print("after appending the first digit to last: ", new_number)


# problem 14
num = int(input("Enter a three digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
new_number = (ones * 100) + (hundreds * 10) + tens
print(new_number)


# problem 15
num = int(input("Enter a three digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
new_number = (tens * 100) + (hundreds * 10) + ones
print(new_number)



# problem 16
num = int(input("Enter a three digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
new_number = (hundreds * 100) + (ones * 10) + tens
print(new_number)


# problem 24
K = int(input("Write a number between 1-365: "))
day_number = (K + 0) % 7
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"The {K}th day is: {days[day_number]}")


# problem 25
K = int(input("Write a number between 1-365: "))
day_number = (K + 3) % 7
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(f"The {K}th day is: {days[day_number]}")



# problem 26
K = int(input("Write a number between 1-365: "))
# jan 1st is Tuesday
day_number = ((K + 1 - 1) % 7) + 1
days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"The {K}th day is: {days[day_number]}")


# problem 27
# jan 1st is Saturday
K = int(input("Write a number between 1-365: "))
days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_number = ((K + 5 - 1) % 7) + 1
print(f"The {K}th day is: {days[day_number]}")


# problem 28
K = int(input("Write a number between 1-365: "))
N = int(input("Write a number between 1-7: "))
days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_number = ((K + N - 2) % 7) + 1
print(f"The {K}th day is: {days[day_number]}")


# problem 29
A = int(input("Enter a positive number A: "))
B = int(input("Enter a positive number B: "))
C = int(input("Enter a positive number C: "))

square_A_side = A // C
square_B_side = B // C

total_squares = square_A_side * square_B_side
remaining_space = (A * B) - total_squares
print(f"Maximum possible squares: {total_squares}")
print(f"Unused part: {remaining_space}")



# problem 30
Y = int(input("Enter a year: "))
century = ((Y - 1) // 100) + 1

print(f"This year is in {century}th century.")
