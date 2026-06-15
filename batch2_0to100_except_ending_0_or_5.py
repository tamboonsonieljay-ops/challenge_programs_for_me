print("\nWant to display all the numbers starting from 0 to 100 except numbers ending in 0 or 5?\n")
print("Say no more! Here they are:\n")
number = 1

while number < 100:
    if number % 10 != 0 and number % 10 != 5:
        print(number)
    number += 1

print("\n.....phew, that was a close one ;)")