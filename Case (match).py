# problem 1
def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Not valid"
a = int(input("Enter day: "))
print(day_of_week(a))



# problem 6
def unit_of_length(unit, length):
    match unit:
        case 1:
            print("From decimeter to meter: ", length / 10)
        case 2:
            print("From kilometer to meter: ", length * 1000)
        case 3:
            print("Meter remains same: ", length)
        case 4:
            print("From millimeter to meter: ", length / 1000)
        case 5:
            print("From centimeter to meter: ", length / 100)
        case _:
            print("Enter a valid length")

unit = int(input("Enter an unit: "))
length = float(input("Enter a length: "))
print(unit_of_length(unit, length))



# problem 11
