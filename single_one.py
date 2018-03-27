# Given an array of integers, every element appears twice except for one.
# Implement a program that will print that single one.

# Example: [1,1,2,2,3,3,4,5,5,6,6,7,7] - 4 would be the odd man out

# Note:
# Your algorithm should have a linear runtime complexity.

example = [1,1,2,2,3,3,4,5,5,6,6,7,7]
def unique(array):
    array.sort()
    for i in range(0,len(array),+2):
        if array[i] != array[i+1]: return array[i]
print(unique(example), 'final')
