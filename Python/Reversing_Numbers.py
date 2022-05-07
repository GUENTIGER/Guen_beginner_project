# """ Alter the calculator project so that the order
# of the numbers doesn’t matter. There are a few ways to get the
# same result; one way is to ask the user if they’d like to reverse the
# placement of the numbers """

def Reversing(n):
    d = 0
    rec = 0
    while(n > 0):
      d = n % 10
      n = int(n/10)
      rec = rec *10 + d

    return rec

ins = input("Enter a number: ")
ar = Reversing(int(ins))
print("Before reversing: {}".format(ins))
print("After reversing: {}".format(ar))
