'''
208. Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode(object):
  def __init__(self, letter = "."):
    """
    Initialize your data structure here.
    """
    self.letter = letter
    self.hasWordEndHere = False
    self.next = {}

class Trie(object):
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    curDict = self.root
    for c in word:
      if not c in curDict.next:
        curDict.next[c] = TrieNode(c)
      curDict = curDict.next[c]
    curDict.hasWordEndHere = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    testRoot = self.root
    for c in word:
      try:
        testRoot = testRoot.next[c]
      except:
        return False
    return testRoot.hasWordEndHere


  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie
    that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    testRoot = self.root
    for c in prefix:
      try:
        testRoot = testRoot.next[c]
      except:
        return False
    return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
# trie.insert("somestring")
# print trie.search("somestring")
# print trie.startsWith("some")
# print trie.startsWith("sime")

# trie.insert("ab")
# print trie.search("a")
# print trie.startsWith("a")

trie.insert("app")
trie.insert("apple")
trie.insert("beer")
trie.insert("add")
trie.insert("jam")
trie.insert("rental")

print trie.search("apps")
print trie.search("app")
print trie.search("ad")
print trie.search("applepie")
print trie.search("rest")
print trie.search("jan")
print trie.search("rent")
print trie.search("beer")
print trie.search("jam")
print trie.startsWith("apps")
print trie.startsWith("app")
print trie.startsWith("ad")
print trie.startsWith("applepie")
print trie.startsWith("rest")
print trie.startsWith("jan")
print trie.startsWith("rent")
print trie.startsWith("beer")
trie.startsWith("jam")