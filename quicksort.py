def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
          i += 1
          temp = arr[i]
          arr[i] = arr[j]
          arr[j] = temp

    swap = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = swap
    return i+1
def Quicksort(arr,low,high):
    if low < high:
        pindex = partition(arr,low,high)
        Quicksort(arr,low,pindex-1)
        Quicksort(arr,pindex+1,high)

arr =[10,80,30,90,40,50,70,100,5,89,1000]   
size = len(arr)
Quicksort(arr,0,size-1)
print("Sorted array: \n",arr) 