# Within a binary tree, a node x is considered good 
# if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

# Given the root of a binary tree root, return the number of good nodes within the tree.

def goodNodes(root):

    def dfs(root, max_val):

        if not root:
            return 0
        
        if root.val >= max_val:
            count = 1
        else:
            count = 0

        max_val = max(root.val, max_val)
        left_count = dfs(root.left, max_val)
        right_count = dfs(root.right, max_val)
        return left_count + right_count + count

    return dfs(root, root.val)
        
 

