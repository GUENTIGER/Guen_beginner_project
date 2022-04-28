import numbers
from unittest import result


def recusive_binary_search(list, target): 
  if len(list) == 0:
      return False
  else:
    midpoint = (len(list))//2 # get the midpoint of the list

    if list[midpoint] == target: 
      return True
    else:
      if list[midpoint] < target: 
        return recusive_binary_search(list[midpoint+1:], target) # return the recusive_binary_search function with midpoit + 1
      else:
        return recusive_binary_search(list[:midpoint],target) # return the recusive_binary_search function with midpoit - 1
def cin(result):
  print("Target found in index at: ", result)
  
numbers = [1,2,3,4,5,6,7,8,9]

result = recusive_binary_search(numbers,12)
cin(result)

result = recusive_binary_search(numbers, 12)
print(result)
      

