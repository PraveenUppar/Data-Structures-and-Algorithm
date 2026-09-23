# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

# In this new place, there are houses and each house has its only one parent house. 
# All houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken.

# You are given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.


def rob(root):
    
    if not root:
        return 0

    res = root.val
    if root.left:
        res += rob(root.left.left) + rob(root.left.right)
    if root.right:
        res += rob(root.right.left) + rob(root.right.right)

    res = max(res, rob(root.left) + rob(root.right))
    return res