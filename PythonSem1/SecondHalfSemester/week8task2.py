def simple_recursive_power(x, n):
    if n == 1:
        return x
    if n % 2 == 1:
        return simple_recursive_power(x, n - 1) * x
    return simple_recursive_power(x,n//2) ** 2

x = 3
n = 10000
print(simple_recursive_power(x,n))