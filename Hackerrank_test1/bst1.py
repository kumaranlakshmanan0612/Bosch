import math
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


    def height(self,node,h):
        if node==None:
            # print("hi")
            h[0]=h[0]+1
            return
        print(node.val)
        self.height(node.left,h)
        self.height(node.right,h)
    
def main():
    bst=BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.insert(90)
    bst.insert(100)
    bst.insert(110)
    bst.insert(120)
    bst.insert(130)
    bst.insert(140)
    bst.insert(150)
    bst.insert(160)
    h=[0]
    bst.height(bst.root,h)
    ## formula - height=log2(total no of last nodes)
    print("Height -",math.log(h[0]/2,2))

if __name__=="__main__":
  main()
