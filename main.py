import math

num = 34.4
ceil_num = math.ceil(num)
floor_num = math.floor(num)
print(f"Ceil of {num}: {ceil_num}")
print(f"Floor of {num}: {floor_num}")

num2 = -96
abs_num2 = math.fabs(num2)
print(f"Absolute value of {num2}: {abs_num2}")

a = 24
b = 6
gdc_a_b = math.gcd(a,b)
print(f"GDC of {a} and {b} is:{gdc_a_b}")

print(math.copysign(4 , -5))
print(math.copysign(-12 , -30))
print(math.copysign(56 , 23))
print(math.copysign(-100 , 80))