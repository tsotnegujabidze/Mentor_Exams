# 8) Find the Kth Smallest Element in an Array

# Write a function that finds the k-th smallest element in an unsorted array.

def kth_smallest(array, k):
    sorted1 = sorted(array) # sort array 
    return sorted1[k-1] # return k-1 since indexing starts from 0

print(kth_smallest([3, 2, 1, 5, 6, 4], 4))

