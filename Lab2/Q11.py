def sum_of_digits(n):
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)
    return sum_digits
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")
