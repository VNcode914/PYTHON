                                    #GAME#
print("choose:\n","1.snake\n","2.water\n","3.gun")
p1=input().lower()
p2=input().lower()
if(p1=='snake' and p2=='water'):
    print("player 1 won")
elif(p1=='snake'and p2=='gun'):
    print("player 2 won")
elif(p1=='water'and p2=='gun'):
    print("player 1 won")
elif(p1=='water' and p2=='snake'):
    print("player 2 won")
elif(p1=='gun'and p2=='snake'):
    print("player 1")
elif(p1=='gun'and p2=='water'):
    print("player 2 won")
else:
    print("tie")