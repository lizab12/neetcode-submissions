class MinStack:

    def __init__(self):
        self.a = []
        self.minA = []
        

    def push(self, val: int) -> None:
        self.a.append(val)
        if not self.minA:
            self.minA.append(val)
        else:
            self.minA.append(min(val,self.minA[-1]))
        

    def pop(self) -> None:
        self.a.pop()
        self.minA.pop()
        

    def top(self) -> int:
        return self.a[-1]
        

    def getMin(self) -> int:
        return self.minA[-1]
        
