import math
sin_60 = math.sin(math.radians(60))
cos_pi = math.cos(math.pi)
sin_value = math.sin(0.8660254037844386)
try:
    tan_90 = math.tan(math.radians(90))
except ValueError:
    tan_90 = 'undefined'
print(f"sin(60 degrees) is: {sin_60}")
print(f"cos(pi) is: {cos_pi}")
print(f"sin(0.8660254037844386) is: {sin_value}")
print(f"tan(90 degrees) is: {tan_90}")
