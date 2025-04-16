# # Question-1:
# import math
# def factorial(n):
#     f1 = 1
#     for i in range(1, n+1):
#         f1 *= i
#     return f1

# def sin_x(x, total=50):
#     sinx = 0
#     for i in range(1, total):
#         sign = pow(-1, i)
#         power = (2 * i) - 1
#         sinx += sign * pow(x, power) / factorial(power)
#     return sinx

# angle = float(input("Enter the angle in radians: "))
# print(f"The value of sin({angle}) using Taylor Series is: {sin_x(angle)}")



# # using one def:
# import math
# def sin_x(x):
#     sinx = 0
#     N=80
#     for i in range(1, N):
#         power = 2 * i - 1
#         f = 1
#         for t in range(1, power + 1):
#             f *= t
#         sign = pow(-1, i-1)
        
#         sinx += sign * pow(x, power) / f
#     return sinx

# angle = float(input("Enter the angle in radians: "))
# print(f"The value of sin({angle}) using Taylor Series is: {sin_x(angle)}")



 # Question-2:
import math
cosx = 0
N = 100

x = math.pi / 2.0
for i in range(N + 1):
    f = math.factorial(2 * i)
    cosx += (-1) ** i * (x ** (2 * i)) / f

print(cosx)







# # Question- 3:

# def calculate_average():
#     numbers = []
    
#     while True:
#         num = int(input("Enter a number from -9999 to +9999 (0 to stop): "))
#         if num == 0:
#             break
#         numbers.append(num)

#     if numbers:
#         avg = sum(numbers) / len(numbers)
#         print(f"Average: {avg:.2f}")
#     else:
#         print("No numbers were entered.")

# calculate_average()



# # Question- 4
# def calculate_payment():
#     while True:
#         code = int(input("Enter employee type (1-Manager, 2-Hourly, 3-Commission, 4-Pieceworker, 0 to Exit): "))

#         if code == 0:
#             print("Exiting payroll system.")
#             break

#         match code:
#             case 1:  # Manager
#                 salary = float(input("Enter fixed weekly salary: "))
#                 print(f"Manager's payment: ${salary:.2f}")

#             case 2:  # Hourly Worker
#                 hourly_wage = float(input("Enter hourly wage: "))
#                 hours_worked = float(input("Enter hours worked: "))
#                 total_payment = (40 * hourly_wage) + ((hours_worked - 40) * 1.5 * hourly_wage) if hours_worked > 40 else hours_worked * hourly_wage
#                 print(f"Hourly worker's payment: ${total_payment:.2f}")

#             case 3:  # Commission Worker
#                 sales = float(input("Enter total sales amount: "))
#                 total_payment = 250 + (0.057 * sales)
#                 print(f"Commission worker's payment: ${total_payment:.2f}")

#             case 4:  # Pieceworker
#                 units_produced = int(input("Enter number of units produced: "))
#                 rate_per_unit = float(input("Enter fixed amount per unit: "))
#                 total_payment = units_produced * rate_per_unit
#                 print(f"Pieceworker's payment: ${total_payment:.2f}")

#             case _:  # Default case
#                 print("Invalid code! Please enter a valid employee type.")

# calculate_payment()
