# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:
        #     return None
        # if root.val>p.val and root.val>q.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        # if root.val<p.val and root.val<q.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        # return root
        cur=root
        while cur:
            if cur.val>p.val and cur.val>q.val:
                cur=cur.left
            elif cur.val<p.val and cur.val<q.val:
                cur=cur.right
            else:
                return cur
                