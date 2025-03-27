from math import pi


def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


def degree_to_radian(degree):
    return degree * (pi / 180)


single_step=lambda n,x:((-1)**n)*(x**(2*n+1))/factorial(2*n+1)


def sine_x(x_degrees, n):
    x = degree_to_radian(x_degrees)
    result = 0
    for i in range(n):
        result += single_step(i, x)
    return result


harmonic_sum = 0


def harmonic(n):
    global harmonic_sum
    if n == 1:
        harmonic_sum = 1
        return harmonic_sum
    harmonic_sum = harmonic(n - 1) + (1 / n)
    return harmonic_sum


if __name__ == "__main__":
    # 1
    print("Factorial (5!):", factorial(5))
    x_degrees = float(input("Please enter the degree of x: "))
    n = int(input("Please enter the numbers of terms n: "))

    # 2
    print("sin(30):", sine_x(x_degrees,n))

    # 3
    print("H_5:", harmonic(5))
