def diff(a, b):
    b_set = set(b)
    result = []
    for something in a:
        if something not in b_set:
            result.append(something)
    return result

print(diff(a=[1,2], b=[1])) # [2]
print(diff(a=[1,2,2,2,3], b=[2,3])) # [1]
print(diff(a=[18, 8, -14], b=[8, -20, -16, -18])) # [18, -14]
print(diff(a=[6, -9, -1], b=[-3, -4, 17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6])) # [-9, -1]
print(diff(a=[-8, -2, -4, 13, 10, -12, -3, 6], b=[-3, 17])) # [-8, -2, -4, 13, 10, -12, 6]