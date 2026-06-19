class MinStack:

    def __init__(self):
        self.arr=[]
        self.min1=[]
    

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.min1)==0:
            self.min1.append(val)
        elif(val > self.min1[-1] ):
                self.min1.append(self.min1[-1])
        else:
                self.min1.append(val)
            
    def pop(self) -> None:
        if self.arr:
            self.arr.pop()
            self.min1.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]

    def getMin(self) -> int:
        return self.min1[-1]


