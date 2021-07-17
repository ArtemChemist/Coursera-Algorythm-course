def PairwiseProduct(n: int, numbers):
    result = 0
    for i in numbers:
        for k in numbers:
            if (i != k and i*k>result):
                result = i*k
    return result

n_str = input()

try:
    n = int(n_str)     
except ValueError:
    print('That was not a number')
    
str_list = input()

try:
    lst_str = str_list.split()
    map_object = map(int, lst_str)
    lst_int = list(map_object)
except ValueError:
    print('That was not a number')
    
print (PairwiseProduct(n, lst_int))


