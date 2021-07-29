# Uses python3
import numpy as np

def sum(a:int, b: int):
    return a+b
def dif (a:int, b:int):
    return a-b
def prod (a:int, b:int):
    return a*b

def parse (data:str):
    ns = []
    os = {}
    counter = 0
    for i in data:
        try: 
            ns.append(int(i))
        except:
            if i == '-':
                os[counter] = dif
            elif i == '+':
                os[counter] = sum
            elif i == '*':
                os[counter] = prod
            counter +=1
    return ns, os
    

def get_maximum_value(dataset:str):
    numbers, ops = parse(dataset)
    size = len(numbers)
           
    Min = np.full((size,size), 0, dtype = int)
    for row in range (0, size):
        for clmn in range (0, size):
            if (row == clmn):
                Min[row,clmn] = numbers[row]
    
    Max = np.full((size,size), 0, dtype = int)
    Max[:] = Min[:]
    values = []
 
    for a in range (1, size):
        for b in range (0, size-a):
            row = b
            clmn = a+b
            for k in range (row, clmn):
                values.append(  ops[k](  Min[row,k], Min[k+1, clmn])   )
                values.append(  ops[k](  Max[row,k], Min[k+1, clmn])   )
                values.append(  ops[k](  Max[row,k], Max[k+1, clmn])   )
                values.append(  ops[k](  Min[row,k], Max[k+1, clmn])   )
                
            Min[row, clmn] = min(values)
            Max[row, clmn] = max(values)

            #print(Min)
            #print('----------------------')
            #print(Max)
            #print('=======================')
            values.clear()
    return Max[0,-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
