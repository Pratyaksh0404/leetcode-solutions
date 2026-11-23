class ProductOfNumbers:

    def __init__(self):
        self.l=[1]
        

    def add(self, num: int) -> None:
        if num==0:
            self.l=[1]
        else:
            self.l.append(self.l[-1]*num)
        

    def getProduct(self, k: int) -> int:
        if k>=len(self.l):
            return 0
        else:
            return self.l[-1]//self.l[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)