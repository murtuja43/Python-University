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
new_number = 



# hometask
# integer :24-30
# Boolean :1-40 (step 4)
