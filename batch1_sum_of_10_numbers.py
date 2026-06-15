print("\nWant to know the total sum of your numbers?\n")

for i in range(1,11):
    number = int(input(f"Please enter number {i}: "))
    if i == 1:
        total_sum = number
    else:
        total_sum += number

print("\n------------------------------------------------------------")
print("\nYour total sum is:", total_sum)
print("\n------------------------------------------------------------")