# Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

# A valid binary search tree satisfies the following constraints:

# The left subtree of every node contains only nodes with keys less than the node's key.
# The right subtree of every node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees are also binary search trees.


def validate(root):

    res = []

    def inorder(root):
        if not root:
            return None
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)

    for i in range(1, len(res)):
        if res[i] <= res[i - 1]:
            return False
    return True