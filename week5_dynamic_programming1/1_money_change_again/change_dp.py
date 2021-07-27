# Uses python3
import sys
import random

def get_change(m):
    lst_m = [0,1,2,1,1]
    lst_min = []
    for i in range (5,m+1):
        lst_min.append(lst_m[i-3]+1)        
        lst_min.append(lst_m[i-4]+1)
        lst_min.append(lst_m[i-1]+1)
        lst_m.append(min(lst_min))
        lst_min.clear()           
    return lst_m[m]

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m = int(input())
    #m = random.randint(1,1000)
    #Result = get_change(m)
    #print(m, Result)
    print(get_change(m))
