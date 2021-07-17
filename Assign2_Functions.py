def PairwiseProduct(numbers):
    result = 0
    for i in numbers:
        for k in numbers:
            if (i != k and i*k>result):
                result = i*k
    return result

def PairwiseProductFast(numbers):
    largest = 0
    largest_ind = 0
    for i in numbers:
        if (i>largest):
            largest = i
            largest_ind = list.index(i)
    second_largest = 0
    for k in numbers:
        if (k>second_largest and list.index(k) != largest_ind):
            second_largest  = i
    return second_largest *largest  