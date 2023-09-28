# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # res=[0]
        # def helper(root,maxi):
        #     if root:
        #         maxi=max(maxi,root.val)
        #         if maxi<=root.val:
        #             res[0]+=1
        #         if root.left:
        #             helper(root.left,maxi)
        #         if root.right:
        #             helper(root.right,maxi)
        # helper(root,-maxsize)
        # return res[0]
        # maxVal=root.val
        # def dfs(root,maxVal):
        #     if not root:
        #         return 0
        #     res=1 if root.val>=maxVal else 0
        #     maxVal=max(root.val,maxVal)
        #     res+=dfs(root.left,maxVal)
        #     res+=dfs(root.right,maxVal)
        #     return res
        # return dfs(root,maxVal)
        stack = [[root, float('-inf')]]
        res = 0

        while stack:
            node, maxNum = stack.pop()

            if node.val>=maxNum:
                res+=1
            maxNum=max(maxNum,node.val)
            if node.left:
                stack.append([node.left, maxNum])
            if node.right:
                stack.append([node.right, maxNum])
        return res
        

        