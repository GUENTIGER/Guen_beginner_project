""" Sort a list in ascending order (thứ tự tăng dần)
return a new sorted list
this function should be recursive(đệ quy)
Devide: Find the midpoint of the list and divide into sublists
Conquer:Recursively call mergesort on the sublists created in previous step
Combine:Merge the sorted sublists(danh sách con) created in previous step

Takes 0 (n log n) time
"""
from re import L
from turtle import left, right


def mergesort(list):
  if len(list) <= 1:
    return list
  left_half, right_half = split(list) 
  left = mergesort(left_half) 
  right = mergesort(right_half)
  
  return merge(left, right)

def split(list):
  """
  Devide the unsorted list at midpoint  into sublists  
  Return two sublists left and right
  
  Takes Overral 0(log n) time
  """
  mid = len(list) // 2 # get the midpoint of the list by the way devide the list at midpoint
  left = list[:mid] 
  right = list[mid:]
  
  return left, right
def merge(left, right):
  """
  Merge the two arrays, sorted them in the process
  
  Return a new marge sorted array
  
  Run in overall 0(log n) time
  """
  l = [] # create a new list
  i = 0
  j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i]) 
      i += 1
    else:
      l.append(right[j]) 
      j += 1
  while i < len(left):
    l.append(left[i])
    i += 1
  while j < len(right):
    l.append(right[j])
    j += 1
  return l

def verify_sorted(list):
  """
  Verify if the list is sorted
  """
  n = len(list)
  if n == 0 or n == 1:
    return True
  return list[0] < list[1] and verify_sorted(list[1:])

arrs = [38,27,43,3,9,82,10]
l = mergesort(arrs)
print(verify_sorted(arrs))
print(verify_sorted(l))

""" arrs = [38,27,43,3,9,82,10]   # test case
l = mergesort(arrs) # call the function and pass the argument
print(l)
      """


    
    

     
      
    
    
    


  
