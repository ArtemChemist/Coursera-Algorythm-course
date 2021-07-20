import sys
from functools import cmp_to_key

def compare(a: int, b:int):
    #Make up numbers by concatenating the input ints two ways 
    a_b = int(str(a)+str(b))
    b_a = int(str(b)+str(a))   
    #Return the difference: negative if they should be sorted one way, positive if another
    return (a_b-b_a)

def largest_number(a):
    #Sort input array using custom comparator
    b = sorted(a, key=cmp_to_key(compare), reverse = True)
    
    #Make a string out of the sorted array
    res_str = ''
    for i in b:
        res_str = res_str + str(i)
    #Cast the string back to int
    return int(res_str)

if __name__ == '__main__':
    #inpt = input()
    inpt = sys.stdin.read()
    data = list(map(int, inpt.split()))
    a = data[1:]
    print(largest_number(a))
    
