class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

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

# 1. Defines a simple `TreeNode` class that stores `data` and references to `left` and `right` child nodes.
# 2. Creates individual `TreeNode` instances for the tree: `root`, `A`..`G`.
# 3. Links nodes together to form a binary tree by assigning `left` and `right` attributes:
#    - `root.left` -> `A`, `root.right` -> `B`
#    - `A.left` -> `C`, `A.right` -> `D`
#    - `B.left` -> `E`, `B.right` -> `F`
#    - `C.left` -> `G`
# 4. The tree structure (by levels) is:
#       Root
#      /    \
#     A      B
#    / \    / \
#   C   D  E   F
#  /
# G
# 5. Example access: `print(root.right.left.data)` prints the `data` value of the node at `root -> right -> left` (which is `E`).
# 6. Terminology:
#    - Root: the top-most node (`root`)
#    - Parent / Child: a node referencing another via `left`/`right`
#    - Leaf: node with no children (e.g., `D`, `E`, `F`, `G` if they have no children)
#    - Internal node: node with at least one child (e.g., `root`, `A`, `B`, `C`)
#    - Depth (of a node): number of edges from the root to the node
#    - Height (of a node): longest path (in edges) from the node down to a leaf
# 7. Traversals (common ways to visit nodes):
#    - Pre-order: visit node, traverse left, traverse right
#    - In-order: traverse left, visit node, traverse right
#    - Post-order: traverse left, traverse right, visit node
# 8. Searching and insertion:
#    - This file shows a generic binary tree (no ordering). To search, you must traverse and compare each node.
#    - A Binary Search Tree (BST) enforces ordering (left < node < right) which enables faster search/insert (avg O(log n)).
#    - For this generic tree, insertion is manual (assigning `left`/`right`) or done via a traversal to find an empty spot.
# 9. Complexity notes (generic binary tree operations):
#    - Traversal/Search (visiting all nodes): O(n) time, O(h) recursion stack where h is tree height
#    - Accessing a child via references (like `root.right.left`) is O(1)
# 10. Extensions you can add:
#    - Helper functions for `insert`, `find`, `delete` (BST-specific or level-order insertion for a complete tree)
#    - Traversal functions that return lists of values for testing and demonstration
#    - Functions to compute `height`, `size` (number of nodes), and `is_leaf` checks
# 11. This implementation is minimal and intended for learning: it demonstrates node linking and basic access by following `left`/`right` references.
