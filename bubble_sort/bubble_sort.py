def bubble_sort(arr):
    # TODO: Implement bubble sort
    n = len(arr)    #no. of elements in the array
    for i in range(n):      #loop continues for n times
        for j in range(0,n-i-1):    #enables us to compare unsorted elements only
            if arr[j]>arr[j+1]: #current index is greater than index after
                arr[j], arr[j+1] = arr[j+1], arr[j]     #swaps the two elements
    return arr

input_list = [20,9,17,12,44]
print(bubble_sort(input_list.copy()))
