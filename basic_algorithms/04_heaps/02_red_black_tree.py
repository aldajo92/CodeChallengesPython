class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color


class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return False

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, current, new_val)
            else:
                current.right = Node(new_val, current, 'red')
        else:
            if current.left:
                self.insert_helper(current.left, current, new_val)
            else:
                current.left = Node(new_val, current, 'red')

