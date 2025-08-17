# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, n: Optional[TreeNode], m: Optional[TreeNode]) -> bool:
        if not n and not m:
            return True
        if not n or not m:
            return False
        return (n.val == m.val) and self.isSameTree(n.left, m.left) and self.isSameTree(n.right, m.right)
