import Assign2_Functions

n_str = input()

try:
    n = int(n_str)     
except ValueError:
    print('That was not a number x')
    
str_list = input()

try:
    lst_str = str_list.split()
    map_object = map(int, lst_str)
    lst_int = list(map_object)
except ValueError:
    print('That was not a number y')
    
print (Assign2_Functions.PairwiseProductFast(lst_int))


