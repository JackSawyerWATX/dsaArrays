class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(node):
  if node is None:
    return
  preOrderTraversal(node.left)
  print(node.data, end=", ")
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
    
# Step-by-step differences between this (in-order) traversal and a pre-order traversal:
# 1. Order definition:
#    - In-order: visit LEFT subtree, then NODE, then RIGHT subtree (left, node, right).
#    - Pre-order: visit NODE first, then LEFT subtree, then RIGHT subtree (node, left, right).
# 2. Where the node's value is processed:
#    - In-order processes a node after completely traversing its left subtree.
#    - Pre-order processes a node immediately when the call reaches it (before its children).
# 3. Example sequence on this sample tree:
#    - In-order output: G, C, A, D, Root, E, B, F
#    - Pre-order output: Root, A, C, G, D, B, E, F
# 4. Call/recursion flow (high level):
#    - In-order for `root`: recurse into `root.left` fully, process `root`, then recurse into `root.right`.
#    - Pre-order for `root`: process `root` immediately, then recurse into `root.left`, then `root.right`.
# 5. Use-cases where they differ in value:
#    - In-order is useful for Binary Search Trees because it produces nodes in sorted (ascending) order.
#    - Pre-order is useful for copying the tree structure or producing prefix notation (e.g., for expression trees).
# 6. Stack/space behavior:
#    - Both use recursion and have the same worst-case time O(n) and recursion depth O(h) where h is tree height.
#    - The difference is only the order nodes are visited, not asymptotic cost.
# 7. How to convert between them conceptually:
#    - To switch this function to pre-order, move the `print(node.data)` before the left recursion.
#    - To switch to post-order, move the `print(node.data)` after both left and right recursions.
# 8. Practical note: ensure the traversal you choose matches the operation you need (sorted output, tree cloning,
#    or evaluation order for expressions).

