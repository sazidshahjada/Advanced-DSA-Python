class EmptyStack(Exception):
    pass

class NotFound(Exception):
    pass

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def show(self):
        if self.is_empty():
            raise EmptyStack
        else:
            return self.stack
    
    def length(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def push_multiple(self, arr: list):
        for item in arr:
            self.push(item= item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise EmptyStack
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise EmptyStack
    
    def clear(self):
        if self.is_empty():
            raise EmptyStack
        else:
            self.stack = []
    
    def find(self, item):
        if self.is_empty():
            raise EmptyStack

        for i in range(self.length()):
            if self.stack[i] == item:
                return i
            raise NotFound
                


if __name__ == "__main__":
    stack = Stack()
