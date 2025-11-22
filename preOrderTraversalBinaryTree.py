class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

root = TreeNode("Root")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.left = nodeG

print(root.right.left.data)
preOrderTraversal(root)



# Step-by-step operations performed by this script:
# 1. Defines the `TreeNode` class with `data`, `left`, and `right` attributes.
# 2. Implements `preOrderTraversal(node)` which visits: node -> left subtree -> right subtree.
#    - The function prints the node's `data`, then recursively traverses `left`, then `right`.
#    - Recursion base case: if `node is None`, the function returns without printing.
# 3. Creates `TreeNode` instances: `root`, `A`..`G`.
# 4. Manually links nodes to form the tree by assigning `left` and `right` references.
# 5. Executes `print(root.right.left.data)` which follows `root -> right -> left` and prints that node's data
#    (in this tree that value is `E`).
# 6. Calls `preOrderTraversal(root)` which prints all node values in pre-order sequence.
#    - For this tree the printed pre-order sequence will be: Root, A, C, G, D, B, E, F
# 7. Complexity notes:
#    - Pre-order traversal visits each node exactly once: O(n) time where n is number of nodes.
#    - Recursion depth equals the tree height: O(h) space on the call stack.
# 8. How to run: `python preOrderTraversalBinaryTree.py` will print the accessed node value and the pre-order listing.
