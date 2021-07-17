def PairwiseProduct(nums: list):
    numbers = nums[:]
    result = 0
    for i in numbers:
        ind_i = numbers.index(i)
        numbers_2 = numbers[:]
        numbers_2.pop(ind_i)
        for k in numbers_2:
            if (i*k>result):
                result = i*k
    return result

def PairwiseProductFast(nums: list):
    numbers = nums[:]
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