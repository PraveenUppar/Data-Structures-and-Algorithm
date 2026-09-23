# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

def element(root, k):

    res = []

    def inorder(root):
        if not root:
            return None
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res[k - 1]