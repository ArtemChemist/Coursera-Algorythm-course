import sys

def compute_min_refills(distance, tank, stops):
    #compile the list of the distances between the refill points
    difs = []
    difs.append(stops[0])
    for i in range(0, len(stops)-1):
        difs.append(stops[i+1]-stops[i])
    difs.append(distance-stops[-1])
    
    #check if there is a stretch without gas too long for my tank
    for dif in difs:
        if (dif>tank):
            return -1
    
    #fill up
    gas_left = tank
    #start driving
    number_of_refills = 0
    for i in range(0, len(difs)-1):
        
        #passing gas station - spent some fuel. 
        gas_left = gas_left - difs[i]
        
        #Is there still enough fuel to go to the next one? If no, refill
        if (gas_left- difs[i+1] <0):
            number_of_refills +=1
            gas_left = tank
    return number_of_refills

if __name__ == '__main__':
    #inpt = input()
    inpt = sys.stdin.read()
    d, m, _, *stops = map(int, inpt.split())
    print(compute_min_refills(d, m, stops))
