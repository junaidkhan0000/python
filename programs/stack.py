class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"pushed{item} to the stack.")t

    def isempty(self):
        n=len(self.stack)
        if n == 0:
            print("Stack is empty.")
            return True
















stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

