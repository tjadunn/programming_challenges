import unittest
from typing import List

class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val) -> None:
        if val <= self.val:
            if self.left == None:
                self.left = TreeNode(val)
            else:
                self.left.inesert(val)
        elif val > self.val:
            if self.right == None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
    def print_tree(self) -> None:
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()

    def return_inorder_traversal(self, result=[]) -> List[int]:
        if self.left:
            self.left.return_inorder_traversal()
        result.append(self.val)
        if self.right:
            self.right.return_inorder_traversal()

        return result


def is_same_tree(tree_one: TreeNode, tree_two: TreeNode) -> bool:
    """
    Given two binary trees check if they are the same

    we define equality as both left and right subtrees and the root node are the same

    Accepts
        (TreeNode, TreeNode): The trees to compare

    Returns
        (bool): If the predicate is met

    Example:
         1
        / \
      2    3
         1
        / \
      2    3

    returns True
    """

    if tree_one != None and tree_two != None:
        is_same_tree(tree_one.left, tree_two.left)
        if tree_one.val != tree_two.val:
            return False
        is_same_tree(tree_one.right, tree_two.right)

    return True

def test_is_same_tree() -> None:
    tree_one = TreeNode(0)
    tree_one.insert(1)
    tree_one.insert(2)

    tree_two = TreeNode(0)
    tree_two.insert(1)
    tree_two.insert(2)

    assert is_same_tree(tree_one, tree_two) == True

class TestTreeNode(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.root = TreeNode(1)
        cls.root.insert(2)
        cls.root.insert(3)

    def test_inorder_traversal(self) -> None:
        self.assertEqual(self.root.return_inorder_traversal(), [1,2,3])

if __name__ == "__main__":
    test_is_same_tree()
