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
    for i in numbers:
        if (i>largest):
            largest = i
    second_largest = 0
    numbers.remove(largest)
    for k in numbers:
        if (k>second_largest):
            second_largest  = k
    return second_largest *largest  