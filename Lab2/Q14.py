def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def factorial_series(terms):
    series = []
    for i in range(1, terms + 1):
        series.append(factorial(i))
    return series
n = int(input("Enter the number of terms: "))
series = factorial_series(n)
print(f"The first {n} terms of the factorial series are: {series}")
