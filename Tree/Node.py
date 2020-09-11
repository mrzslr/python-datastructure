class BSTNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class AVLNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 0


class RBNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.height = 0
        self.color = 0
