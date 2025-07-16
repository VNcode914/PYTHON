def hello():
        try:
            a=int(input("enter your name :-"))
            print(a)
        except Exception as e:#doesnt let program crash
            print(e)#print the error

        print("thank you !! have a nice day✌")#doesnt break the prgram flow

        #your program should neve crash

def handlingExceptions():
#      a=int(input("enter 1 number : "))
#      b=int(input("enter 2 number : "))
#      print(a/b)

    try:
        a=int(input("enter 1 number : "))
        b=int(input("enter 2 number : "))
        print(a/b)
    except ZeroDivisionError as z:
        print(z)

    print("thanks❤")
# handlingExceptions()

def raisingExceptions():
    a=int(input("enter 1 number : "))
    b=int(input("enter 2 number : "))
    if(b==0):
         raise ZeroDivisionError("program is not meant to divide by zero")
    print(a/b)
# raisingExceptions()
    

def tryelse():
      try:
            a=int(input("enter your name :-"))
            print(a)
      except Exception as e:#doesnt let program crash
            print(e)#print the error
      else:
           print("else statement")
           print("try was succesfull")
tryelse()
     
