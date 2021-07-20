import sys
def get_optimal_value(capacity, weights, values):
    density = []
    value = 0
    for i in range(0, len(weights)):
        if (weights[i]>0):         
            density.append((i,values[i]/weights[i]))
        
    #sort items by thier value density
    sorted_density = sorted(density, key=lambda tup: tup[1], reverse=True)
    

    #start looking at the items, one by one 
    for item in sorted_density:      
        #find out how much of this item fits in the sack
        fits = 0
        if (capacity >= weights[item[0]]):
            fits = weights[item[0]]
        else:
            fits = capacity
                
        #update capacity and value
        capacity = capacity-fits
        value = value + fits*item[1]
            
        #Stop if the sack is full already
        if (capacity == 0):
            break
    return value


if __name__ == "__main__":
    #inpt = input()
    inpt = sys.stdin.read()
    data = list(map(int, inpt.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
