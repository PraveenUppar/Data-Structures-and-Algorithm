# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

def balance(self, root):

    self.res = True

    def depth(root):

        if not root:
            return 0

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if abs(right_depth - left_depth) > 1:
            self.res = False

        return max(left_depth, right_depth) + 1

    depth(root)
    return self.res