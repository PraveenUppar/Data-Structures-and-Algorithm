# You are given the root node of a binary search tree (BST) and a value val to insert into the tree. 
# Return the root node of the BST after the insertion. 
# It is guaranteed that the new value does not exist in the original BST.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):

    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)

    return root

    