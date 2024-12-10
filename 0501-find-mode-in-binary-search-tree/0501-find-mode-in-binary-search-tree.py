# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def in_order_traversal(node):
            nonlocal prev, count, max_count, modes
            if not node:
                return None
            in_order_traversal(node.left)
            current_val = node.val
            if node.val == prev:
                count += 1
            else:
                count = 1
                prev = node.val
            if count > max_count:
                max_count = count
                modes = [current_val]
            elif count == max_count:
                modes.append(current_val)
            in_order_traversal(node.right)
        
        prev = None
        count = 0
        max_count = 0
        modes = []
        in_order_traversal(root)
        return modes
            
        