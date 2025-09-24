# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder = deque(preorder)

        def helper(preorder, inorder):
            if inorder:
                poping_element = preorder.popleft()
                inorder_index = inorder.index(poping_element)
                root = TreeNode(inorder[inorder_index])
                root.left = helper(preorder, inorder[:inorder_index])
                root.right = helper(preorder, inorder[inorder_index+1:])
                return root
        return helper(preorder, inorder)

        