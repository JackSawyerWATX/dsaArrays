class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

def search(node, target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif target < node.data:
    return search(node.left, target)
  else:
    return search(node.right, target)

root = TreeNode(50)
node7 = TreeNode(72)
node15 = TreeNode(154)
node3 = TreeNode(23)
node9 = TreeNode(60)
node20 = TreeNode(200)
node1 = TreeNode(10)
node72 = TreeNode(75)

root.left = node7
root.right = node15
node7.left = node3
node7.right = node9
node15.right = node20
node3.left = node1
node9.right = node72

inOrderTraversal(root)


# 1. `inOrderTraversal` visits left -> node -> right.
# 2. Output is sorted only when the tree satisfies BST rules (left < node < right).
# 3. If output isn't sorted: ensure the tree is a BST and that `inOrderTraversal(root)` is called.
