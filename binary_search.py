


def binary_search(list, target): # binary search algorithm
  """ 
  Returns the index position of the target if found, else return None
   """
  first = 0  
  last = len(list) - 1 

  while first <= last: 
    midpoint = (first + last)//2 

    if list [midpoint] == target: 
      return midpoint

    elif list[midpoint] < target: 
      first = midpoint + 1
    else: # excuted the else then return
      last = midpoint - 1

  return None

def verify(index):
  if index is not None:
    print("Target found in index at", index)
  else:
    print("Target is not found")

# get the variable numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,12)
verify(result)

result = binary_search(numbers,12)
print(result)






