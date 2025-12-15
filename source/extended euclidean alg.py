def extended_eucl(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return (a, x0, y0)


a = int(input("Введите число: "))
b = int(input("Введите число: "))
if b > a:
    a, b = b, a
gcd, x, y = extended_eucl(a, b)
print(f"НОД({a}, {b}) = {gcd}")
print(f"Коэффициенты: {a}*{x} + {b}*{y} = {a * x + b * y}")
