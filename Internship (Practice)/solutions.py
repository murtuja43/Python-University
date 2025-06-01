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



# Question-3

word = input("Word? ").upper()
n = int(input("N? "))

# Step 1: Shift letters to the right
shifted = word[-n:] + word[:-n]

# Step 2: Shift letters forward in the alphabet
encrypted = ""
for letter in shifted:
    position = ord(letter) - ord('A')  # Turn letter into a number (0–25)
    new_position = (position + n) % 26
    new_letter = chr(new_position + ord('A'))
    encrypted += new_letter

print("Output:", encrypted)
