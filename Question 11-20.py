# # Question-11
# num = int(input("Enter a number:"))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# # Question-12
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = int(input("Enter number 3: "))

# max_number = a

# if b > max_number:
#     max_number = b
# if c > max_number:
#     max_number = c

# print(f"max number is: {max_number}")


#  # Question-13
# import math
# def calculate_ex(x, terms = 20):
#     ex = 0
#     for n in range(0, terms):
#         ex += (x ** n) / math.factorial(n)
#     return ex
# print(calculate_ex(1))


# # Question-14
# import math
# def calculate_sinx(x, terms = 10):
#     results = 0
#     for n in range(0, terms):
#         num1 = ((-1) ** n) * (x ** (2 * n +1))
#         num2 = math.factorial(2 * n + 1)
#         results += num1 / num2
#     return results
# print(calculate_sinx(math.pi/2))


# Question-15
# import math
# def calculate_cosx(x, terms = 10):
#     results = 0
#     for n in range(terms):
#         num1 = (-1) ** n * x ** (2*n)
#         num2 = math.factorial(2 * n)
#         results += num1 / num2
#     return results

# print(calculate_cosx(0))  #output 1, [cos(0)]


# # Question-16
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Ask the user how many terms to print
# terms = int(input("Enter the number of terms: "))

# # Print the Fibonacci sequence
# print("Fibonacci sequence:")
# for i in range(terms):
#     print(fibonacci(i))


# # Question-18
# def display_array(arr):
#     for rows in arr:
#         print(rows)
    
# matrix = [[2,3], [1,4], [4,7]]
# display_array(matrix)


# # Question-19
# num = int(input("Enter a number:"))

# factorial = 1
# i = 1
# while i <= num:
#     factorial *= i
#     i += 1

# print("Factorial is:", factorial)



# # Question-20
# for i in range(1, 11):
#     print