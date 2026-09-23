# You are given the root of a binary tree, return the preorder traversal of its nodes' values.

def preorder(root):

    res = []

    if not root:
        return None

    res.append(root.val)
    preorder(root.left)
    preorder(root.right)

    return res