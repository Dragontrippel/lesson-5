
print("===== ARMSTRONG NUMBER CHECKER =====")

number = input("Enter a number: ")
digit_count = len(number)
print(f"Number of digits: {digit_count}")

total = 0
5

for digit in number:
    power = int(digit) ** digit_count
    print(f"{digit} to the power {digit_count} = {power}")
    total += power

print(f"Sum of the powers = {total}")

if total == int(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
