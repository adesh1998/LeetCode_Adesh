# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque([root])
        res=[root.val]
        while q:
            j=0
            for i in range(len(q)):
                node=q.popleft()
                if node.right:
                    q.append(node.right)
                    if j==0:
                        res.append(node.right.val)
                        j+=1
                if node.left:
                    q.append(node.left)
                    if j==0:
                        res.append(node.left.val)
                        j+=1       
        return res