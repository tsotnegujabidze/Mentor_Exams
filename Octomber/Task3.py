# 3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array.

def task3(numbers):
    whatever = 0
    whatever2 = None # ცვლადი, რომელსაც დააბრუნებს ფუნქცია
    for i in range(len(numbers)):
        if whatever == 0:
            whatever2 = numbers[i]
        if numbers[i] == whatever2:
            whatever += 1
        else:
            whatever -= 1
    return whatever2

print(task3([3, 2, 3]))
print(task3([2, 2, 1, 1, 2]))
print(task3([1, 1, 1, 1, 1]))
