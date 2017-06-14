import argparse


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                # inserts an empty subtree
                self.left = Node(data=value)
            else:
                # continue searching for an empty subtree
                self.left.insert(value=value)
        else:
            if self.right is None:
                # inserts an empty subtree
                self.right = Node(data=value)
            else:
                self.right.insert(value=value)

    def contains(self, value):
        if value == self.data:
            # value found
            return true
        elif value < self.data:
            return false if self.left is None else self.left.contains(value)
        else:
            return false if self.right is None else self.right.contains(value)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data, end=" ")
        if self.right is not None:
            self.right.print_in_order()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Binary Search Tree implementation')
    parser.add_argument('-i', '--input', help='A single line of space-separated integers where each integer denotes'
                                              ' the data value of a node to be inserted into the tree.', required=True)
    args = parser.parse_args()
    values = list(map(int, args.input.split(' ')))
    root = Node(values[0])
    for value in values[1:]:
        root.insert(value)

    root.print_in_order()