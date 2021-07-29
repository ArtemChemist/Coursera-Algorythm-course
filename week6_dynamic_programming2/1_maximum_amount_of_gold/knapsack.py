# Uses python3
import sys
import numpy as np

def optimal_weight(W, w):
    w = [0]+w[:]
    sln = np.full((len(w),W+1), 0, dtype = int)
    for row in range (1,len(w)):
        for clmn in range (1, W+1):
            #print(sln)
            sln[row,clmn] = sln[row-1, clmn]
            if (w[row]<=clmn):
                no_add = sln[row, clmn]
                add = sln[row-1, clmn-w[row]]+w[row]
                sln[row,clmn] = max (add, no_add )
                #print(sln)
                #print('------------')

    return sln[-1,-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
