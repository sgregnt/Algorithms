"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """what are the principles of deepcopy?
        """


        # I initialize the head of a linked list,  then add it's children and so on.
        # how can I go about doing this? Can I do this in place? That's hard.
        # Let's start with an easy idea,
        # I have hash whose index in the pointer, can this work?


        # This is the idea that I had, I first copied the list, and then I've added random pointers.

