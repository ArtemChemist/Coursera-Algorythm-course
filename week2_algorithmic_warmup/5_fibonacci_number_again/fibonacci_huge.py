# Uses python3
import sys

def PisanoLength(m):
    latest_two= (0, 1)
    for i in range(0, m**2):
        new_second = (latest_two[0] + latest_two[1]) % m
        latest_two = (latest_two[1], new_second)
        if (latest_two == (0,1)):
            return i + 1

def calc_fib(n):
    if (n == 0):
        return 0
    F = []
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[-1]

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    remainder_fib_number = n%PisanoLength(m)
    fib = calc_fib(remainder_fib_number)
    return fib % m

if __name__ == "__main__":
    inpt = input()
    a, b = map(int, inpt.split())
    print(get_fibonacci_huge(a, b))
