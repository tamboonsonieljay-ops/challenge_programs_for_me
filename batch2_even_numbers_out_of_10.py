print("\nWant to know how many even numbers are in your list?\n")

even_count = 0

for i in range(1,11):
    number = int(input(f"Please enter number {i}: "))
    if number % 2 == 0:
        even_count += 1

print("\n------------------------------------------------------------")
print(f"\nThe number of even numbers in your list: {even_count}")
print("\n------------------------------------------------------------")