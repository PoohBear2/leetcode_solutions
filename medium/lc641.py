class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0 for _ in range(k)]
        self.front = 0
        self.cap = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = (self.front - 1) % len(self.arr)
        self.arr[self.front] = value
        self.cap += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        rear = (self.front + self.cap) % len(self.arr)
        self.arr[rear] = value
        self.cap += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.cap -= 1
        self.front = (self.front + 1) % len(self.arr)
        return True

        """
        [1, _, _, 2]
        """

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.cap -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.arr[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        rear = (self.front + self.cap - 1) % len(self.arr)
        return self.arr[rear]

    def isEmpty(self) -> bool:
        return self.cap == 0

    def isFull(self) -> bool:
        return self.cap == len(self.arr)
        


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
