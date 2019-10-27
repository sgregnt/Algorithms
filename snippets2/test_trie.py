class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score



a = MapSum()
a.insert("apple",3)
a.insert("app",10)
print(a.sum("apple"))
print(a.c_dict)
a.insert("appx",3)
# print(a.c_dict)
# a.insert("appxxxe",3)
# print(a.c_dict)
print(a.sum("app"))