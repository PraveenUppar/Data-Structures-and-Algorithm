# Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
# A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

# The path sum of a path is the sum of the node's values in the path.

def max_path(self, root):

    self.res = root.val

    def depth(root):
        if not root:
            return 0

        left_depth = max(depth(root.left), 0)
        right_depth = max(depth(root.right), 0)

        self.res = max(self.res, left_depth + right_depth + root.val)
        return max(left_depth, right_depth) + root.val  

    depth(root)
    return self.res
    