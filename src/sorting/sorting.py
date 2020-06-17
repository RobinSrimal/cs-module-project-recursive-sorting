# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    counter = 0


    while len(arrA) > 0 or len(arrB) > 0 :

        if len(arrA) == 0:

            for number in arrB:

                merged_arr[counter] = number

                counter += 1

            return merged_arr

        if len(arrB) == 0:

            for number in arrA:

                merged_arr[counter] = number

                counter += 1

            return merged_arr

        if arrA[0] <= arrB[0]:

            number = arrA.pop(0)

            merged_arr[counter] = number

            counter += 1

        else: 

            number = arrB.pop(0)

            merged_arr[counter] = number

            counter += 1

# TO-DO: implement the Merge Sort function below recursively

[1,5,2,7,6,8]

def merge_sort(arr):
    # Your code here


    if len(arr) > 1:

        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        return merge(merge_sort(left), merge_sort(right))

    else:

        return arr






# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here

    
    a = start
    b = mid

    while a < mid or b <= end:











def merge_sort_in_place(arr, l, r):
    # Your code here

    if len(arr) > 1:

        mid = (r - l)//2

        left = arr[l:mid]
        right = arr[mid:r]


        return merge_in_place

    
    else: 
        return arr



    

