def multiples_of_10(start, end):
    for i in range(start, end + 1):
        if i % 10 == 0:
            print(i)
# Input from user
start = int(input("Enter the starting value of the interval: "))
end = int(input("Enter the ending value of the interval: "))
print(f"Multiples of 10 between {start} and {end}:")
multiples_of_10(start, end)
