class EmptyList(Exception):
    pass

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def show(self):
        if not self.head:
            raise EmptyList
        
        curr = self.head
        items = []

        while curr:
            items.append(curr.value)
            curr = curr.next
        
        return items
    
    def length(self):
        if not self.head:
            return 0
        
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        
        return count

    def append(self, item):
        node = Node(item)

        if not self.head:
            self.head = node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node
    
    def build(self, arr: list):
        for item in arr:
            self.append(item= item)
    
    def prepend(self, item):
        node = Node(item)

        if not self.head:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def insert(self, item, index):
        if index > self.length():
            raise IndexError
        
        if index == 0:
            self.prepend(item= item)
            return
        
        node = Node(item)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        node.next = curr.next
        curr.next = node

    def trauncate(self):
        if not self.head:
            raise EmptyList
        
        curr = self.head
        while curr.next.next:
            curr = curr.next
        
        curr.next = None

    def headectomy(self):
        if not self.head:
            raise EmptyList
        
        self.head = self.head.next

    def delete(self, index):
        if not self.head:
            raise EmptyList
        if index >= self.length():
            raise IndexError
        
        if index == 0:
            self.headectomy()
            return
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        
        curr.next = curr.next.next
    
    def get(self, index):
        if not self.head or index >= self.length():
            raise IndexError
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.value


if __name__ == "__main__":
    ll = LinkedList()

    ll.build([1,2,3,4,5,6])
    ll.append(10)
    ll.prepend(20)
    print(ll.show())

    ll.delete(3)
    print(ll.show())

    ll.headectomy()
    print(ll.show())


    