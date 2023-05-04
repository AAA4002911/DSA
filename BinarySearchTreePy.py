class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        while True:
            if new_val < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(new_val)
                    break
            elif new_val > current.value:
                if current.right:
                    current = current.right
                else:
                    current.left = Node(new_val)
                    break
            else:
                break

    def search(self, find_val):
        current = self.root
        while current:
            if find_val == current.value:
                return True
            elif find_val < current.value:
                current = current.left
            else:
                current = current.right
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
