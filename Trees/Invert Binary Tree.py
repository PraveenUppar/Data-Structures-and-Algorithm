# You are given the root of a binary tree root. Invert the binary tree and return its root.

def invert(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root