print("\nWant to know how many odd numbers are in your list?\n")

odd_count = 0

for i in range(1,11):
    number = int(input(f"Please enter number {i}: "))
    if number % 2 != 0:
        odd_count += 1

print("\n------------------------------------------------------------")
print(f"\nThe number of odd numbers in your list: {odd_count}")
print("\n------------------------------------------------------------")