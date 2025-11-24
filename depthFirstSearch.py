binary_tree_array = ["Root", "1", "2", "3", "4", "5", "6", None, None, None, None, None, None, "G"]

def left_child_index(index):
  return 2 * index + 1

def right_child_index(index):
  return 2 * index + 2

def pre_order_traversal(index):
  if index >= len(binary_tree_array) or binary_tree_array[index] is None:
    return []
  return [binary_tree_array[index]] + pre_order_traversal(left_child_index(index)) + pre_order_traversal(right_child_index(index))

def in_order_traversal(index):
  if index >= len(binary_tree_array) or binary_tree_array is None:
    return []
  return in_order_traversal(left_child_index(index)) + [binary_tree_array[index]] + in_order_traversal(right_child_index(index))

def post_order_traversal(index):
  if index >= len(binary_tree_array) or binary_tree_array[index] is None:
    return []
  return post_order_traversal(left_child_index(index)) + post_order_traversal(right_child_index(index)) + [binary_tree_array[index]]


print("Pre-order Traversal:", pre_order_traversal(0))
print("In-order Traversal:", in_order_traversal(0))
print("Post-order Traversal:", post_order_traversal(0))

# Step-by-step process (what this file does and how the traversals work):
# 1. `binary_tree_array` stores a binary tree in a flat list using level-order (breadth-first) layout.
#    - Each index corresponds to a node position. `None` marks missing nodes.
#    - Example: index 0 is the root, index 1 is root.left, index 2 is root.right, etc.
# 2. `left_child_index(i)` returns `2*i + 1` and `right_child_index(i)` returns `2*i + 2`.
#    - These formulas map a parent index to its children's indices in a zero-based array.
# 3. `pre_order_traversal(index)` (implemented correctly) does:
#    - Base case: if `index` is out of range or the array entry is `None`, return an empty list.
#    - Otherwise return a list: `[node] + pre_order(left) + pre_order(right)`.
#    - This visits the node first, then left subtree, then right subtree (node, left, right).
# 4. `in_order_traversal(index)` is intended to do left -> node -> right, but currently contains two bugs:
#    - The guard checks `binary_tree_array is None` instead of `binary_tree_array[index] is None`.
#    - The recursive calls pass the function `left_child_index` instead of its result for the given `index`.
#    - Correct behavior should be:
#      def in_order_traversal(index):
#        if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#          return []
#        return in_order_traversal(left_child_index(index)) + [binary_tree_array[index]] + in_order_traversal(right_child_index(index))
# 5. `post_order_traversal(index)` is intended to do left -> right -> node, but currently has
#    a guard bug using `binary_tree_array(index)` (function-call syntax) instead of indexing.
#    - Correct behavior should be:
#      def post_order_traversal(index):
#        if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#          return []
#        return post_order_traversal(left_child_index(index)) + post_order_traversal(right_child_index(index)) + [binary_tree_array[index]]
# 6. Each traversal returns a Python list of node values; concatenation builds the final traversal order.
# 7. Example usage in this script:
#    - `pre_order_traversal(0)` traverses the whole tree starting at root index 0 and returns the pre-order list.
#    - `in_order_traversal(0)` and `post_order_traversal(0)` should behave similarly once the bugs are fixed.
# 8. Complexity:
#    - Each traversal visits every node at most once: O(n) time where n is number of nodes in the array.
#    - Recursion depth equals tree height h, so recursion stack is O(h).
# 9. Quick fixes (summary):
#    - In `in_order_traversal`, change `binary_tree_array is None` to `binary_tree_array[index] is None`, and
#      call `left_child_index(index)` / `right_child_index(index)` when recursing.
#    - In `post_order_traversal`, change `binary_tree_array(index)` to `binary_tree_array[index]` in the guard.


