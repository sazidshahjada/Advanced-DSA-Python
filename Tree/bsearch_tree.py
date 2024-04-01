from btree import Btree, Node, EmptyTree, NotExists

class BST(Btree):
    def __init__(self) -> None:
        self.root = None
    
    def insert_bst(self, val):
        pass
    
    def build_bst(self, arr: list):
        for val in arr:
            self.insert_bst(val= val)
    

if __name__ == "__main__":
    bst = BST()
    
    bst.build_bst([46, 19, 15, 36, 24])

    print(bst.level_travarsal())
    print(bst.inorder_travarsal())
    