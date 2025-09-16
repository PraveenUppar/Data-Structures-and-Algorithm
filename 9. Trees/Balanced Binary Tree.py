# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if not node:
                return [True,0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            # [True,0] == [boolean,height_of_subtree]
            # left[0] or right[0] is True or False
            # left[1] or right[1] is the height of subtree

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, max(left[1],right[1]) + 1]

        return dfs(root)[0]