print("\nWant to display all the number in between two numbers?\n")
first_number = int(input("Please enter your first number: "))
second_number = int(input("Please enter your second number: "))

print(" ")

start = min(first_number, second_number) + 1
end = max(first_number, second_number)

for number in range(start, end):
    print(number)