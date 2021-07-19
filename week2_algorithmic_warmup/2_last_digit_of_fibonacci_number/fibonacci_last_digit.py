# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    F = []
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        last_digt = (F[i-1]+F[i-2])%10
        F.append(last_digt)
    return F[-1]

if __name__ == '__main__':

    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
