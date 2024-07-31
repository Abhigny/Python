def reverse_number(n):
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n // 10
    return reversed_number
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}.")
