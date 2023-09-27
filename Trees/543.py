# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi = 0
    def f(self, root):
        if not root: return 0
        left = self.f(root.left)
        right = self.f(root.right)
        self.maxi = max(self.maxi,left+right)
        return 1 +max(left , right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # l=root.left
        # r=root.right
        # def dfs(root, depth):
        #     if not root: return depth
        #     return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        
        # return dfs(l,0)+dfs(r,0)

        
        self.f(root)
        return  self.maxi
        
        
        