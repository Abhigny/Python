def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
def compute_e(n_terms):
    e_value = 1
    for i in range(1, n_terms):
        e_value += 1 / factorial(i)
    return e_value
n_terms = int(input("Enter the number of terms to compute e: "))
e_value = compute_e(n_terms)
print(f"The approximate value of Euler's number e using {n_terms} terms is {e_value}.")
