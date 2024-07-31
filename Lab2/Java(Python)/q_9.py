def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    
    return median
numbers = list(map(float, input("Enter the numbers separated by spaces: ").split()))
median = find_median(numbers)
print(f"The median of the given numbers is {median}.")
