from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def max_depth(root: Optional[TreeNode]) -> int:
    # Base case: empty tree has depth 0
    if root is None:
        return 0
    
    # Recursively calculate depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the maximum of the two depths plus 1 (for current node)
    return max(left_depth, right_depth) + 1

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case: if root is None (shouldn't happen in valid BST)
    if root is None:
        return None
    
    # Get the values for comparison
    root_val = root.val
    p_val = p.val
    q_val = q.val
    
    # If both p and q are smaller than root, LCA lies in left subtree
    if p_val < root_val and q_val < root_val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both p and q are greater than root, LCA lies in right subtree
    elif p_val > root_val and q_val > root_val:
        return lowest_common_ancestor(root.right, p, q)
    
    # If p and q are on different sides of root, or one equals root,
    # then root is the LCA
    else:
        return root


# Optional: Helper functions for testing and visualization
def print_tree_inorder(root: Optional[TreeNode]) -> None:
    """Helper function to print tree in inorder traversal for debugging."""
    if root:
        print_tree_inorder(root.left)
        print(root.val, end=" ")
        print_tree_inorder(root.right)

def create_sample_bst() -> TreeNode:
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root

# Demo code (runs when file is executed directly)
if __name__ == "__main__":
    print("🌳 Binary Tree Lab Demo")
    print("=" * 40)
    
    # Test max_depth function
    print("\n1. Testing max_depth function:")
    
    # Create sample trees
    # Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print(f"   Balanced tree depth: {max_depth(root1)}")
    
    # Left-skewed tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    
    print(f"   Left-skewed tree depth: {max_depth(root2)}")
    
    # Single node
    root3 = TreeNode(42)
    print(f"   Single node tree depth: {max_depth(root3)}")
    
    # Empty tree
    print(f"   Empty tree depth: {max_depth(None)}")
    
    # Test lowest_common_ancestor function
    print("\n2. Testing lowest_common_ancestor function:")
    
    bst = create_sample_bst()
    
    # Test case 1: nodes 2 and 8 (LCA should be 6)
    p1 = bst.left  # node with value 2
    q1 = bst.right  # node with value 8
    lca1 = lowest_common_ancestor(bst, p1, q1)
    print(f"   LCA of {p1.val} and {q1.val}: {lca1.val}")
    
    # Test case 2: nodes 3 and 5 (LCA should be 4)
    p2 = bst.left.right.left   # node with value 3
    q2 = bst.left.right.right  # node with value 5
    lca2 = lowest_common_ancestor(bst, p2, q2)
    print(f"   LCA of {p2.val} and {q2.val}: {lca2.val}")
    
    # Test case 3: nodes 2 and 4 (LCA should be 2, since 2 is ancestor of 4)
    p3 = bst.left        # node with value 2
    q3 = bst.left.right  # node with value 4
    lca3 = lowest_common_ancestor(bst, p3, q3)
    print(f"   LCA of {p3.val} and {q3.val}: {lca3.val}")
    
    print("\n" + "=" * 40)
    print("Demo complete! Run 'python binary_tree_tests.py' to run full tests.")