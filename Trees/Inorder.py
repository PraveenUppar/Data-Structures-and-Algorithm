# You are given the root of a binary tree, return the inorder traversal of its nodes' values.

def inorder(root):

    res = []

    if not root:
        return None

    inorder(root.left)
    res.append(root.val)
    inorder(root.right)

    return res