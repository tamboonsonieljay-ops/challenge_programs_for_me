print("\nWant to know if your numbers are not equal?")

first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

print("\n------------------------------")

print("Comparing the two numbers...")
if first_number != second_number:
    print(f"\nYes! Both numbers are not equal ({first_number}, {second_number}).")
else:
    print(f"\nNope! The numbers are the same.")

print("------------------------------")