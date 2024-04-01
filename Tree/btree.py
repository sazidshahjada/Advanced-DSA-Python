class EmptyTree(Exception):
    pass

class NotExists(Exception):
    pass

class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None
    
class Btree:
    def __init__(self) -> None:
        self.root = None
    
    def insert_level(self, val):
        node = Node(val= val)

        if not self.root:
            self.root = node
            return
        
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if not curr.left:
                curr.left = node
                break
            elif not curr.right:
                curr.right = node
                break
            else:
                queue.append(curr.left)
                queue.append(curr.right)
    
    def level_travarsal(self):
        if not self.root:
            raise EmptyTree
        
        arr = list()
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            arr.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return arr
    
    def build_btree(self, arr: list):
        for item in arr:
            self.insert_level(val= item)
    
    def inorder_travarsal(self):
        def inorder_rec(curr: Node, arr: list):
            if curr:
                inorder_rec(curr.left, arr)
                arr.append(curr.value)
                inorder_rec(curr.right, arr)
        
        if not self.root:
            raise EmptyTree
        
        arr = list()
        inorder_rec(self.root, arr= arr)

        return arr
    
    def preorder_travarsal(self):
        def preorder_rec(curr: Node, arr: list):
            if curr:
                arr.append(curr.value)
                preorder_rec(curr.left, arr)
                preorder_rec(curr.right, arr)
        
        if not self.root:
            raise EmptyTree
        
        arr = list()
        preorder_rec(self.root, arr= arr)

        return arr
    
    def postorder_travarsal(self):
        def postorder_rec(curr: Node, arr: list):
            if curr:
                postorder_rec(curr.left, arr)
                postorder_rec(curr.right, arr)
                arr.append(curr.value)
        
        if not self.root:
            raise EmptyTree
        
        arr = list()
        postorder_rec(self.root, arr= arr)

        return arr
    
    def tree_level(self):
        if not self.root:
            return 0
        
        level = 0
        queue = [self.root]

        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return level
    
    def find_level(self, val):
        if not self.root:
            return 0
        
        level = 0
        queue = [self.root]

        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr.value == val:
                    return level
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        raise NotExists


if __name__ == "__main__":
    bt = Btree()

    bt.build_btree([1,2,3,4])
    
    bt.insert_level(5)

    array = [6,7,8]
    for i in array:
        bt.insert_level(i)

    arr = bt.level_travarsal()
    print(arr)

    inorder = bt.inorder_travarsal()
    print(inorder)

    preorder = bt.preorder_travarsal()
    print(preorder)

    postorder = bt.postorder_travarsal()
    print(postorder)

    level = bt.tree_level()
    print(level)

    val_lev = bt.find_level(3)
    print(val_lev)

    