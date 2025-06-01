# Question-1

time = int(input("Give time (in seconds): "))
distance = int(input("Give distance (in meters): "))

time_in_hours = time / 3600
distance_in_km = distance / 1000
print(f"The output is: {int(distance_in_km/time_in_hours)} km/h")



# Question-2

n = int(input("What's N? "))

sum_of_factors = 0

for i in range(1, n):
    if n % i == 0:
        sum_of_factors += i

print(f"Output: {sum_of_factors}")



