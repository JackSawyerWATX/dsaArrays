binary_tree_array = ["Root", "1", "2", "3", "4", "5", "6", None, None, None, None, None, None, "G"]

def left_child_index(index):
  return 2 * index + 1

def right_child_index(index):
  return 2 * index + 2

def get_data(index):
  if 0 <= index < len(binary_tree_array):
    return binary_tree_array[index]
  return None

right_child = right_child_index(0)
left_child_of_right_child = left_child_index(right_child)
data = get_data(left_child_of_right_child)

print("root.right.left.data =", data)

# Step-by-step explanation of this array-based binary tree implementation:
# 1. `binary_tree_array` is a flat list representing a binary tree in level-order (breadth-first).
#    - Each index corresponds to a node position in the tree. `None` denotes no node at that position.
#    - Example array: ["Root", "1", "2", "3", "4", "5", "6", None, None, None, None, None, None, "G"]
# 2. Child index formulas (for zero-based arrays):
#    - `left_child_index(i) = 2*i + 1`
#    - `right_child_index(i) = 2*i + 2`
#    These map a parent's index `i` to its left and right child positions in the array.
# 3. `get_data(index)` safely returns the value at `binary_tree_array[index]` if the index is in range,
#    otherwise it returns `None`. This avoids IndexError and models missing nodes.
# 4. The example access performed in this script is:
#    - Compute `right_child = right_child_index(0)` which gives the index of the root's right child.
#    - Compute `left_child_of_right_child = left_child_index(right_child)` which gives the index of that node's left child.
#    - Call `get_data(left_child_of_right_child)` to retrieve the stored value (or `None` if missing).
#    - Finally print the result as `root.right.left.data = <value>`.
# 5. For the provided `binary_tree_array`, the computed path `root -> right -> left` resolves to the array element
#    at index `left_child_index(right_child_index(0))`, which in this array holds the value `"G"`.
# 6. Advantages of array representation:
#    - Simple and memory-efficient for complete or nearly-complete binary trees (no pointers required).
#    - Constant-time computation of child/parent indices using arithmetic.
# 7. Limitations of array representation:
#    - Wastes space if the tree is sparse (many `None` placeholders for missing nodes).
#    - Harder to perform dynamic insertions/deletions except at the end or when managing a complete tree.
# 8. Correspondence to pointer-based trees:
#    - In a pointer-based tree each node stores `left` and `right` references; here those relationships are implicit
#      via index math. Conceptually `array[i]` corresponds to a node whose children are at the computed indices.
# 9. Extensions you might add:
#    - Helper functions for `parent_index(i)` to move upward: `parent = (i - 1) // 2` (for i > 0).
#    - Functions to perform traversals (pre/in/post/level-order) that skip `None` values.
#    - Utilities to insert or remove nodes while keeping the array representation consistent.

