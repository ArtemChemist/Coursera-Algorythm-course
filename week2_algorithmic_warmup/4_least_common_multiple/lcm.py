def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a%b)

def lcm(a, b):
    if (a == 0 or b==0):
        return 0
    if (a>b):
        return a*b//gcd(a,b)
    else: 
        return a*b//gcd(b,a)

if __name__ == "__main__":
    inpt = input()
    a, b = map(int, inpt.split())
    print(lcm(a, b))