
import numbers
from random import randint
from IPython.display import clear_output

guessed = False
number = randint(0,10)
guesses = 0
while not guessed:
  ans = input("Try to guess the number from 0 to 10: ")
  #tab to indent
  guesses += 1
  clear_output() #clear the outpuyt
  
  if int(ans) == number:
          print("Congrat!!! You guess is correctly")
          #tab twice to indent twice
          print("It tooks you {} guess".format(guesses))
          break #break to out the condition
        
  elif int(ans) < number:
          print("The number is higher than you guess...")
  elif int(ans) > number:
          print("The number is lower than you guess...")
  
          
            
    
  
    
      
    
    
      
        
    
      
    


    
      
        
          
    
      
        
          
    
  
  

    
    
      
        
          
            
            
    
  
        
        
  
      
      
        
        
    
        
    
  
  
    
