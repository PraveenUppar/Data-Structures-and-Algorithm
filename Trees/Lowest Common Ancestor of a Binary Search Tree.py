# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, 
# return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q are descendants. 
# The ancestor is allowed to be a descendant of itself.


def lca(root, p, q):

    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root

