# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def helper(node, path):
            if not node:
                return
            if path:
                path += "->"+str(node.val)
            else:
                path = str(node.val)
            if not node.right and not node.left:
                result.append(path)
                return
            helper(node.right, path)
            helper(node.left, path)
        helper(root, "")
        return result
    