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
        """
        :type head: Node
        :rtype: Node
        """

        hash_id_aliases = {}

        if not head:
            return None

        node = head
        while node:
            if node in hash_id_aliases:
                node = node.next
            else:
                hash_id_aliases[node] = Node(node, None, None)
                node = node.next

        node = head
        while node:

            hash_id_aliases[node].val = node.val

            if node.random:
                hash_id_aliases[node].random = hash_id_aliases[node.random]
            else:
                hash_id_aliases[node].random = None

            if node.next:
                hash_id_aliases[node].next = hash_id_aliases[node.next]
            else:
                hash_id_aliases[node].next = None

            node = node.next

        return hash_id_aliases[head]
