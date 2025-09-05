class _BSTNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if self.root is None:
            self.root=_BSTNode(value)
            return
        curr=self.root
        while True:
            if value==curr.val:
                return
            elif value<curr.val:
                if curr.left is None:
                    curr.left=_BSTNode(value)
                    return
                curr=curr.left
            else:
                if curr.right is None:
                    curr.right=_BSTNode(value)
                    return
                curr=curr.right

    def search(self,value):
        curr=self.root
        while curr:
            if value==curr.val:
                return True
            curr=curr.left if value<curr.val else curr.right
        return False

    def inorder(self):
        res=[]
        def dfs(node):
            if not node:return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(self.root)
        return res

    def preorder(self):
        res=[]
        def dfs(node):
            if not node:return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(self.root)
        return res

    def postorder(self):
        res=[]
        def dfs(node):
            if not node:return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(self.root)
        return res
    
def main():
    bst=BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())
    print(bst.search(40))
    print(bst.search(90))

if __name__=="__main__":
  main()
