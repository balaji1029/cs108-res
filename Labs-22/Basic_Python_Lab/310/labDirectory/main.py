'''
    Sieve of Eratosthenes
'''

import sys

# read the parameter from command line using sys
n=(int)(sys.argv[1])
# your implementation for printing the list of prime numbers
thisList=[x for x in range(2, n+1)]
newList=[]
primeList=[]
length=len(thisList)
while(length>=1):
  num=thisList[0]
  primeList.append(num)
  for i in thisList:
    if i%num==0:
      length-=1
    else:
      newList.append(i)
  thisList=newList
  newList=[]
print(primeList)