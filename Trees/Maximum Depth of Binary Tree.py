# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path 
# from the root node down to the farthest leaf node.

def depth(root):

    if not root:
        return 0

    left_depth = depth(root.left)
    right_depth = depth(root.right)

    return max(left_depth, right_depth) + 1