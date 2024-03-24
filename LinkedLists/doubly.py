class EmptyList(Exception):
    pass

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None
        self.prev = None
    
class DoublyList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def show(self):
        if not self.head:
            raise EmptyList
        
        list_items = []
        curr = self.head
        while curr:
            list_items.append(curr.value)
            curr = curr.next
        
        return list_items
    
    def show_rev(self):
        if not self.tail:
            raise EmptyList
        
        list_items = []
        curr = self.tail
        while curr:
            list_items.append(curr.value)
            curr = curr.prev
        
        return list_items
    
    def append(self, item):
        node = Node(item)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def build(self, arr: list):
        for item in arr:
            self.append(item= item)
    
    def prepend(self, item):
        node = Node(item)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
            return
        
        self.head.prev = node
        node.next = self.head
        self.head = node

if __name__ == "__main__":
    dl = DoublyList()

    dl.build([1,2,3])
    dl.append(4)
    dl.prepend(0)

    print(dl.show())
    print(dl.show_rev())

