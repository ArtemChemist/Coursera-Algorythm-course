# Uses python3
import numpy as np

def edit_distance(s, t):
    sln = np.ndarray(shape=(len(s)+1,len(t)+1), dtype = int)
    sln[0,0]=0
    for i in range (1, len(t)+1):
        sln[0,i] = i
    for i in range (1, len(s)+1):
        sln[i,0] = i
    for strng in range (1,len(s)+1):
        for clmn in range (1, len(t)+1):
            #print(sln)
            if (s[strng-1]==t[clmn-1]):
                sln[strng,clmn] = sln[strng-1, clmn-1]
            else:
                sln[strng,clmn] = min(sln[strng-1, clmn-1], sln[strng-1, clmn], sln[strng, clmn-1])+1
            #print(sln)
            #print('------------')

    return sln[len(s),len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
