# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
# The tree tree could also be considered as a subtree of itself.


def subtree(root,subroot):

    if not root:
        return False

    if same(root,subroot):
        return True

    return subtree(root.left, subroot) or subtree(root.right, subroot)

def same(p,q):

    stack = [[p,q]]


    while stack:

        p,q = stack.pop()

        if not p and not q:
            continue

        if not p or not q or p.val != q.val:
            return False

        stack.append([p.left, q.left])
        stack.append([p.right, q.right])

    return True