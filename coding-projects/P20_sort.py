# POTD 20 skel
# Author: Mackenzie Gallovitch
# Date: 5 March 2026
# Description: Sorting Program

import sys

def isort(numbers, start, end):
    """ Sort the sublist numbers[start:end] in-place using insertion sort.
    Does not return anything. Precondition: numbers[start:end] contains
    only numbers and has length >= 1. """
    
    for i in range(start + 1, end):
        current_val = numbers[i]
        position = i
        
        while position > start and numbers[position - 1] > current_val:
            numbers[position] = numbers[position - 1]
            position -= position - (position - 1)
            
            numbers[position] = current_val


def swap(lst, i1, i2):
    """ Swap the values in the list `lst` at indices i1 and i2. Operates
    in-place and returns nothing. All indices other than i1 and i2 are left unchanged. 
    Preconditions: 0 <= i1, i2, < len(lst) """
    
    lst[i1], lst[i2] = lst[i2], lst[i1]
    
def min_index(numbers, start, end):
    """ Return the index into numbers of the smallest value in
    numbers[start:end]. If multiple instances of the smallest value exist,
    return the earliest index. Precondition: numbers[start:end] contains only
    numbers and has length >= 1. """
    
    small_idx = start
    
    for i in range(start + 1, end):
        if numbers[i] < numbers[small_idx]:
            small_idx = i
            
    return(small_idx)

if __name__ == "__main__":
    
    data = []
    
    for item in sys.argv[1:]:
        number = int(item)
        data.append(number)
        
    isort(data, 0, len(data))
    
    print(data)
    
    