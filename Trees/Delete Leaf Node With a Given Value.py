# You are given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, 
# if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).


def delete(root, target):

    if not root:
        return None

    root.left = delete(root.left, target)
    root.right = delete(root.right, target)

    if not root.left and not root.right and root.val == target:
        return None

    return root