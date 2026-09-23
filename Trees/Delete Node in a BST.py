# You are given a root node reference of a BST and a key, delete the node with the given key in the BST, if present. 
# Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.


def delete(root, val):

    if not root:
        return None

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:

            cur = root.right
            while cur.left:
                cur = cur.left

            cur.left = root.left
            res = root.right

            del root
            return res 

    return root