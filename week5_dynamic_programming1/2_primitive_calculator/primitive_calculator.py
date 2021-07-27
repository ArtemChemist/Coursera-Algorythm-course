# Uses python3
import sys

def optimal_sequence(n):
    lst_master = [0,1,1,1]
    lst_min =[]
    for i in range(4,n+1):
        if i%3 == 0:
            lst_min.append(lst_master[i//3]+1)
        if i%2 == 0:
            lst_min.append(lst_master[i//2]+1)
        lst_min.append(lst_master[i-1]+1)
        lst_master.append(min(lst_min))
        lst_min.clear()      
#   print(lst_master[-1])
    dict_min={}
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            dict_min[n//3] = lst_master[n//3]
        if n % 2 == 0:
            dict_min[n//2] = lst_master[n//2]
        dict_min[n-1]  = lst_master[n-1]
        n = min(dict_min, key=dict_min.get)
        dict_min.clear()
    return reversed(sequence)

#inpt = sys.stdin.read()
inpt = input()
n = int(inpt)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
