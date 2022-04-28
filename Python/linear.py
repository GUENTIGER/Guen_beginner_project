# concept linear-search algorithm in Python



def linear_search(list,target):
  """ 
  Return the index position of the target is found, else return None
  """
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None

def verify(index):
  if index is not None:
    print("the target is found at: ", index)
  else:
    print("the target is not found")

numbers = [0,1,2,3,4,5,6,7,8,9,0]
result = linear_search(numbers, 6)
ronin = linear_search(numbers, 14)
verify(result)
verify(ronin)    
      
    

    
    
    
  