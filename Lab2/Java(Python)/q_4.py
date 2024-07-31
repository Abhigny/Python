def sum_of_natural_numbers(n):
    return n * (n + 1) / 2
n = int(input("Enter the range: "))
sum_natural = sum_of_natural_numbers(n)
print(f"The sum of natural numbers up to {n} is {sum_natural}.")
