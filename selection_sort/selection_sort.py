def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    for i in range(n):  #loops through each element
        min_idx = i     #assumes current element is the smallest
        for j in range(i+1, n): #checks for smaller element in each index
            if arr[j] < arr[min_idx]: #if found
                min_idx = j         #that element becomes the smallest
        arr[i], arr[min_idx] = arr[min_idx], arr[i]    #swaps the current index with the smaller one
    return arr

input_list = [33,10,88,54,20]
print(selection_sort(input_list.copy()))