def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series
n = int(input("Enter the upper limit (n): "))
fib_series = fibonacci_series(n)
print(f"Fibonacci series up to {n} is: {fib_series}")
