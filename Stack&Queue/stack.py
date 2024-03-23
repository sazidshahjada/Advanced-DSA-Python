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
            stack.push(item= item)
    
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
        else:
            for i in range(self.length()):
                if self.stack[i] == item:
                    return i
                else:
                    raise NotFound
                

# Terminal Based Interface
def main(stack: Stack):
    print("""
        Commands:
            s. Show items
            P. Push item.
            PP. Push multiple items.
            p. Pop item.
            t. Top item.
            i. Is Empty?.
            l. Length of Stack.
            f. Find any item.
            c. Clear Stack.
            q. Quit Program
    """)

    prompt = input("Enter Your Command >>> ")

    if prompt == "s":
        try:
            items = stack.show()
            print("\nThe Items Are : ", end= " ")
            for item in items:
                print(item, end= " ")
            print()
        except EmptyStack:
            print("\nThe Stack is Empty.")

    elif prompt == "P":
        item = input("Enter Item to Push :  ")
        if item.isdigit():
            item = int(item)
        
        stack.push(item= item)
        print(f"\nThe Item {item} Added Successfully.")
    
    elif prompt == "PP":
        items = input("Enter Items to Push : ").split()
        for i in range(stack.length()):
            if items[i].isdigit():
                items[i] = int(items[i])
        
        stack.push_multiple(arr= items)
        print("\nAll Items are Added Successfully.")

    elif prompt == "p":
        try:
            pop_item = stack.pop()
            print(f"Popped Item {pop_item}.")
        except EmptyStack:
            print("\nThere is Nothing to Pop.")
    
    elif prompt == "t":
        try:
            top_item = stack.top()
            print(f"\nTop Item {top_item}.")
        except EmptyStack:
            print("\nThere is Nothing.")
    
    elif prompt == "i":
        if stack.is_empty():
            print("\nThe Stack is Empty.")
        else:
            print("\nThe Stack is not Empty.")
    
    elif prompt == "l":
        length = stack.length()
        print(f"\nThe Stack Has {length} Items.")
    
    elif prompt == "f":
        item = input("Enter Item to Find :  ")
        if item.isdigit():
            item = int(item)

        try:
            idx = stack.find(item= item)
            print(f"\nItem {item} is at Index {idx}")
        except EmptyStack:
            print("\nThere is Nothing in Stack.")
        except NotFound:
            print(f"\n{item} Not Found in Stack.")
    
    elif prompt == "c":
        try:
            stack.clear()
            print("\nStack Has Been Cleared Successfully.")
        except EmptyStack:
            print("\nThe Stack is Empty Already.")
    
    elif prompt == "q":
        exit()
    
    else:
        print("\nYou Have Pressed The Wrong Key.")



if __name__ == "__main__":
    stack = Stack()

    while True:
        main(stack= stack)