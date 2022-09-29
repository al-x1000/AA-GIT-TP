###############################################################
#                                                             #
#               Script to print Primary Number.               #
#                       1 to 100 000                          #
#                                                             #
#              HUELLOU Alexis, TAILLANDER Aliaume             #
#                                                             #
###############################################################

# Based on Python3

#Check if number is primary
def isPrime(n):
  #If 0 and 1 is not prime return false.
  if(n==1 or n==0):
    return False
    
  #Run a loop
  for i in range(2,n):
    #If the number is divisible by i, then n is not a primary number.
    if(n%i==0):
      return False
    
  #Otherwise, n is primary number.
  return True
  

N = 100000;
#Check for every number from 1 to 100000
for i in range(1,N+1):
  #Check if current number is primary
  if(isPrime(i)):
    print(i,end=" ")
