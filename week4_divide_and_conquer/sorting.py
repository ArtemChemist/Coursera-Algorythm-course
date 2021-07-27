# Uses python3
import sys
import random

def partition3(a, l, r):
    #Pivot
    x = a[l]
    #Index of the last element that is less than pivot that we met so far
    j = l
    #Number of elements equal to pivot we met so far
    k = 0
    #Go from l to r one by one
    for i in range(l + 1, r + 1):
        #Let's call the element right in front of the sequence of the equal ones the 'gate'
 
        if a[i] < x:
            # Sawap the one under consideration with the gate
            a[i], a[j+k+1] = a[j+k+1], a[i]
            #Increase index of the last one < pivot. Temporarily it points to the one that is actually == pivot
            j += 1
            #Swap it with the one waiting in the gate
            a[j+k], a[j] = a[j], a[j+k]

        # If the element in the gate is eqaul to pivot
        elif a[i] == x:
            #Bump up the counter
            k += 1
            # Sawap the one under consideration with the gate
            a[i], a[j+k] = a[j+k], a[i]

         #If the element is larger than pivot - do nothing.
    a[l], a[j] = a[j], a[l]
    result = j, j+k
    return result 


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = l
    #k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, n + 1, r);


if __name__ == '__main__':
    inpt = sys.stdin.read()
    #inpt = input()
    n, *a = list(map(int, inpt.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
