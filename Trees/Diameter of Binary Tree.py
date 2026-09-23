# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. 
# The path does not necessarily have to pass through the root.

# The length of a path between two nodes in a binary tree is the number of edges between the nodes. 
# Note that the path can not include the same node twice.

# Given the root of a binary tree root, return the diameter of the tree.


def diameter(self, root):
    self.res = 0

    def depth(root):

        if not root:
            return 0

        left_depth = depth(root.left)
        right_depth = depth(root.right)
        self.res = max(self.res, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    depth(root)
    return self.res