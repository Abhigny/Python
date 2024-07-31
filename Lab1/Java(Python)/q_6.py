def check_positive_negative(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
number = float(input("Enter a number: "))
result = check_positive_negative(number)
print(f"The number {number} is {result}.")
