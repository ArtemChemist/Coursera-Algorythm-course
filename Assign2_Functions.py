def PairwiseProduct(numbers: list):
    result = 0
    for i in numbers:
        ind_i = numbers.index(i)
        for k in numbers:
            ind_k = numbers.index(k)
            if (ind_i != ind_k and i*k>result):
                result = i*k
    return result

def PairwiseProductFast(numbers: list):
    largest = 0
    largest_ind = 0
    for i in numbers:
        if (i>largest):
            largest = i
            largest_ind = numbers.index(largest)
    second_largest = 0
    for k in numbers:
        if (k>second_largest and numbers.index(k) != largest_ind):
            second_largest  = k
    return second_largest *largest  