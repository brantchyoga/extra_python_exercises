# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"

another_string = "Let's do a coding challenge"
def splits(str):
    str = str.split(' ')
    print(str)
    for i in range(len(str)):
        str[i] = str[i][::-1]
    return ' '.join(str)
print(splits(another_string))
