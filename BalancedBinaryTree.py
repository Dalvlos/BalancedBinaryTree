class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right
    
    # Perform rotation
    x.right = y
    y.left = T2
    
    # Update heights
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    
    # Perform rotation
    y.left = x
    x.right = T2
    
    # Update heights
    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1
    
    return y

def insert(root, key):
    if not root:
        return Node(key)
    elif key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    root.height = max(get_height(root.left), get_height(root.right)) + 1
    balance = get_balance(root)
    
    # Left Left Case
    if balance > 1 and key < root.left.value:
        return rotate_right(root)
    
    # Right Right Case
    if balance < -1 and key > root.right.value:
        return rotate_left(root)
    
    # Left Right Case
    if balance > 1 and key > root.left.value:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    
    # Right Left Case
    if balance < -1 and key < root.right.value:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Exemplo de uso
root = None
values = [10, 20, 30, 40, 50, 25]
for value in values:
    root = insert(root, value)

inorder_traversal(root)  # Saída: 10 20 25 30 40 50