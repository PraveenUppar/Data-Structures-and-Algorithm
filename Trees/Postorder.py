# You are given the root of a binary tree, return the postorder traversal of its nodes' values.

def postorder(root):

    res = []

    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    res.append(root.val)

    return res