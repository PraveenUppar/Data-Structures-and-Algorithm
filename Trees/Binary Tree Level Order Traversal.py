# Given a binary tree root, return the level order traversal of it as a nested list, 
# where each sublist contains the values of nodes at a particular level in the tree, from left to right.


def solve(self, root):

    self.res = []

    def level(root, depth):

        if not root:
            return 

        if len(self.res) == depth:
            self.res.append([])

        self.res[depth].append(root.val)
        level(root.left,depth + 1)
        level(root.right, depth + 1)

    level(root, 0)
    return self.res


    