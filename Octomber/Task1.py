#1.Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.

def task1(numbers):
    whatever = len(numbers) + 1
    whatever2 = whatever * (whatever + 1) // 2
    sum1 = sum(numbers)
    return whatever2 - sum1

print(task1([1, 2, 4, 5]))
print(task1([1]))
print(task1([2, 3, 1, 5]))