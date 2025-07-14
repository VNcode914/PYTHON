class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def vec(self):
        print("vector is:-",self.i,"i+",self.j,"j")
        
class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def vec(self):
        print("vector is:-",self.i,"i+",self.j,"j+",self.k,"k")


v=twoDvector(2,4)
h=threeDvector(3,5,3)
v.vec()
h.vec()