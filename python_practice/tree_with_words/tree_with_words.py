class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.c_dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """

        def get_last_node(key):

            prev_dic = self.c_dict
            c_dic = self.c_dict
            remain = key
            prev_ch = None
            while remain:
                ch = remain[0]
                if not ch in c_dic:
                    return prev_dic, remain, prev_ch
                else:
                    prev_ch = ch
                    prev_dic = c_dic
                    _, c_dic = c_dic[ch]
                    remain = remain[1:]

            return prev_dic, remain, prev_ch

        node, remain, prev_ch = get_last_node(key)

        if remain:
            while len(remain) > 1:
                prev_ch = remain[0]
                a = {}
                node[prev_ch] = (None, a)
                node = a
                remain = remain[1:]

            ch = remain[0]
            a = {}
            _, zz = node[prev_ch]
            zz[ch] = (val, a)

        else:
            _, a =  node[ch]
            node[ch] = (val, a)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        def get_last_node(key):

            prev_dic = self.c_dict
            c_dic = self.c_dict
            remain = key

            while remain:
                ch = remain[0]
                if not ch in c_dic:
                    return prev_dic, remain, ch
                else:
                    prev_dic = c_dic
                    _, c_dic = c_dic[ch]
                    remain = remain[1:]

            return prev_dic, remain, ch

        def sum_tree(node):

            total = 0
            queue = []
            queue.append(node)

            while queue:
                node = queue.pop()
                keys = node.keys
                for ch in node:
                    val, child = node[ch]
                    queue.append(child)
                    if val:
                        total += val

            return total

        node, remain, ch = get_last_node(prefix)
        res = sum_tree(node)
        return res

a = MapSum()
a.insert("apple", 3)
a.insert("app", 10)
print(a.sum("apple"))
print(a.c_dict)
a.insert("appx",3)
# print(a.c_dict)
# a.insert("appxxxe",3)
# print(a.c_dict)
print(a.sum("app"))
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple",3], ["ap"], ["app",2], ["ap"]]