class EmptyQueue(Exception):
    pass

class NotFound(Exception):
    pass

class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def show(self):
        if self.is_empty():
            raise EmptyQueue
        else:
            return self.queue
    
    def length(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def enqueue_multiple(self, arr: list):
        for item in arr:
            self.enqueue(item= item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise EmptyQueue
    
    def first(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise EmptyQueue
    
    def clear(self):
        if self.is_empty():
            raise EmptyQueue
        else:
            self.queue = []
    
    def find(self, item):
        if self.is_empty():
            raise EmptyQueue
        
        for i in range(self.length()):
            if self.queue[i] == item:
                return i
        raise NotFound
                


if __name__ == "__main__":
    queue = Queue()

    