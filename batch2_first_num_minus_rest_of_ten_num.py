print("\nWant to display the result of the first number minus the rest of the ten numbers?\n")

first_number = int(input("Please enter the first number: "))

for i in range(2, 11):
    number = int(input(f"Please enter number {i}: "))
    first_number -= number

print(f"\nThe result is: {first_number}")
