class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.secondStack = []
        

    def push(self, x: int) -> None:
        
        self.firstStack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.secondStack.pop()

    def peek(self) -> int:
        if not self.secondStack:
            while self.firstStack:
                self.secondStack.append(self.firstStack.pop())
            
        return self.secondStack[-1]
        

    def empty(self) -> bool:
        
        return len(self.firstStack) == 0 and len(self.secondStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
