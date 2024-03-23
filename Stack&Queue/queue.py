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
            queue.enqueue(item= item)
    
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
        else:
            for i in range(self.length()):
                if self.queue[i] == item:
                    return i
                else:
                    raise NotFound
                

# Terminal Based Interface
def main(queue: Queue):
    print("""
        Commands:
            s. Show items
            e. Enqueue item.
            ee. Enqueue multiple items.
            d. Dequeue item.
            f. First item.
            i. Is Empty?.
            l. Length of Queue.
            F. Find any item.
            c. Clear Queue.
            q. Quit Program
    """)

    prompt = input("Enter Your Command >>> ")

    if prompt == "s":
        try:
            items = queue.show()
            print("\nThe Items Are : ", end= " ")
            for item in items:
                print(item, end= " ")
            print()
        except EmptyQueue:
            print("\nThe Queue is Empty.")

    elif prompt == "e":
        item = input("Enter Item to Enqueue :  ")
        if item.isdigit():
            item = int(item)
        
        queue.enqueue(item= item)
        print(f"\nThe Item {item} Enqueued Successfully.")
    
    elif prompt == "ee":
        items = input("Enter Items to Enqueue : ").split()
        for i in range(queue.length()):
            if items[i].isdigit():
                items[i] = int(items[i])
        
        queue.enqueue_multiple(arr= items)
        print("\nAll Items are Enqueued Successfully.")

    elif prompt == "d":
        try:
            dequeue_item = queue.dequeue()
            print(f"Dequeued Item {dequeue_item}.")
        except EmptyQueue:
            print("\nThere is Nothing to Dequeue.")
    
    elif prompt == "f":
        try:
            top_item = queue.first()
            print(f"\nFirst Item {top_item}.")
        except EmptyQueue:
            print("\nThere is Nothing.")
    
    elif prompt == "i":
        if queue.is_empty():
            print("\nThe Queue is Empty.")
        else:
            print("\nThe Queue is not Empty.")
    
    elif prompt == "l":
        length = queue.length()
        print(f"\nThe Queue Has {length} Items.")
    
    elif prompt == "F":
        item = input("Enter Item to Find :  ")
        if item.isdigit():
            item = int(item)

        try:
            idx = queue.find(item= item)
            print(f"\nItem {item} is at Index {idx}")
        except EmptyQueue:
            print("\nThere is Nothing in Queue.")
        except NotFound:
            print(f"\n{item} Not Found in Queue.")
    
    elif prompt == "c":
        try:
            queue.clear()
            print("\nQueue Has Been Cleared Successfully.")
        except EmptyQueue:
            print("\nThe Queue is Empty Already.")
    
    elif prompt == "q":
        exit()
    
    else:
        print("\nYou Have Pressed The Wrong Key.")



if __name__ == "__main__":
    queue = Queue()

    while True:
        main(queue= queue)