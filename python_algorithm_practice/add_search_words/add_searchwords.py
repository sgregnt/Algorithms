class prefixT(object):
    def __init__(self):
        self.ch = {}
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.prefix = prefixT()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        
        node = self.prefix
        for w in word:
            if w in node.ch:
                node = node.ch[w]
            else:
                node.ch[w] = prefixT()           
                node = node.ch[w]
                
        node.isWord= True        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        res = self.dfs(word, self.prefix)
        if res:
            return True
        else:
            return False
       
    def dfs(self,  word, node):
       
        if not word:
            if node.isWord:
                return True
            else:
                pass
        
        for w in word:
            if w == ".":
                for next_n in node.ch:
                    res = self.dfs(word[1:], node.ch[next_n])
                    if res:
                        return True
                
                return False 
            
            else:   
                if w in node.ch:
                    return self.dfs(word[1:], node.ch[w])
                else:
                    return False
            
word = "hello11"
obj = WordDictionary()
obj.addWord(word)
word = "heallo"
obj.addWord(word)
word = "haello"
obj.addWord(word)
word = "ahello"
obj.addWord(word)
word = "hell.."
param_2 = obj.search(word)
print(param_2)