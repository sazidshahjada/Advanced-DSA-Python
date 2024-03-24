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
        

def main(ll: LinkedList):
    print(
        """
    Commands:
        s. Show
        l. Length
        b. Build
        a. Append
        p. Prepend
        i. Insert
        t. Trauncate
        h. Headectomy
        d. Delete
        g. Get
        q. Quit
    """
    )
    prompt = input("Enter Your Command >>> ")

    if prompt == "s":
        try:
            lst = ll.show()
            print("\nThe List is : ", lst)
        except EmptyList:
            print("\nThe List is Empty.")
    
    elif prompt == "l":
        print(f"\nThe List Has {ll.length()} Items.")
    
    elif prompt == "a":
        item = input("Enter Item to Append : ")
        if item.isdigit():
            item = int(item)
        
        ll.append(item= item)
        print(f"\n The item {item} Appended Successfully.")
    
    elif prompt == "b":
        items = input("Enter Items To Build List : ").split()
        for i in range(len(items)):
            if items[i].isdigit():
                items[i] = int(items[i])
        
        for item in items:
            ll.append(item= item)
        
        print("\nThe List Built Successfully.")

    elif prompt == "p":
        item = input("Enter Item to Prepend : ")
        if item.isdigit():
            item = int(item)
        
        ll.prepend(item= item)
        print(f"\n The item {item} Prepended Successfully.")

    elif prompt == "i":
        item = input("Enter Item to Insert : ")
        index = input("Enter Index to Insert : ")        
        if item.isdigit():
            item = int(item)
            
        try:
            ll.insert(item= item, index= index)
            print(f"\nThe item {item} Inserted Successfully.")

        except IndexError:
            print("\nIndex Out of Range.")
    
    elif prompt == "t":
        try:
            ll.trauncate()
            print("\nLast Item Deleted Successfully.")
        except EmptyList:
            print("\nThere is Nothing to Delete.")
    
    elif prompt == "h":
        try:
            ll.headectomy()
            print("\nFirst Item Deleted Successfully.")
        except EmptyList:
            print("\nThere is Nothing to Delete.")
    
    elif prompt == "d":
        index = int(input("Enter Index to Delete : "))

        try:
            ll.delete(index= index)
            print(f"\nItem in Index {index} Deleted Successfully.")
        except EmptyList:
            print("\There is Nothing to Delete.")
        except IndexError:
            print("\nIndex Out of Range.")
    
    elif prompt == "g":
        index = int(input("Enter Index to Get : "))

        try:
            value = ll.get(index= index)
            print(f"\nThe Value at Index {index} is {value}.")
        except IndexError:
            print("\nIndex Out of Range.")
    
    elif prompt == "q":
        exit()
    
    else:
        print("\nYou Pressed The Wrong Key.")


if __name__ == "__main__":
    ll = LinkedList()

    while True:
        main(ll= ll)


    