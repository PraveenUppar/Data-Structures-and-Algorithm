# Given the roots of two binary trees p and q, 
# return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent 
# if they share the exact same structure and the nodes have the same values.


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

