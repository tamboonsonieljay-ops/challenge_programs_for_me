print("\nWant to know which number is smaller?")

first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

print("\n------------------------------")

print("Comparing the two numbers...")
if first_number < second_number:
    print(f"\nThe first number ({first_number}) is smaller.")
elif second_number < first_number:
    print(f"\nThe second number ({second_number}) is smaller.")
else:
    print("\nOh no! Both numbers are equal, kindly enter different numbers next time.")

print("------------------------------")