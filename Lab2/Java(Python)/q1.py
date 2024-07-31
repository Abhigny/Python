number = int(input("Take a number : "))
lastDigit = number%10
if(lastDigit == 7 or number%7 == 0):
    print(f"{number} is a Buzz Number.")
else:
    print(f"{number} is not a Buzz Number.")
