# Reverse Strings in a Sentence

# Given a string, implement a program that will reverse the order of the characters
# in each word within a sentence while still preserving whitespaces and initial word order.

# Example:
# Input: "Let's do a coding challenge"
# Output: "s'teL od a gniedoc egnellahc"

another_string = "Let's do a coding challenge"
def reverse_words(str):
    str = str.split(' ')
    for i in range(len(str)):
        str[i] = str[i][::-1]
    return ' '.join(str)
print(reverse_words(another_string))
