L=[1,2,"ansh",0.5,7.8,"#","()"]
print(L)

L.append("ABC")#append add element to the last
print(L)

L.pop(3)#pop removes that element of correspondng index 
print(L)

L.remove("ABC")#remove delete the desired element
print(L)

L.reverse()#reverse flips the order of the list
print(L)

L.insert(3,"yy")#insert adds element at desired index
print(L)

#all these methods one by one takes the edited list not the original list
#                               LIST SLICING
L=L[0::]
print(L)#OG order

L=L[::-1]
print(L)#reverse order
