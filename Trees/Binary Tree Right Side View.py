# You are given the root of a binary tree. 
# Return only the values of the nodes that are visible from the right side of the tree, 
# ordered from top to bottom.

def solve(root):

    res = []

    def level(root, depth):

        if not root:
            return None

        if len(res) == depth:
            res.append(root.val)

        level(root.right,depth + 1)
        level(root.left, depth + 1)

    level(root, 0)
    return res
