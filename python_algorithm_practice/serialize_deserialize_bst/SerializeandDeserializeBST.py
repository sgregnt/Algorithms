# Serialization is the process of converting a data structure or object into a sequence of
# bits so that it can be stored in a file or memory buffer, or transmitted across a network
# connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary search tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# The encoded string should be as compact as possible.
#
# Note: Do not use class member/global/static variables to store states. Your serialize and
# deserialize algorithms should be stateless.


#=========================================
# I have memory limit exceeded
#=========================================

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """

    res = []
    index = 1
    myq = deque()
    myq.append((root, index))
    last_ind = 0
    while myq:

        node, index = myq.pop()
        n = len(res)
        diff = index - n

        if diff > 0:
            res.extend([None] * diff)

        if node:
            res[index-1] = node.val
            last_ind = index
            myq.appendleft((node.left, 2 * index))
            myq.appendleft((node.right, 2 * index + 1))
        else:
            pass

    return res[0:last_ind]

a = TreeNode(10)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(20)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

res = serialize(a)
print(res)

def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    def recursion(nodes, index, n):
        if index > n or nodes[index -1] == None:
            return None

        node = TreeNode(nodes[index - 1])
        node.left = recursion(nodes, 2 * index, n)
        node.right = recursion(nodes, 2 * index + 1, n)

        return node


    return recursion(data, 1, len(data))


new_tree = deserialize(res)
# print(new_tree.val)
# print(new_tree.left.val)
# print(new_tree.right.val)
# print(new_tree.left.left.val)
# print(new_tree.left.right.val)

print(serialize(new_tree))


#=========================================
# Tree traversal
#=========================================

# Construct binary tree from preorder and inorder traversal
# Return the root node of a binary search tree that matches the given preorder traversal.

# in-order left-root-right
# postorder left-right-root
# preorder root-left-right



#===========================================
# Delete node in a BST
#===========================================



#===========================================
# Construct Binary Search Tree from Preorder Traversal
#
# The proposed solution says that you
# need to get inorder by sorting the
# preorder and then use both to construct
# the solution. As discribed in here:  Inorder traversal of BST is an array sorted in the ascending order.
#
#===========================================

# Return the root node of a binary search tree that matches the given preorder traversal.
# preorder root-left-right

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    """
    :type preorder: List[int]
    :rtype: TreeNode
    """

    if not preorder:
        return

    def add_element(side, prev, root, elem):

        if root == None:
            if side == 1:
                prev.right = TreeNode(elem)
            else:
                prev.left = TreeNode(elem)

            return

        if root.val < elem:
            add_element(1, root, root.right, elem)
        else:
            add_element(0, root, root.left, elem)

    root = TreeNode(preorder[0])

    n = len(preorder)

    for i in range(1, n):
        add_element(0, root, root, preorder[i])

    return root

#===========================================
# Construct Binary Search Tree from inorder Traversal
# this seems to be more tricky
# still not sure how to construct a tree from
# in order traversal.
#===========================================

# in order, left root right, not sure how to process with this
# 1 5 7 8 10 12


# you get the node, and new element if the value of the node is
# smaller than the elemen you create a new node and
# make the previous node to be it's left or right
# descendent, but this way the tree will be just a linear tree.
# okay so what you can do is start at the middle this is you root, then check the value of the
# left tree and appand it accordingly and check the value of the right tree
# not clear how you do this.

# here is an explanation: https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/


# We all know that different binary trees can have the same inorder,
# preorder, or postorder traversal. But if we were to include null
# elements into a preorder traversal, then result of the traversal
# would be unique as long as the trees are unique. Consider these
# two trees:


#===========================================
# Do inorder traversal without recursion
#===========================================

# Use stack push root, and set root.left to be the root
# if root left does not exists pop, print and set toot to root.right
# repeat procedure from the left,


#===========================================
# Do postorder traversal without recursion
#===========================================

# This is hard

#===========================================
# Let's use here the fact that BST could be constructed from preorder or postorder traversal only
#===========================================

#============================================
# Delete node in a BST
#============================================
# Given a root node reference of a BST and a key, delete the node with the given
# key in the BST. Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
#     Search for a node to remove.
#     If the node is found, delete the node.

# What happens if I delet the root.
#  I need to replace the node with the largest element in the right array.
#  Which is the right most element in the sub tree.



#============================================
# Validate Binary Search Tree
#============================================