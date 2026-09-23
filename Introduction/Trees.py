class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

def buildTree(arr):

    if not arr or arr[0] is None:
        return None 

    root = TreeNode(int(arr[0]))
    i = 1
    queue = deque([root])

    while queue and i < len(arr):
        node = queue.popleft()

        if i < len(arr):
            if arr[i] is not None:
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
        i += 1

        if i < len(arr):
            if arr[i] is not None:
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
        i += 1

    return root

def printTree(root):

    res = []

    if not root:
        return res

    queue = deque([root])
    res.append(root.val)

    while queue:
        node = queue.popleft()

        if node.left:
            res.append(node.left.val)
            queue.append(node.left)
        else:
            res.append(None)

        if node.right:
            res.append(node.right.val)
            queue.append(node.right)
        else:
            res.append(None)

    return res

    

    