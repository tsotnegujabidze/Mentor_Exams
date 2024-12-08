# 4) Generate Pascal’s Triangle Up to a Given Row

# Write a function to generate Pascal's Triangle up to the specified number of rows.

def pascal(n):
    triangle = [] # array which will store final information 

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            first = [1]
            second = triangle[i-1]

            for k in range(1, i):
                first.append(second[k-1] + second[k])

            first.append(1)
            triangle.append(first)
    return triangle

print(pascal(0))