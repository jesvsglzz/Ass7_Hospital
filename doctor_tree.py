class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        
        def _insert_recursive(node):
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
                    print("Error: Invalid side value. Use 'left' or 'right'.")
                    return False
            return _insert_recursive(node.left) or _insert_recursive(node.right)

        if self.root is None:
            print("Error: Tree is empty. Please set a root before inserting.")
            return
        inserted = _insert_recursive(self.root)
        if not inserted:
            print(f"Error: Parent '{parent_name}' not found in the tree.")

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

print("Preorder:", tree.preorder(tree.root))
print("Inorder:", tree.inorder(tree.root))
print("Postorder:", tree.postorder(tree.root))


