import math


def make_veb_order(start, depth):
    if depth == 0:
        return [start]

    lower_depth = depth // 2
    upper_depth = depth - lower_depth - 1

    depth_cutoff = start.depth + upper_depth
    frontier = [start]
    recurse_nodes = []

    for node in frontier:
        if node.depth == depth_cutoff + 1:
            recurse_nodes.append(node)
        if node.depth > depth_cutoff + 1:
            break
        if node.leftChild is not None:
            frontier.append(node.leftChild)
        if node.rightChild is not None:
            frontier.append(node.rightChild)

    veb_order = make_veb_order(start, upper_depth)
    for node in recurse_nodes:
        veb_order += make_veb_order(node, lower_depth)

    return veb_order


class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.i_veb = None


class BSTVEB:
    def __init__(self, bst, n):
        max_depth = int(math.log(n, 2) + +1)
        self.veb_ordered_nodes = make_veb_order(bst.root, max_depth)
        self.root = self.veb_ordered_nodes[0]

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
