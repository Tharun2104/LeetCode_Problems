#  232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.data = [] #Stack

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        self.data = self.data[::-1]
        removed = self.data.pop()
        self.data = self.data[::-1]
        return removed

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        print(self.data)
        if self.data:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()