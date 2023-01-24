class MyCircularDeque:
    def __init__(self, k: int):
        self.l = list()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.l) < self.k:
            self.l.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.l) < self.k:
            self.l.insert(len(self.l), value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.l) > 0:
            self.l.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.l) > 0:
            self.l.pop(-1)
            return True
        return False

    def getFront(self) -> int:
        if len(self.l) > 0:
            return self.l[0]
        return -1

    def getRear(self) -> int:
        if len(self.l) > 0:
            return self.l[-1]
        return -1

    def isEmpty(self) -> bool:
        return True if len(self.l) == 0 else False

    def isFull(self) -> bool:
        return True if len(self.l) == self.k else False



#     def __init__(self, k: int):
#         self.head = 0
#         self.tail = 0
#         self.k = k
#         self.size = 0
#         self.queue = []
        

#     def insertFront(self, value: int) -> bool:
#         if self.isEmpty():
#             self.queue[self.head] = value
#             self.size += 1
#             return True
#         elif not self.isFull():
#             self.head = (self.head-1)%self.k
#             self.queue[self.head] = value
#             self.size += 1
#             return True
#         else:
#             return False

#     def insertLast(self, value: int) -> bool:
#         if self.isEmpty():
#             self.queue[self.tail] = value
#             self.size += 1
#             return True
#         elif not self.isFull():
#             self.tail = (self.tail+1)%self.k
#             self.queue[self.tail] = value
#             self.size += 1
#             return True
#         else:
#             return False

#     def deleteFront(self) -> bool:
#         if not self.isEmpty():
#             self.queue[self.head] = None
#             if self.size != 1:
#                 self.tail = (self.head +1)%self.k
#             self.size -= 1
#             return True
#         return False
        

#     def deleteLast(self) -> bool:
#         if not self.isEmpty():
#             self.queue[self.tail] = None
#             if self.size != 1:
#                 self.tail = (self.tail-1)%self.k
#             self.size -= 1
#             return True
#         return False

#     def getFront(self) -> int:
#         if self.isEmpty():return -1
#         return self.queue[self.head]

#     def getRear(self) -> int:
#         if self.isEmpty():return -1
#         return self.queue[self.tail]
        

#     def isEmpty(self) -> bool:
#         if self.size == 0: return True
#         return False

#     def isFull(self) -> bool:
#         if self.size == self.k: return True
#         return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()