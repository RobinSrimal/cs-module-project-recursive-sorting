# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here

    if len(arr) == 0:

        return -1

    split_point = start + int((end - start)/2)

    if arr[split_point] == target:

        return split_point

    elif arr[split_point] < target:

        start = start + split_point + 1

    else:

        end = end - split_point - 1 

    return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    start = 0 

    end = len(arr) - 1


    if arr[0] < arr[-1]:

        binary_search(arr, target, start, end)


    else:

        binary_search(arr.reverse(), target, start, end)







