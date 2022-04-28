def bublesort(arr):
    for i in range(len(arr)):
      for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
          temp = arr[j] #  delcare temp variable to store the value 
          arr[j] = arr[j+1]
          arr[j+1] = temp # get the swaped value

arr = [64, 34, 25, 12, 22, 11, 90] # unsorted array
bublesort(arr) # arguemnt is the array
print("Sorted array: \n",arr) 