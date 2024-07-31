def is_buzz_number(n):
    return (n % 7 == 0) or (str(n)[-1] == '7')
numbers = [7, 14, 27, 37, 49, 50]
for num in numbers:
    if is_buzz_number(num):
        print(f"{num} is a Buzz number.")
    else:
        print(f"{num} is not a Buzz number.")
