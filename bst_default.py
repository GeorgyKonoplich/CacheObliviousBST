class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.depth = 0


class BST:
    def __init__(self, array=None):
        self.root = Node(array[0])
        for i, x in enumerate(array[1:]):
            self.insert_node(self.root, x, 0)

    def insert_node(self, current_node, val, d):
        if val <= current_node.val:
            if current_node.leftChild:
                self.insert_node(current_node.leftChild, val, d + 1)
            else:
                current_node.leftChild = Node(val)
                current_node.leftChild.depth = d + 1

        elif val > current_node.val:
            if current_node.rightChild:
                self.insert_node(current_node.rightChild, val, d + 1)
            else:
                current_node.rightChild = Node(val)
                current_node.rightChild.depth = d + 1

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, current_node, val):
        if current_node is None:
            return False
        elif val == current_node.val:
            return True
        elif val < current_node.val:
            return self.find_node(current_node.leftChild, val)
        else:
            return self.find_node(current_node.rightChild, val)