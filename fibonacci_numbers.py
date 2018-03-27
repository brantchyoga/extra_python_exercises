# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


def fibonacci(num):
    lists = [0,1]
    for i in range(num-2):
        print(i)
        thing = lists[len(lists) - 2] + (lists[len(lists)-1])
        lists.append(thing)
    return lists
print(fibonacci(10))
