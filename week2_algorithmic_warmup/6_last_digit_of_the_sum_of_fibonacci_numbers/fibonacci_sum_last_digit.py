def fib_sum_lastdgt_naive(n):
    Period_sum = 0
    for i in range(0, n+1):
        Period_sum = Period_sum + fib(i)
    return Period_sum%10

def PisanoLength(m):
    latest_two= (0, 1)
    for i in range(0, m**2):
        new_second = (latest_two[0] + latest_two[1]) % m
        latest_two = (latest_two[1], new_second)
        if (latest_two == (0,1)):
            return i + 1

def fib(n):
    if (n == 0):
        return 0
    F = []
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-1]+F[i-2])
    return F[-1]

def fib_sum_lastdgt(n):
    PL = PisanoLength(10)
    Period_sum = 0
    for i in range(0, PL):
        Period_sum = Period_sum + fib(i)%10
    Number_of_periods = n//PL
    Stub_length = n%PL
    Sum_of_stub = 0
    for i in range(0,Stub_length+1):
        Sum_of_stub = Sum_of_stub + fib(i)%10

    return (Period_sum * Number_of_periods + Sum_of_stub)%10

if __name__ == '__main__':
    n = int(input())
    print(fib_sum_lastdgt(n))
