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

# def leap_year(year):
#     year = int(year)
#     if year%400==0:
#         return f'is a leap year {year}'
#     elif year%100==0:
#         return f'not a leap year {year}'
#     elif year%4==0:
#         return f'is a leap year {year}'
#     else:
#         return f'not a leap year {year}'
# year = input('enter year')
# print(leap_year(year))
hamming_string = 'Find the distance!'
def hamming(string1,string2):
    # string becomes uppercase, splits on spaces,joins with spaces,then splits on every character
    string1 = list(''.join(string1.upper().split(' ')))
    string2 = list(''.join(string2.upper().split(' ')))
    maxs = len(string1) if len(string1)>len(string2) else len(string2)
    mins = len(string1) if len(string1)<len(string2) else len(string2)
    dist = 0
    for i in range(mins):
        dist = dist + 1 if string1[i]!=string2[i] else dist
    # dist = dist+(maxs-mins) if ((dist+(maxs-mins))<=maxs)else dist = maxs
    #Why can't I do the commented code
    if ((dist+(maxs-mins))<=maxs):
        dist += (maxs-mins)
    else:
        dist = maxs
    return(dist)
print("I'm designing the hamming function to ignore spaces and case sensitivity")
string_to_compare = input('What is the Hamming distance? Quote"Find the distance!"')
print(hamming(hamming_string,string_to_compare), '-Is the hamming distance!')
