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

