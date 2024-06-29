class Counter:
    def __init__(self,start):
        self.st=start
    def increment(self):
        self.st+=3
        return self.st
    def decrement(self):
        self.st-=2
        return self.st 
 
ct1=Counter(7)
print(ct1.increment())
print(ct1.decrement())

