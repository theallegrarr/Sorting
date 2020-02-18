# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


print(selection_sort([4,2,5,7]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    freq = {}
    if all(i >= 0 for i in arr):
        for n in arr:
            if n not in freq and n > maximum:
                    freq[n] = 0
            freq[n] += 1

        newArray = []
        for n, count in sorted(freq.items()):
            for i in range(count):
                newArray.append(n)

        return newArray
    else:
        return("Error, negative numbers not allowed in Count Sort")

print(count_sort([1, 1, 2, 5, 8, 4, 2, 9, 6, 0, 3, 7]))