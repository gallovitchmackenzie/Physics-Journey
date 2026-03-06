# POTD 19 skel
# Author: Mackenzie Gallovitch
# Date: 5 March 2026
# Description: Sieve Program

import sys

def get_factors(n):
    """ Return a dictionary with the integers from 2 to N (inclusive) as keys.
    The value associated with a key k is a list of the positive integer factors
    (divisors) of that number, in ascending order.
    Precondition: N is an integer >= 2 """
    factor_dict = {}
    
    for i in range(2, n + 1):
        factor_dict[i] = [1]
        
        for potential_factor in range(2, n + 1):
            
            if i % potential_factor == 0:
                factor_dict[i].append(potential_factor)
    
    return(factor_dict)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        N = int(sys.argv[1])
        key = int(sys.argv[2])
        
        results = get_factors(N)
        
        print(results.get(key))
        
    else:
       N = sys.argv[1]
       
       results = get_factors(N)
       
       for i in range(2, N + 1):
           print(i, ": ", results.get(i), sep="")
        

    