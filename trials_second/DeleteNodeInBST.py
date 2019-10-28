#===========================
# Delete node in BST
#===========================

# Three facts to know about BST
# inorder traversal
# predecessor
# successor
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        def find_leftmost(root):
            while root.left:
                root = root.left
            return root.val

        def find_rightmost(root):

            while root.right:
                root = root.right

            return root.val

        def deleteNode(root, key):
            if root == None:
                return None

            if root.val == key:
                if root.right:
                    new_val = find_leftmost(root.right)
                    root.val = new_val
                    root.right = deleteNode(root.right, new_val)
                    return root

                elif root.left:
                    new_val = find_rightmost(root.left)
                    root.val = new_val
                    root.left = deleteNode(root.left, new_val)
                    return root

                else:
                    return None
            else:
                if root.val > key:
                    root.left = deleteNode(root.left, key)
                    return root
                else:
                    root.right = deleteNode(root.right, key)
                    return root

        root = deleteNode(root, key)

        return root

