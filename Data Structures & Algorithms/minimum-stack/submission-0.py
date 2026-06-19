class MinStack:

    def __init__(self):
        self.arr=[]
    
    

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        min1=float('inf')
        for i in self.arr:
            if i<min1:
                min1=i
        return min1 
