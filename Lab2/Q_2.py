import cmath
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
root1, root2 = solve_quadratic(a, b, c)
print(f"The solutions are: {root1} and {root2}")
