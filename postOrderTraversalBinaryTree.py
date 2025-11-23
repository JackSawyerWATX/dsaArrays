class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(node):
  if node is None:
    return
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)
  print(node.data, end=", ")

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

# Step-by-step differences between this (post-order) traversal and pre-order / in-order traversals:
# 1. Order definition:
#    - Post-order: visit LEFT subtree, then RIGHT subtree, then NODE (left, right, node).
#    - Pre-order: visit NODE first, then LEFT, then RIGHT (node, left, right).
#    - In-order: visit LEFT, then NODE, then RIGHT (left, node, right).
# 2. When the node is processed (printed):
#    - Post-order processes the node after both subtrees have been fully visited.
#    - Pre-order processes the node immediately when the traversal first reaches it.
#    - In-order processes the node between visiting its left and right subtrees.
# 3. Example sequences for the sample tree in this file:
#    - Post-order (this file): G, C, D, A, E, F, B, Root
#    - Pre-order: Root, A, C, G, D, B, E, F
#    - In-order: G, C, A, D, Root, E, B, F
# 4. Recursion/call flow differences (high-level):
#    - Post-order for `root`: recurse into `root.left` fully, recurse into `root.right` fully, then process `root`.
#    - Pre-order for `root`: process `root` immediately, then recurse `root.left`, then `root.right`.
#    - In-order for `root`: recurse `root.left`, process `root`, recurse `root.right`.
# 5. Use-cases and semantic differences:
#    - Post-order: useful for deleting/freeing nodes (children removed before parent) and evaluating expression trees
#      where you need child results before applying an operator (postfix evaluation).
#    - Pre-order: useful for serializing or cloning the tree structure and producing prefix notation for expressions.
#    - In-order: especially useful on Binary Search Trees (BSTs) because it visits nodes in sorted order.
# 6. Complexity and space:
#    - All three traversals visit each node exactly once: O(n) time where n is number of nodes.
#    - All use recursion (or an explicit stack) with worst-case space O(h) where h is tree height.
# 7. Converting between traversals (conceptually):
#    - Move the point where you process the node (print/collect) relative to the left/right recursion calls:
#      * Pre-order: process before recursing left/right.
#      * In-order: process between left and right recursion.
#      * Post-order: process after left and right recursion.
# 8. Practical note: choose the traversal based on the task — e.g., deletion and postfix evaluation use post-order,
#    sorted output from a BST uses in-order, and structure-preserving serialization often uses pre-order.
