"""
        An array is data structrue that a collection
        of items stored at contiguous memory locations.
"""


arr = [1, 2, 3, 4, 5, 6]
print(len(arr))  # length of array
# accessing the last elemet <O(1)>
print(arr[len(arr) - 1])

arr.insert(5, 34)
print(arr)

# del arr[3]
print(arr)

# merging two arrays

arr2 = [7, 9, 10, 8]

merged_array = arr + arr2
print(merged_array)

# sorting element in array
merged_array.sort()
print(merged_array)

def calc_sum_of_elements(merged_array):
    total = arr