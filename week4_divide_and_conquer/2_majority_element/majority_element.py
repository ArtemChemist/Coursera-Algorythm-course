# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    counter = 1
    for i in range(1, right):
        if (  a[i] == a[i-1]  ):
            counter +=1
            if (counter>right/2):
                return 1
        else:
            counter = 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n))
