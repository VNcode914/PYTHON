from random import randint
n=randint(1,25)
print("guess number from 1-1000")

b=0
count=0
at=100

print("initial score is",at)
while(b!=n):
  b=int(input(""))
  if(b>n):
    print("try smaller")
  elif(b<n):
    print("try bigger")
  elif(b==n):
    print("hooray!,you won🎉")  

  count=count+1
  if(count>20):
    print("Game Over🤔!!!!\noutof attempts")
    break
  at=at-10
  
print("You took",count,"attempts✌✌")
print("final score:" ,at,"points")








