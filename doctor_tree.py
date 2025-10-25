class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        if self.root is None:
            print("Error: Tree is empty. Please set a root first.")
            return

        def find_and_insert(node):
            if node is None:
                return False
            if node.name == parent_name:
                new_node = DoctorNode(child_name)
                if side == "left":
                    if node.left is None:
                        node.left = new_node
                        return True
                    else:
                        print(f"Error: {parent_name} already has a left child.")
                        return False
                elif side == "right":
                    if node.right is None:
                        node.right = new_node
                        return True
                    else:
                        print(f"Error: {parent_name} already has a right child.")
                        return False
                else:
                    print("Error: Side must be 'left' or 'right'.")
                    return False
            # search left and right subtrees
            return find_and_insert(node.left) or find_and_insert(node.right)

        if not find_and_insert(self.root):
            print(f"Error: Parent '{parent_name}' not found.")

    # Preorder traversal:
    def preorder(self, node):
        if node is None:
            return []
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    # Inorder traversal:
    def inorder(self, node):
        if node is None:
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)
        return result

    # Postorder traversal:
    def postorder(self, node):
        if node is None:
            return []
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)
        return result


# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Gonzalez")
tree.insert("Dr. Gonzalez", "Dr. Alonso", "right")
tree.insert("Dr. Gonzalez", "Dr. Campelo", "left")
tree.insert("Dr. Campelo", "Dr. Iglesias", "right")
tree.insert("Dr. Campelo", "Dr. Benito", "left")

# Traversal tests
assert tree.preorder(tree.root) == [
    "Dr. Gonzalez", "Dr. Campelo", "Dr. Benito", "Dr. Iglesias", "Dr. Alonso"
]
assert tree.inorder(tree.root) == [
    "Dr. Benito", "Dr. Campelo", "Dr. Iglesias", "Dr. Gonzalez", "Dr. Alonso"
]
assert tree.postorder(tree.root) == [
    "Dr. Benito", "Dr. Iglesias", "Dr. Campelo", "Dr. Alonso", "Dr. Gonzalez"
]

# Edge case 1: Empty tree
empty_tree = DoctorTree()
assert empty_tree.preorder(empty_tree.root) == []
assert empty_tree.inorder(empty_tree.root) == []
assert empty_tree.postorder(empty_tree.root) == []

# Edge case 2: Single node tree
single_tree = DoctorTree()
single_tree.root = DoctorNode("Dr. Vazquez")
assert single_tree.preorder(single_tree.root) == ["Dr. Vazquez"]
assert single_tree.inorder(single_tree.root) == ["Dr. Vazquez"]
assert single_tree.postorder(single_tree.root) == ["Dr. Vazquez"]

print("All tests passed successfully!")
