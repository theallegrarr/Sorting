# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    result=[] 
    i,j=0,0
    while i<len(arrA) and j<len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1

    merged_arr.extend(arrA[i:])
    merged_arr.extend(arrB[j:])

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left_sequence = merge_sort(arr[:mid])
    right_sequence = merge_sort(arr[mid:])

    return merge(left_sequence, right_sequence)


print(merge_sort([6,3,4,5,1,2,7,8,9]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
